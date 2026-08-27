# Procedural Knowledge — Stable Core / Release-Blocked Topics

> **Status:** knowledge capture only. Not an operationally released PO/IT.
>
> Purpose: preserve stable procedure/capability knowledge now while explicitly keeping Metal Nobre-specific current-state, ownership and decision gaps blocked by their existing `PEN-###` / `UNC-###` items.

## 1. Administrator users and access

### What is already known

JET supports creation of administrator users and tool/module-level access control.

Demonstrated user registration includes a small form with status, name, code, login/user and e-mail, followed by access areas and sensitive permissions.

`Áreas de Acesso` mirrors the main admin areas/tools. A tool that is not enabled for a user is not shown to that user in the demonstrated behavior.

Sensitive permissions demonstrated include:

- anonymize customers;
- remove current order status;
- change order status;
- view monetary values/dashboard information;
- access administrator-user management.

This is enough to establish a **least-privilege guardrail** even before Metal Nobre defines its final access matrix.

### What is not safe to release yet

- actual list of required Metal Nobre admin users;
- role-by-role permission matrix;
- whether IP restriction will be used and for whom;
- exact first-access behavior in the current project;
- exact relationship between temporary password, publication, e-mail infrastructure, sender and `Recuperar Senha`.

Blockers: `PEN-033`, `UNC-008`.

Evidence: MOD1 `09:00–14:21`, `MOD1-VIS-001/002`, `JET-KB-004–006`.

---

## 2. Transactional sender configuration

### What is already known

JET has a `Configurar Remetente` surface for sender identities used in transactional/institutional e-mail.

The training states that at least one default sender must be configured before publication.

Sender identity uses a Metal Nobre e-mail/domain identity rather than treating the trainer's examples as a fixed required address.

Different transactional events can use different senders/copies according to the demonstrated model.

### What is not safe to release yet

- final Metal Nobre default sender;
- final event-specific senders;
- final copy recipients;
- operational routing to invoicing/separation/etc.;
- current domain/sender validation state.

Blockers: `PEN-014`, `PEN-015`.

Evidence: MOD1 `21:53–29:15`, `MOD1-VIS-003`, `JET-KB-049`.

---

## 3. Transactional e-mail template maintenance

### What is already known

JET transactional/institutional e-mails are distinct from marketing/campaign automation.

The demonstrated transactional e-mail surface allows maintenance of:

- message body;
- subject;
- template tags/variables;
- HTML/source content;
- sender/copy behavior associated with events.

Marketing automation was discussed as external/integrated tooling and must not be flattened into the transactional-template procedure.

### What is not safe to release yet

- final Metal Nobre wording for each event;
- final subject lines;
- required legal/commercial copy;
- actual sender/copy routing;
- which event templates are launch-critical versus post-launch refinement.

Blocker: `PEN-017` plus `PEN-014/015` for sender/routing.

Evidence: MOD1 `20:50–29:15`, `JET-KB-047–049`.

---

## 4. Integration credentials and queues

### What is already known

JET exposes integration credentials and credential scopes.

At training time, BLP credentials for the Sankhya integration had already been generated.

JET integration works with separated queues by domain; examples demonstrated include brand, product, stock and price.

Queue activation determines whether JET feeds data for integrator consumption in the demonstrated model.

The queue surface also exposes technical resources/actions such as JSON/documentation and operations including load and cleanup.

### Critical guardrail

Load/cleanup/queue manipulation is **privileged integration work**, not routine ecommerce-operator work.

The trainer explicitly advises operating these technical actions with the integrator or JET support.

Credential values themselves are secrets and are not canonical knowledge.

### What is not safe to release yet

- current support/escalation route;
- who in Metal Nobre is authorized to request/approve queue operations;
- exact runbook for load/cleanup recovery;
- rollback behavior after a bad queue operation;
- current queue inventory/status.

Blockers: `PEN-038`, current integration operating model.

Evidence: MOD1 `29:23–32:09`, `MOD1-VIS-004`, `JET-KB-064–066`, `JET-RULE-004`.

---

## 5. Product Similar

### What is already known

JET supports `Produto Semelhante` for grouping separate products into a variation-like customer selection experience.

The demonstrated setup includes:

- grouping name shown to the customer;
- grouping code used as an internal reference;
- product selection/linking;
- presentation using color palette;
- main product image;
- text;
- uploaded image.

Training states one Product Similar grouping per product at that time.

Current Metal Nobre direction is to keep separate product/SKU records and use Product Similar instead of immediately remodelling the catalog into traditional JET variations.

### What is not safe to release yet

- which Metal Nobre families will use it;
- customer-facing dimension per family (voltage, color, power, etc.);
- naming standard for grouping names/codes;
- whether any family should instead become a true variation later.

Blocker: `PEN-012`.

Evidence: MOD2 `27:12–35:14`, `01:34:56–01:40:47`, `MOD2-VIS-008`, `MN-DEC-002`, `JET-KB-024–027`.

---

## 6. Produtos Aguardados / Avise-me

### What is already known

JET separately controls sold-out visibility in listing pages and product-detail pages.

The training visibly demonstrates:

1. sold-out product detail returning 404 while detail visibility is disabled;
2. changing the detail visibility setting;
3. the product detail becoming accessible;
4. `Esgotado` / `Avise-me` appearing;
5. customer registration of interest;
6. the product/customer appearing in `Produtos Aguardados`;
7. access to waiting-customer information and export/report workflow.

Metal Nobre identified this as a lead opportunity, including possible use for products normally handled as encomenda.

### Stable strategic guidance

Faster follow-up was recommended because the trainer described the interested customer as high-intent and the probability of conversion decreasing as time passes.

This is guidance, not a Metal Nobre SLA yet.

### What is not safe to release yet

- process owner;
- SLA/time target;
- exact contact channel;
- when to offer substitute/similar products;
- what to do for encomenda products;
- whether automated awaited-product e-mail should remain enabled in the current configuration;
- how manual follow-up interacts with automatic notification.

Blockers: `PEN-018`, `PEN-027`.

Evidence: MOD2 `01:44:19–01:49:05`, `MOD2-VIS-010`, `MN-DEC-005/006`, `JET-KB-041–046`.

---

## 7. Banner maintenance

### What is already known

JET banner management demonstrated support for:

- existing-banner maintenance;
- human-friendly naming;
- redirect link;
- desktop/mobile assets;
- banner types/positions;
- scheduling;
- randomized display/rotation;
- image/video content;
- reordering.

The training also distinguishes configuration capability from layout/creative strategy.

Trainer advice about keeping roughly three to four full banners is `TRAINER_GUIDANCE`, not a hard JET technical limit.

### What is not safe to release yet

- official/current dimensions for each Metal Nobre banner type;
- final launch banner inventory;
- naming convention;
- owner/approval of creative assets;
- current layout positions/types;
- whether all Pack B visual evidence needed for the future IT has been captured.

Blockers: `PEN-022`, `PEN-023`.

Evidence: MOD1 `58:57–01:07:58`, `JET-KB-061/062`.

---

## 8. Custom institutional pages

### What is already known

JET custom/personalized pages support maintenance of:

- page name;
- content;
- URL;
- SEO;
- HTML/source.

The panel grouping model and the storefront visual organization are separate concepts.

The training presents HTML/source as a possible aid when migrating content from an existing site.

### What is not safe to release yet

- which Metal Nobre pages are required at launch;
- final migrated copy/content;
- final grouping/navigation presentation;
- current interface path if it has drifted;
- owner/approval of institutional text.

Blocker: `PEN-024`.

Evidence: MOD1 `01:08:22–01:11:22`, `JET-KB-063`.

---

## 9. Privacy-policy publication mechanism

### What is already known

JET provides a surface to maintain/publish a privacy-policy text/link/configuration.

That proves the **mechanism**, not legal correctness.

### Critical boundary

Verbal LGPD/legal explanations from training are not sufficient authority for Metal Nobre compliance rules.

Any future IT may document:

- where/how to publish the approved policy in JET;

but must not define the legal content based solely on the trainer's speech.

### What is not safe to release yet

- final approved legal text;
- legal basis/interpretation;
- required acceptance/consent wording;
- responsibility for legal approval;
- current policy state.

Blockers: `PEN-020`, `UNC-006`.

Evidence: MOD1 `48:56–50:14`, `JET-KB-056/057`.

---

## Topics intentionally not expanded here

### Category maintenance

The UI/procedure is known, but the canonical category tree/mapping is still active work. A prescriptive Metal Nobre maintenance note risks encoding the wrong authority model before `PEN-001/002` close.

### Product master/image maintenance

Stable authority concepts already live in the Integration Authority Matrix, but actual enrichment/image mapping remains active (`PEN-007/008`, `UNC-004`).

### Porcelain m²/box

The platform procedure is visually strong, but integration/return conversion is too critical to present as an operational Metal Nobre procedure before `PEN-009/010/035` evidence.

### Storewide parametrizations

Historical behavior is known, but current launch values must be read from live JET and closed through `PEN-018`.

### Order/payment/freight/cutover

These depend on active current architecture/readiness work and cannot be derived from the training corpus alone.

## Rewatch rule

When the trainings are reassessed, update this file only with **new stable procedural knowledge**.

Do not resolve current-state, integration implementation or legal questions merely because the old video contains an example or an opinion.

Use `docs/research/strategic-rewatch-checklist.md` as the audit guide.
