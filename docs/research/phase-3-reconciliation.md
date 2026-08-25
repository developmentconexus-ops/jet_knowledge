# Phase 3 — Cross-Module Reconciliation

## Scope

This reconciliation uses only the two training transcripts supplied for the Metal Nobre JET project:

- `Treinamento Módulo 2` — product/catalog/integration training;
- `Treinamento Módulo 1` — administration/store configuration/SEO/content training.

No external JET documentation or video evidence is used in this phase. Statements remain source-derived unless explicitly marked as interpretation, decision, uncertainty or pending validation.

## Chronology and precedence

Despite the filenames, **Módulo 2 occurred before Módulo 1**. Módulo 2 repeatedly says banners/SEO would be covered in the next Módulo 1. Therefore:

1. later explicit information in Módulo 1 may clarify earlier generic statements from Módulo 2;
2. an actual configuration changed during Módulo 2 remains evidence of project state unless a later source explicitly changes it;
3. recommendations do not override executed decisions;
4. uncertainty is preserved rather than resolved by inference.

## Canonical reconciliations

### RCN-001 — Environment and mutation risk

The training states that changes made in the JET panel affect the project store directly and that no sandbox/homologation store is available in this scenario. The Metal Nobre store is still under a temporary JET domain while the project is not officially published.

**Canonical treatment:** `RISK_GUARDRAIL`. Never assume a safe sandbox for mutating actions.

Sources: MOD1 00:53–01:24.

### RCN-002 — Interface names and layout migration

JET was migrating tools between an old and a new panel layout. Internal names/positions can differ; the training says the name currently shown in the tool/tab is the one to follow, and `Ajuda`/`Saiba mais` routes to JET Experience.

**Canonical treatment:** documentation must carry capture date/interface context and avoid treating old menu positions as timeless.

Sources: MOD1 16:22–17:34.

### RCN-003 — Categories and current system authority

JET supports up to three category levels. A category with no linked product is not shown on the storefront. In the current integration model, category structure/name should originate in Sankhya; direct name edits in JET can be overwritten. URL and SEO are described as JET-local fields. Category reordering in JET can also alter hierarchy, so it is a high-risk operation when the tree is sourced from Sankhya.

**Canonical treatment:** Sankhya is the current authority for category hierarchy/name; JET is the authority for category URL/SEO unless the integration mapping is deliberately changed.

Sources: MOD2 02:01–06:16 and 21:20–26:04.

### RCN-004 — SEO priority and status

The modules are consistent. Módulo 2 establishes the priority order:

1. store SEO (`Minha Loja > Opções da Loja > Editar Dados da Loja`);
2. category SEO;
3. product SEO, prioritizing strategic/car flagship products first.

Módulo 1 then expands the operational/strategic guidance. Product-level completion may continue after publication according to the trainer.

**Canonical treatment:** platform fields are facts; ranking/performance advice remains `STRATEGIC_GUIDANCE`, not guaranteed outcomes.

Sources: MOD2 06:16 onward; MOD1 41:33–47:11.

### RCN-005 — Product authority matrix

Under the current mapping described in training:

**Sankhya/current upstream flow:** product name, GTIN, NCM, product code, stock, price, category, weight/dimensions when populated, product images and descriptions.

**JET-local / JET-managed examples:** product URL, product video, tags/labels, availability messaging, related-product relationships, Product Similar, product groups, kit/conjunto catalog constructs and various merchandising/configuration fields.

**Still unresolved:** cross-docking source/mapping, Atributo Único integration and m²/box return conversion.

**Guardrail:** UI editability does not imply field authority. Quick Edit can expose stock/price/status fields that should still be maintained upstream for Metal Nobre.

Sources: MOD2 51:07–01:08:34.

### RCN-006 — Variation vs Product Similar

JET supports variations, but the current Metal Nobre strategy in the training is to keep separate product records and use `Produto Semelhante` to give the customer a variation-like experience. This is a current strategy, not a platform limitation or irreversible architecture decision.

Sources: MOD2 27:12–35:14 and 01:34:56–01:40:48.

### RCN-007 — Brands

Brand associations originate from Sankhya in the demonstrated model. JET is used for brand image, URL, SEO, text and home/destaque configuration. The transcript supports a Metal Nobre **intent** to preserve brand-based navigation, but not proof that the final JET layout/configuration was approved and completed.

**Decision correction:** prior `MN-DEC-009` is downgraded from final decision to non-final intent.

Sources: MOD2 36:45–41:19.

### RCN-008 — Out-of-stock, `Avise-me` and executed state

The apparent differences between modules reconcile cleanly:

- during Módulo 2, `Exibir produtos e variações esgotados nas páginas de listagens` was already `Sim`;
- `Exibir ... na página do produto` was `Não` and was changed to `Sim` during the meeting;
- `Atualização automática da flag esgotado` was also changed to `Sim` during Módulo 2;
- Módulo 1 later explains that disabling the product-detail page removes access to `Avise-me` and explains the lead strategy behind `Produtos Aguardados`.

**Canonical state from the training evidence:** list view = yes; product detail = changed to yes; automatic sold-out flag = changed to yes. These are executed project-state observations, not generic recommendations.

Sources: MOD2 01:03:00–01:06:18 and 01:44:19–01:49:05; MOD1 34:12–39:13.

### RCN-009 — Transactional e-mail vs marketing e-mail

The training differentiates JET transactional/institutional e-mails from marketing automation. Transactional templates and subjects are customizable, including tags and HTML. Marketing/campaign automation is described as external/integrated tooling.

A default sender is described as required before publication. However, the exact boundary between project-mode e-mail infrastructure, temporary-password delivery and sender configuration is not fully proven by the transcript and remains open in `UNC-008` / `PEN-033`.

Sources: MOD1 20:50–29:15 and 14:21–16:05.

### RCN-010 — Integration credentials and queues

BLP credentials for the Sankhya integration had already been generated at training time. JET integration queues are separated by domain (examples include brand, product, stock and price), and the BLP team had activated the demonstrated queues. Queue activation controls whether the integrator can consume information. Load/cleanup operations should be performed with the integrator or JET support.

**Canonical treatment:** privileged integration operations; not routine user actions.

Sources: MOD1 29:23–32:09.

### RCN-011 — Two different 404 scenarios

Two unrelated causes of 404 appear in the training and must not be merged:

1. **out-of-stock detail page hidden** — when the product-detail out-of-stock flag is `Não`;
2. **legacy URL after platform migration** — addressed through 301 redirects.

Metal Nobre explicitly chose not to execute the broad 301 migration initially because the current site had very low traffic/sales and little developed Google work. That project decision does not mean 301 is an invalid JET capability.

Sources: MOD2 01:45:19–01:46:03; MOD1 53:28–58:34.

### RCN-012 — Banners

Módulo 2 intentionally defers banner training; Módulo 1 becomes the authoritative source for this topic. It covers editing vs deleting, naming, redirects, desktop/mobile assets, full/half banner types, scheduling, randomized rotation, placement, video and reordering.

The trainer recommends roughly three to four full banners to avoid perceived slowdown. Treat this as trainer guidance, not an independently benchmarked platform limit.

Sources: MOD1 58:57–01:07:58.

### RCN-013 — Custom pages

JET panel custom pages use two platform groups by default. Names/content/URL/SEO can be edited; HTML source can be used for migration. The front-end layout can visually organize those pages differently from the panel's two-group rule.

**Canonical treatment:** separate panel data model from storefront presentation.

Sources: MOD1 01:08:22–01:11:22.

### RCN-014 — External ecosystem / freight context

The App Store training shows JET as the commerce platform and presents specialized partners for areas such as freight, chat, marketing and loyalty. Freight examples include Frenet, Intelipost and SmartEnvios. This proves partner/integration capability only; it does **not** select a freight architecture for Metal Nobre.

The two transcripts also do not define the final payment gateway. `PEN-029` and `PEN-030` therefore remain independent decision work.

Sources: MOD1 01:12:44–01:14:34.

### RCN-015 — Support handoff

At the start of Módulo 1, the trainer says operational questions should still go through Fabrício/Rafa because the handoff to JET support had not yet happened. No later transcript confirms completion.

**Canonical treatment:** historical state + current-status verification required (`PEN-038`).

Source: MOD1 01:49 onward.

### RCN-016 — Time-sensitive/deprecation statements

The trainer says `Comentários de Clientes sobre o Produto` was being discontinued at training time. This is a temporal source statement, not a safe current platform fact for future manuals or agents without revalidation.

Source: MOD1 17:34 onward.

## Unresolved after reconciliation

The following items must remain unresolved rather than inferred:

- sitemap refresh interval (12h vs 24h stated without confirmation);
- automation of `Quem comprou, comprou também` (manual at training time; future intelligence uncertain);
- whether Atributo Único can be integrated from Sankhya;
- whether m²/box return conversion is already implemented;
- cross-docking existence/mapping in Sankhya;
- exact first-access/e-mail behavior before vs after publication;
- current completion state of the JET support handoff;
- current status of features described as being discontinued;
- legal/compliance claims made verbally in the training.

## Result

No structural contradiction between the two modules blocks consolidation. The material is now reconciled into:

- platform facts;
- executed Metal Nobre configuration state;
- Metal Nobre decisions/intent;
- integration authority rules;
- strategic guidance;
- temporal statements;
- unresolved questions.

The next stage is **Phase 4 — Visual Evidence Map**. Phase 4 must use the reconciled knowledge to request only screenshots/clips that materially improve operational documentation, field/path certainty, guardrails or future agent grounding.