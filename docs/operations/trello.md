# Trello Operating Model

Board: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

## Papel do Trello

O Trello é a fonte de verdade do estado operacional das pendências `PEN-###`.

## Colunas

- `Backlog` — identificado, mas ainda não priorizado para execução imediata.
- `Próximo` — selecionado para execução em curto prazo.
- `Em andamento` — trabalho efetivamente iniciado.
- `Aguardando / Validar` — depende de terceiro, decisão, confirmação técnica ou evidência adicional.
- `Concluído` — ação encerrada e validada.

## Regras

1. Cada pendência mantém o mesmo ID `PEN-###` durante todo o ciclo.
2. Mover o cartão no Trello atualiza o estado operacional; não é necessário editar um Markdown para refletir status.
3. O GitHub mantém contexto canônico, evidências, decisões e conhecimento; o Trello mantém workflow.
4. Antes de responder “o que está pendente?”, reler o Trello.
5. Quando uma pendência gerar conhecimento novo, registrar o resultado no GitHub antes de considerá-la encerrada quando isso for material.
6. Não duplicar cartão para a mesma pendência; atualizar/mover o cartão existente.

## Integração conceitual

`PEN-###` é a chave de correlação entre GitHub e Trello. URLs específicas de cartão podem ser acrescentadas ao índice do GitHub quando isso trouxer valor, mas o board continua sendo a fonte de status.
