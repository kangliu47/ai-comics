# Public-content security and privacy

This is a creative repository of synthetic enterprise AI scenarios. Its privacy boundary covers source notes, every draft, artwork, metadata, and Git history as well as selected comics. The current durable policy is in [AGENTS.md](AGENTS.md#public-content-privacy-rules).

## Required review

1. Check for names, identity mappings, personal details, employer/client references, recognizable private incidents, and combinations of vendor, role, timing, or workflow details that identify a workplace.
2. Use generic roles and hypothetical scenarios. Invent figures and filenames. Preserve useful editorial reasoning without retaining private inspiration or conversational transcripts.
3. Inspect new or edited images at readable resolution and inspect their metadata. Check all duplicated versions. After approval, record each PNG's SHA-256, review date, and a short generic review note in `artwork-review.json`.
4. Run `python3 scripts/check_public_release.py`. It checks the candidate files, links, gallery references, image approvals, and all locally reachable Git history for common exposure patterns and approved commit identity. It cannot establish whether a story is a recognizable private incident or reliably identify every person's name.
5. Review the staged diff, author/committer identity, published branches/tags, and GitHub-only descriptions, discussions, issues, releases, and workflow artifacts before publication.

Configure repository-local identity before committing:

```sh
git config user.name KKLL
git config user.email kkll@contributors.invalid
```

The alias email is a non-delivery placeholder. Hosting under a personal account still exposes the account association. GitHub-created merge or web-edit commits may use that account's identity, so inspect their metadata before using them in this public history.

## If a disclosure is found

Keep credentials out of issues and comments. Revoke a credential if one is exposed. Remove the sensitive material from candidate files and every published version that contains it; a normal deletion commit leaves earlier versions. Do not paste identifying findings into a public remediation report. Keep private backups separate, and agree on history replacement before changing a published repository.

## Scope of the automated check

The checker uses only the Python standard library. Approved-image hashes establish which exact files received visual review; the checker cannot read scene meaning or approve an image automatically. Public product names and generation-service certificates are not by themselves personal information. Genuine AI-generation provenance should remain intact when safe.
