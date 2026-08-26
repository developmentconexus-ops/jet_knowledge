# Phase 5 — Visual Validation

## Purpose

Validate the Pack A visual evidence produced from the two Metal Nobre JET training videos against the reconciled transcript knowledge.

This phase does **not** treat a screenshot as stronger than the spoken context by default. The validation rule is:

- the transcript establishes what was said, instructed, recommended or left uncertain;
- the visual evidence establishes what the interface visibly showed and, when the sequence is captured, what behavior visibly occurred;
- a visual snapshot taken before an instructed mutation cannot be used as proof of the post-mutation state;
- interface editability does not establish system authority;
- old training evidence does not establish current platform state where the subject is time-sensitive.

## Input package verification

The submitted Pack A contained 27 files:

- 13 MP4 clips;
- 13 PNG screenshots;
- 1 manifest CSV.

The 13 MP4 clips were checked for readable media structure and expected duration. Their durations matched the requested capture windows, with no truncated or empty clip found.

The validation then inspected screenshots directly and sampled clips across the relevant UI transitions. Higher-density inspection was used where before/after behavior mattered, especially the sold-out-product / 404 / `Avise-me` flow.

## Result classes

- `VERIFIED` — the visual evidence materially supports the intended interface or behavioral claim and agrees with the transcript.
- `INSUFFICIENT` — the evidence is valid, but does not prove the specific state that the map intended it to prove.
- `DIVERGENCE` — screen and transcript materially conflict.
- `METADATA_CORRECTION` — the capture is useful, but its original note or A/B responsibility needs correction; no recapture required.

## Pack A validation matrix

| Visual ID | Result | What the screen materially confirms | Canonical consequence |
|---|---|---|---|
| `MOD1-VIS-001` | `VERIFIED` | `Novo Usuário`, user form, `Áreas de Acesso`, modules/tools and access toggles | Supports future admin-access IT and access guardrails. |
| `MOD1-VIS-002` | `VERIFIED` | Sensitive permission controls for anonymization, removing/changing order status and viewing monetary/dashboard information | Supports access matrix and least-privilege review. Legal meaning of anonymization remains separately governed by external legal validation. |
| `MOD1-VIS-003` | `VERIFIED` | `Configurar Remetente`, sender list and sender-creation fields including the default-sender control | Supports `PEN-014` and future launch/e-mail IT. |
| `MOD1-VIS-004` | `VERIFIED` | Integration credential surface, order scope controls and integration queues with status/actions | Supports integration-runbook and queue-operation guardrails. Secrets themselves are not canonical knowledge. |
| `MOD1-VIS-005` | `VERIFIED` + `METADATA_CORRECTION` | Store parameter screen, zero-price/listing examples, sold-out detail with `Avise-me`, discount-basis control and automatic awaited-product e-mail flag | No recapture. Correct two screenshot notes in the future Evidence Index; see metadata corrections below. |
| `MOD2-VIS-001` | `VERIFIED` | Category tree/nesting, product count, actions and category edit fields including URL/SEO | Supports category procedure. Sankhya authority is established by transcript/integration evidence, not by UI editability. |
| `MOD2-VIS-002` | `VERIFIED` | `Reordenar categorias` and drag/drop across nested positions | Visually supports the hierarchy-mutation risk behind `JET-RULE-003`. |
| `MOD2-VIS-003` | `VERIFIED` | Product `Dados principais`: identity fields, stock/price/category, dimensions and cross-docking field surface | Supports Integration Authority Matrix. Visual presence of a field does not establish its source of truth. |
| `MOD2-VIS-004` | `VERIFIED` | Main image, alternative image/hover role and multifoto interface/behavior | Supports `PEN-008` and future media mapping IT. |
| `MOD2-VIS-005` | `INSUFFICIENT` for final-state proof | Product stock controls are visible, but the screenshot at `01:04:06` captures `Atualização automática da flag "Esgotado"? = não`, immediately before the trainer instructs the operator to change it to `Sim` and save | This is **not a screen/transcript contradiction**. Preserve the transcript-derived executed-state record, but do not claim this screenshot proves the final `Sim`. Validate the current live setting under existing `PEN-018`; no new PEN and no historical recapture are required. |
| `MOD2-VIS-006` | `VERIFIED` | `Importar produtos`, tutorial/model spreadsheet and bulk-update structure | Supports `JET-RULE-006` and future bulk-update IT/agent guardrail. |
| `MOD2-VIS-007A/B` | `VERIFIED` + `METADATA_CORRECTION` | A: `Atributo Único` / meter-per-box value management. B: product linking plus storefront calculator, m²/box presentation, rounding and cart quantity behavior | No recapture. Normalize A/B responsibility in the Evidence Index. Integration from Sankhya and return conversion remain open technical questions. |
| `MOD2-VIS-008` | `VERIFIED` | Product Similar setup, grouping name/code, product selection, palette/image/text modes and storefront behavior | Supports current merchandising model and future Product Similar IT. |
| `MOD2-VIS-009` | `VERIFIED` | Product-group list, IDs, edit/link-product flows, group creation and storefront presentation | Supports `JET-RULE-005`. The rule that existing home groups are layout-bound by ID is strengthened by transcript + visible ID/group surface. |
| `MOD2-VIS-010` | `VERIFIED` | Sold-out settings, actual 404 before the detail-page flag change, accessible detail afterward, `Esgotado`/`Avise-me`, Produtos Aguardados and reporting/customer-interest flow | Strong before/after support for `MN-DEC-005` and operational evidence for `MN-DEC-006` / `PEN-027`. |

## Metadata corrections

### `MOD1-VIS-005`

The captures are useful, but two original notes do not match the captured screen:

- `MOD1_VIS_005_B_00h35m30s.png` is a category/listing view showing product cards, including zero-value examples. It is not the product-detail proof.
- `MOD1_VIS_005_C_00h37m20s.png` is the sold-out product-detail state showing `Esgotado` and `Avise-me`. It is not the zero-price-product screenshot.

The evidence files remain valid; only their descriptive metadata must be normalized later.

### `MOD2-VIS-007A/B`

The practical boundary differs slightly from the Phase 4 description:

- `007A` covers the Atributo Único / meter-per-box value-management portion;
- the `Vincular produto` interaction occurs at the beginning of `007B`, which then continues through the storefront calculator and cart behavior.

No recapture is needed.

## Important non-divergence — automatic sold-out flag

`MOD2-VIS-005` is the only logical Pack A item that does not visually prove all of its intended claim.

The screen at the chosen instant shows the automatic sold-out flag as `não`. The transcript at that same point instructs the operator to change it to `Sim` and save, then describes the intended behavior as automatic.

Therefore:

1. the screenshot is valid **pre-action evidence**;
2. it cannot be promoted as visual proof of the post-action `Sim` state;
3. there is no contradiction between screen and transcript;
4. the historical transcript-derived record may remain, with its evidence type made explicit;
5. the go-live-relevant question is the **current JET configuration**, which belongs to `PEN-018`.

This avoids wasting effort recapturing a historical state when the live configuration is the operational authority that matters now.

## Cross-source outcome

Across Pack A:

- 15 logical evidence items were validated;
- 14 are `VERIFIED` for their intended visual purpose;
- 1 is `INSUFFICIENT` only for final-state proof (`MOD2-VIS-005`);
- 0 material screen/transcript divergences were found;
- 2 metadata-boundary corrections require no recapture;
- Pack B does not need to be promoted solely because of a Pack A evidence gap.

## Canonical implications

The visual pass strengthens the following existing rules and decisions without changing their semantic classification:

- `JET-RULE-002` — UI-editable does not mean source of truth;
- `JET-RULE-003` — category hierarchy mutations require Sankhya-aware discipline;
- `JET-RULE-004` — integration queues are privileged operational surfaces;
- `JET-RULE-005` — do not delete home groups fixed to layout IDs;
- `JET-RULE-006` — preserve JET bulk-import spreadsheet structure and exact values;
- `MN-DEC-005` — out-of-stock product detail was changed to be accessible, enabling the `Avise-me` flow;
- `MN-DEC-006` — Produtos Aguardados / `Avise-me` is an operational lead opportunity.

`MN-DEC-004` remains supported by the training transcript as an executed instruction/state, but the Pack A screenshot must **not** be cited as final-state visual proof. Current-state acceptance belongs to `PEN-018`.

## Phase 5 conclusion

Phase 5 is complete as a validation phase. Its purpose was to determine what the Pack A media can and cannot legitimately prove, not to force every historical screenshot to become perfect evidence.

The visual evidence can now be normalized into the canonical evidence layer with explicit provenance and confidence.

## Next — Phase 6

Build the canonical operational knowledge layer defined by the approved design:

- Platform Map;
- Knowledge Base;
- Pending / Decision Registers normalization;
- Integration Authority Matrix;
- Strategy Playbook;
- Evidence Index.

Phase 6 should consume the reconciled transcript knowledge plus this validated evidence set. It must not flatten uncertainties, recommendations or historical UI state into permanent platform facts.
