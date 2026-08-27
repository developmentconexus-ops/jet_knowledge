# JET Knowledge System Design

## Propósito

Construir uma camada canônica e auditável de conhecimento sobre a JET E-commerce na Metal Nobre, derivada de treinamentos, validações e evidências, antes da criação formal de POs/ITs e antes de definir a arquitetura final do time de agentes.

## Objetivos

1. Dominar o funcionamento da JET: telas, menus, campos, regras e capacidades.
2. Preservar matéria-prima confiável para futuras POs, ITs, checklists e treinamentos.
3. Rastrear pendências, decisões e validações sem depender de memória de conversa.
4. Capturar conhecimento estratégico de SEO, catálogo, merchandising, campanhas, CRO e CRM.
5. Mapear autoridade entre JET, Sankhya, BLP/integração, AnyMarket e demais sistemas.
6. Preparar conhecimento recuperável e seguro para futuros agentes de IA.
7. Manter rastreabilidade até módulo, timestamp e, quando necessário, evidência visual.

## Arquitetura de autoridade

### GitHub

Fonte canônica para:
- conhecimento atomizado;
- decisões;
- incertezas;
- guardrails;
- evidências;
- modelos de dados;
- documentação futura.

### Trello

Fonte de verdade para o **estado operacional vivo** das pendências `PEN-###`.

Arquivos Markdown podem indexar uma pendência, mas não devem duplicar seu status como autoridade.

### Transcrições e vídeos

São fontes primárias de evidência. Não são diretamente a base canônica de agentes porque contêm exemplos, improvisações, hipóteses e afirmações incertas.

## Classes de conhecimento

- `PLATFORM_FACT`
- `PROCEDURE`
- `BUSINESS_RULE`
- `INTEGRATION_RULE`
- `METAL_NOBRE_DECISION`
- `ACTION_REQUIRED`
- `OPEN_QUESTION`
- `STRATEGIC_GUIDANCE`
- `RISK_GUARDRAIL`
- `TROUBLESHOOTING`
- `TRAINER_UNCERTAINTY`
- `VISUAL_REQUIRED`

## Modelo atômico

Cada item deverá carregar, quando aplicável:

- `knowledge_id`
- `type`
- `capability`
- `module`
- `timestamp_start`
- `timestamp_end`
- `subject`
- `statement`
- `scope`: `JET_PLATFORM` ou `METAL_NOBRE`
- `authority`: `JET`, `SANKHYA`, `INTEGRATION`, `METAL_NOBRE`, `UNKNOWN`
- `certainty`: `CONFIRMED`, `TRAINER_RECOMMENDATION`, `METAL_NOBRE_DECISION`, `UNCERTAIN`, `REQUIRES_EXTERNAL_VERIFICATION`
- `operational_risk`: `NONE`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`
- `visual_required`
- `future_consumers`
- `evidence`

## Princípios de reconciliação

1. Capacidade da JET não é decisão da Metal Nobre.
2. Recomendação do instrutor não é regra da plataforma.
3. Hipótese ou dúvida não vira fato.
4. Campo editável não determina sistema mandante.
5. Alterações executadas durante o treinamento podem representar configuração vigente e devem ser separadas de tarefas abertas.
6. Afirmações jurídicas ou regulatórias do treinamento exigem validação externa antes de virar regra de compliance.
7. Procedimentos críticos para futuras ITs exigem evidência visual quando o transcript não captura suficientemente a interface.

## Fluxo aprovado e estado

1. Inventário integral MOD1 + MOD2. — **CONCLUÍDO**
2. Atomização e classificação. — **CONCLUÍDO na camada canônica v1**
3. Reconciliação entre módulos. — **CONCLUÍDO**
4. Visual Evidence Map. — **CONCLUÍDO**
5. Validação transcript ↔ tela. — **CONCLUÍDO**
6. Construção da camada canônica: Platform Map, Knowledge Base, Pending/Decision Registers, Integration Matrix, Strategy Playbook e Evidence Index. — **CONCLUÍDO (v1)**
7. POs/ITs. — **READINESS GATE CONCLUÍDO; knowledge-first drafting EM ANDAMENTO; release seguirá somente onde a base está suficientemente decidida/validada**
8. Futuramente: RAG/knowledge para agentes.
9. Futuramente: arquitetura mínima do time de agentes.

## Camada canônica v1

- `docs/canonical/platform-map.md` — mapa humano das capacidades e fronteiras.
- `docs/canonical/knowledge-base.md` — ledger canônico atomizado/classificado.
- `docs/canonical/integration-authority-matrix.md` — autoridade e política segura de escrita por dado/capacidade.
- `docs/canonical/strategy-playbook.md` — decisões, intenções e guidance separados de fatos de plataforma.
- `docs/evidence/evidence-index.md` — o que cada evidência visual validada realmente prova.
- `docs/registers/decisions.md` — decisões/classificações históricas normalizadas.
- `docs/registers/uncertainties.md` — lacunas e caminho exigido para resolução.
- `docs/registers/pending-index.md` — índice canônico de escopo das pendências; status vivo continua no Trello.

## Phase 7 — document readiness and knowledge-first drafts

`docs/iso/phase-7-document-readiness.md` classifica cada candidato a PO/IT em:

- `READY_FOR_DRAFT`;
- `DRAFT_READY_RELEASE_BLOCKED`;
- `BLOCKED`;
- `DEFER`.

O gate não cria um segundo backlog: `PEN-###` e `UNC-###` existentes continuam donos das lacunas.

### Rascunhos knowledge-first já criados

- `docs/iso/drafts/it-bulk-update-jet-managed-product-fields.md` — atualização massiva via planilha, com autoridade, guardrails, erro/verificação e pontos de reassistida;
- `docs/iso/drafts/it-product-group-maintenance.md` — manutenção/criação de grupos, preservando IDs vinculados ao layout;
- `docs/iso/drafts/release-blocked-procedural-knowledge.md` — núcleo procedural estável de usuários/acessos, e-mails, filas, Produto Semelhante, Avise-me, banners, páginas e publicação de privacidade, mantendo blockers explícitos;
- `docs/research/strategic-rewatch-checklist.md` — reassistida futura orientada por delta contra a base canônica, sem retranscrever as aulas.

A prioridade nesta etapa é **não perder conhecimento válido só porque o documento ISO final ainda não está formatado ou liberado**. Ao mesmo tempo, nenhum gap de integração, estado atual, responsabilidade ou jurídico deve ser preenchido por inferência.

## Regra para as próximas etapas

PO/IT, RAG e agentes devem consumir a camada canônica v1, **não** os transcripts crus como fonte operacional direta. Quando houver conflito com estado vivo ou nova evidência, atualizar a camada canônica preservando proveniência/supersessão.

Um PO/IT não deve ser liberado como instrução operacional se o texto precisar preencher por inferência um `UNKNOWN`, `UNC-###`, mapeamento de autoridade ou valor atual de go-live ainda não validado.

A reassistida estratégica deve produzir **deltas** — conhecimento novo, correções, evidência mais forte, passos/guardrails/troubleshooting faltantes — e reconciliá-los com os IDs existentes.

## Board operacional

https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre
