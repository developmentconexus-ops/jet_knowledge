# Strategic Rewatch Checklist — JET Trainings / Metal Nobre

## Purpose

Use the second viewing of the two JET trainings as a **targeted audit of the canonical knowledge**, not as a fresh transcription exercise.

The goal is to answer:

1. Did the first pass miss any operationally relevant capability, rule, field, exception or decision?
2. Did we accidentally compress a nuanced explanation into a statement that is too broad?
3. Is any historical example being mistaken for a Metal Nobre decision?
4. Is any field path, status or configuration better evidenced by the video than by the transcript?
5. Which current `PEN-###` / `UNC-###` can be better prepared by information already present in the training?

This checklist does **not** resolve current-state questions by replaying old video. Current platform/configuration state must still be validated through the appropriate live source.

## How to review

For every relevant moment, classify what is being said/shown as one of:

- `PLATFORM_FACT`;
- `PROCEDURE`;
- `INTEGRATION_RULE`;
- `METAL_NOBRE_DECISION`;
- `STRATEGIC_GUIDANCE`;
- `RISK_GUARDRAIL`;
- `OPEN_QUESTION` / `TRAINER_UNCERTAINTY`;
- historical `CURRENT_STATE`;
- example only / no canonical value.

If the video supports a correction or new knowledge atom, record:

- module;
- timestamp;
- exact subject;
- what the current canonical layer says;
- what should be added/corrected;
- related `JET-KB`, `MN-DEC`, `UNC`, `PEN` or `VIS` ID.

## MOD2 — product, catalog and integration

### Categories — `≈00:30–26:04`

Review for:

- exact distinction between category status, hierarchy, name, URL, SEO, text and image;
- every statement about what Sankhya overwrites versus what remains JET-local;
- whether any alternative integration mapping was discussed beyond the three possibilities already captured;
- category deletion prerequisites and order;
- drag/drop behavior that changes hierarchy, not only visual order;
- rules for empty categories and product counts;
- whether any category-navigation decision was actually made or only suggested;
- precise discussion of hover, number of top categories and `Ver todos`.

Related: `JET-KB-007–012`, `PEN-001–004`, `MN-DEC-003`.

### Marketplace / Google taxonomy — `≈14:26–17:19`

Review for:

- exact role attributed to JET, AnyMarket and marketplaces;
- whether the training describes an actual current integration or only a future de/para concept;
- Google/XML catalog wording and any assumptions that should remain future work.

Related: `PEN-028`, Platform Map, Integration Authority Matrix.

### Variations and Product Similar — `≈27:12–35:14` and `01:34:56–01:40:48`

Review for:

- difference between a real JET variation and separate products grouped by Produto Semelhante;
- whether any limitation was stated versus merely a current Metal Nobre strategy;
- available display types: text, palette, product image, uploaded image;
- exact meaning/use of grouping name and code;
- statement that one Product Similar grouping is allowed per product;
- any SEO statement that is clearly trainer strategy rather than platform fact.

Related: `JET-KB-024–027`, `MN-DEC-002`, `PEN-012`, `STR-002`.

### Brands — `≈36:45–41:19`

Review for:

- what originates upstream versus what is configured in JET;
- image, URL, SEO, text and home/highlight controls;
- Deca Metal / Deca Louça consolidation discussion;
- whether brand navigation was a final layout decision or only intent.

Related: `PEN-005`, `PEN-006`, corrected `MN-DEC-009`.

### Product search / reports / Quick Edit — `≈46:00–51:07`

Review for:

- search/filter/report capabilities;
- exact Quick Edit fields exposed;
- any warning about fields editable in UI but owned by Sankhya;
- whether report behavior is useful enough for a future operating instruction.

Related: `JET-RULE-002`, Integration Authority Matrix.

### Product master data — `≈51:07–55:40`

Review field by field:

- name;
- GTIN;
- NCM;
- URL;
- code;
- stock;
- price;
- category association;
- weight;
- dimensions;
- cross docking.

For each field, record separately:

- visible/editable in JET?;
- stated authority?;
- demonstrated current value?;
- open integration question?

Special attention: cross-docking wording was uncertain and must not become confirmed Sankhya mapping without evidence.

Related: `JET-KB-013–018`, `UNC-004`, `PEN-007`.

### Images / video / descriptions — `≈55:40–01:00`

Review for:

- main image role;
- alternative/hover image role;
- multifoto ordering/repetition;
- exact upstream image-order discussion;
- video hosting/configuration;
- description source.

Look for anything missing from `PEN-008` that Rodrigo/integration must validate.

### Product configuration — `≈01:00–01:15:27`

Review all fields that were passed quickly, especially:

- sold-out controls;
- gift/brinde;
- manual stock control;
- sell without stock control;
- brand;
- labels;
- availability;
- unit multiplier;
- order/display positions;
- min/max quantity;
- `Compre Junto`;
- `Relacionados`;
- `Comprados`.

Separate:

- generic capability;
- Metal Nobre applicability;
- recommendation/example;
- dangerous override of Sankhya authority.

Pay special attention to `Comprados`: trainer uncertainty must remain uncertainty unless another source resolves it.

Related: `UNC-002`, `PEN-013`, `JET-KB-028/029/036/041–043`.

### Bulk spreadsheet — `01:15:27–01:20:00`

Audit the new draft:

`docs/iso/drafts/it-bulk-update-jet-managed-product-fields.md`

Look specifically for:

- exact current path/button wording;
- every rule in the tutorial/model;
- mandatory fields for update;
- exact-value matching rules;
- upload/error-result behavior;
- any limit, validation, rollback or recovery behavior that was missed;
- whether additional JET-local fields were explicitly shown as safe examples.

### Conjunto / Kit — `01:20:00–01:28:25`

Review for knowledge completeness even if no IT is planned now:

- customer selection difference;
- discount difference;
- kit component discount logic;
- stock limiting component;
- quantity per component;
- weight/dimensions/cross docking;
- exclusive-sale behavior;
- whether kit/conjunto IDs have integration significance.

Related: `JET-KB-034/035`.

### Atributo Único / m² / calculator — `01:28:28–01:34:54`

Maximum-priority rewatch.

Confirm:

- exact sequence for creating a value;
- decimal format shown;
- linking products to a value;
- save actions;
- storefront price per m² / per box;
- rounding behavior;
- cart quantity semantics;
- every sentence about Sankhya integration;
- every sentence about order/inventory return conversion;
- what Fabrício knew versus what he explicitly did **not** confirm.

Do not use the historical video to resolve whether the integration is implemented today.

Related: `PEN-009`, `PEN-010`, `UNC-003`, `MOD2-VIS-007A/B`.

### Product groups — `01:40:48–01:44:19`

Audit the new draft:

`docs/iso/drafts/it-product-group-maintenance.md`

Look for:

- exact fields in group edit;
- IDs shown and how layout binding is explained;
- home visibility behavior;
- linked-product search/add/remove behavior;
- whether product order inside group is configurable;
- new-group behavior and URL;
- recovery guidance after accidental deletion;
- any limit or layout dependency not yet captured.

### Produtos Aguardados / Avise-me — `01:44:19–01:49:05`

Review for:

- exact before/after 404 sequence;
- listing vs detail-page flags;
- customer registration flow;
- awaited-products screen fields;
- report/export behavior;
- customer timestamp/data shown;
- Metal Nobre discussion about encomenda;
- strategic guidance versus actual process decision.

Related: `PEN-018`, `PEN-027`, `MN-DEC-005/006`.

## MOD1 — administration, configuration, content and acquisition

### Environment / navigation / support — beginning of module

Review for:

- temporary project domain;
- no assumed sandbox;
- what changes affect immediately;
- exact support route at that historical moment;
- JET Experience/help navigation;
- old/new UI migration statements.

Do not promote the historical support route to current state.

Related: `JET-RULE-001`, `UNC-009`, `PEN-038`.

### Admin users / access — `≈09:00–16:05`

Review for:

- every user form field;
- `Áreas de Acesso` hierarchy;
- sensitive permissions;
- IP restrictions, if shown/discussed;
- first-access behavior;
- temporary password / Recuperar Senha;
- what specifically depended on publication/e-mail infrastructure;
- what remains ambiguous.

Related: `PEN-033`, `UNC-008`, `MOD1-VIS-001/002`.

### Alerts / Fale Conosco — `≈17:34–20:30`

Review for:

- exact alert sources;
- recipient selection;
- frequency/period behavior;
- distinction between Fale Conosco, Produto Aguardado and any other alerts;
- whether layout enablement is required.

Related: `PEN-016`.

### Transactional e-mail — `≈20:50–29:15`

Review for:

- transactional/institutional versus marketing distinction;
- sender creation fields;
- default sender requirement;
- event-specific sender/copy behavior;
- template body;
- subject;
- tags;
- HTML/source;
- preview;
- exact publication/sender/dispatch relationship;
- any Metal Nobre-specific recipient decision actually made versus examples.

Related: `PEN-014`, `PEN-015`, `PEN-017`, `UNC-008`.

### Integration credentials / queues — `≈29:23–32:09`

Review for:

- credential creation and scope controls;
- Base64 statement;
- exact queue domains shown;
- activation/inactivation semantics;
- JSON/documentation links;
- load and cleanup actions;
- explicit instruction to operate with integrator/JET support.

Do not copy credential values into canonical documentation.

Related: `JET-RULE-004`, `PEN-038`.

### Editar Dados da Loja — `≈32:24–41:13`

Maximum-priority go-live rewatch.

Review every parameter individually, including:

- sold-out in listing;
- sold-out on detail;
- zero-value product display;
- discount calculation basis;
- automatic awaited-product e-mail;
- Termo de Aceite;
- company data;
- e-mail logo/identity.

Record whether each item was:

- merely explained;
- recommended;
- changed during training;
- left for homework;
- already configured.

Current live values still belong to `PEN-018`/`PEN-019` rather than historical video.

### SEO — `≈41:33–47:11`

Review for:

- exact store SEO fields;
- category/product relationships;
- strategic order of work;
- sitemap/robots statements;
- any ranking/performance statement that is opinion/guidance rather than platform fact;
- sitemap cadence uncertainty.

Related: `PEN-025`, `UNC-001`, `STR-017`.

### Maintenance / privacy — `≈47:57–50:14`

Review separately:

- maintenance mode mechanics;
- allowed IP behavior;
- privacy-policy publication mechanics;
- every legal/LGPD statement.

Do not turn legal speech into compliance policy without external validation.

Related: `PEN-020`, `UNC-006`.

### Social / Instagram / 301 — `≈50:31–58:34`

Review for:

- social-link fields;
- Instagram integration/showcase mechanics;
- 301 source/destination fields;
- distinction between JET capability and Metal Nobre decision to skip broad migration initially.

Related: `PEN-021`, `MN-DEC-007`.

### Banners — `≈58:57–01:07:58`

High-priority rewatch before banner IT.

Review for:

- types;
- positions;
- desktop/mobile assets;
- redirects;
- schedule;
- randomization;
- video;
- order/reordering;
- exact dimensions mentioned versus explicitly left to confirmation;
- existing Metal Nobre banners and naming issues;
- trainer performance advice versus hard limitation.

Related: `PEN-022`, `PEN-023`, `JET-KB-061/062`.

### Custom pages / FAQ / App Store — `≈01:08:22–01:14:34`

Review for:

- default page groups;
- page fields;
- URL/SEO;
- HTML/source migration;
- panel grouping versus storefront layout;
- FAQ capability;
- App Store partner examples;
- anything that could be mistaken as vendor selection.

Related: `PEN-024`, `PEN-029`, `PEN-030` boundary.

## Cross-module questions to answer during rewatch

At the end, explicitly answer:

1. Did any later MOD1 statement supersede or clarify a generic MOD2 statement?
2. Did we miss any configuration actually executed during the calls?
3. Did we classify any trainer recommendation as a Metal Nobre decision?
4. Did we classify any Metal Nobre question/preference as a final decision?
5. Did we miss a field whose authority is integration-sensitive?
6. Did we miss a dangerous mutation surface that deserves a guardrail?
7. Did we miss any troubleshooting pattern (symptom → likely cause → action)?
8. Did we miss any report/export capability useful for operations?
9. Are there paths/buttons that deserve Pack B capture when a future IT is drafted?
10. Which unresolved items truly require external/current validation and cannot be solved by rewatching?

## Expected output of the second viewing

Do not rewrite the transcripts.

Produce only deltas:

```text
NEW KNOWLEDGE
CORRECTION
STRONGER EVIDENCE
MISSING PROCEDURE STEP
MISSING GUARDRAIL
MISSING TROUBLESHOOTING
DECISION CLASSIFICATION FIX
UNCERTAINTY CONFIRMED
NO CHANGE
```

Every delta should point back to the existing canonical ID when possible. Create a new ID only when the concept is genuinely new.
