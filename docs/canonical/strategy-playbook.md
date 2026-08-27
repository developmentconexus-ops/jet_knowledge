# Strategy Playbook — JET / Metal Nobre

## Purpose

This playbook keeps **how Metal Nobre intends to use JET** separate from universal platform behavior.

It contains three kinds of material:

- `DECISION` — explicit Metal Nobre project decision;
- `INTENT` — direction/preference that still depends on implementation or validation;
- `TRAINER_GUIDANCE` — advice from the training that may be useful, but is not a guaranteed fact or mandatory Metal Nobre policy.

Platform facts belong in `knowledge-base.md`; live task status belongs in Trello.

## Catalog and navigation

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-001` | `DECISION` | Keep Sankhya/upstream as the preferred source for integrated product master data. | Avoid divergence and overwrite cycles observed in training. | `MN-DEC-001`; changes to mapping require explicit integration redesign. |
| `STR-002` | `DECISION` | Use separate products/SKUs + `Produto Semelhante` for the current variation-like experience. | Fits current catalog structure and avoids immediate variation remodel. | `MN-DEC-002`; can be revisited later. |
| `STR-003` | `INTENT` | Prefer subcategory disclosure on hover rather than requiring a click. | User preference during category/navigation discussion. | Implementation remains pending in `PEN-003`. |
| `STR-004` | `INTENT` | Keep only the most useful top categories visible in the primary menu and provide broader discovery such as `Ver todos` if needed. | Trainer/layout discussion about limited physical menu space. | Exact number/layout is not yet a decision; `PEN-004`. |
| `STR-005` | `INTENT` | Preserve meaningful shopping/navigation by brand. | Metal Nobre explicitly works with brands and wanted that path retained. | Not a final approved JET layout; `PEN-005`/`PEN-006`; corrected `MN-DEC-009`. |

## Product data and media

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-006` | `DECISION` | Enrich product names, dimensions, images and descriptions upstream so JET receives usable product data through the integration. | Metal Nobre described a third-party enrichment flow feeding Sankhya → JET. | Current work is `PEN-007`/`PEN-008`; exact integration mapping must be validated. |
| `STR-007` | `TRAINER_GUIDANCE` | Use image 1 as main, image 2 as alternative/hover, and ensure gallery images are mapped/repeated as needed. | Demonstrated JET image-role behavior. | Treat as desired mapping pattern, not proof that current integration already does it correctly. |
| `STR-008` | `DECISION` | Do not prioritize encomenda/cross-docking implementation in the immediate rollout. | Explicit project focus decision. | `MN-DEC-010`; capability remains available for future work. |

## Porcelain / m² workflow

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-009` | `INTENT` | Prefer the JET porcelain calculator experience over a raw unit-multiplier-only experience for floor/porcelain products. | Training demonstrated customer entry by m² with box-aware rounding. | Integration of Atributo Único and Sankhya return conversion are still blockers (`PEN-009`, `PEN-010`). |
| `STR-010` | `INTENT` | Improve the visual layout/clarity of the porcelain calculator after the core behavior is validated. | User explicitly asked about improving the layout during training. | `PEN-011`; UX refinement must not mask unresolved quantity/integration logic. |

## Out-of-stock, CRM and merchandising

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-011` | `DECISION` | Keep sold-out product detail accessible so the customer can use `Avise-me`. | Change from `Não` to `Sim` was executed during MOD2. | `MN-DEC-005`; verify current live parameter under `PEN-018`. |
| `STR-012` | `DECISION` | Treat `Produtos Aguardados` / `Avise-me` as a lead source, including possible use for products normally handled by encomenda. | Metal Nobre explicitly identified follow-up opportunity. | Operating routine still needs definition in `PEN-027`. |
| `STR-013` | `TRAINER_GUIDANCE` | Follow up quickly on high-intent awaited-product leads and offer relevant alternatives where useful. | Trainer described decreasing conversion probability with delay. | Strategic advice, not a measured Metal Nobre SLA yet. |
| `STR-014` | `TRAINER_GUIDANCE` | Use `Compre Junto` / related products to suggest contextually complementary bathroom/kitchen items. | Training examples: fittings, seats, valves, accessories. | Manual merchandising until/unless automation is proven. |
| `STR-015` | `TRAINER_GUIDANCE` | Use product groups as campaign landing pages even when they are not placed on the home. | New groups have URLs and can be linked by banners/e-mail. | Preserve existing layout-bound group IDs (`JET-RULE-005`). |

## SEO and acquisition

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-016` | `DECISION` | Execute SEO internally for now rather than hire an agency. | Explicit Metal Nobre choice. | `MN-DEC-008`. |
| `STR-017` | `TRAINER_GUIDANCE` | Prioritize SEO in this sequence: store → categories → strategic/car-flagship products → broader product coverage. | Repeated training guidance. | This is prioritization guidance, not a ranking guarantee. |
| `STR-018` | `DECISION` | Do not perform a broad legacy 301 migration initially. | Low prior ecommerce traffic/sales and limited Google work reduced immediate value. | `MN-DEC-007`; revisit if evidence/traffic changes. |
| `STR-019` | `TRAINER_GUIDANCE` | Keep the number of large/full banners restrained rather than overloading the home. | Trainer suggested roughly 3–4 full banners for perceived performance. | Not a hard JET limit; dimensions/actual layout still need validation. |

## E-mail and operations

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-020` | `INTENT` | Use transactional e-mail copies/remetentes as operational routing where useful, e.g. informing invoicing/separation teams when an order is approved. | Trainer described this as a common operational pattern. | Exact recipients/event mapping is `PEN-015`, not decided here. |
| `STR-021` | `TRAINER_GUIDANCE` | Keep transactional e-mail customer communication clear and contextual using JET tags/subject/body customization. | Demonstrated template capability and trainer advice. | Final content review is `PEN-017`. |

## Integration and go-live

| Strategy ID | Class | Play | Why / source basis | Operational boundary |
|---|---|---|---|---|
| `STR-022` | `DECISION` | Do not select freight architecture merely because a partner appears in the JET App Store. | Training proves ecosystem options, not fit for Metal Nobre. | Historical decision principle; provider study was closed in `PEN-030`. |
| `STR-023` | `DECISION` | Do not infer the payment gateway from training; decide it through current payment work. | Transcripts do not close gateway choice. | Historical decision principle; provider study was closed in `PEN-029`. |
| `STR-024` | `DECISION` | Treat go-live as evidence-based readiness, not “looks ready”. | Current readiness plan requires payment, freight, data, integrations, access, content and E2E evidence. | `PEN-031`–`PEN-036`. |
| `STR-025` | `DECISION` | Use **Pagar.me** as the gateway/PSP for the JET ecommerce. | Explicit provider decision after the payment study; contracting process has started. | `MN-DEC-011`; implementation/validation remains `PEN-042` and E2E proof `PEN-035`. |
| `STR-026` | `DECISION` | Use **Frenet** as the freight hub for the JET ecommerce. | Explicit provider/hub decision after the freight study. | `MN-DEC-012`; implementation/validation remains `PEN-043` and E2E proof `PEN-035`. |

## Strategy that must NOT be promoted

Do not turn the following into Metal Nobre strategy unless a later explicit decision does so:

- trainer guesses about product attributes/competitors;
- trainer opinions about AI models;
- sitemap 12h/24h claim;
- assumed automatic `Quem comprou, comprou também`;
- assumed current support/deprecation state;
- legal/LGPD interpretations from training;
- partner examples as vendor selection.

## Revision rule

When a strategy changes:

1. preserve the old `MN-DEC-*` / `STR-*` reference;
2. record what superseded it and why;
3. update impacted Knowledge Base/Integration Matrix rows;
4. create/update live Trello work only if execution is actually required.
