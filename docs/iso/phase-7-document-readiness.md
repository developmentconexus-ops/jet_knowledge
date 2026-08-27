# Phase 7 — PO/IT Document Readiness Gate

## Purpose

Determine which operational documents can be drafted from the canonical JET knowledge layer **without converting unresolved implementation, current-state or business decisions into false procedure**.

This is a readiness gate, not a new task backlog and not a go-live readiness gate. Existing `PEN-###` and `UNC-###` items remain the owners of unresolved work, and Trello remains authoritative for live status.

## Readiness states

- `READY_FOR_DRAFT` — canonical platform/procedure knowledge and guardrails are sufficient to draft a controlled document. Final release may still require owner/format approval.
- `DRAFT_READY_RELEASE_BLOCKED` — the stable platform procedure can be drafted, but Metal Nobre-specific values/choices must be resolved before the document becomes an operational instruction.
- `BLOCKED` — a key system authority, implementation or go-live fact is unresolved; drafting a prescriptive procedure now would encode assumptions.
- `DEFER` — capability exists but is not currently important enough to justify formal documentation.

## Candidate ITs / runbooks

| Candidate document | Readiness | Canonical basis | Release blocker / boundary |
|---|---|---|---|
| IT — Bulk update of JET-managed product fields | `READY_FOR_DRAFT` | `JET-KB-032`, `JET-KB-033`, `JET-RULE-006`, `MOD2-VIS-006` | Must explicitly prohibit using the spreadsheet to bypass Sankhya authority. |
| IT — Product-group maintenance | `READY_FOR_DRAFT` | `JET-KB-030`, `JET-KB-031`, `JET-RULE-005`, `MOD2-VIS-009` | Preserve layout-bound group IDs; actual merchandising content remains business work. |
| IT — Admin user/access management | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-004`–`006`, `MOD1-VIS-001/002` | `PEN-033` must resolve current users, least privilege and first-access/e-mail behavior. Legal interpretation of anonymization remains outside this IT. |
| IT — Configure transactional sender | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-049`, `MOD1-VIS-003` | `PEN-014` must establish current valid sender/domain; `PEN-015` owns event-specific routing. |
| IT — Transactional e-mail template maintenance | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-047`–`050` | `PEN-017` must close actual Metal Nobre content; marketing automation must remain a separate domain. |
| IT — Integration queue operations | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-064`–`066`, `JET-RULE-004`, `MOD1-VIS-004` | Privileged runbook only. Current support/escalation route must be known (`PEN-038`); do not normalize secrets into documentation. |
| IT — Category maintenance | `BLOCKED` | `JET-KB-007`–`012`, Integration Authority Matrix | `PEN-001`/`PEN-002` must close mapping and canonical tree before prescriptive maintenance rules are released. |
| IT — Product master-data maintenance | `BLOCKED` | `JET-KB-013`–`018`, `MN-DEC-001` | `PEN-007` must close enrichment flow; cross-docking mapping remains `UNC-004`. |
| IT — Product image mapping | `BLOCKED` | `JET-KB-019`, `JET-KB-020`, `MOD2-VIS-004` | `PEN-008` must prove integration order/repetition mapping. |
| IT — Product Similar | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-024`–`027`, `MN-DEC-002`, `MOD2-VIS-008` | `PEN-012` must define the actual Metal Nobre families/customer-facing dimension. |
| IT — Porcelain Atributo Único / calculator | `BLOCKED` | `JET-KB-037`–`040`, `MOD2-VIS-007A/B` | `PEN-009` and `PEN-010` must resolve integration and m²/box return conversion; E2E proof belongs to `PEN-035`. |
| IT — Storewide parametrizations / sold-out behavior | `BLOCKED` | `JET-KB-041`–`046`, `JET-KB-051`, `MOD2-VIS-010` | `PEN-018` must record current live settings, especially automatic sold-out flag = `Sim`. |
| IT — Produtos Aguardados / Avise-me lead handling | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-045`, `JET-KB-046`, `MN-DEC-006`, `STR-012/013` | Platform workflow is known; Metal Nobre operating routine/SLA/ownership remains `PEN-027`. |
| IT — Banner maintenance | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-061`, `STR-019` | `PEN-022`/`PEN-023`; official/current dimensions and actual banner organization still open. Pack B visual evidence may be promoted when this IT is authored. |
| IT — Custom institutional pages | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-063` | Actual migration/content remains `PEN-024`; current UI path may require Pack B evidence when authored. |
| IT — Privacy-policy publication flow | `DRAFT_READY_RELEASE_BLOCKED` | `JET-KB-056`, `JET-KB-057` | IT may document the JET publication mechanism only. Legal content cannot be released from training claims; `UNC-006` / `PEN-020`. |
| IT — Social/Instagram configuration | `DEFER` | `JET-KB-058` | Low operational complexity; document only if repeatability/audit need justifies it after `PEN-021`. |
| IT — 301 redirect management | `DEFER` | `JET-KB-059`, `JET-KB-060` | Capability known, but broad migration was intentionally not selected for current rollout. |

## Candidate POs

| Candidate PO | Readiness | Why |
|---|---|---|
| PO — E-commerce order operation | `BLOCKED` | Payment, freight, end-to-end order/integration behavior and go-live criteria are not yet closed (`PEN-029`, `PEN-030`, `PEN-031`, `PEN-035`). |
| PO — Catalog/product governance | `DRAFT_READY_RELEASE_BLOCKED` | Authority model is strong, but category mapping/tree, image mapping, product enrichment and porcelain integration are still active blockers. |
| PO — E-commerce content & merchandising governance | `DRAFT_READY_RELEASE_BLOCKED` | Strategy/ownership boundaries can be drafted, but brand, banners, pages, Product Similar families and launch content are still incomplete. |
| PO — Transactional communication operation | `DRAFT_READY_RELEASE_BLOCKED` | JET capability is known; actual sender/event routing/templates and operational recipients remain open. |
| PO — Launch / cutover operation | `BLOCKED` | Go-live target/readiness, payment, freight, E2E testing and cutover evidence remain active work (`PEN-029`–`PEN-036`). |
| PO — Post-go-live monitoring / hypercare | `DRAFT_READY_RELEASE_BLOCKED` | Planning model exists, but the actual go-live date and final operational surfaces must be known before release (`PEN-037`). |

## First documents worth drafting

The highest-value low-risk first drafts are:

1. **IT — Bulk update of JET-managed product fields** — clear procedure, strong visual evidence, strong authority guardrail.
2. **IT — Product-group maintenance** — clear UI behavior and critical layout-ID safety rule.
3. **IT — Admin user/access management** — draft now, but hold release until `PEN-033` closes current-state behavior.
4. **IT — Integration queue operations** — technical draft only, explicitly privileged and support-mediated.

Do **not** start with a giant all-in-one ecommerce PO. That would force unresolved payment, freight, catalog, integration and launch assumptions into one document.

## Release rule

A document can move from draft to operational/ISO-controlled release only when:

1. every prescriptive Metal Nobre-specific value in the document is supported by a decision/current-state evidence;
2. no relevant `UNKNOWN` / `UNC-###` is silently resolved by prose;
3. system authority matches the Integration Authority Matrix;
4. high-risk mutation steps include verification and rollback/escalation boundaries where applicable;
5. screenshots/UI paths are labeled with interface context when they may drift;
6. legal statements are externally validated when the document contains compliance requirements;
7. any related live blocker that changes the procedure has been resolved or explicitly accepted.

A document being `READY_FOR_DRAFT` does **not** close a `PEN-###`, satisfy go-live readiness or prove the live implementation is correct.

## Phase 7 next increment

Draft the two `READY_FOR_DRAFT` ITs first:

- bulk update of JET-managed product fields;
- product-group maintenance.

Then draft blocked-by-current-state ITs only as controlled drafts, without pretending they are ready for operational release.

## Status

**READINESS GATE COMPLETE.** No PO/IT operational release has been authorized by this gate itself.
