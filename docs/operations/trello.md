# Trello Operating Model

Board: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

## Papel do Trello

O Trello é a fonte de verdade do estado operacional das pendências `PEN-###`.

## Colunas — estado atual

- `Backlog` — identificado, mas ainda não priorizado para execução imediata.
- `Próximo` — selecionado para execução em curto prazo.
- `Em andamento` — trabalho efetivamente iniciado.
- `Aguardando / Validar` — depende de terceiro, decisão, confirmação técnica ou evidência adicional.
- `Concluído` — ação encerrada e validada.

## Etiquetas coloridas — fase de lançamento

A cor da etiqueta indica quando a pendência precisa ser tratada no ciclo. A coluna continua indicando o estado atual. Os títulos permanecem limpos no formato `PEN-### — descrição`.

- 🔴 **Vermelho — Go-live blocker**. Precisa estar resolvido, explicitamente aceito ou ter risco formalmente aceito antes do lançamento.
- 🟡 **Amarelo — Pré-lançamento**. Deve idealmente estar pronto antes de publicar, mas não é blocker técnico absoluto.
- 🔵 **Azul — Lançamento / cutover**. Executado na preparação final ou na janela de publicação.
- 🟢 **Verde — Pós-lançamento**. Pode ser ativado depois da loja entrar no ar.
- 🟣 **Roxo — Melhoria contínua**. Otimização, experimento ou evolução; não deve segurar o go-live.

A integração Trello disponível nesta sessão consegue aplicar etiquetas existentes, mas não renomeá-las. Por isso a correlação canônica é pela cor; os nomes podem ser adicionados uma única vez pela interface do Trello sem alterar os vínculos dos cartões.

## Regras

1. Cada pendência mantém o mesmo ID `PEN-###` durante todo o ciclo.
2. Mover o cartão no Trello atualiza o estado operacional; não é necessário editar um Markdown para refletir status.
3. O GitHub mantém contexto canônico, evidências, decisões e conhecimento; o Trello mantém workflow.
4. Antes de responder “o que está pendente?”, reler o Trello.
5. Quando uma pendência gerar conhecimento novo, registrar o resultado no GitHub antes de considerá-la encerrada quando isso for material.
6. Não duplicar cartão para a mesma pendência; atualizar/mover o cartão existente.
7. Uma etiqueta vermelha não significa automaticamente `Próximo`: um blocker pode estar em `Aguardando / Validar`, `Em andamento` ou `Backlog`. Fase e estado são dimensões independentes.
8. Itens verdes e roxos não devem ocupar `Próximo` antes da hora sem uma razão explícita.

## Datas e compromissos

1. Datas no Trello podem representar reunião, deadline externo ou **data-alvo de planejamento**.
2. Datas-alvo definidas durante o planejamento são revisáveis; o estado/due date atual no Trello prevalece sobre snapshots do GitHub.
3. A data de uma reunião não significa que a pendência está concluída; o cartão continua aberto até a decisão ou entrega esperada ser registrada.
4. Pendências de decisão devem registrar os critérios usados, a decisão, justificativa e novas pendências quando necessário.
5. A data oficial de go-live não deve ser inferida das datas-alvo de preparação. Ela será definida explicitamente em `PEN-031`.
6. `PEN-036` (Go/No-Go) e `PEN-037` (hypercare) recebem datas derivadas somente após a definição do go-live.

## Integração conceitual

`PEN-###` é a chave de correlação entre GitHub e Trello. O board continua sendo a fonte de status e datas atuais; a cor da etiqueta é a fonte visual da fase de lançamento.