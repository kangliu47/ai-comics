#!/usr/bin/env python3
"""Check public creative files and reachable history. Human contextual review is required."""
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import urllib.parse
import zlib

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {'KKLL', 'AKB', 'TT'}
EMAIL = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
PATTERNS = {
    'absolute personal path': re.compile(r'/(?:Users|home)/[\w.-]+|[A-Za-z]:\\Users\\[\w.-]+'),
    'private key': re.compile(r'-----BEGIN (?:[A-Z ]*PRIVATE KEY)-----'),
    'provider credential': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b|\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}\b|\bxox[baprs]-[A-Za-z0-9-]{10,}\b'),
    'credential assignment': re.compile(r'''(?i)(?:api[_-]?key|password|client[_-]?secret|access[_-]?token)\s*[:=]\s*["'][^"'\s]{8,}["']|authorization\s*[:=]\s*bearer\s+\S+'''),
    'named person placeholder': re.compile(r'\bAsk\s+[A-Z][a-z]{2,}\b'),
    'real rollout framing': re.compile(r'\breal pilot rollout\b', re.I),
}
ALLOWED_SUFFIXES = {'.md', '.json', '.png', '.py', '.yml', '.yaml'}
ALLOWED_DOTFILES = {'.gitignore', '.gitkeep', '.gitattributes'}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], stderr=subprocess.DEVNULL)


def text_issues(text):
    issues = [label for label, regex in PATTERNS.items() if regex.search(text)]
    for email in EMAIL.findall(text):
        domain = email.rsplit('@', 1)[1].lower()
        if not (domain.endswith('.invalid') or domain in {'example.com', 'example.org', 'example.net'}):
            issues.append('non-placeholder email address')
    return sorted(set(issues))


def file_issues(name, data):
    p = Path(name)
    issues = text_issues(name)
    if p.suffix not in ALLOWED_SUFFIXES and p.name not in ALLOWED_DOTFILES:
        issues.append('file type needs explicit publication review')
    if any(part in {'.tmp', 'tmp', '.superpowers', '.codex', '.agents', '__pycache__'} for part in p.parts):
        issues.append('private/scratch path')
    if p.name.startswith('.env') or p.suffix in {'.pem', '.key', '.p12', '.pfx', '.bundle', '.bak'}:
        issues.append('private configuration or backup file')
    if p.suffix == '.png':
        if not data.startswith(b'\x89PNG\r\n\x1a\n'):
            return issues + ['invalid PNG signature']
        pos = 8
        ended = False
        while pos < len(data):
            if pos + 12 > len(data):
                return issues + ['truncated PNG chunk']
            size = struct.unpack('>I', data[pos:pos + 4])[0]
            kind = data[pos + 4:pos + 8]
            end = pos + size + 12
            if end > len(data):
                return issues + ['truncated PNG data']
            payload = data[pos + 8:pos + 8 + size]
            crc = struct.unpack('>I', data[pos + 8 + size:end])[0]
            if zlib.crc32(kind + payload) & 0xffffffff != crc:
                issues.append('PNG checksum mismatch')
            if kind not in {b'IHDR', b'IDAT', b'IEND', b'caBX'}:
                issues.append('PNG ancillary metadata requires review/export')
            if kind == b'caBX':
                # Certificate-service emails are expected; inspect identities manually.
                printable = '\n'.join(x.decode() for x in re.findall(rb'[\x20-\x7e]{5,}', payload))
                issues.extend(label for label, regex in PATTERNS.items() if regex.search(printable))
            pos = end
            if kind == b'IEND':
                ended = True
                if pos != len(data):
                    issues.append('unreviewed trailing PNG data')
                break
        if not ended:
            issues.append('PNG missing end chunk')
    else:
        try:
            issues.extend(text_issues(data.decode('utf-8')))
        except UnicodeDecodeError:
            issues.append('unexpected binary file')
    return sorted(set(issues))


def main():
    errors = []
    try:
        if Path(git('rev-parse', '--show-toplevel').decode().strip()).resolve() != ROOT:
            raise ValueError('run from a standalone release repository')
        if git('rev-parse', '--is-shallow-repository').decode().strip() != 'false':
            errors.append('history: shallow clone cannot verify all published history')
        names = sorted(set(git('ls-files', '--cached', '--others', '--exclude-standard', '-z').decode().split('\0')) - {''})
    except (subprocess.CalledProcessError, ValueError) as exc:
        print('FAIL: initialize a standalone repository before checking.')
        return 1
    manifest = json.loads((ROOT / 'artwork-review.json').read_text())
    approvals = {e['path']: e['sha256'] for e in manifest['images']}
    for name in names:
        path = ROOT / name
        if path.is_symlink():
            errors.append(name + ': symlinks require explicit review')
            continue
        if not path.is_file():
            errors.append(name + ': tracked file missing')
            continue
        data = path.read_bytes()
        errors.extend(name + ': ' + issue for issue in file_issues(name, data))
        if path.suffix == '.png' and approvals.get(name) != hashlib.sha256(data).hexdigest():
            errors.append(name + ': image is new or changed since visual approval')
        if path.suffix == '.md':
            for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', data.decode()):
                target = link.split('#', 1)[0].strip('<>')
                if not target or urllib.parse.urlsplit(target).scheme:
                    continue
                candidate = (path.parent / urllib.parse.unquote(target)).resolve()
                if ROOT not in candidate.parents or not candidate.exists():
                    errors.append(name + ': missing/outside repository link ' + target)
    for name in approvals:
        if name not in names:
            errors.append('artwork-review.json: stale image approval ' + name)
    # Check staged bytes too: a clean working file can hide a previously staged leak.
    for row in git('ls-files', '--stage', '-z').split(b'\0'):
        if not row:
            continue
        metadata, name = row.split(b'\t', 1)
        mode, oid, stage = metadata.split()
        if stage != b'0' or mode != b'100644':
            errors.append('index: unresolved or unsupported entry')
            continue
        name = name.decode()
        data = git('cat-file', 'blob', oid.decode())
        errors.extend('index ' + name + ': ' + issue for issue in file_issues(name, data))
        if name.endswith('.png') and approvals.get(name) != hashlib.sha256(data).hexdigest():
            errors.append('index ' + name + ': image bytes lack visual approval')
    for row in git('for-each-ref', 'refs/tags', '--format=%(objectname) %(objecttype)').decode().splitlines():
        oid, kind = row.split()
        if kind == 'tag':
            raw = git('cat-file', 'tag', oid).decode()
            errors.extend('tag ' + oid[:8] + ': ' + issue for issue in text_issues(raw))
            m = re.search(r'^tagger (.+) <([^>]+)>', raw, re.M)
            if not m or m[1] not in ALIASES or m[2] != m[1].lower() + '@contributors.invalid':
                errors.append('tag ' + oid[:8] + ': unapproved tagger identity')
    gallery = json.loads((ROOT / 'ai-vehicle-comics/gallery/gallery.json').read_text())
    ids = [e['id'] for e in gallery]
    if len(ids) != len(set(ids)):
        errors.append('gallery: duplicate episode IDs')
    for entry in gallery:
        for key in ('image', 'concept', 'prompt', 'revision_prompt'):
            if key in entry:
                target = (ROOT / 'ai-vehicle-comics/gallery' / entry[key]).resolve()
                if ROOT not in target.parents or not target.is_file():
                    errors.append('gallery: missing/outside ' + entry['id'] + ' ' + key)
    commits = git('rev-list', '--all').decode().splitlines()
    blobs = set()
    for sha in commits:
        raw = git('cat-file', 'commit', sha).decode()
        errors.extend('commit ' + sha[:8] + ': ' + issue for issue in text_issues(raw))
        for field in ('author', 'committer'):
            m = re.search(r'^' + field + r' (.+) <([^>]+)>', raw, re.M)
            if not m or m[1] not in ALIASES or m[2] != m[1].lower() + '@contributors.invalid':
                errors.append('commit ' + sha[:8] + ': unapproved ' + field + ' identity')
        for line in git('ls-tree', '-r', '-z', sha).split(b'\0'):
            if not line:
                continue
            metadata, name = line.split(b'\t', 1)
            mode, kind, oid = metadata.split()
            if mode != b'100644' or kind != b'blob':
                errors.append('history: unsupported file mode/type')
                continue
            pair = (name.decode(), oid.decode())
            if pair in blobs:
                continue
            blobs.add(pair)
            data = git('cat-file', 'blob', pair[1])
            errors.extend('history ' + pair[0] + ': ' + issue for issue in file_issues(pair[0], data))
            if pair[0].endswith('.png') and hashlib.sha256(data).hexdigest() not in set(approvals.values()):
                errors.append('history ' + pair[0] + ': image version lacks current visual approval')
    if errors:
        for error in sorted(set(errors)):
            print('FAIL: ' + error)
        return 1
    print('PASS: {} files, {} approved images, {} commits, {} historical file versions.'.format(len(names), len(approvals), len(commits), len(blobs)))
    print('Human review is still required for names and recognizable personal/workplace context.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
