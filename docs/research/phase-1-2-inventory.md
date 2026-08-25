# Phase 1–2 — Initial Knowledge Inventory

## Scope

Initial inventory from the two Metal Nobre JET training transcripts. This is not yet the reconciled canonical knowledge base; Phase 3 will reconcile duplicates, confirmations and contradictions across modules.

## Module 1 — Administration, configuration, content and acquisition

Domains identified:

- navigation and search;
- production behavior / no assumed sandbox;
- JET Experience and API documentation;
- support routing;
- administrator users, IP restrictions and permissions;
- customer anonymization / privacy-related operations;
- alerts and Fale Conosco;
- transactional e-mails, senders, templates and tags;
- integration credentials and queues;
- Editar Dados da Loja / parametrizations;
- out-of-stock visibility and Avise-me;
- SEO, sitemap and robots;
- maintenance mode;
- privacy policy;
- social networks and Instagram showcase;
- URL 301 redirects;
- banners;
- custom institutional pages;
- FAQ;
- App Store / integration ecosystem.

## Module 2 — Catalog, product, merchandising and integration

Domains identified:

- categories and category hierarchy;
- category authority and Sankhya integration;
- category URL/SEO/content;
- navigation architecture and filters;
- marketplace categorization / AnyMarket;
- Google/XML catalog capability;
- category ordering and hierarchy risk;
- variations and Similar Products;
- brands;
- labels/tags;
- product availability messaging;
- product search/filter/reporting;
- quick editing guardrails;
- field authority between JET and Sankhya;
- package dimensions and freight;
- cross docking;
- main/alternative/multiphoto image behavior;
- product video;
- restricted delivery, freight, out-of-stock, gift and inventory controls;
- unit multiplier and purchase limits;
- product display ordering;
- Compre Junto / Related / Purchased relationships;
- mass product update spreadsheet;
- sets and kits;
- unique attributes;
- porcelain tile m²/box calculator;
- product groups tied to storefront layout IDs;
- Products Awaited / Avise-me lead handling.

## Initial guardrails

- `JET-RULE-001` — Do not assume a sandbox; changes may affect the live storefront.
- `JET-RULE-002` — Editable does not mean authoritative; identify the system of record before mutations.
- `JET-RULE-003` — Category deletion/editing must respect Sankhya authority and hierarchy.
- `JET-RULE-004` — Integration queue operations are privileged and should be done with integrator/JET support.
- `JET-RULE-005` — Do not delete storefront product groups bound by layout IDs.
- `JET-RULE-006` — Mass-update spreadsheets must preserve the JET model/schema and exact expected values.

## Visual evidence candidates

High-value future evidence extraction:

- MOD1 09:00–13:43 — administrator permissions / access areas.
- MOD1 20:50–29:15 — transactional e-mail templates, tags and senders.
- MOD1 32:24–41:13 — Editar Dados da Loja flags.
- MOD1 58:57–01:07:58 — banner types, fields, placement, desktop/mobile and ordering.
- MOD1 01:08:22–01:11:22 — custom pages structure.
- MOD2 02:01–06:16 — category tree and edit fields.
- MOD2 21:46–26:04 — submenu behavior, ordering and hierarchy risk.
- MOD2 38:24–41:19 — brand configuration and home highlight.
- MOD2 51:07–01:06:18 — product fields and system authority.
- MOD2 01:15:27–01:20:00 — bulk update spreadsheet.
- MOD2 01:28:28–01:34:54 — Unique Attribute and porcelain calculator (maximum visual priority).
- MOD2 01:34:56–01:40:48 — Similar Products display types.
- MOD2 01:40:48–01:44:19 — storefront product groups.
- MOD2 01:44:19–01:49:05 — Avise-me and Products Awaited.

## Next phase

Phase 3: reconcile Module 1 and Module 2, identify confirmation/supersession/contradictions and close the current state of configurations before building the Visual Evidence Map.
