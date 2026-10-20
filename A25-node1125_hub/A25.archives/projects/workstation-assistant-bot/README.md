# Workstation Assistant Bot — Project Home

Owner: Zed
Status: Owner-proposed future bot; requirements capture only, not built or deployed
Project home: A25.archives/projects/workstation-assistant-bot/
Charter: [Node 11 Hub](../../README.md)

## Purpose

A document-preparation assistant operating before a record is submitted to A25.office, a project repository, or Archives. It assists each responsible human or AI agent in completing their own portion of a work order or other document, then organizes the supplied information into the appropriate section-specific template. Archives receives an attributable, structured record it can index and retrieve for later build orders and information requests.

## Proposed workflow

1. Identify the originating agent, role, team, project, intended destination and document type.
2. Select the approved template for that document and its destination, rather than using one generic form for every team.
3. Guide each contributor through only their required sections. Show missing fields, unclear authority, unsupported claims and inconsistent references. Do not fill missing facts with guesses or impersonate contributors.
4. Preserve the original supplied information and attribute each section to its actual author or source. Separate reported results from independently verified evidence and owner-adopted decisions.
5. Validate the document against the applicable team rules and root charter, including actual timestamps, source links, project identity, order scope and requested response location. An information request is not an implementation order.
6. Prepare a draft for responsible review. Do not silently sign, approve, issue, or publish an order on anyone's behalf.
7. Once authorized, route the final document to its proper Office, repository or project location. Supply Archives with stable record ID, source, document type, project path and links so it can index without reconstructing the source.
8. If a required contribution or authorization is missing, retain a clearly marked incomplete draft and return it to the correct contributor rather than treating it as a completed official record.

## Candidate document classes

Work requests (WR), work orders (WO), information requests (IR), response reports (RR), security notes (SR), audit records (AR), owner decisions (OD), handoffs/recovery (HR), evidence reviews (ER), and owner seals (SEAL). Each type may need different fields and different authorized signers. A template must not confer authority by itself.

## Relationship to other bots

- **Workstation Assistant:** prepares and checks the document before formal filing.
- **Archives Bot:** indexes, preserves, links and recovers the official project record and its sources.
- **Security Bot:** examines changes and reports evidence with monitoring limitations.
- **Office/team leads:** retain their real assignment, review and approval authority.
- **Training/Workshop:** may design or integrate components only under appropriate authorization.

## Required safeguards

No invented answers, approvals, timestamps, verification or author identity. Preserve original content and unresolved GPT/Claude disagreements. Distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN. Keep private and sensitive material outside public GitHub. Never overwrite existing official records or submit documents automatically without separately authorized permissions. Do not create duplicate project homes or an extra active-session tree.

## Open design questions

Approved templates per document type and team; mandatory versus optional fields; who can edit or sign each section; handling drafts and revisions; identity and permissions; validation logic; delivery interfaces; error recovery; offline use; and how Archives receives indexing metadata. These remain future design decisions, not implemented features.

## Project lifecycle

All work on this bot starts and stays in this folder. If development pauses indefinitely, the same folder is its archive. No bot code, template engine, publishing workflow or integration is claimed by this README.
