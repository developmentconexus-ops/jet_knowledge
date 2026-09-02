# jet_knowledge — contrato de trabalho

Base canônica de conhecimento sobre a plataforma **JET E-commerce (NEO)** na
**Metal Nobre**. Quem lê este repositório — humano ou agente — está lendo o que
a Metal Nobre considera verdade sobre a JET.

## Autoridade: quem manda em quê

| Pergunta | Fonte de verdade |
|---|---|
| O que a JET faz / como se comporta | `docs/canonical/` neste repo |
| Qual sistema é dono de um campo | `docs/canonical/integration-authority-matrix.md` |
| Qual o status de uma pendência hoje | **Trello**, nunca este repo |
| O que foi decidido e por quê | `docs/registers/decisions.md` |
| O que ainda não sabemos | `docs/registers/uncertainties.md` |
| Prova visual de uma afirmação | `docs/evidence/evidence-index.md` |

Board operacional: https://trello.com/b/4h9NzL77/jet-knowledge-metal-nobre

Um arquivo Markdown pode **indexar** uma pendência `PEN-###`; nunca duplicar o
status dela como autoridade. Status de Markdown envelhece e mente.

## As sete guardrails

Herdadas do `platform-map.md` e válidas para qualquer escrita neste repo:

1. **Não existe sandbox.** Toda mutação no painel pode atingir o projeto/loja real.
2. **Editável ≠ mandante.** Campo editável na JET não significa que a JET é dona do dado.
3. **Estado atual vence estado de treinamento** para aceite de go-live.
4. **Recomendação ≠ fato de plataforma.** Conselho de instrutor mora no Strategy Playbook.
5. **Capacidade ≠ decisão da Metal Nobre.** A feature existir não significa que vamos usar.
6. **Afirmação temporal expira.** "hoje", "ainda", "está sendo descontinuado" precisam de revalidação.
7. **Afirmação jurídica exige validação externa.** Print da UI não estabelece conformidade legal.

## Como escrever aqui

**Fato novo sobre a plataforma** → entra em `docs/canonical/knowledge-base.md` como
item atômico com `knowledge_id`, `type`, `authority`, `certainty`, `evidence`.
O modelo completo de campos está em `docs/superpowers/specs/2026-08-24-jet-knowledge-design.md`.

**Não sei ao certo** → não complete por inferência. Abra um `UNC-###` em
`uncertainties.md` com o caminho de resolução exigido. `UNKNOWN` explícito vale
mais que um preenchimento plausível, porque um agente vai agir em cima disso.

**Decisão da Metal Nobre** → `MN-DEC-###` em `decisions.md`, com a data e o motivo.
Decisão sem motivo registrado volta a ser discutida daqui a três meses.

**Trabalho a fazer** → card no Trello, não parágrafo aqui. Se o documento precisa
citar, cita o `PEN-###` e para por aí.

**Resolveu uma incerteza** → preserve o texto original do `UNC-###` e anexe o
bloco de resolução (formato em `uncertainties.md`). Apagar a incerteza apaga o
motivo pelo qual desconfiávamos.

## Segredos

Integration Key, senha, token, dados pessoais de cliente e IP **não são
conhecimento canônico** e não entram neste repo em nenhuma hipótese — nem em
print, nem em transcrição, nem em exemplo. Credenciais do programa vivem em
`~/.sankhya-gateway.env`, fora de qualquer repositório.

Antes de subir evidência visual extraída de treinamento ou do painel, tarje
credenciais, e-mails e IPs.

## Consumidores futuros

Este repo é a matéria-prima de POs/ITs e do time de agentes (manutenção, gestão
de produto, campanha, SEO, atendimento). Um agente só recebe permissão de
escrita depois que a matriz de autoridade disser, campo a campo, o que ele pode
tocar — por isso o rigor acima não é burocracia, é o que impede um agente de
gravar num campo que o Sankhya sobrescreve na próxima sincronização.
