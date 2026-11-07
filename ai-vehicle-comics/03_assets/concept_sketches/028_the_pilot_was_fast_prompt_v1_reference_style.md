# Comic 028 — Reference-Style Generation Prompt v1

Status: generation source for an unselected draft; no gallery approval.

## Pre-production gate — 2026-11-07

The [episode source](../../01_comic_backlog/028_the_pilot_was_fast.md#pre-production-design-check--2026-11-07) records the completed design and identity/context checks before generation. Preserve the locked script. Omit optional fuel/dashboard labels; stationary wheel rotation carries the resource-burn metaphor. Keep the train a faint background hint.

## Exact prompt

```text
Use case: illustration-story
Asset type: unselected draft page for AI Vehicle Comics
Primary request: Create a square 2x2 editorial comic page titled "THE PILOT WAS FAST" using the exact four-panel script below. This is fictional industry-wide enterprise AI satire: leadership mistakes a successful three-car pilot for a scalable commuting model, then recalls keys after systemic gridlock. The tools work; leadership chose the wrong success metric.

Style/medium: minimalist monochrome stick-figure workplace editorial comic. Clean hand-drawn pen-and-ink outlines, light gray marker planes, subtle pencil hatching and grounded shadows. Round heads, dot eyes, spare expressive faces, simple shirts and ties; executive wears a simple gray suit and keeps the same appearance across panels. Vehicles are recognizable generic Formula 1-style open-wheel race cars, slightly more rendered than the people, without logos or sponsorships. Dry professional sarcasm. Match a hand-lettered newspaper workplace cartoon, not a polished racing advertisement.
Composition: near-square white page, large natural medium-weight hand-lettered title at top; four equal panels in a 2x2 grid; thick slightly imperfect black borders; black square number badges containing white "1.", "2.", "3.", "4." in the upper-left corners. One exact narrator caption at the top of each panel, clear of the scene. Large readable regular-weight hand lettering in speech bubbles with unambiguous tails to the correct speakers. Centered bottom kicker outside the grid, small "KKLL" signature at bottom right. Keep margins and all text inside the page. Black, white and gray only. Allocate space for Panel 4's three bubbles before drawing its action.

PAGE TITLE, exact: "THE PILOT WAS FAST"

PANEL 1 — TOP LEFT
Badge: "1."
Narrator caption: "First, everyone got a race car."
Scene: A simple corporate rollout stage, executive on the right of a waist-high key table, employees on the left. A large tray overflowing with race-car keys makes broad availability obvious; only three interested employees are stepping forward. The executive is visibly passing a key to one employee, with many keys left. A generic open-wheel race car is visible beside the stage. Keep the building backdrop spare.
Banner behind stage, exact: "EVERYONE DRIVES"
Executive's sole speech bubble, exact: "We're democratizing speed."
Key handoff and lightly smug executive confidence carry the joke; employees look capable and reasonable.

PANEL 2 — TOP RIGHT
Badge: "2."
Narrator caption: "Three drivers. An entire city to themselves."
Scene: An elevated three-quarter view of a broad city boulevard with two connected cross intersections. Spare rectangular building outlines only. Vast empty road area, green/go signals indicated by the illuminated lower traffic-light lens in grayscale, clear cross streets. EXACTLY THREE open-wheel race cars, each distinct and large enough to count, are driving through the open network; unobtrusive speed lines show real movement. No parked cars, no extra miniature cars, no crowds. Place the executive on the near-right sidewalk speaking into a reporter's microphone; reporter is a simple figure with an unbranded microphone. Driver bubble tail clearly terminates at one of the three visible drivers. Executive's bubble tail clearly points to the suited executive, separate from the driver.
Driver dialogue, exact: "This is incredible."
Executive dialogue, exact: "Our rollout is a huge success."
Establish road geometry for Panel 3: same diagonal boulevard, same two cross junctions, same camera angle, same traffic-signal positions.

PANEL 3 — BOTTOM LEFT
Badge: "3."
Narrator caption: "Then the whole office took the same route."
Scene: Repeat Panel 2's boulevard, two connected cross intersections, camera angle, buildings and traffic-signal positions. Now the same kind of working open-wheel race cars pack every approach. Show two clearly gridlocked junctions: cars block cross traffic and queues spill into the adjoining junction. Use recognizable cars rather than a tiny-car texture. No crashes, broken vehicles or reckless drivers. Shared road capacity and coordination are visibly overwhelmed.
CRITICAL foreground metaphor: At least two large race cars are stopped nose-to-tail at blocked intersections. Their chassis stay fixed behind other cars and stop lines, but their rear wheels have circular rotation strokes and small tire-smoke wisps. No forward speed lines on these stopped cars. Small exhaust/heat strokes reinforce power being consumed without progress. Wheel-spinning is visible from the wheel hubs, with dark scrub marks beneath fixed tires. This is stationary wasted power, not racing through traffic.
A small calm competent traffic-control operator works a signal-control box at the near-right curb. The box has the sole optional scene label "TRAFFIC CONTROL". The operator has a clipboard or controls, with no frantic or foolish gestures. The same suited executive stands beside the operator.
Executive speech bubble, exact: "But the pilot was fast."
Traffic-control operator speech bubble, exact: "There were three cars."
Place bubbles clear of the gridlocked junctions and the foreground spinning wheels; give each line its correct speaker.

PANEL 4 — BOTTOM RIGHT
Badge: "4."
Narrator caption: "Next quarter, the strategy evolved."
Scene: Mirror Panel 1's corporate stage, same executive on the right of the same waist-high table, same employee side on the left, same framing and executive hand gesture. The direction of key transfer is now reversed: an employee holds a key by its ring directly ABOVE an open collection box, dropping it in, and another employee waits with a key in hand. The executive accepts returned keys. A conspicuous pile of returned keys is visible inside the open box. The dominant action is COLLECTING THE KEYS BACK.
Large box label, exact: "KEY RETURNS"
Restrained background banner, exact: "POLICY UPDATE"
Employee bubble on the left, exact: "Why are you taking the keys back?"
Executive's first bubble above/right, exact: "We don't need to drive fast."
Executive's second bubble below it, exact: "We need more people to get to work."
Both executive bubble tails clearly point to the same executive. Read employee question, then first executive statement, then second statement. Keep returned keys and box clear of bubbles.
Background hint only: Through a small distant window at the far edge, a faint tiny unlabelled train silhouette, at most one-tenth the scene width. It has no visible passengers, celebration, destination sign or proof of success. Its tone is much lighter than the key-return action. Do not give it a reveal frame, hero angle or its own dialogue.

BOTTOM KICKER, exact and centered: "The cars were fast. The commute wasn't."
SIGNATURE, exact at bottom right: "KKLL"

Constraints: Preserve exact title, captions, dialogue, banners, return-box label, kicker and signature. Include no additional dialogue. Panel 2 must have exactly three cars. Panel 3 must show visible stationary wheel-spinning and multi-intersection blockage. Panel 4 must be about key recall and the belated metric change. Mirror Panels 1/4 and road logic in Panels 2/3. All characters and surroundings are generic fictional composites.
Avoid: glossy color, cinematic lighting, photorealism, anime, dense architecture, racing decals, vehicle branding, tiny dashboard text, fuel invoices, extra labels, boxed governance signals, driver-training jokes, employee incompetence, angry drivers, IT/security villains, a triumphant solution, a dominant train, employer identities, real people, personal details, watermarks or signatures other than KKLL.
```

## Production record

- Built-in image generation; no CLI/API fallback.
- Textual style foundation: `02_prompt_library/visual_style_master_prompt.md`.
- Reviewed visual references: Comics 001, 003, 015 v3, 017 v5, and 019 signed; the lighter lettering of 003 and grayscale race cars of 015 guide this page.
- No external reporting, personal source brief, or real organizational event is included in the production prompt.
- Preserve every generated iteration in this folder. Selection and gallery promotion require user approval.
