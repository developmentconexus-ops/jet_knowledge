# Phase 4 — Visual Evidence Map

## Purpose

This map defines which parts of the two Metal Nobre JET training videos are worth capturing as visual evidence after Phase 3 reconciliation.

The objective is **not** to archive every screen shown in the training. Visual evidence is requested only when it materially improves one or more of:

- operational procedure certainty;
- exact field/menu/button identification;
- integration or mutation guardrails;
- proof of an executed project configuration;
- future ISO-ready work instructions;
- future LLM/agent grounding;
- troubleshooting and auditability.

The transcript remains the primary record of what was said. Video/screenshots are evidence of what was shown and how the interface behaved at training time.

## Evidence classes

- `SCREENSHOT` — one static screen/state is enough.
- `MULTI_FRAME` — a few screenshots are better than a long clip.
- `SHORT_CLIP` — sequence, navigation, before/after or storefront behavior matters.
- `DEFER` — visual evidence may be useful later, but should not be extracted in the first pass.
- `NO_VISUAL` — transcript/evidence from another source is more appropriate.

## Priority packs

### Pack A — mandatory first pass

Capture these first. They contain high-value procedures, guardrails, executed configuration state or future agent/IT-critical UI.

| ID | Module | Source window | Evidence | What must be visible | Why capture | Future consumers |
|---|---|---|---|---|---|---|
| `MOD1-VIS-001` | MOD1 | `00:09:00–00:10:45` | SHORT_CLIP | `Novo Usuário`, main form, `Áreas de Acesso`, tool selection/expansion | Exact access-control workflow and UI model | IT-admin, access review, agent guardrail |
| `MOD1-VIS-002` | MOD1 | `00:13:06–00:14:21` | SHORT_CLIP | permission controls for anonymization, removing/changing order status, monetary dashboard; transition to user registration | Sensitive administrative permissions must not be reconstructed from prose alone | access matrix, IT-admin, security review |
| `MOD1-VIS-003` | MOD1 | `00:21:53–00:24:10` | SHORT_CLIP | `Configurar Remetente`, sender name/e-mail, default-sender control, save flow | Go-live-relevant procedure and exact field naming | PEN-014, future IT, launch checklist |
| `MOD1-VIS-004` | MOD1 | `00:29:23–00:32:09` | SHORT_CLIP / REDACTED | credential scope options and integration queues; queue activation and load/cleanup area | High-risk integration surface and queue guardrail | integration runbook, agent deny/approval guardrail |
| `MOD1-VIS-005` | MOD1 | `00:34:12–00:39:29` | MULTI_FRAME | flags for out-of-stock listing/detail, zero-price display, payment-discount base, automatic awaited-product e-mail | Several behavior-changing store flags are described; static proof is more useful than an 8-minute clip | PEN-018, launch config baseline, troubleshooting |
| `MOD2-VIS-001` | MOD2 | `00:02:01–00:06:16` | SHORT_CLIP | category tree, three levels, product count, edit/delete/view actions, status/name/URL/SEO area | Establishes category structure and where direct edits can conflict with upstream authority | category IT, integration guardrail, PEN-001/PEN-002 |
| `MOD2-VIS-002` | MOD2 | `00:22:53–00:26:04` | SHORT_CLIP | `Reordenar categorias`, drag/drop and hierarchy movement; top-category display concept | Reordering can accidentally mutate hierarchy; needs visual warning | risk guardrail, category IT |
| `MOD2-VIS-003` | MOD2 | `00:51:07–00:55:40` | MULTI_FRAME | `Dados principais`: name, GTIN, NCM, URL, code, stock, price, category, weight/dimensions, cross-docking location | Core authority matrix: UI editability versus Sankhya ownership | integration authority matrix, product IT, agent write policy |
| `MOD2-VIS-004` | MOD2 | `00:55:40–00:59:02` | SHORT_CLIP | principal image, alternative image, storefront hover behavior, multifotos and ordering/repetition | Exact image-role mapping is integration-sensitive and easy to misread from transcript | PEN-008, product media IT |
| `MOD2-VIS-005` | MOD2 | `01:03:00–01:06:18` | MULTI_FRAME | path to `Atualização automática da flag esgotado`, value changed to `Sim`, product-level `Produto esgotado`, manual stock and sell-without-stock controls | Proof of an executed Metal Nobre configuration plus high-risk stock controls | MN-DEC-004, PEN-018, troubleshooting, agent guardrail |
| `MOD2-VIS-006` | MOD2 | `01:15:27–01:20:00` | SHORT_CLIP | `Importar produtos`, model spreadsheet, column order/names, required product code, label/SEO columns, upload/result flow | Bulk update has strict formatting rules and can affect many products | future IT, campaign/SEO automation, agent bulk-write guardrail |
| `MOD2-VIS-007A` | MOD2 | `01:29:30–01:31:20` | SHORT_CLIP | `Atributo Único`, `Inserir valores`, value `2.4/2,40`, `Vincular produto`, left/right linkage areas, save/link actions | Configuration procedure for the porcelain calculator | PEN-009, future porcelain IT |
| `MOD2-VIS-007B` | MOD2 | `01:31:01–01:34:19` | SHORT_CLIP | storefront calculator, price per m² and per box, requested m², rounding to box multiple, cart showing box quantity | The transcript cannot convey the customer-facing calculator behavior adequately | product UX, training, E2E validation |
| `MOD2-VIS-008` | MOD2 | `01:34:56–01:40:47` | SHORT_CLIP | Product Similar group name/code, product selection, palette/image/text presentation, storefront switching | Likely Metal Nobre merchandising workflow; exact setup and customer behavior both matter | PEN-012, future merchandising IT, agent catalog capability |
| `MOD2-VIS-009` | MOD2 | `01:40:48–01:44:19` | SHORT_CLIP | existing product groups, IDs/layout relationship, edit/rename, linked products, new group behavior and URL | Critical guardrail: do not delete layout-bound groups; new groups do not automatically appear on home | PEN-026, layout guardrail, campaign playbook |
| `MOD2-VIS-010` | MOD2 | `01:45:19–01:49:05` | SHORT_CLIP | listing/detail sold-out flags, 404 before change, change to `Sim`, accessible detail, `Avise-me`, Produtos Aguardados list/customer/report | Captures both executed state change and full lead workflow | MN-DEC-005/006, PEN-027, CRM playbook, future IT |

### Pack A capture notes

1. **Do not upload secrets to an external multimodal service.** `MOD1-VIS-004` may expose integration credentials such as Integration Key, user or password. Crop to the queue/scope area or redact secrets before any external upload.
2. Redact personal e-mails, customer data, IPs, credentials and any other sensitive information before sharing screenshots/clips outside the approved project context.
3. Keep original resolution when text size matters. Avoid downscaling small UI text.
4. For `MULTI_FRAME`, prefer 2–5 clear PNG screenshots instead of a long clip.
5. Preserve about 3–5 seconds of context before and after a meaningful action when creating clips.

## Pack B — important second pass

Capture these after Pack A, or earlier if the related pending item becomes active.

| ID | Module | Source window | Evidence | What must be visible | Why / condition |
|---|---|---|---|---|---|
| `MOD1-VIS-006` | MOD1 | `00:16:22–00:17:34` | SHORT_CLIP | old/new JET layout difference, current tab/tool naming, `Ajuda` vs `Saiba mais` | Needed for version-aware documentation and UI-drift warnings |
| `MOD1-VIS-007` | MOD1 | `00:17:34–00:20:30` | SHORT_CLIP | Gerência de Alertas, Fale Conosco/Produto Aguardado, status/period, user selection, copy e-mails | Capture when PEN-016 is executed or an alert IT is drafted |
| `MOD1-VIS-008` | MOD1 | `00:24:10–00:29:15` | SHORT_CLIP | transactional e-mail list, status template, preview, tags, HTML/source button, subject and sender controls | Useful for PEN-015/PEN-017 and lifecycle messaging documentation |
| `MOD1-VIS-009` | MOD1 | `00:40:35–00:41:13` | SCREENSHOT | company information and `Logomarca da loja` field used for automatic e-mails | Useful for PEN-019 / launch baseline |
| `MOD1-VIS-010` | MOD1 | `00:47:57–00:48:56` | SHORT_CLIP / REDACTED | maintenance mode and allowed-IP area | Useful for cutover/runbook; redact real IP values |
| `MOD1-VIS-011` | MOD1 | `00:48:56–00:50:14` | SHORT_CLIP | privacy-policy text area, link tag and publish/activate flow | UI evidence only; does **not** validate legal correctness |
| `MOD1-VIS-012` | MOD1 | `00:53:28–00:58:34` | SHORT_CLIP | old/new URL comparison and 301 source/destination fields | Historical capability evidence; current Metal Nobre decision remains to skip broad migration initially |
| `MOD1-VIS-013` | MOD1 | `00:58:57–01:03:06` | SHORT_CLIP | existing banners, image-based identification, rename/edit, link, desktop/mobile assets | Capture for PEN-023 / banner maintenance IT |
| `MOD1-VIS-014` | MOD1 | `01:03:51–01:07:58` | SHORT_CLIP | new full banner, random flag, schedule, placement, image/video, reordering | Capture when campaign/banner procedure is formalized |
| `MOD1-VIS-015` | MOD1 | `01:08:22–01:11:22` | SHORT_CLIP | Personalized Pages, two panel groups, page fields, source/HTML, create/edit/delete | Capture for PEN-024 / institutional-page IT |
| `MOD1-VIS-016` | MOD1 | `01:12:44–01:14:34` | SCREENSHOT / SHORT_CLIP | App Store category/partner view, especially freight/marketing examples | Historical ecosystem evidence only; partner availability must be revalidated when selecting a vendor |
| `MOD2-VIS-011` | MOD2 | `00:21:17–00:22:37` | SHORT_CLIP | current click-to-expand behavior versus hover example/request | Evidence for PEN-003 and layout acceptance |
| `MOD2-VIS-012` | MOD2 | `00:38:24–00:41:19` | SHORT_CLIP | brand edit screen, image, URL, SEO/text, home/destaque flag and storefront carousel | Capture for PEN-005/PEN-006 or brand-management IT |
| `MOD2-VIS-013` | MOD2 | `≈00:46:00–00:51:07` | SHORT_CLIP after video refinement | `Meus produtos`, filters, Quick Edit, report/download and product opening | Transcript transition lacks an exact timestamp at the start; refine against video before extraction. Useful for Quick Edit guardrail and reporting workflow |
| `MOD2-VIS-014` | MOD2 | `01:20:00–01:28:25` | SHORT_CLIP | Conjunto vs Kit storefront behavior; kit discount, stock limiting component, exclusive sale | Capture only if kits/conjuntos enter the operating roadmap |

## Pack C — deferred until needed

The following topics are visually useful but do not justify first-pass extraction now:

- JET home/search shortcuts and `Ver Loja`;
- JET Experience navigation/tutorial lookup;
- SEO Title/Meta fields themselves — field names are already clear; current UI screenshot is preferable when SEO work begins;
- social-network URL configuration and Instagram Vitrine;
- Tags/labels and Disponibilidade unless a campaign procedure is being authored;
- Multiplicador de unidades, order-position fields and min/max purchase limits unless they enter active product rules;
- Relacionados / Compre Junto / Comprados unless merchandising execution begins;
- FAQ creation;
- category image/text examples unless category content production begins.

## Explicit `NO_VISUAL` cases

Do **not** use old-video visuals to resolve these items:

1. legal/LGPD statements — visual evidence cannot validate legal correctness;
2. sitemap refresh interval — trainer uncertainty must be resolved through current JET documentation/support, not video;
3. current automation state of `Quem comprou, comprou também` — the training only proves what was said then;
4. current state of features described as being discontinued — requires current revalidation;
5. whether Atributo Único integration from Sankhya exists — needs Rodrigo/integration or current technical documentation;
6. whether the m²/box return conversion is implemented — needs integration evidence/test;
7. final freight and payment-gateway architecture — requires current vendor/technical decision work.

## Capture file naming

Use stable IDs in filenames so evidence can be linked to knowledge records later.

Examples:

```text
MOD1_VIS_003_00h21m53s-00h24m10s.mp4
MOD1_VIS_005A_00h34m12s.png
MOD2_VIS_007A_01h29m30s-01h31m20s.mp4
MOD2_VIS_007B_01h31m01s-01h34m19s.mp4
```

Recommended directory structure:

```text
evidence/
├── MOD1/
│   ├── clips/
│   └── screenshots/
└── MOD2/
    ├── clips/
    └── screenshots/
```

## Evidence metadata after extraction

Each accepted image/clip will later receive:

```yaml
visual_id: MOD2-VIS-007A
source_module: MOD2
source_video: "[Metal Nobre] Treinamento Módulo 2"
timestamp_start: "01:29:30"
timestamp_end: "01:31:20"
evidence_type: SHORT_CLIP
status: EXTRACTED | VERIFIED | REJECTED | SUPERSEDED
ui_version: UNKNOWN
captured_at: 2026-08
verified_against_transcript: true
supports:
  - knowledge atom / rule / decision / pending IDs
notes: ""
```

## Validation rule for Phase 5

After the user extracts Pack A:

1. inspect visual evidence against the transcript;
2. record any screen/transcript divergence;
3. never overwrite transcript meaning with an unsupported visual inference;
4. update exact path/field/button names only when visible;
5. attach evidence IDs to canonical knowledge records;
6. promote Pack B items only where Pack A exposes a gap or the operating roadmap makes them relevant.

## Phase 4 result

The visual workload is reduced from full-video review to a targeted first pass of **15 high-value evidence items** (with `MOD2-VIS-007` split into configuration and storefront subclips), followed by an optional second pass.

The next step is Phase 5: extract Pack A from the original videos, then verify each evidence item against the reconciled knowledge base.