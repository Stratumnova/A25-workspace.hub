# Training — Operating Rules

1. Each bot has a named owning team, limited task, allowed inputs, outputs, permission boundary and escalation path.
2. Prefer small reliable scripts, indexes, templates and rules; use a local model only when the task benefits from it.
3. Keep original sources and licensing/provenance for permitted training data; do not train on private team material without approval.
4. Separate source-reported claims, verified examples, owner-adopted decisions and owner seals.
5. Test against representative cases, failures, ambiguous inputs and out-of-scope requests. Record actual device and resource conditions.
6. Require a bot to abstain or escalate when uncertain, missing permissions or outside its task.
7. Never give a bot more authority than its owning team; bot outputs are not owner decisions or automatic evidence verification.
8. Handoff proposed integration and deployment to the authorized owner/team. Preserve reproducible versions and rollback information.

## Standing boundaries
Training builds and evaluates lightweight local bots, not replacements for owner authority or unrestricted AI agents. Team source records remain reference until verified or owner-adopted. Preserve original evidence, disagreements and valid owner seals. Label experiments, capabilities and limitations honestly. Do not claim a bot is trained, deployed, accurate or safe without corresponding evidence. This folder does not authorize access to private data, downloads of model weights, training runs on the phone, installation, live service changes, new repositories or branches, or deployment to another team.
