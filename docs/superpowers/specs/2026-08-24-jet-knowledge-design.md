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

## Fluxo aprovado

1. Inventário integral MOD1 + MOD2.
2. Atomização e classificação.
3. Reconciliação entre módulos.
4. Visual Evidence Map.
5. Validação transcript ↔ tela.
6. Construção da camada canônica: Platform Map, Knowledge Base, Pending/Decision Registers, Integration Matrix, Strategy Playbook e Evidence Index.
7. Futuramente: POs/ITs.
8. Futuramente: RAG/knowledge para agentes.
9. Futuramente: arquitetura mínima do time de agentes.

## Board operacional

https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre
