# Trello Operating Model

Board: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

## Papel do Trello

O Trello é a fonte de verdade do estado operacional das pendências `PEN-###`.

Isso inclui:

- coluna/status atual;
- etiqueta de fase atualmente vinculada;
- due date vigente;
- checklist operacional atual.

O GitHub é a autoridade para conhecimento canônico, decisões, incertezas, significado das evidências, regras de integração e escopo canônico dos IDs `PEN-###`.

## Colunas — estado atual

- `Backlog` — identificado, mas ainda não priorizado para execução imediata.
- `Próximo` — selecionado para execução em curto prazo.
- `Em andamento` — trabalho efetivamente iniciado.
- `Aguardando / Validar` — depende de terceiro, decisão, confirmação técnica ou evidência adicional.
- `Concluído` — ação encerrada e validada.

## Etiquetas coloridas — fase de lançamento

A etiqueta indica quando a pendência precisa ser tratada no ciclo. A coluna continua indicando o estado atual. Os títulos permanecem limpos no formato `PEN-### — descrição`.

- 🔴 **Go-live blocker**. Precisa estar resolvido, explicitamente aceito ou ter risco formalmente aceito antes do lançamento.
- 🟡 **Pré-lançamento**. Deve idealmente estar pronto antes de publicar, mas não é blocker técnico absoluto.
- 🔵 **Lançamento / Cutover**. Executado na preparação final ou na janela de publicação.
- 🟢 **Pós-lançamento**. Pode ser ativado depois da loja entrar no ar.
- 🟣 **Otimização**. Melhoria contínua, experimento ou evolução; não deve segurar o go-live.

Os nomes e cores acima foram verificados diretamente no board. O Trello, e não este arquivo, continua sendo a autoridade para a etiqueta atualmente vinculada a cada cartão.

## Regras

1. Cada pendência mantém o mesmo ID `PEN-###` durante todo o ciclo.
2. Mover o cartão no Trello atualiza o estado operacional; não é necessário editar um Markdown para refletir status.
3. O GitHub mantém contexto canônico, evidências, decisões e conhecimento; o Trello mantém workflow.
4. Antes de responder “o que está pendente?”, reler o Trello.
5. Quando uma pendência gerar conhecimento novo, registrar o resultado no GitHub antes de considerá-la encerrada quando isso for material.
6. Não duplicar cartão para a mesma pendência; atualizar/mover o cartão existente.
7. Uma etiqueta vermelha não significa automaticamente `Próximo`: um blocker pode estar em `Aguardando / Validar`, `Em andamento` ou `Backlog`. Fase e estado são dimensões independentes.
8. Itens verdes e roxos não devem ocupar `Próximo` antes da hora sem uma razão explícita.
9. Se o usuário alterar cartão, coluna, etiqueta ou data diretamente no Trello, a próxima leitura do board prevalece sobre qualquer snapshot anterior desta conversa ou do GitHub.
10. Antes de criar novo `PEN-###`, pesquisar Trello e `docs/registers/pending-index.md` para evitar duplicação semântica.
11. Um ID pode permanecer no índice canônico depois de concluído, pois continua fazendo parte da rastreabilidade histórica.

## Datas e compromissos

1. Datas no Trello podem representar reunião, deadline externo ou **data-alvo de planejamento**.
2. Datas-alvo definidas durante o planejamento são revisáveis; o estado/due date atual no Trello prevalece sobre snapshots do GitHub.
3. A data de uma reunião não significa que a pendência está concluída; o cartão continua aberto até a decisão ou entrega esperada ser registrada.
4. Pendências de decisão devem registrar os critérios usados, a decisão, justificativa e novas pendências quando necessário.
5. A data oficial de go-live não deve ser inferida das datas-alvo de preparação. Ela será definida explicitamente em `PEN-031`.
6. `PEN-036` (Go/No-Go) e `PEN-037` (hypercare) recebem datas derivadas somente após a definição do go-live.

## Roteamento após a Fase 6

A camada canônica v1 define o seguinte caminho de consulta:

- “O que a JET faz / quais superfícies existem?” → `docs/canonical/platform-map.md`
- “Qual é a afirmação canônica e sua classificação?” → `docs/canonical/knowledge-base.md`
- “Quem manda neste campo / onde posso escrever?” → `docs/canonical/integration-authority-matrix.md`
- “O que a Metal Nobre decidiu, prefere ou recebeu como orientação?” → `docs/registers/decisions.md` e `docs/canonical/strategy-playbook.md`
- “O que essa captura realmente prova?” → `docs/evidence/evidence-index.md`
- “O que ainda é incerto?” → `docs/registers/uncertainties.md`
- “Qual é o estado atual / prazo / coluna?” → **ler Trello ao vivo**

## Integração conceitual

`PEN-###` é a chave de correlação entre GitHub e Trello. O board continua sendo a fonte de status, fase e datas atuais. A camada canônica explica o significado e a autoridade do trabalho; não tenta congelar seu estado operacional.
