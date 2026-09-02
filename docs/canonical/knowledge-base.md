# Canonical Knowledge Base — JET / Metal Nobre

## Purpose

This is the normalized knowledge layer derived from:

- MOD1 and MOD2 training transcripts;
- Phase 3 cross-module reconciliation;
- Phase 5 transcript ↔ screen validation;
- explicit Metal Nobre decisions and unresolved questions.

The ledger is intentionally **atomic enough to retrieve safely**, but not one-record-per-sentence. It contains only statements that materially affect operation, documentation, integration, strategy or future agent behavior.

## Consumption rules

- `PLATFORM_FACT` describes demonstrated JET behavior/capability, not a Metal Nobre choice.
- `INTEGRATION_RULE` describes the current demonstrated authority/mapping model.
- `METAL_NOBRE_DECISION` is project-specific and may later be superseded.
- `STRATEGIC_GUIDANCE` is advice/strategy, not guaranteed platform behavior.
- `RISK_GUARDRAIL` constrains potentially damaging actions.
- `TRAINER_UNCERTAINTY` and `OPEN_QUESTION` must never be completed by inference.
- Historical training state is not automatically current go-live state.

## Environment, UI and administration

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-001` | `RISK_GUARDRAIL` | In the demonstrated Metal Nobre project, no safe sandbox/homologation environment should be assumed; panel mutations may affect the project/live storefront. | JET / `CONFIRMED` | CRITICAL | MOD1 00:53–01:24; `JET-RULE-001` |
| `JET-KB-002` | `PLATFORM_FACT` | JET was migrating tools between old and new admin layouts; tool names and locations may differ by interface version. | JET / `CONFIRMED` at training time | MEDIUM | MOD1 16:22–17:34; `RCN-002` |
| `JET-KB-003` | `PROCEDURE` | Use the current visible tool/tab name as the operative UI reference; `Ajuda` / `Saiba mais` routes to JET Experience/tutorial material in the demonstrated interface. | JET / `CONFIRMED` | LOW | MOD1 16:22–17:34 |
| `JET-KB-004` | `PLATFORM_FACT` | Administrator users can be granted access at tool/module level; disabled tools are not shown to that user. | JET / `CONFIRMED` | HIGH | MOD1 09:00–10:45; `MOD1-VIS-001` |
| `JET-KB-005` | `RISK_GUARDRAIL` | Admin permissions include sensitive controls such as customer anonymization, order-status removal/change, monetary/dashboard visibility and user administration; use least privilege. | JET + Metal Nobre / `CONFIRMED` | HIGH | MOD1 13:06–14:21; `MOD1-VIS-002`; `PEN-033` |
| `JET-KB-006` | `TRAINER_UNCERTAINTY` | The exact relationship between project-mode first access, temporary-password e-mail delivery, publication infrastructure and configured sender was not technically demonstrated end to end. | UNKNOWN / `UNCERTAIN` | MEDIUM | `UNC-008`; `PEN-033` |

## Categories and navigation

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-007` | `PLATFORM_FACT` | JET supports up to three demonstrated category levels. | JET / `CONFIRMED` | LOW | MOD2 02:01–06:16; `MOD2-VIS-001` |
| `JET-KB-008` | `PLATFORM_FACT` | A category with no linked product is not shown on the storefront in the demonstrated behavior. | JET / `CONFIRMED` | LOW | MOD2 02:01–06:16 |
| `JET-KB-009` | `INTEGRATION_RULE` | In the current demonstrated integration, category hierarchy/name originates from Sankhya; a direct JET name edit can be overwritten by later upstream synchronization. | SANKHYA / `CONFIRMED` | HIGH | MOD2 02:01–06:16; `PEN-001`, `PEN-002` |
| `JET-KB-010` | `INTEGRATION_RULE` | Category URL and category SEO are described as JET-local in the current mapping and are not overwritten by the demonstrated category-name synchronization. | JET / `CONFIRMED` | MEDIUM | MOD2 02:01–06:16 |
| `JET-KB-011` | `RISK_GUARDRAIL` | `Reordenar categorias` can move items between hierarchy levels/families, not only change visual order; do not reorder casually when Sankhya owns the tree. | JET + SANKHYA / `CONFIRMED` | HIGH | MOD2 22:53–26:04; `MOD2-VIS-002`; `JET-RULE-003` |
| `JET-KB-012` | `PROCEDURE` | For category deletion in the demonstrated workflow, remove linked products first and delete from lower level toward parent; Metal Nobre should additionally respect upstream Sankhya ownership. | JET + SANKHYA / `CONFIRMED` | HIGH | MOD2 22:53 onward; `JET-RULE-003` |

## Product master data and integration authority

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-013` | `INTEGRATION_RULE` | In the demonstrated mapping, product name, GTIN, NCM, product code, stock, price and category are sourced from Sankhya/upstream and should not be maintained independently in JET. | SANKHYA / `CONFIRMED` | CRITICAL | MOD2 51:07–54:17; `MOD2-VIS-003`; `MN-DEC-001` |
| `JET-KB-014` | `INTEGRATION_RULE` | Product weight/dimensions are expected from Sankhya/upstream when populated; training identifies these as package dimensions relevant to freight calculation. | SANKHYA / `CONFIRMED` for demonstrated mapping | HIGH | MOD2 53:53–55:15; `PEN-007` |
| `JET-KB-015` | `INTEGRATION_RULE` | Product images and descriptions were intended to flow from upstream/Sankhya in the Metal Nobre implementation. | SANKHYA / `CONFIRMED` for current model | HIGH | MOD2 55:40–59:40; `PEN-007`, `PEN-008` |
| `JET-KB-016` | `PLATFORM_FACT` | Product URL can be changed locally in JET in the demonstrated product editor. | JET / `CONFIRMED` | MEDIUM | MOD2 51:07 onward |
| `JET-KB-017` | `RISK_GUARDRAIL` | JET UI editability does not establish source of truth. Quick Edit exposes fields such as stock/price/cross-docking/status, but Metal Nobre must respect upstream authority. | SANKHYA + JET / `CONFIRMED` | CRITICAL | MOD2 ~46:00–51:07; `JET-RULE-002` |
| `JET-KB-018` | `OPEN_QUESTION` | Cross-docking exists as a JET product field and represents added delivery lead time, but its actual source/mapping in Sankhya is not confirmed. | UNKNOWN / `UNCERTAIN` | HIGH | `UNC-004` |

## Product media and merchandising fields

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-019` | `PLATFORM_FACT` | JET distinguishes main image, alternative image and multifotos; the alternative image is used for the demonstrated listing-hover behavior. | JET / `CONFIRMED` | MEDIUM | MOD2 55:40–59:02; `MOD2-VIS-004` |
| `JET-KB-020` | `INTEGRATION_RULE` | The intended Metal Nobre image mapping requires validating upstream order/repetition so the desired images land in main, alternative and multifoto roles. | INTEGRATION / `CONFIRMED` need for validation | HIGH | `PEN-008` |
| `JET-KB-021` | `PLATFORM_FACT` | Product video is configured locally in JET in the demonstrated model through a hosted-video link. | JET / `CONFIRMED` | LOW | MOD2 59:02 onward |
| `JET-KB-022` | `PLATFORM_FACT` | JET supports product labels/tags as a merchandising overlay; the training says up to four can be associated with a product. | JET / `CONFIRMED` | LOW | MOD2 01:06:18 onward |
| `JET-KB-023` | `PLATFORM_FACT` | Product availability messaging can be configured in JET and displayed in listing, product detail and cart contexts depending on the configured messages. | JET / `CONFIRMED` | LOW | MOD2 ~41:19–46:00 |

## Variations, Product Similar and relationships

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-024` | `PLATFORM_FACT` | JET supports traditional variations and multiple presentation types such as text/image/color palette. | JET / `CONFIRMED` | LOW | MOD2 27:12–35:14 |
| `JET-KB-025` | `METAL_NOBRE_DECISION` | Current Metal Nobre strategy is separate products/SKUs plus `Produto Semelhante` for a variation-like customer experience, rather than restructuring into traditional JET variations now. | METAL_NOBRE / `METAL_NOBRE_DECISION` | MEDIUM | `MN-DEC-002`; `PEN-012` |
| `JET-KB-026` | `PLATFORM_FACT` | `Produto Semelhante` can group separate products and expose choices using palette, product image, text or uploaded image; the grouping name is customer-facing. | JET / `CONFIRMED` | MEDIUM | MOD2 01:34:56–01:40:47; `MOD2-VIS-008` |
| `JET-KB-027` | `PLATFORM_FACT` | Training states one Product Similar grouping per product. | JET / `CONFIRMED` at training time | MEDIUM | MOD2 01:40:00–01:40:47 |
| `JET-KB-028` | `PLATFORM_FACT` | JET exposes three demonstrated related-product relationship types: `Compre Junto`, `Relacionados` and `Comprados`. | JET / `CONFIRMED` | LOW | MOD2 01:08:34–01:15:27 |
| `JET-KB-029` | `TRAINER_UNCERTAINTY` | At training time, the trainer said `Comprados` / “Quem comprou, comprou também” was manual and was unsure whether an intelligent/automatic strategy was operating. | UNKNOWN / `UNCERTAIN` | MEDIUM | `UNC-002`; `PEN-013` |

## Groups, bulk updates, sets and kits

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-030` | `RISK_GUARDRAIL` | Existing Metal Nobre home product groups are tied to fixed layout positions by ID; do not delete them casually. | JET layout / `CONFIRMED` | HIGH | MOD2 01:40:48–01:44:19; `MOD2-VIS-009`; `JET-RULE-005` |
| `JET-KB-031` | `PLATFORM_FACT` | New product groups can be created and have their own URL, but they do not automatically appear on the home layout unless the layout is changed. | JET / `CONFIRMED` | MEDIUM | MOD2 01:40:48–01:44:19 |
| `JET-KB-032` | `RISK_GUARDRAIL` | JET bulk product update requires the official model spreadsheet; do not change formatting, column names/order or expected exact values. Product code is required for update targeting in the demonstrated flow. | JET / `CONFIRMED` | HIGH | MOD2 01:15:27–01:20:00; `MOD2-VIS-006`; `JET-RULE-006` |
| `JET-KB-033` | `PROCEDURE` | Bulk spreadsheet should be used for JET-managed fields only; upstream-authoritative fields should not be used to bypass the integration authority model. | METAL_NOBRE + JET / `CONFIRMED` derivation from authority rules | HIGH | `JET-KB-013`, `JET-KB-017`, `JET-RULE-006` |
| `JET-KB-034` | `PLATFORM_FACT` | In the demonstrated catalog model, a `Conjunto` lets the customer choose which linked items to buy and does not provide the same kit-discount mechanism. | JET / `CONFIRMED` | LOW | MOD2 01:20:00–01:22:26 |
| `JET-KB-035` | `PLATFORM_FACT` | A `Kit` is purchased as a closed set and can apply discount per linked product; kit availability is constrained by component stock in the demonstrated behavior. | JET / `CONFIRMED` | MEDIUM | MOD2 01:22:09–01:28:25 |

## Product quantity controls and porcelain

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-036` | `PLATFORM_FACT` | Product unit multiplier enforces allowed purchase multiples; min/max purchase limits are separate controls. | JET / `CONFIRMED` | MEDIUM | MOD2 01:06:18–01:13:17 |
| `JET-KB-037` | `PLATFORM_FACT` | `Atributo Único` was demonstrated as the JET mechanism used to associate meter-per-box values with porcelain/floor products and enable the calculator. | JET / `CONFIRMED` | HIGH | MOD2 01:28:28–01:34:54; `MOD2-VIS-007A/B` |
| `JET-KB-038` | `CURRENT_STATE` | At training time the Atributo Único value/linking process was manual in JET; possible Sankhya integration was left for Rodrigo/integration validation. | JET + INTEGRATION / `CONFIRMED` historical + unresolved future | HIGH | `PEN-009` |
| `JET-KB-039` | `PLATFORM_FACT` | The demonstrated porcelain calculator shows price per m² and per box and rounds requested area to valid box multiples; the cart reflects the resulting box quantity. | JET / `CONFIRMED` | HIGH | MOD2 01:31:01–01:34:19; `MOD2-VIS-007B` |
| `JET-KB-040` | `OPEN_QUESTION` | The return/conversion behavior between sold m²/box quantities and Sankhya inventory/order representation was not confirmed as implemented. | UNKNOWN / `UNCERTAIN` | CRITICAL | `UNC-003`; `PEN-010` |

## Out-of-stock and customer-interest workflow

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-041` | `PLATFORM_FACT` | JET separately controls whether sold-out products appear in listing pages and whether their detail pages remain accessible. | JET / `CONFIRMED` | HIGH | MOD1 34:12–35:46; MOD2 01:45:19 onward |
| `JET-KB-042` | `METAL_NOBRE_DECISION` | During MOD2, Metal Nobre changed sold-out product-detail visibility from `Não` to `Sim`, enabling the demonstrated `Avise-me` flow. | METAL_NOBRE / `METAL_NOBRE_DECISION` | HIGH | `MN-DEC-005`; `MOD2-VIS-010` |
| `JET-KB-043` | `CURRENT_STATE` | Training records an instruction/execution to enable automatic sold-out flag updating; the Pack A screenshot caught the pre-action `Não`, so current live `Sim` must be verified in JET before go-live. | METAL_NOBRE / historical `CONFIRMED`, current state requires validation | CRITICAL | `MN-DEC-004`; Phase 5; `PEN-018` |
| `JET-KB-044` | `PLATFORM_FACT` | When sold-out product detail is hidden, the demonstrated product URL can return 404; enabling detail access allows the unavailable-product page and `Avise-me`. | JET / `CONFIRMED` | HIGH | MOD2 01:45:19–01:46:03; `MOD2-VIS-010` |
| `JET-KB-045` | `PLATFORM_FACT` | `Produtos Aguardados` shows products/customers waiting for unavailable items and supports customer-interest/report workflows in the demonstrated interface. | JET / `CONFIRMED` | MEDIUM | MOD2 01:46:45–01:49:05; `MOD2-VIS-010` |
| `JET-KB-046` | `METAL_NOBRE_DECISION` | Metal Nobre identified `Avise-me` / Produtos Aguardados as an opportunity for lead follow-up, including potential use with products normally handled by order/encomenda. | METAL_NOBRE / `METAL_NOBRE_DECISION` | MEDIUM | `MN-DEC-006`; `PEN-027` |

## E-mail, alerts and customer communication

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-047` | `PLATFORM_FACT` | JET transactional/institutional e-mails are distinct from marketing/campaign automation; the training describes marketing automation as external/integrated tooling. | JET / `CONFIRMED` | MEDIUM | MOD1 20:50–21:53; `RCN-009` |
| `JET-KB-048` | `PLATFORM_FACT` | JET transactional e-mail templates are customizable in body, subject, tags and HTML/source in the demonstrated interface. | JET / `CONFIRMED` | MEDIUM | MOD1 24:10–28:30; `PEN-017` |
| `JET-KB-049` | `PLATFORM_FACT` | The training states at least one default sender is required before publication; sender identity can be configured and different events can use different senders/copies. | JET / `CONFIRMED` | HIGH | MOD1 21:53–29:15; `MOD1-VIS-003`; `PEN-014`, `PEN-015` |
| `JET-KB-050` | `PLATFORM_FACT` | JET alert configuration includes demonstrated alert sources such as Fale Conosco and Produto Aguardado, with recipient/frequency controls. | JET / `CONFIRMED` | LOW | MOD1 17:34–20:30; `PEN-016` |

## Storewide configuration, SEO and content

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-051` | `RISK_GUARDRAIL` | `Editar Dados da Loja` contains storewide behavior flags affecting sold-out visibility, zero-value display, discount basis and awaited-product e-mail behavior; live settings should be verified before launch. | JET / `CONFIRMED` | CRITICAL | MOD1 32:24–40:35; `MOD1-VIS-005`; `PEN-018` |
| `JET-KB-052` | `STRATEGIC_GUIDANCE` | SEO priority taught in training is store SEO first, category SEO second, then strategic/car-flagship products before broad product coverage. | TRAINER / `TRAINER_RECOMMENDATION` | LOW | MOD2 06:16 onward; MOD1 41:33–47:11; `PEN-025` |
| `JET-KB-053` | `METAL_NOBRE_DECISION` | Metal Nobre intends to execute SEO internally rather than hire an agency at this stage. | METAL_NOBRE / `METAL_NOBRE_DECISION` | LOW | `MN-DEC-008` |
| `JET-KB-054` | `TRAINER_UNCERTAINTY` | Sitemap refresh timing was stated inconsistently/without confirmation; do not encode a 12h or 24h SLA from the training. | UNKNOWN / `UNCERTAIN` | MEDIUM | `UNC-001` |
| `JET-KB-055` | `PLATFORM_FACT` | JET provides maintenance mode and IP access controls in the demonstrated store configuration. | JET / `CONFIRMED` | MEDIUM | MOD1 47:57–48:56 |
| `JET-KB-056` | `PLATFORM_FACT` | JET provides a privacy-policy publication/configuration surface; this establishes the UI mechanism only, not legal correctness. | JET / `CONFIRMED` | HIGH | MOD1 48:56–50:14; `PEN-020` |
| `JET-KB-057` | `LEGAL_CLAIM_NEEDS_VERIFICATION` | Verbal legal/LGPD claims from training must be externally validated before becoming compliance rules or agent guardrails. | EXTERNAL / `REQUIRES_EXTERNAL_VERIFICATION` | CRITICAL | `UNC-006` |
| `JET-KB-058` | `PLATFORM_FACT` | JET supports social-network links and an Instagram showcase/integration surface in the demonstrated project. | JET / `CONFIRMED` | LOW | MOD1 ~50:31–52:45; `PEN-021` |
| `JET-KB-059` | `PLATFORM_FACT` | JET provides 301 redirect capability with source/destination URL mapping. | JET / `CONFIRMED` | MEDIUM | MOD1 53:28–58:34 |
| `JET-KB-060` | `METAL_NOBRE_DECISION` | Metal Nobre chose not to execute a broad legacy-URL 301 migration initially because the previous ecommerce had low traffic/sales and little developed Google work. | METAL_NOBRE / `METAL_NOBRE_DECISION` | MEDIUM | `MN-DEC-007` |
| `JET-KB-061` | `PLATFORM_FACT` | Banner management supports demonstrated desktop/mobile assets, redirects, types/placement, scheduling, randomization, video and ordering. | JET / `CONFIRMED` | MEDIUM | MOD1 58:57–01:07:58; `PEN-022`, `PEN-023` |
| `JET-KB-062` | `STRATEGIC_GUIDANCE` | Trainer advised keeping roughly three to four full banners for perceived performance; this is guidance, not a benchmarked hard platform limit. | TRAINER / `TRAINER_RECOMMENDATION` | LOW | `RCN-012` |
| `JET-KB-063` | `PLATFORM_FACT` | Custom institutional pages support editable name/content/URL/SEO and HTML/source; panel grouping and storefront presentation are separate concepts. | JET / `CONFIRMED` | MEDIUM | MOD1 01:08:22–01:11:22; `PEN-024` |

## Integrations, ecosystem and temporal claims

| ID | Type | Canonical statement | Authority / certainty | Risk | Evidence / related |
|---|---|---|---|---|---|
| `JET-KB-064` | `PLATFORM_FACT` | JET integration credentials expose partner credential/scoping controls in the demonstrated interface. | JET / `CONFIRMED` | CRITICAL | MOD1 29:23–31:15; `MOD1-VIS-004` |
| `JET-KB-065` | `PLATFORM_FACT` | JET uses separated integration queues by domain (examples shown include brand, product, stock and price); active queues are fed for integrator consumption. | JET / `CONFIRMED` | CRITICAL | MOD1 31:15–32:09; `MOD1-VIS-004` |
| `JET-KB-066` | `RISK_GUARDRAIL` | Queue load/cleanup and related technical operations should be treated as privileged and performed with the integrator/JET support, not as routine operator actions. | JET + INTEGRATION / `CONFIRMED` | CRITICAL | `JET-RULE-004` |
| `JET-KB-067` | `PLATFORM_FACT` | JET App Store/ecosystem demonstrated specialized partner integrations, including freight examples; partner presence proves integration capability only. | JET ecosystem / `CONFIRMED` at training time | LOW | MOD1 01:12:44–01:14:34 |
| `JET-KB-068` | `METAL_NOBRE_DECISION` | Metal Nobre selected **Frenet** as the freight hub for the JET ecommerce after the freight study. Provider selection is decided; integration/configuration and end-to-end operational validation remain open. | METAL_NOBRE / `METAL_NOBRE_DECISION` | CRITICAL | `MN-DEC-012`; `STR-026`; `PEN-043`; `PEN-035` |
| `JET-KB-069` | `METAL_NOBRE_DECISION` | Metal Nobre selected **Pagar.me** as the gateway/PSP for the JET ecommerce and began the contracting process. Provider selection is decided; integration/configuration and end-to-end payment validation remain open. | METAL_NOBRE / `METAL_NOBRE_DECISION` | CRITICAL | `MN-DEC-011`; `STR-025`; `PEN-042`; `PEN-035` |
| `JET-KB-070` | `CURRENT_STATE` | At MOD1 training time, support handoff to the normal JET support route had not yet been confirmed complete; current support route must be revalidated. | UNKNOWN current / historical `CONFIRMED` | MEDIUM | `UNC-009`; `PEN-038` |
| `JET-KB-071` | `DEPRECATED/EVOLVING_FEATURE` | Trainer stated that customer product comments were being discontinued at training time; this is a temporal statement and is not safe as a permanent current fact. | JET historical / requires current revalidation | MEDIUM | `UNC-010` |

## Project-specific decisions and intent not to flatten into platform facts

The authoritative decision register remains `docs/registers/decisions.md`. In this Knowledge Base, decisions are included only when they directly change how a platform capability is to be interpreted or operated.

Notably:

- `MN-DEC-009` is **not** a final brand-layout decision. It records only the intent to preserve brand navigation, pending implementation/validation.
- `MN-DEC-010` records that encomenda/cross-docking is not an immediate implementation focus; it does not remove JET capability or future use.
- `MN-DEC-011` / `MN-DEC-012` close provider selection for payment/freight only; they do not prove the integrations are configured or accepted.

## Live-state boundary

This file must never answer “what is currently in progress / due / waiting?” from embedded history. Read the Trello board live for current status. This file answers only what the project currently knows and how that knowledge is classified.
