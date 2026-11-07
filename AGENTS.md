# AGENTS.md

Durable instructions for future Codex sessions in the top-level `ai-comics` workspace.

## Public-content privacy rules

This repository contains fictional, industry-wide enterprise AI satire. Apply these rules to prose, prompts, filenames, artwork, metadata, commit messages, and Git author/committer fields.

- Use roles or approved initials (`KKLL`, `AKB`, `TT`) for people. Never expand initials, map them to identities, or add biographical/relationship details. Avoid realistic personal names even as placeholders.
- Exclude personal facts, contact details, account identifiers, home paths, private URLs, employer/client identities, internal project names, real incidents, actual staffing assignments, nonpublic strategy, procurement details, and workplace conversations.
- Write synthetic scenarios and invented figures. Remove identifying combinations of details; a fictional disclaimer does not make a recognizable private incident safe.
- Keep public product references only when needed to understand the metaphor. Describe pilots, policies, budgets, and workflows as hypothetical industry examples; never imply that they describe a contributor's workplace.
- Never commit credentials, tokens, private keys, environment files, raw exports, personal source briefs, local session logs, or unsanitized audit reports/backups. Use repository-relative paths.
- Inspect every image visually, including signs, badges, tiny text, signatures, and background screens. Inspect metadata for identities, local paths, coordinates, and private source references. Retain AI-generation provenance when it contains no personal information.
- Preserve creative reasoning and safe artwork. Put private inspiration or source-event notes outside the public repository. Rewrite a revealing label in every image copy and corresponding prompt before publication.
- Use `KKLL <kkll@contributors.invalid>` for this repository's author and committer metadata. Configure repository-local Git identity before committing. A personal hosting account remains publicly associated with the repository.
- Before a public commit or push, run `python3 scripts/check_public_release.py`, review the diff for contextual identification, and verify new/changed images. Record approved image hashes in `artwork-review.json` only after inspection. Automated checks supplement human review.
- Review every branch/tag intended for publication and GitHub-only surfaces. Do not merge private history into public history. Keep private backups and release workspaces excluded. Prepare any history replacement or visibility change for explicit final approval.

## Repository Scope

Treat the entire `ai-comics` folder as the Git repository. Individual comic series should live in subfolders, such as `ai-vehicle-comics/`, so future analogy projects can sit beside the vehicle series.

## Creative Posture

This is a content-development and visual-storytelling workspace. Preserve creative reasoning, style decisions, prompts, visual drafts, and revision notes as first-class artifacts.

## Signature And Credit

Default artifact signature should be `KKLL`.

Only prepend another contributor's signature when that person provided the idea, inspiration, or meaningful creative input for that specific artifact. For example, use `AKB + KKLL` only on artifacts where AKB should receive front-of-signature credit for that artifact.

## Series Structure

For each new series, prefer a Markdown-first structure similar to:

- `README.md`
- `AGENTS.md`
- `00_core_framework/`
- `01_comic_backlog/`
- `02_prompt_library/`
- `03_assets/`
- `04_decision_log/`

## Working Rules

- Read the relevant series-level `AGENTS.md` before making changes inside a series folder.
- Keep analogies compact and repeatable.
- Challenge weak metaphors and generic punchlines.
- Preserve prompts and style recipes that led to useful visual outputs.
- Store share-worthy generated artifacts under the appropriate `03_assets/` folder.
