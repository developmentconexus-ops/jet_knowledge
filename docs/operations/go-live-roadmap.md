# JET Go-Live Readiness Roadmap

> **Status authority:** Trello board `JET Knowledge — Metal Nobre`.
>
> This document records the planning model and target sequence. It is not authoritative for the current Kanban state or due dates after the Trello board changes.

Board: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

## Operating principle

The launch plan separates **phase** from **status**:

- phase: Trello color label;
- status: `Backlog`, `Próximo`, `Em andamento`, `Aguardando / Validar`, `Concluído`.

Color convention:

- 🔴 red — go-live blocker;
- 🟡 yellow — pre-launch;
- 🔵 blue — launch / cutover;
- 🟢 green — post-launch;
- 🟣 purple — continuous optimization.

A task can therefore be a red go-live blocker and simultaneously be waiting on a third party.

## Phase portfolio at this checkpoint

### 🔴 Go-live blockers

`PEN-001`, `PEN-002`, `PEN-007`, `PEN-008`, `PEN-009`, `PEN-010`, `PEN-014`, `PEN-018`, `PEN-019`, `PEN-020`, `PEN-024`, `PEN-026`, `PEN-029`, `PEN-030`, `PEN-031`, `PEN-033`, `PEN-035`.

### 🟡 Pré-lançamento

`PEN-003`, `PEN-004`, `PEN-005`, `PEN-006`, `PEN-011`, `PEN-015`, `PEN-016`, `PEN-017`, `PEN-022`, `PEN-023`, `PEN-025`, `PEN-034`, `PEN-038`.

### 🔵 Lançamento / cutover

`PEN-032`, `PEN-036`.

### 🟢 Pós-lançamento

`PEN-012`, `PEN-021`, `PEN-027`, `PEN-028`, `PEN-037`.

### 🟣 Melhoria contínua

`PEN-013`.

## Target preparation calendar

These dates are planning targets, not the official go-live date.

| Date | Target work |
|---|---|
| 25 Aug 2026 | `PEN-029` payment-gateway meeting at 09:30 BRT |
| 26 Aug 2026 | `PEN-031` define go-live target and objective readiness criteria |
| 27 Aug 2026 | `PEN-001` integration/category mapping validation |
| 28 Aug 2026 | `PEN-002`, `PEN-008`, `PEN-009`, `PEN-010`, `PEN-030` — category model, image mapping, porcelain attribute/conversion and freight decision |
| 31 Aug 2026 | `PEN-014`, `PEN-019` — sender and company/email identity data |
| 1 Sep 2026 | `PEN-005`, `PEN-018`, `PEN-022` — brand mapping, store parameters and banner specifications |
| 2 Sep 2026 | `PEN-004`, `PEN-007`, `PEN-015`, `PEN-020`, `PEN-033` — category presentation, product-data readiness, e-mail routing, privacy and admin access |
| 3 Sep 2026 | `PEN-003`, `PEN-016`, `PEN-017`, `PEN-038` — navigation refinement, Fale Conosco, transactional templates and support handoff verification |
| 4 Sep 2026 | `PEN-006`, `PEN-011`, `PEN-023`, `PEN-024`, `PEN-032`, `PEN-034` — brands, porcelain UX, banners, institutional content, cutover plan and analytics readiness |
| 7 Sep 2026 | `PEN-025`, `PEN-035` — priority SEO and end-to-end launch validation |

## Date intentionally not set

- `PEN-036` — Go/No-Go and cutover execution: derived from the official go-live chosen in `PEN-031`.
- `PEN-037` — seven-day hypercare: derived from the actual go-live date.
- green post-launch and purple optimization work has no artificial deadline unless it becomes operationally relevant.

## Go/No-Go minimum readiness model

Before a `GO`, the project should have evidence that the relevant red go-live blockers are resolved or their residual risk is explicitly accepted. At minimum this covers:

1. payment architecture;
2. freight architecture;
3. catalog and authoritative product data;
4. Sankhya/JET integration behavior;
5. porcelain m²/box behavior when in launch scope;
6. sender/e-mail identity;
7. store parameters;
8. company/legal/institutional content required for operation;
9. admin access and permissions;
10. cleanup of test content that would leak to production;
11. end-to-end order validation;
12. domain/publication cutover plan.

`PEN-031` will turn this model into an explicit launch target and acceptance gate. `PEN-036` is the final execution gate.