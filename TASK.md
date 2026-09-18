# TASK — Banners de Marcas Metal Nobre

> **Escopo atual:** programa de banners das páginas de fabricante/marca do e-commerce Metal Nobre na JET.
>
> **Autoridade:** repository current authority > este TASK > ROADMAP.md > histórico de chat.
>
> **Status operacional vivo:** Trello continua sendo a autoridade para execução operacional da JET. Este arquivo registra o contexto, decisões e gates do trabalho criativo/técnico de banners; não substitui o Kanban.

## 1. Objetivo

Criar um sistema repetível para produzir banners premium de páginas de marca na JET sem depender de um ZIP monolítico, de prompts gigantes ou de banners antigos como template.

O resultado final de cada marca é uma **imagem estática pronta para upload na JET**, com fidelidade aos produtos reais e direção de arte específica para a marca.

## 2. Arquitetura aprovada do fluxo

### A. Planner / Art Director
Responsável por:
- pesquisar/entender a marca e a categoria;
- selecionar explicitamente os produtos que aparecerão;
- verificar referências oficiais;
- definir Product Story;
- definir hierarquia dos produtos;
- definir direção de arte, ambiente, materiais, luz e composição;
- definir copy;
- gerar um prompt curto e preciso;
- gerar spec de pós-produção e checklist de QA.

Skill canônica:
`.claude/skills/metal-nobre-banner-art-director/SKILL.md`

Método complementar quando disponível:
`UI/UX Pro Max / banner-design`
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/banner-design/SKILL.md

### B. Tarefa Codex de geração — uma por marca
Mantém a geração e suas revisões visuais fora da conversa de planejamento. Recebe um pacote fechado após D1 e B2:
- brief e prompt aprovados;
- imagens reais dos produtos escolhidos, anexadas diretamente e mapeadas por SKU/função;
- destino dos arquivos e critério de recorte para o tamanho final.

Usa a ferramenta integrada de geração de imagens do Codex por padrão. A tarefa não decide estratégia, mix ou copy e não reconstrói instruções a partir de ZIPs, prompts antigos ou histórico de chat. Salva a geração selecionada e a prévia recortada em arquivos versionados no workspace; devolve os caminhos, dimensões medidas e pontos de QA para D2.

Responsável por gerar:
- ambiente;
- integração arquitetônica;
- produtos dentro do ambiente.

Não deve ser responsável por:
- escolher livremente o mix de produtos;
- recriar logo oficial;
- escrever headline/supporting copy;
- decidir estratégia da marca.

### C. Pós-produção determinística
Responsável por:
- aplicar logo oficial;
- aplicar headline;
- aplicar supporting copy;
- ajustar/cortar para o tamanho final;
- otimizar/comprimir;
- validar peso e dimensões;
- produzir arquivo final da JET.

## 3. Regras permanentes já decididas

1. Não usar banners antigos gerados como referência visual por padrão.
2. Não transformar Deca em template visual para todas as marcas.
3. Consistência entre marcas vem de qualidade, hierarquia, sofisticação, produto e disciplina tipográfica — não de repetir ambiente/câmera/paleta.
4. O planner escolhe os produtos; o gerador não escolhe o mix.
5. Quando fidelidade importa, imagens reais dos produtos são anexadas diretamente à sessão de geração.
6. Logo oficial é aplicada deterministicamente na pós-produção.
7. Copy final é aplicada deterministicamente na pós-produção.
8. O gerador não deve inventar, substituir, duplicar ou redesenhar produtos obrigatórios; verificar visualmente, pois o prompt não garante fidelidade exata.
9. Entregável é imagem. Não produzir HTML/CSS/página como parte deste fluxo.
10. Limite informado da JET: **máximo 1 MB**.
11. Recomendação originalmente informada pela JET: **1920 × 500 px**; Metal Nobre pode deliberadamente usar altura menor.
12. A altura não vira regra global até ser testada visualmente na página real.
13. A proporção da imagem gerada e o tamanho final da JET são coisas distintas. O enquadramento da geração deve reservar uma faixa segura para o recorte final; D2 avalia a prévia já recortada.
14. Uma tarefa Codex separada por marca concentra geração e iterações. A conversa de planejamento concentra decisões e gates.

## 4. Caso de validação atual — Deca

### Estado do checkpoint

A nova metodologia está aceita.

O **brief e o prompt Deca 1920 × 320 px descritos abaixo foram aprovados explicitamente pelo usuário em 2026-09-18 (Gate D1)**. As quatro referências de B2 foram conferidas por SKU contra as fichas técnicas da Deca e estão preparadas no workspace de imagens. Próximo passo: B3, geração base em tarefa Codex separada e avaliação no Gate D2.

### Produtos obrigatórios

| Papel | Produto | Referência |
|---|---|---|
| Hero | Misturador Level Black Matte | `2880.BL26.MT` |
| Hero pair | Cuba Slim branca | `L.11040.17` |
| Secondary | Chuveiro de teto Black Matte | `1992.BL.TET.MT` |
| Secondary | Bacia suspensa Slim Total Clean | `KP.8630.17` |

### Product Story validado anteriormente

- **Hero zone:** misturador + cuba.
- **Secondary:** chuveiro.
- **Secondary:** bacia.
- Os quatro produtos precisam existir na composição.
- A bacia deve ficar completamente dentro do enquadramento/safe area.
- A cena deve parecer um único ambiente arquitetônico, não uma colagem de packshots.

### Copy validada

Headline:
`Design para viver cada detalhe.`

Supporting:
`Metais, louças e acabamentos com sofisticação atemporal.`

### Dimensão em validação nesta rodada

`1920 × 320 px`

Razão: `6:1`.

Motivo:
- o banner de 500/650 px ocupava altura excessiva na página de marca;
- a intenção é permitir que o usuário veja a abertura da marca e chegue mais cedo à grade de produtos;
- 320 px dá um pouco mais de espaço aos quatro produtos e à leitura do banner sem voltar à altura de 500 px;
- 320 px é **hipótese de UX a testar na JET**, não nova regra técnica universal.

A geração integrada não oferece controle de dimensão exata no chamado da ferramenta. A proporção final 6:1 também excede o limite 3:1 documentado para geração direta. Portanto, compor para um recorte seguro: a imagem base pode ter mais altura, mas todos os produtos obrigatórios e o espaço de branding devem permanecer dentro da faixa que resultará em 1920 × 320 px. Verificar o recorte real antes de D2.

### Direção de arte proposta para esta rodada

Linguagem:
- architectural editorial;
- premium;
- contemporânea;
- quiet luxury;
- banheiro brasileiro sofisticado;
- composição muito horizontal;
- não tentar mostrar um banheiro inteiro;
- tratar como uma faixa arquitetônica/editorial.

Ambiente:
- superfícies minerais claras;
- off-white / areia / greige;
- pedra natural clara;
- madeira apenas se discreta;
- Black Matte dos metais como contraste;
- pouca decoração;
- nada de showroom carregado;
- evitar clichê de hotel de luxo.

Luz:
- daylight premium suave;
- sombras controladas;
- materialidade realista;
- contraste suficiente para os metais pretos;
- sem excesso de brilho/render artificial.

### Composição proposta

Faixas aproximadas, não grid rígido:
- `0–700 px`: negative space para logo/copy em pós;
- `720–1270 px`: hero zone — misturador + cuba;
- `1220–1570 px`: chuveiro integrado à arquitetura;
- `1530–1830 px`: bacia suspensa;
- `1830–1920 px`: margem arquitetônica/safe area.

A composição deve ser assimétrica e contínua. Não dividir o banner em quatro colunas.

### Branding na geração

A sessão de imagens deve gerar:
- ambiente;
- produtos;
- luz;
- materiais;
- composição.

Ela não deve gerar:
- logo Deca;
- headline;
- supporting;
- CTA;
- texto decorativo;
- signage.

## 5. Reference Map para a sessão de geração

Anexar diretamente as imagens nesta ordem, idealmente em boa resolução e com fundo limpo/transparente:

- Image 1 = Misturador Level Black Matte `2880.BL26.MT` — hero.
- Image 2 = Cuba Slim branca `L.11040.17` — hero pair.
- Image 3 = Chuveiro de teto Black Matte `1992.BL.TET.MT` — secondary.
- Image 4 = Bacia suspensa Slim Total Clean `KP.8630.17` — secondary.

A logo oficial **não precisa ser fornecida ao gerador** se ela será aplicada somente em pós-produção.

## 6. Generation Prompt aprovado

Prompt aprovado no Gate D1:

> Create one premium wide architectural bathroom scene intended for a final 1920×320 px e-commerce brand-banner crop. The generated landscape image may be taller; keep all four mandatory products and the left-side branding space within the central crop-safe horizontal band. Use the four supplied Deca product images as mandatory visual references and preserve their recognizable geometry, proportions, colors and finishes.
>
> Build one coherent contemporary bathroom composition, not a product collage. The main hero is the supplied Black Matte Level faucet paired naturally with the supplied white Slim basin on a refined vanity. Integrate the supplied Black Matte ceiling shower as a secondary architectural element and keep the supplied white wall-hung toilet clearly visible on the far right, fully inside the frame.
>
> Reserve the left third as calm architectural negative space for later branding and copy. Use sophisticated light mineral surfaces, warm off-white and greige tones, subtle natural stone, soft premium daylight and restrained editorial styling.
>
> Keep the products visually distinct and realistic. Do not invent, replace, duplicate or redesign them. Do not add other faucets, basins, showers or toilets.
>
> No logo, no text, no typography, no signage.

Princípio: o prompt não carrega toda a metodologia. O planner toma as decisões; as referências reais fixam os produtos; o prompt orienta a composição.

## 7. Pós-produção candidata — Deca

Canvas final:
`1920 × 320 px`

Logo:
- usar asset oficial;
- não redesenhar;
- posição inicial sugerida: canto esquerdo com margem aproximada de 80–90 px;
- tamanho final deve ser ajustado visualmente no contexto real.

Headline:
- texto exato: `Design para viver cada detalhe.`
- posição à esquerda;
- leitura principal;
- aproximadamente 36–40 px como ponto de partida, sujeito a ajuste visual.

Supporting:
- texto exato: `Metais, louças e acabamentos com sofisticação atemporal.`
- aproximadamente 17–19 px como ponto de partida;
- 1–2 linhas no máximo.

Não usar CTA nesta versão de página de marca, salvo nova decisão explícita.

Export:
- primeiro preservar um master de alta qualidade;
- depois gerar arquivo final para JET;
- preferir JPG de alta qualidade ou WebP quando operacionalmente aceito;
- PNG apenas quando houver justificativa;
- final ≤ 1 MB;
- não criar um limite artificial menor como requisito de plataforma.

## 8. QA obrigatório

### Produtos
- [ ] Os 4 produtos obrigatórios estão presentes.
- [ ] Misturador mantém geometria/proporção/acabamento reconhecíveis.
- [ ] Cuba mantém geometria Slim reconhecível.
- [ ] Chuveiro mantém forma/acabamento reconhecíveis.
- [ ] Bacia é suspensa e reconhecível.
- [ ] Bacia está completamente dentro do enquadramento.
- [ ] Nenhum produto obrigatório foi substituído.
- [ ] Nenhum produto sanitário extra foi inventado/duplicado.

### Story / composição
- [ ] Misturador + cuba formam claramente o hero.
- [ ] Chuveiro e bacia são secondary.
- [ ] Parece um único ambiente coerente.
- [ ] Não parece catálogo/colagem.
- [ ] Existe negative space utilizável à esquerda.
- [ ] A prévia recortada em 1920×320 não esmaga/corta produtos.
- [ ] Produtos não tocam bordas críticas.

### Direção de arte
- [ ] Premium e arquitetônica.
- [ ] Materialidade realista.
- [ ] Ambiente apoia produtos em vez de competir.
- [ ] O banner parece Deca sem depender apenas da logo.
- [ ] Não replica literalmente um banner antigo.
- [ ] Não vira template genérico para outras marcas.

### Branding / texto
- [ ] Logo é asset oficial aplicado depois.
- [ ] Headline está exata.
- [ ] Supporting está exato.
- [ ] Não há texto gerado pela IA dentro da cena.

### JET
- [ ] Arquivo final exatamente 1920×320 na rodada atual.
- [ ] Arquivo final ≤ 1 MB.
- [ ] Sem artefatos visíveis relevantes.
- [ ] Validado dentro da página real da JET.
- [ ] Altura permite que a grade de produtos apareça cedo o suficiente.
- [ ] Após teste, decidir manter 320 px ou recalibrar.

## 9. Gates de decisão

### Gate D1 — Aprovar brief/prompt Deca
Estado atual: **aprovado explicitamente pelo usuário em 2026-09-18**.

Sem D1:
- não gerar;
- não pós-produzir;
- não generalizar.

### Gate D2 — Aprovar geração base
Verificar produto, composição e direção visual na imagem base **e na prévia recortada em 1920×320** antes de aplicar branding final.

### Gate D3 — Aprovar versão pós-produzida
Logo/copy corretos, dimensão e peso corretos.

### Gate D4 — Validar na página real JET
A captura/visualização na página decide se 320 px funciona.

### Gate D5 — Congelar learnings
Somente depois do teste real atualizar a skill/references com regras verdadeiramente generalizáveis.

## 10. Próximo teste após Deca

**Docol** é o primeiro teste de generalização.

Objetivo:
- provar que o método mantém qualidade e disciplina;
- provar que ele **não copia o banheiro, paleta ou composição da Deca**;
- adaptar Product Story e direção à identidade Docol.

Não começar Docol antes de concluir o ciclo Deca até o gate de validação na JET, salvo decisão explícita do usuário.

## 11. Não fazer

- não ressuscitar o ZIP gigante como arquitetura principal;
- não usar prompt histórico v5/v6/v7/v8 como autoridade;
- não carregar banners antigos para a geração por padrão;
- não deixar o modelo escolher os produtos;
- não confiar em memória visual do modelo quando há packshot real;
- não pedir para a IA recriar logo;
- não codificar HTML/CSS para resolver este entregável;
- não promover 320 px a regra global antes do teste real;
- não atualizar a skill com uma preferência específica da Deca como se fosse regra multi-brand.

## 12. Cold start recomendado para Codex

1. `AGENTS.md`
2. `TASK.md`
3. `ROADMAP.md`
4. `.claude/skills/metal-nobre-banner-art-director/SKILL.md`
5. somente as references pedidas pela skill
6. consultar histórico/commits apenas se ainda houver uma lacuna factual

Ao retomar, o Codex deve começar de **B3 (geração base)**. D1 foi aprovado e B2 concluído em 2026-09-18. O mapa de referências com fontes e caminhos locais está em `C:\Users\leandro.theodoro\Pictures\imagens e-commerce\deca\referencias\REFERENCIAS.md`.
