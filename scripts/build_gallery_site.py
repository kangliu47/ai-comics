#!/usr/bin/env python3
"""Build the public gallery from selected metadata and reviewed original artwork."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import struct

ROOT = Path(__file__).resolve().parents[1]


def build(output):
    gallery_dir = ROOT / "ai-vehicle-comics/gallery"
    entries = json.loads((gallery_dir / "gallery.json").read_text())
    approvals = {
        entry["path"]: entry["sha256"]
        for entry in json.loads((ROOT / "artwork-review.json").read_text())["images"]
    }
    comics, cards, seen = [], [], set()
    for entry in sorted(entries, key=lambda item: int(item["id"]), reverse=True):
        episode_id = entry["id"]
        if not re.fullmatch(r"\d{3}", episode_id) or episode_id in seen:
            raise ValueError("Invalid or duplicate gallery episode ID")
        seen.add(episode_id)
        source = (gallery_dir / entry["image"]).resolve()
        relative = source.relative_to(ROOT).as_posix()
        if not relative.startswith("ai-vehicle-comics/03_assets/selected_drafts/"):
            raise ValueError("Gallery artwork must come from selected_drafts")
        data = source.read_bytes()
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or approvals.get(relative) != hashlib.sha256(data).hexdigest():
            raise ValueError("Gallery image lacks matching visual approval: " + episode_id)
        width, height = struct.unpack(">II", data[16:24])
        image = "artwork/" + episode_id + ".png"
        comic = {
            "id": episode_id, "title": entry["title"], "message": entry["message"],
            "image": image, "width": width, "height": height,
        }
        comics.append(comic)
        title = html.escape(comic["title"], quote=True)
        caption = html.escape(comic["message"], quote=True)
        loading = 'fetchpriority="high"' if not cards else 'loading="lazy"'
        cards.append(f'''          <article class="comic" id="comic-{episode_id}">
            <a class="comic-link" href="{image}" data-comic="{episode_id}" aria-label="Read {title}">
              <img src="{image}" alt="Comic {episode_id}: {title}" width="{width}" height="{height}" {loading} decoding="async">
              <p class="eyebrow">COMIC {episode_id}</p>
              <h2>{title}</h2>
              <p class="comic-caption">{caption}</p>
              <span class="read-label">Read comic →</span>
            </a>
          </article>''')
    if not comics:
        raise ValueError("The selected gallery is empty")
    output.mkdir(parents=True, exist_ok=True)
    (output / "artwork").mkdir(exist_ok=True)
    # Never transform reviewed artwork: retain its original bytes and provenance.
    for comic, entry in zip(comics, sorted(entries, key=lambda item: int(item["id"]), reverse=True)):
        shutil.copyfile(gallery_dir / entry["image"], output / comic["image"])
    template = (ROOT / "site/index.html").read_text()
    data_json = json.dumps(comics, ensure_ascii=False).replace("<", "\\u003c")
    page = template.replace("{{GALLERY_CARDS}}", "\n".join(cards)).replace("{{COMIC_DATA}}", data_json)
    (output / "index.html").write_text(page)
    for name in ("gallery.css", "gallery.js"):
        shutil.copyfile(ROOT / "site" / name, output / name)
    (output / ".nojekyll").write_text("")
    print(f"Built {len(comics)} selected comics with original artwork and brief captions.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".tmp/gallery-site")
    build(parser.parse_args().output.resolve())
