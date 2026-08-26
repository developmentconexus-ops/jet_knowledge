# Canonical Platform Map — JET / Metal Nobre

## Purpose

This map is the human entry point to the canonical JET knowledge layer. It shows the main operational capabilities, the role of JET, the current authority boundary, and the guardrails or unresolved work that matter for Metal Nobre.

It is **not** a live task board. Current `PEN-###` status, phase and due dates remain authoritative only in Trello.

## Authority legend

- `JET` — configuration/content is managed locally in JET in the demonstrated model.
- `SANKHYA` — current upstream system of record in the demonstrated integration.
- `INTEGRATION` — mapping/transport logic controlled by the integration layer or integrator.
- `METAL_NOBRE` — business choice or operating policy.
- `UNKNOWN` — source of truth or implementation is not yet confirmed.

## Capability map

| Capability | JET role | Current authority / source | Canonical operating note | Related |
|---|---|---|---|---|
| Environment / store mutation | Project/store administration | JET | No safe sandbox should be assumed; panel mutations may affect the project/live storefront directly. | `JET-RULE-001` |
| Panel navigation / UI | Admin interface | JET | Tool names and positions may change as JET migrates old/new layouts; documentation must carry UI context. | `RCN-002` |
| Administrator users | User creation and tool-level access | JET | Use least privilege; permissions include sensitive order/customer/admin capabilities. | `PEN-033` |
| Categories | Tree, visibility, URL, SEO, content | Sankhya for tree/name; JET for URL/SEO in current model | Do not treat JET editability as authority. Reordering can mutate hierarchy. | `PEN-001`, `PEN-002`, `JET-RULE-003` |
| Category storefront navigation | Menu/subcategory presentation | JET layout + Metal Nobre choice | Hover behavior and number of top categories remain implementation/UX work. | `PEN-003`, `PEN-004` |
| Product master data | Product identity, stock, price, category, dimensions, media, descriptions | Primarily Sankhya/upstream in current model | JET may expose editable controls that upstream synchronization can overwrite. | `PEN-007`, `JET-RULE-002` |
| Product media | Main, alternative and multifoto display | Sankhya/upstream mapping; JET presentation | Alternative image has a specific hover role; integration ordering must be validated. | `PEN-008` |
| Product video | Video URL in product gallery | JET | Training describes video as JET-local, linked from supported external hosting. | — |
| Brands | Brand association + brand merchandising | Sankhya/integration for association; JET for image/URL/SEO/text/highlight | Brand grouping upstream is unresolved; brand navigation is an intent, not a completed final layout decision. | `PEN-005`, `PEN-006` |
| Tags / labels | Product merchandising labels | JET | JET-local merchandising field; bulk updates require exact expected values. | `JET-RULE-006` |
| Availability messaging | Product availability text | JET | Can expose different messages in listing/detail/cart. | — |
| Product Similar | Variation-like navigation across separate products | JET + Metal Nobre merchandising choice | Current strategy is separate SKUs + Product Similar, not traditional variations. | `MN-DEC-002`, `PEN-012` |
| Traditional variations | Product variants | JET capability / upstream data when used | Supported by JET, but not the current Metal Nobre strategy. | — |
| Related products | Compre Junto / Relacionados / Comprados | JET | Training shows manual relationships; automation of `Comprados` is not confirmed. | `UNC-002`, `PEN-013` |
| Product groups | Home/storefront groups and campaign pages | JET | Existing home groups are layout-bound by IDs; do not delete them casually. | `JET-RULE-005`, `PEN-026` |
| Sets / kits | Catalog constructs | JET | Set lets customer choose components; kit is closed and can apply per-product discount. | — |
| Bulk product update | Spreadsheet-based JET-local updates | JET | Preserve model, column order/names and exact values. Use only for fields that are legitimately JET-managed. | `JET-RULE-006` |
| Porcelain m²/box | Atributo Único + storefront calculator | JET UI; integration authority unresolved | Training demonstrates manual JET setup and calculator behavior; Sankhya integration and return conversion remain unresolved. | `PEN-009`, `PEN-010`, `PEN-011` |
| Out-of-stock behavior | Listing/detail visibility, sold-out flag, Avise-me | JET parameters + Sankhya stock | Detail visibility was changed to allow `Avise-me`; current automatic sold-out setting must be verified live. | `MN-DEC-005`, `PEN-018` |
| Produtos Aguardados | Lead/report workflow for unavailable products | JET + Metal Nobre operating process | Treat interested customers as an operational lead opportunity; process still needs definition. | `MN-DEC-006`, `PEN-027` |
| Transactional e-mail | Automated institutional/customer lifecycle e-mails | JET | Sender, templates, subjects, tags and HTML are configurable. Marketing automation is a different domain. | `PEN-014`, `PEN-015`, `PEN-017` |
| Marketing automation | Campaign/behavioral e-mail | External integrated tools | Training distinguishes this from JET transactional e-mail. | — |
| Alerts / Fale Conosco | Operational alerts and contact intake | JET | Alert recipients/frequency and Fale Conosco layout enablement remain operating work. | `PEN-016` |
| Store parametrizations | Storewide behavior flags | JET | High-impact configuration surface; verify live state before go-live rather than relying on historical screenshots. | `PEN-018` |
| Company/e-mail identity | Company data and e-mail logo | JET | Validate company data and e-mail identity used in automated communications. | `PEN-019` |
| SEO | Store/category/product SEO fields | JET | Priority taught: store → categories → strategic products; performance claims remain guidance, not guarantees. | `MN-DEC-008`, `PEN-025` |
| Sitemap / robots | Search-engine technical controls | JET | Sitemap refresh cadence is uncertain in training and must not be invented. | `UNC-001` |
| Maintenance mode / IP access | Storefront access control | JET | Useful for exceptional operational/cutover scenarios; historical UI paths may drift. | `PEN-032` |
| Privacy policy | Policy content/publication mechanism | JET for publishing; legal authority external | UI capability is known; legal correctness requires separate legal validation. | `UNC-006`, `PEN-020` |
| Social / Instagram | Social links and Instagram showcase | JET + external accounts | Real Metal Nobre accounts still need connection/configuration. | `PEN-021` |
| 301 redirects | Legacy-to-new URL redirect capability | JET + Metal Nobre migration choice | Capability exists; Metal Nobre decided not to perform broad migration initially. | `MN-DEC-007` |
| Banners | Storefront campaign/content surfaces | JET | Desktop/mobile assets, placement, schedule, rotation and links are configurable; exact official dimensions remain pending. | `PEN-022`, `PEN-023` |
| Custom pages | Institutional/custom content | JET | Panel has its own grouping model; storefront presentation can differ. HTML/source migration is possible. | `PEN-024` |
| Integration credentials | Partner/API credentials and scopes | JET + integrator | Privileged configuration surface. Credential values themselves are secrets, not canonical knowledge. | `JET-RULE-004` |
| Integration queues | Domain queues and load/cleanup actions | JET + integrator | Activation controls feed availability; load/cleanup should be operated with integrator/JET support. | `JET-RULE-004` |
| Marketplace taxonomy | Future category mapping toward marketplaces | Integration / AnyMarket path | Training shows de/para concept, not a finished Metal Nobre mapping. | `PEN-028` |
| Google/XML catalog | Catalog distribution capability | Integration / external ecosystem | Training proves capability/context, not completed production configuration. | `PEN-028` |
| Freight | Checkout/logistics ecosystem | UNKNOWN until architecture decision | App Store partner examples do not select the Metal Nobre solution. | `PEN-030` |
| Payment | Checkout payment ecosystem | UNKNOWN until architecture decision | Training transcripts do not define the final gateway/PSP. | `PEN-029` |
| Support handoff | Operational support route | UNKNOWN current state | Training records historical pre-handoff state only. | `UNC-009`, `PEN-038` |
| Go-live readiness | Publication/cutover | Metal Nobre + JET/integrators | Must be evidence-driven across payment, freight, catalog, integrations, access, content and E2E flow. | `PEN-031`–`PEN-037` |

## Cross-cutting guardrails

1. **No assumed sandbox.** Treat mutation as potentially project/live-impacting.
2. **Editable ≠ authoritative.** Resolve source of truth before writing.
3. **Current state beats historical training state for go-live acceptance.**
4. **Recommendation ≠ platform fact.** Keep trainer advice in the Strategy Playbook.
5. **Capability ≠ Metal Nobre decision.** A feature existing does not mean Metal Nobre will use it.
6. **Temporal statements expire.** Revalidate deprecation/support/current-feature claims.
7. **Legal claims require external validation.** JET UI evidence cannot establish legal correctness.

## Consumer routing

- Need to understand the JET surface? → this Platform Map.
- Need the exact canonical statement/provenance? → `knowledge-base.md`.
- Need to know which system owns a field? → `integration-authority-matrix.md`.
- Need Metal Nobre strategy/recommendations? → `strategy-playbook.md`.
- Need proof/timestamps/visual status? → `docs/evidence/evidence-index.md`.
- Need current task status/due date? → Trello, not these documents.
