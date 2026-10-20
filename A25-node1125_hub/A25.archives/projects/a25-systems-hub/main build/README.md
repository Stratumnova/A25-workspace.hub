# A25 Systems Hub — Main Build Integration

Owner: Zed
Status: Integration landing only; no assembled system or deployment

This folder is where the separately built and verified A25 Systems Hub components are connected into one working system **after scoped authorization**. It is not the development home for each component.

## Component boundaries

- [A25chatroom](../A25chatroom/README.md): first planned component, durable GPT/Claude/owner messaging.
- Future components such as terminals, tunnels, authentication, storage and recovery will receive their own sibling folders **when actually needed and authorized**. Do not create empty placeholder components now.

Each component owns its source, design, tests, failures, revisions and recovery at its permanent location. Integration may use approved versions, interfaces, build artifacts or explicit references; it must not move the component's canonical workspace. If one part fails, isolate and fix that component, verify it, then update integration under an authorized order.

## Integration gate

Before connecting a component: identify its version/source commit, required interfaces, security review, reproducible tests, known risks, owner approvals, rollback and recovery. Record actual outcomes, not predicted PASS claims. Never treat an Archives folder or GitHub commit as proof of a running system.

Use only the existing repository on main. No fork, new branch, new repository, old-repo edits, secrets, phone actions, tunnel changes or deployment without separate owner authorization.

Read [parent project onboarding](../ONBOARDING.md) and [Node 11 charter](../../../../README.md).
