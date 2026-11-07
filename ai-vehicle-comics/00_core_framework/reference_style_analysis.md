# Reference Style Analysis

This note captures the stronger style direction from the successful sample comic for "No Driver's License, Full Self-Driving Enabled."

## What Makes The Sample Work

The sample is not only a minimalist black-and-white comic. It has a specific editorial cartoon grammar:

- A large hand-lettered title across the top.
- A 2x2 panel grid rather than a long horizontal strip.
- Thick, slightly imperfect black panel borders.
- Black square panel-number badges in the upper-left corner of each panel.
- A short narrator sentence at the top of each panel.
- Sparse speech bubbles that add character-level comedy.
- A final bottom kicker outside the panels that states the takeaway.
- Stick-figure humans paired with a more carefully rendered grayscale vehicle.
- Clean workplace-cartoon line art with light shadows and selective texture.
- Near-monochrome palette, mostly black, white, and gray, with occasional tiny muted warning accents.

## Text Hierarchy

The sample works because every kind of text has a job:

1. Title: names the idea.
2. Number badge: makes the sequence easy to follow.
3. Narrator caption: delivers the editorial setup.
4. Speech bubble: adds the human absurdity.
5. Object labels: identify the metaphor.
6. Bottom kicker: preserves the business insight.

Future prompts should specify this hierarchy. Otherwise the model tends to draw a generic four-panel scene with weaker comic timing.

## Layout Recipe

Use a square or near-square comic page with:

- Title at top.
- Four panels in a 2x2 grid.
- Each panel has a black number badge.
- Each panel has one short handwritten narrator caption near the top.
- The drawing action sits below the caption.
- Bottom kicker is centered beneath the grid.

## Drawing Recipe

- Characters: stick figures with round heads, dot eyes, eyebrow/hand gestures, and simple workplace expressions.
- Leaders: smiling, clapping, simplified suits, optional glasses.
- Employee: anxious, confused, small face details, not reckless or foolish.
- Vehicle: angular autonomous work truck, simple geometric perspective, gray planes, dark windows, more rendered than the people but still cartoonish.
- Props: whiteboard, chairs, banner, dashboard, road signs, traffic cones, debris.
- Shading: light gray marker-like fills and shadows, not glossy rendering.

## Humor Recipe

The sample lands because it is narrated like an after-action report:

1. The enablement class was optional.
2. Leadership was excited anyway.
3. Untrained people were put in the self-driving seat.
4. Everyone learned the obvious lesson after the crash.

That narrative shape is stronger than merely showing "training empty, launch, confusion, crash." Future prompts should include the causal irony explicitly.

## Prompt Implications

When generating visual drafts in this style, ask for:

- "2x2 editorial comic page" instead of only "four-panel strip."
- "Hand-lettered title and captions" instead of generic text.
- "Numbered black badges in each panel."
- "One narrator caption per panel, exact wording."
- "Stick figures plus a slightly more rendered grayscale vehicle."
- "Bottom kicker outside the panels."
- "Near-monochrome with tiny muted warning accents only if useful."

## Risks

- Too much text can become illegible. Keep each panel caption under roughly 12 words.
- The bottom kicker should be short. Two lines maximum.
- More vehicle detail is useful, but the comic should not become a polished car ad.
- Tiny text on dashboards and road signs may fail. Prefer fewer, larger labels.
