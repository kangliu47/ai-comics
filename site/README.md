# Public Comic Gallery

Approved flow: newest-first artwork grid → full-size comic reader, with brief captions, previous/next navigation and a per-comic share link. The user approved this flow on 2026-11-07 after reviewing an interactive mock with sample content.

The public gallery lives at [AI Vehicle Comics](https://kangliu47.github.io/ai-comics/). A comic can be shared directly, for example [Comic 028](https://kangliu47.github.io/ai-comics/#comic-028).

## Maintain the gallery

The selected [gallery metadata](../ai-vehicle-comics/gallery/gallery.json) is the single source of titles, captions, ordering and approved artwork paths. Add selected episodes there and record their inspected hashes in [artwork-review.json](../artwork-review.json). Do not add drafts to the website.

Build locally:

```sh
python3 scripts/check_public_release.py
python3 scripts/build_gallery_site.py
python3 -m http.server 8000 --directory .tmp/gallery-site
```

Open the local server in a browser. Build output stays in the ignored .tmp directory. The builder checks image hashes against the review manifest and copies original PNG bytes, including AI provenance, without transformation. Only selected artwork, the rendered gallery page and its CSS/JavaScript enter the deployment artifact.

The [GitHub Pages workflow](../.github/workflows/gallery-pages.yml) checks the public release, builds the site and deploys changes from main. It can also be run manually in GitHub Actions. GitHub Pages uses the workflow publishing source.

Gallery cards render in the generated HTML. Without JavaScript, their links still open the original artwork. The enhanced reader uses hash links, restores gallery position on return, supports browser Back and left/right/Escape keys, and offers a selectable link when clipboard copying is unavailable.

## Verification

Before initial publication, browser checks covered the ten-card newest-first grid, full-size reader, next navigation, browser Back, direct-link reload, clipboard sharing and one-/two-/three-column responsive layouts. The phone gallery was checked at 320 pixels, the reader at 375 pixels and the tablet grid at 768 pixels without horizontal overflow. Console inspection found no page errors.
