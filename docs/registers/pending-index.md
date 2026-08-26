# Pending Index

> **Trello is the authority for current status, phase label and due date.** This file is only the canonical ID/scope map for `PEN-###` work.

Board: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

## Catalog, categories and product data

| ID | Scope | Canonical links |
|---|---|---|
| `PEN-001` | Validate category mapping with Rodrigo/integration, including unwanted codes and update/overwrite behavior. | `JET-KB-009`–`012`; Integration Matrix |
| `PEN-002` | Close the canonical category tree in Sankhya for JET and future channels. | `JET-KB-009`, `JET-KB-011`; Integration Matrix |
| `PEN-003` | Confirm/implement subcategory navigation by hover. | `MN-DEC-003`; `STR-003` |
| `PEN-004` | Define top categories visible in primary navigation and whether/how `Ver todos` is exposed. | `STR-004` |
| `PEN-005` | Validate upstream/integration brand consolidation such as Deca Metal / Deca Louça → Deca. | Integration Matrix; corrected `MN-DEC-009` |
| `PEN-006` | Prepare JET brand merchandising fields/presentation. | `STR-005`; Integration Matrix |
| `PEN-007` | Complete product-data enrichment flowing toward Sankhya → JET. | `JET-KB-013`–`015`; `STR-006` |
| `PEN-008` | Validate image mapping/order between upstream/Sankhya and JET main/alternative/multifoto roles. | `JET-KB-019`, `JET-KB-020`; `MOD2-VIS-004` |
| `PEN-009` | Validate whether Atributo Único m²/box can be created/updated from Sankhya/integration rather than manually. | `JET-KB-037`, `JET-KB-038`; `UNC-003` boundary |
| `PEN-010` | Confirm m²/box conversion/return behavior in Sankhya/integration. | `JET-KB-040`; `UNC-003` |
| `PEN-011` | Review porcelain-calculator layout/clarity after functional behavior is validated. | `STR-010`; `MOD2-VIS-007B` |
| `PEN-012` | Define Product Similar families and customer-facing dimension (voltage/color/power/etc.). | `JET-KB-025`–`027`; `STR-002` |
| `PEN-013` | Confirm current automation state of “Quem comprou, comprou também”. | `JET-KB-029`; `UNC-002` |

## E-mail, access, store configuration and compliance

| ID | Scope | Canonical links |
|---|---|---|
| `PEN-014` | Configure and validate at least one default transactional sender before publication. | `JET-KB-049`; `MOD1-VIS-003` |
| `PEN-015` | Define sender/copy routing by transactional event and operational need. | `STR-020`; `JET-KB-049` |
| `PEN-016` | Enable/configure Fale Conosco and alert recipients/frequency as applicable. | `JET-KB-050` |
| `PEN-017` | Review transactional e-mail body, subject, tags and communication. | `JET-KB-048`; `STR-021` |
| `PEN-018` | Close current `Editar Dados da Loja` parametrizations, including live verification that automatic sold-out flag updating is `Sim`. | `JET-KB-043`, `JET-KB-051`; Phase 5 |
| `PEN-019` | Validate company registration data and e-mail logo/identity used in automated communications. | Platform Map |
| `PEN-020` | Review/publish privacy policy through the correct JET flow; validate legal content separately. | `JET-KB-056`, `JET-KB-057`; `UNC-006` |
| `PEN-021` | Connect real social-network/Instagram accounts. | `JET-KB-058` |

## Content, storefront and acquisition

| ID | Scope | Canonical links |
|---|---|---|
| `PEN-022` | Confirm official/current dimensions for banner types before production at scale. | `JET-KB-061`; Evidence Map Pack B |
| `PEN-023` | Organize existing banners, names, assets, links and layout placement. | `JET-KB-061`; `STR-019` |
| `PEN-024` | Migrate/review institutional content into JET custom pages, using HTML/source where useful. | `JET-KB-063` |
| `PEN-025` | Execute SEO in the established priority order. | `JET-KB-052`, `JET-KB-053`; `STR-016`, `STR-017` |
| `PEN-026` | Remove test content from product groups while preserving layout-bound group IDs. | `JET-KB-030`, `JET-KB-031`; `JET-RULE-005` |
| `PEN-027` | Define operational handling for Produtos Aguardados / `Avise-me` leads. | `JET-KB-045`, `JET-KB-046`; `STR-012`, `STR-013` |
| `PEN-028` | Structure future category de/para for AnyMarket/marketplaces and Google/XML catalog. | Platform Map; Integration Matrix |

## Payment, freight and launch readiness

| ID | Scope | Canonical links |
|---|---|---|
| `PEN-029` | Study and decide the payment gateway/PSP architecture: JET integration, fees, Pix/card, installments, settlement, reconciliation, antifraud/chargeback and operational constraints. | `JET-KB-069`; `STR-023` |
| `PEN-030` | Study and decide full freight architecture: checkout rating, services/carriers, coverage, deadlines, rules, JET/Sankhya integration, tracking and operational exceptions. | `JET-KB-068`; `STR-022` |
| `PEN-031` | Define target go-live and objective readiness/Go-No-Go criteria using payment/freight viability and other blockers. | `STR-024`; Platform Map |
| `PEN-032` | Plan publication, domain/DNS, cutover window, dependencies, post-publish validation and contingency. | `JET-KB-055`; launch layer |
| `PEN-033` | Review admin users, least-privilege access and first-access/e-mail behavior. | `JET-KB-004`–`006`; `UNC-008`; `MOD1-VIS-001/002` |
| `PEN-034` | Define launch analytics/conversion instrumentation and validate events. | Planning-derived readiness work; not established by training. |
| `PEN-035` | Execute end-to-end purchase/integration tests with evidence. | Critical for `UNC-003`, payment/freight/integration validation. |
| `PEN-036` | Perform evidence-based Go/No-Go and execute cutover if GO. | `STR-024` |
| `PEN-037` | Operate first-seven-day post-go-live hypercare across checkout, integrations and customer-impact signals. | Planning-derived operations |
| `PEN-038` | Confirm current JET support channel, handoff, owners and escalation route. | `JET-KB-070`; `UNC-009` |
| `PEN-039` | Extract Pack A targeted visual evidence from the training videos according to the Phase 4 map. | `docs/evidence/evidence-index.md`; Phase 5 validation |

## Operational rule

Never infer `Backlog`, `Próximo`, `Em andamento`, `Aguardando / Validar`, `Concluído`, phase color or due date from this file. Read Trello live before reporting current state.

This index may retain IDs after their work is completed because the IDs are part of the canonical traceability graph.
