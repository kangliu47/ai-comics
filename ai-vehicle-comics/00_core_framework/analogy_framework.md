# Analogy Framework

The series uses a compact vehicle metaphor to explain AI capability, adoption, and risk. The analogy should stay useful, legible, and bounded.

## Core Map

| AI Concept | Vehicle Analogy | Notes |
|---|---|---|
| Large language models | Car engines | The power source, not the whole user experience. |
| Frontier reasoning models | Powerful V8-class engines | Impressive, expensive, capable, and often over-discussed. |
| Strong general-purpose models | Refined V6-class engines | Practical, capable, and often enough for real work. |
| Everyday AI assistants such as ChatGPT, Claude Chat, or Copilot | Regular cars, sedans, practical vehicles | Useful today for many tasks without agentic theatrics. |
| Premium Assistant for a selected business pilot group | Tesla Model Y with autopilot | Capable daily-use business vehicle: more powerful than a basic sedan, less reckless than a full autonomous work truck. |
| Coding agents such as Codex or Claude Code | Cybertrucks or autonomous work vehicles | More specialized, more powerful, more operationally risky. |
| Token usage / context budget | Fuel, battery charge, energy, and driving range | Wasteful prompting, oversized context, and unnecessary document dumps burn range. |
| Enterprise data foundations | Trusted maps, navigation data, road signs, and destination information | Bad, missing, stale, or inaccessible information causes the autopilot to route badly. |
| Integrations across enterprise systems | Roads, bridges, access ramps, and open routes | Without route access, useful vehicles cannot reach valuable destinations. |
| AI enablement / literacy | Driver's education and driver's license | People need skills before autonomy can be trusted. |
| Human oversight for agents | Ability to take over the wheel | Autonomy does not remove human accountability. |
| Enterprise governance | Traffic rules, road safety, inspections, fleet management | Makes scale possible without chaos. |
| Security requirements | Guardrails, median barriers, lane shoulders, and rumble strips | Security should be designed into the road, not added as paperwork after launch. |
| PII, secrets, and credentials | Stop signs, no-entry signs, cargo placards, and checkpoints | Make restricted data visible: "NO PII," "NO SECRETS," "NO CREDENTIALS." |
| Logging, monitoring, and auditability | Traffic cameras, dashcams, trip logs, road sensors, and control rooms | Enterprise AI routes need visibility into what happened, where, and why. |
| Zero data retention | No vendor parking lot, no overnight storage, cargo leaves with the vehicle | Vendor AI standards should prevent company data from being stored after the trip. |
| AI operating-model capability | Skilled drivers and mechanics who can actually operate the vehicle | The vehicle can be powerful, but scale depends on people who understand the trip, the controls, and the failure modes. |
| AI operating-model access | Keys, route passes, dispatch assignment, decision rights, and open gates | The right driver must be authorized and paired with the right vehicle, route, and business use case. |
| AI operating-model capacity | Enough lanes, bridges, road crew, merge room, support, and bandwidth | A pilot cannot become a highway if the same narrow lane or overloaded support crew must carry every trip. |

## Central Insight

The AI problem in many enterprises is no longer access to powerful vehicles. It is whether people can drive them, whether the vehicles have enough range for the trip, whether the maps are trustworthy, whether the roads are built, whether the route has guardrails and visibility, and whether anyone is managing traffic.

## Distinguish These Three Layers

Do not collapse tokens, data, and integrations into one generic "foundation" metaphor. They create different enterprise failure modes.

| Layer | Vehicle Role | Enterprise Failure Mode |
|---|---|---|
| Tokens / context budget | Fuel, battery charge, range | Users burn range by loading too much context, asking inefficiently, or using a premium vehicle for short errands. |
| Data foundations | Maps, navigation data, road signs, destination information | The vehicle can move, but the autopilot is guided by stale, incomplete, inaccessible, or misleading information. |
| System integrations | Roads, bridges, ramps, gated access | The vehicle knows where to go but cannot physically reach the system or workflow. |

## Distinguish Operating-Model Pillars

Do not collapse capability, access, and capacity into one generic "readiness" label. They create different scaling failures.

| Pillar | Vehicle Role | Enterprise Failure Mode |
|---|---|---|
| Capability | Skilled driver or AI/data/engineering operator | The organization has road or permission, but the assigned person cannot operate the AI vehicle for the use case. |
| Access | Keys, route passes, dispatch pairing, business decision rights, and open gates | Skilled people and useful vehicles exist, but they are not authorized, matched, or allowed onto the route. |
| Capacity | Lanes, bridges, merge room, road crew, support coverage, and implementation bandwidth | The right driver and vehicle are approved, but the route cannot carry more than a small pilot. |

Access in this operating-model sense is different from system integrations. Access is authorization and pairing; integrations are the physical roads, ramps, and bridges the vehicle uses after authorization.

## Distinguish Security Control Types

Do not collapse security into one generic "governance" sign. Different controls should look different on the road.

| Security Layer | Vehicle Role | Enterprise Failure Mode |
|---|---|---|
| Security requirements | Guardrails and road design standards | The route exists but was not engineered to keep the vehicle inside safe boundaries. |
| Data restrictions | Stop signs, no-entry signs, cargo labels | PII, secrets, or credentials enter a route that was not approved for them. |
| Logging and monitoring | Traffic cameras, trip logs, road sensors | Nobody can reconstruct where the AI vehicle went or what it did. |
| Vendor retention standards | No parking lot, no overnight storage | Data passes through a vendor route and remains stored where it should not. |

## Metaphor Boundaries

Use the vehicle world as a compact explanatory lens, not as worldbuilding. The series should not accumulate lore, recurring villains, invented cities, or elaborate mechanics unless they make a specific enterprise AI point clearer.

The best strips should be readable even if the viewer has never seen another strip in the series.

## Useful Recurring Devices

- Driver's education classroom for enablement gaps.
- Corporate parking garage for license procurement without adoption.
- Battery range, fuel gauge, charging stops, and heavy cargo for token usage.
- Maps, navigation screens, outdated road signs, and missing destinations for data foundations.
- Broken roads, missing bridges, closed ramps, locked gates, and detour signs for integration gaps.
- Autopilot dashboard and takeover wheel for agent oversight.
- Traffic lights, lane markings, inspections, and fleet managers for governance.
- Guardrails, median barriers, shoulder lines, and rumble strips for security requirements.
- Stop signs labeled "NO PII," "NO SECRETS," or "NO CREDENTIALS" for restricted data.
- Traffic cameras, dashcams, trip logs, road sensors, and control rooms for logging, monitoring, and auditability.
- No-parking zones, no overnight storage signs, and vendor rest stops for zero data retention.
- Malicious signs, forged detours, and hijackers for prompt injection and indirect instructions.
- Locked dispatch gates, route passes, and badge readers for decision rights and business access.
- Narrow pilot lanes, missing bridges, and overburdened road crews for capacity constraints.

## Risks To Avoid

- Letting the metaphor become more important than the insight.
- Over-labeling every object in the panel.
- Using futuristic vehicles when a boring sedan makes the joke sharper.
- Treating "more powerful model" as inherently better.
- Turning every punchline into an explanatory slogan.
- Making security a generic blocker instead of a specific designed control.
