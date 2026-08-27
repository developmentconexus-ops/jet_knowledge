# Metal Nobre Decision Register

## Purpose

Canonical register of Metal Nobre-specific decisions, preferences and corrected historical classifications derived from the JET training/project work.

These entries must not be confused with universal JET platform facts. Current execution status of related work remains authoritative only in Trello.

## Classification

- `DECISION` — explicit project choice currently valid until superseded.
- `EXECUTED_TRAINING_STATE` — project choice/change executed during training; current live state may still require revalidation.
- `PREFERENCE` — desired direction, not yet a completed implementation decision.
- `INTENT` — business direction supported by source, but implementation scope remains open.
- `CORRECTED_NOT_FINAL` — historical ID preserved after evidence showed the prior “final decision” classification was too strong.

## Register

| ID | Classification | Canonical statement | Evidence basis | Related work / boundary |
|---|---|---|---|---|
| `MN-DEC-001` | `DECISION` | Keep Sankhya/upstream as the preferred source for integrated product master data, avoiding independent JET edits to fields that synchronization can overwrite. | MOD2 product/integration training; `RCN-005` | `PEN-007`; `JET-KB-013`–`017` |
| `MN-DEC-002` | `DECISION` | For the current rollout, keep separate product records/SKUs and use `Produto Semelhante` instead of restructuring into traditional JET variations. | MOD2 27:12–35:14 and 01:34:56–01:40:48 | Current strategy, not platform limitation; `PEN-012` |
| `MN-DEC-003` | `PREFERENCE` | Prefer subcategory display by hover rather than requiring a click. | MOD2 navigation discussion | Implementation remains open in `PEN-003`. |
| `MN-DEC-004` | `EXECUTED_TRAINING_STATE` | Enable automatic sold-out flag updating. Training records the instruction/execution to set it to `Sim`. | MOD2 01:03:00–01:06:18 | Phase 5 visual capture shows the pre-action `Não`, not the final state. Current live `Sim` must be verified under `PEN-018`. |
| `MN-DEC-005` | `EXECUTED_TRAINING_STATE` | Show sold-out products on their detail page so `Avise-me` remains available; the setting was changed from `Não` to `Sim` during MOD2. | MOD2 01:45:19–01:46:03; `MOD2-VIS-010` | Strong before/after visual evidence; current go-live settings still belong to `PEN-018`. |
| `MN-DEC-006` | `DECISION` | Treat `Produtos Aguardados` / `Avise-me` as an operational lead opportunity, including potential use for items normally handled by encomenda. | MOD2 01:46:25 onward | Operating process remains to be defined in `PEN-027`. |
| `MN-DEC-007` | `DECISION` | Do not initially execute a broad 301 redirect migration from the old ecommerce because prior traffic/sales and Google work were limited. | MOD1 53:28–58:34 | This does not invalidate 301 as a JET capability; revisit if migration value changes. |
| `MN-DEC-008` | `DECISION` | Conduct SEO internally at this stage rather than engage an agency. | MOD1 SEO discussion | Execution/prioritization in `PEN-025`. |
| `MN-DEC-009` | `CORRECTED_NOT_FINAL` | Preserve the intent to support meaningful brand navigation/shopping, but do **not** treat the final JET brand layout/presentation as approved or completed. | MOD2 36:45–41:19; corrected in Phase 3 | Brand grouping/config remains `PEN-005`/`PEN-006`. ID preserved for historical traceability. |
| `MN-DEC-010` | `DECISION` | Products handled by encomenda/cross-docking are not an immediate focus of the current rollout. | MOD2 product discussion | Does not remove future capability; cross-docking authority remains `UNC-004`. |
| `MN-DEC-011` | `DECISION` | Use **Pagar.me** as the Metal Nobre gateway/PSP for the JET ecommerce. The contracting process has started. | Explicit project update on 2026-08-27 after payment study/review. | Provider decision closes `PEN-029`; implementation and functional validation remain `PEN-042` and feed `PEN-035`. |
| `MN-DEC-012` | `DECISION` | Use **Frenet** as the Metal Nobre freight hub for the JET ecommerce. | Explicit project update on 2026-08-27 after freight study/review. | Provider/hub decision closes `PEN-030`; integration and operational validation remain `PEN-043` and feed `PEN-035`. |

## Supersession rule

A decision may change. When it does:

1. preserve the existing `MN-DEC-*` ID and historical statement;
2. record the replacement/superseding decision explicitly;
3. identify impacted `JET-KB-*`, `STR-*`, Integration Matrix rows and procedures;
4. create/update Trello work only where execution is actually required.

Never silently rewrite a prior decision so old evidence appears to have supported a choice that was made later.

## Interpretation rule

Decision, executed training state, preference, intent and recommendation are not interchangeable. If evidence supports only a preference or intent, keep it bounded rather than promoting it to a final decision.
