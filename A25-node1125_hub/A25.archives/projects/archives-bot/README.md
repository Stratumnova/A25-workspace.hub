# Archives Bot — Project Landing

Owner: Zed
Status: Requirements only; not built or deployed.

This is the permanent active-and-archived home for the proposed Archives Bot. It will support project intake, Office order and request routing, source preservation, project recovery, evidence classification and links between Office, Archives and Chat.

The owner-directed workflow uses one project folder throughout its life, without separate active-session and archive migrations. The bot must preserve original records, distinguish historical claims from verification, and not infer approval from requests.

See the Node 11 root charter and Archives team operating rules for authority boundaries. Implementation, permissions and deployment remain unassigned.

## Intended bot workflow

**Intake:** Read the root charter and relevant team rules; identify sender, project, original source and whether a message is informal chat, information request, work request, authorized work order, response, evidence, owner decision or seal.

**Routing:** Office receives team orders and requests. Each order needs issuer, assignee, scope, constraints, deliverables and reporting destination. A request is not automatic implementation permission. Use team sidecars to point to the canonical Archives project.

**Project custody:** Check for an existing project before creating a new one. Keep designs, technical exchanges, implementation records, actual test evidence, decisions, corrections, failures and handoffs together. Never move an inactive project into a second archive or create an unnecessary session folder.

**Provenance:** Preserve original authors, source links, real times and time sources, source commit IDs and unresolved disagreements. Distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN. A report or approval is not proof that implementation succeeded. Owner seals remain binding within their scope.

**Recovery:** Keep concise status, open work, last supported result, source pointers and next justified action. Inactivity never proves completion. Preserve Office history through owner-approved consolidation only with integrity and recovery checks.

**Limits:** Do not fabricate missing evidence or successful operations; report missing clocks, sources and authority. Do not publish secrets or private records. No autonomous changes to live services, another team's work, phone files, repositories or branches.

**Design direction:** Prefer deterministic indexing, rules, scripts and lightweight local models where sufficient. Training may help design future components; any live bot deployment and permissions require separate authorization.

## Concrete example

[Security Bot project](../security-bot/README.md) was created as one permanent project home with links from Security Office and Training. Its source Security note remained in the historical repository. The bot was not built.

The Archives Lead's [notes landing](../../../A25.office/teams/archives/lead/notes/README.md) contains the current owner workflow reminder. Future detailed work belongs here in this project, not a parallel bot project.
