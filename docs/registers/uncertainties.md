# Uncertainty Register

## Purpose

Items here must **not** be treated as confirmed facts by operators, future documents, RAG retrieval or agents.

Resolution must come from the named evidence path; inference is not an acceptable substitute.

## Register

| ID | Uncertainty | Required resolution path | Consumers / related |
|---|---|---|---|
| `UNC-001` | Sitemap refresh frequency: trainer cited 12 or 24 hours without confirming. | Current JET documentation/support or direct observed behavior. | `JET-KB-054`; future SEO/technical docs |
| `UNC-002` | Automation of “Quem comprou, comprou também”: trainer needed to validate and said it was 100% manual at that time. | Current JET capability validation before claiming automation. | `JET-KB-029`; `PEN-013` |
| `UNC-003` | Whether m²/box conversion/return handling is already implemented by Rodrigo/integration. | Integration evidence + end-to-end order/inventory test. | `JET-KB-040`; `PEN-010`, `PEN-035` |
| `UNC-004` | Whether/how cross-docking is represented and mapped in Sankhya. | Rodrigo/integration mapping evidence. | `JET-KB-018`; Integration Matrix |
| `UNC-005` | Competitor/product examples explicitly made as guesses/opinions by trainer. | Do not resolve unless the example becomes operationally relevant; then research the specific claim independently. | Prevents accidental fact promotion. |
| `UNC-006` | Legal/LGPD statements made verbally during training. | External legal/compliance validation before becoming policy, PO/IT rule or agent guardrail. | `JET-KB-057`; `PEN-020`, access/privacy docs |
| `UNC-007` | Comparative opinions about AI models made by trainer. | Not needed for JET operations; exclude from canonical technical facts. | Agent/RAG hygiene |
| `UNC-008` | Exact first-access/e-mail behavior before vs after publication, including temporary password, `Recuperar Senha`, dispatch infrastructure and sender relationship. | Current JET behavior/support validation in project context. | `JET-KB-006`; `PEN-033`, `PEN-014` |
| `UNC-009` | Current JET support handoff state. Training only proves that handoff had not yet completed at that historical moment. | Confirm current support channel, owners and escalation route. | `JET-KB-070`; `PEN-038` |
| `UNC-010` | Current status of features described as “being discontinued”, especially customer product comments. | Revalidate current JET feature availability/status before documentation or agent use. | `JET-KB-071` |

## Resolution states

When an uncertainty is resolved, preserve the ID and append a resolution record containing:

```yaml
uncertainty_id: UNC-003
resolved_at:
resolution:
evidence:
impacted_knowledge_ids:
impacted_pending_ids:
```

Do not delete the original uncertainty text.

## Consumption guardrails

1. Prefer `UNKNOWN` / `REQUIRES_EXTERNAL_VERIFICATION` over completing a gap by inference.
2. Temporal speech such as “today”, “still”, “being discontinued” or “not yet” is not a permanent current fact.
3. A screenshot of a field does not resolve integration implementation or field authority.
4. A training recommendation does not resolve an uncertainty about current platform behavior.
5. Legal uncertainty is resolved externally, not through more screenshots of the JET UI.
