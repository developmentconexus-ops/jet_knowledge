# Integration Authority Matrix — JET / Metal Nobre

## Purpose

This matrix answers a specific operational question:

> **For each important data domain, where should Metal Nobre treat the authoritative value as coming from before changing it?**

It reflects the **current demonstrated training/integration model**, not a universal JET architecture. Any future mapping change must explicitly supersede the relevant row rather than silently assuming the authority changed.

## Authority states

- `SANKHYA` — upstream system of record in the current demonstrated mapping.
- `JET` — local JET-managed configuration/content.
- `INTEGRATION` — transformation/mapping responsibility belongs to the integration layer/integrator.
- `METAL_NOBRE` — business/operating decision, usually implemented in another system.
- `UNKNOWN` — not yet confirmed; do not automate writes until resolved.

## Core matrix

| Data / capability | Current authority | JET may expose edit? | Safe operating rule | Validation / pending |
|---|---|---:|---|---|
| Category hierarchy | `SANKHYA` | Yes | Build/change the canonical tree upstream; do not use JET reordering to redesign hierarchy casually. | `PEN-001`, `PEN-002` |
| Category name | `SANKHYA` | Yes | Direct JET edits can be overwritten by synchronization in current mapping. | `PEN-001` |
| Category status/visibility | `JET` surface, integration interaction possible | Yes | Treat current configuration deliberately; do not infer upstream ownership from UI alone. | verify during category readiness |
| Category URL | `JET` | Yes | JET-local in demonstrated mapping. | — |
| Category SEO title/meta | `JET` | Yes | Maintain in JET unless a future integration mapping explicitly changes authority. | `PEN-025` |
| Category page text/content | `JET` | Yes | JET-local content surface. | category content strategy |
| Category image | `JET` in training context | Yes | Treat as JET merchandising/content unless future mapping says otherwise. | — |
| Product name | `SANKHYA` / upstream enrichment flow | Yes | Change upstream; current sync can overwrite JET. | `PEN-007` |
| GTIN | `SANKHYA` | Yes / displayed | Change upstream, not independently in JET. | — |
| NCM | `SANKHYA` | Yes / displayed | Change upstream, not independently in JET. | — |
| Product code | `SANKHYA` | Restricted/displayed | Preserve upstream identity. | — |
| Product stock | `SANKHYA` | Yes through some JET controls | Do not use JET Quick Edit/manual control as normal Metal Nobre stock authority. | `JET-RULE-002` |
| Product price | `SANKHYA` | Yes through some JET controls | Change upstream; avoid JET-local divergence. | `JET-RULE-002` |
| Product category association | `SANKHYA` | Yes | Maintain upstream in current model. | `PEN-001`, `PEN-002` |
| Product weight | `SANKHYA` / upstream | Yes | Populate upstream; package weight participates in freight logic. | `PEN-007` |
| Product dimensions | `SANKHYA` / upstream | Yes | Populate package dimensions upstream; validate completeness before freight/E2E readiness. | `PEN-007`, `PEN-043`, `PEN-035` |
| Product descriptions | `SANKHYA` / upstream | Yes | Current intended flow is upstream → JET. | `PEN-007` |
| Main product image | `SANKHYA` / upstream + `INTEGRATION` mapping | Yes | Upstream order/mapping must land correctly as main image. | `PEN-008` |
| Alternative image | `SANKHYA` / upstream + `INTEGRATION` mapping | Yes | Validate how image order maps to hover-role alternative image. | `PEN-008` |
| Multifotos | `SANKHYA` / upstream + `INTEGRATION` mapping | Yes | Validate repetition/order rules so all desired photos reach gallery. | `PEN-008` |
| Product URL | `JET` | Yes | JET-local in demonstrated model. | — |
| Product video | `JET` | Yes | Add hosted-video link locally in JET. | — |
| Product label/tag | `JET` | Yes | JET-local merchandising field; mass update only using official model/exact values. | `JET-RULE-006` |
| Product availability text | `JET` | Yes | JET-local merchandising/operational message. | — |
| Product Similar grouping | `JET` + `METAL_NOBRE` choice | Yes | Define families/dimension intentionally; do not confuse with upstream product identity. | `MN-DEC-002`, `PEN-012` |
| Traditional variation data | Upstream when used + JET presentation | Yes | Not current Metal Nobre strategy; future adoption requires explicit remapping/design. | — |
| Related products (`Compre Junto`, `Relacionados`, `Comprados`) | `JET` | Yes | Treat as JET merchandising relationships. `Comprados` automation remains unconfirmed. | `UNC-002`, `PEN-013` |
| Product group membership | `JET` | Yes | Edit linked products, but preserve layout-bound group IDs. | `PEN-026`, `JET-RULE-005` |
| New product groups | `JET` | Yes | New group gets URL; home placement requires layout work. | — |
| Kit / Conjunto definitions | `JET` | Yes | JET catalog constructs unless a future integration explicitly adopts them. | — |
| Product multiplier / min-max limits | `JET` | Yes | Use only when Metal Nobre has an explicit selling rule; do not assume porcelain should use multiplier instead of calculator. | future rule if activated |
| Cross docking / added lead time | `UNKNOWN` | Yes | Do not automate or establish authority until Sankhya/integration mapping is confirmed. | `UNC-004`, `MN-DEC-010` |
| Atributo Único m²/caixa | `UNKNOWN` integration authority; manual JET at training time | Yes | Historical process is JET-manual; do not assume Sankhya integration exists. | `PEN-009` |
| m²/box order/inventory return conversion | `UNKNOWN` / `INTEGRATION` | n/a | Must be proven by integration evidence/test before operational acceptance. | `UNC-003`, `PEN-010`, `PEN-035` |
| Brand association on product | `SANKHYA` / `INTEGRATION` | Yes | Association comes upstream in demonstrated model. | `PEN-005` |
| Brand consolidation/grouping (e.g. Deca Metal/Louça → Deca) | `INTEGRATION` | n/a | Resolve mapping before JET receives brand taxonomy. | `PEN-005` |
| Brand image | `JET` | Yes | JET-local brand merchandising. | `PEN-006` |
| Brand URL | `JET` | Yes | JET-local in demonstrated model. | `PEN-006` |
| Brand SEO/text | `JET` | Yes | JET-local brand content. | `PEN-006` |
| Brand home/highlight flag | `JET` | Yes | Capability exists; final brand presentation still requires project validation. | `PEN-006`, corrected `MN-DEC-009` |
| Sold-out product-detail visibility | `JET` | Yes | Current project intent/executed training change is to allow detail page for `Avise-me`; verify live under readiness. | `MN-DEC-005`, `PEN-018` |
| Automatic sold-out flag update | `JET` parameter + `SANKHYA` stock input | Yes | Training instructed `Sim`; current live state must be verified before completion. | `MN-DEC-004`, `PEN-018` |
| Transactional e-mail sender | `JET` config + Metal Nobre e-mail identity | Yes | Configure at least one valid default sender before publication per training. | `PEN-014` |
| Transactional e-mail body/subject/tags | `JET` | Yes | Review and maintain in JET. | `PEN-017` |
| Event-specific sender/copies | `JET` + `METAL_NOBRE` operating choice | Yes | Define routing intentionally for operational alerts/workflows. | `PEN-015` |
| Marketing automation | External integrated tooling | n/a | Do not treat JET transactional templates as campaign automation. | future martech choice |
| Store SEO | `JET` | Yes | JET-local configuration. | `PEN-025` |
| Privacy-policy publication | `JET` mechanism / external legal content authority | Yes | JET publishes; legal correctness is not determined by JET/training. | `PEN-020`, `UNC-006` |
| Banners | `JET` | Yes | Manage content/assets/links/scheduling in JET; official dimensions still need confirmation. | `PEN-022`, `PEN-023` |
| Custom institutional pages | `JET` | Yes | Manage/migrate content in JET; HTML source may be used. | `PEN-024` |
| Marketplace taxonomy/de-para | `INTEGRATION` / AnyMarket path | n/a | Future mapping work; do not assume JET category tree alone satisfies every marketplace. | `PEN-028` |
| Google/XML catalog categorization | `INTEGRATION` / external feed path | n/a | Future configuration; training establishes context/capability only. | `PEN-028` |
| Freight provider/rating architecture | `METAL_NOBRE` provider decision = `FRENET`; implementation via `JET`/`INTEGRATION` | n/a | Frenet is the selected hub, but provider choice does not prove services, rules, rating, tracking or exception handling are configured. Validate the actual integration before go-live. | `MN-DEC-012`, `PEN-043`, `PEN-035` |
| Payment gateway/PSP | `METAL_NOBRE` provider decision = `PAGAR.ME`; implementation via `JET`/`INTEGRATION` | n/a | Pagar.me is selected and contracting has started, but provider choice does not prove payment methods/status flows/reconciliation are configured. Validate the actual integration before go-live. | `MN-DEC-011`, `PEN-042`, `PEN-035` |

## High-risk write policy for future agents

A future agent **must not mutate** the following without resolving authority and required approval/evidence first:

- category hierarchy/name;
- product identity/master data;
- stock or price;
- integration credential scopes;
- integration queues/load/cleanup;
- storewide parametrizations;
- sold-out/stock-control flags;
- Atributo Único or m² conversion logic;
- layout-bound product groups;
- bulk spreadsheet updates.

Recommended default agent posture:

```text
READ → identify authority → classify change → check related PEN/decision → request/obtain bounded approval → mutate → verify source + downstream result → record evidence
```

## Supersession rule

If Rodrigo/integration/JET later changes a mapping, update this matrix with:

1. old authority;
2. new authority;
3. effective date/evidence;
4. impacted `JET-KB-*` IDs;
5. impacted operating procedures/agents.

Do not silently rewrite history in a way that makes old evidence appear to have proven the new mapping.
