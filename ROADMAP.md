# ROADMAP — Programa de Banners de Marcas Metal Nobre

> Este roadmap descreve sequência, gates e critérios de aceite do programa de banners.
>
> **Não é autoridade do status operacional da JET/Trello.**
>
> Para detalhes e estado do caso atual, ler `TASK.md`.

## Resultado final desejado

Construir um processo simples e repetível para produzir banners premium de marcas da Metal Nobre com:

- produtos reais e controlados;
- direção de arte específica por marca;
- alta fidelidade visual;
- branding determinístico;
- dimensão adequada à UX da página;
- arquivo compatível com a JET;
- baixa dependência de histórico de chat.

O processo deve ser generalizável sem transformar uma marca em template de outra.

---

## B0 — Foundation do método

### Objetivo
Separar planejamento, geração e pós-produção.

### Contrato
`Planner / Art Director → tarefa Codex de geração por marca → Post-production → JET validation`

### Artefato canônico
`.claude/skills/metal-nobre-banner-art-director/SKILL.md`

### Critério de aceite
- skill orienta planejamento, não render;
- referências reais são enviadas diretamente à geração;
- logo/copy ficam fora da geração;
- prompt final é curto;
- QA existe;
- não existe dependência obrigatória de banner anterior.

**Checkpoint:** metodologia já definida e adotada.

---

## B1 — Deca: fechar brief de 320 px

### Objetivo
Transformar o aprendizado dos testes anteriores em um brief simples para a nova arquitetura.

### Entrada já definida
- 4 produtos obrigatórios;
- Product Story;
- copy;
- target experimental `1920×320`;
- geração planejada para recorte seguro, pois o alvo final 6:1 excede a proporção de geração direta documentada;
- direção arquitetônica/editorial;
- layout horizontal com negative space à esquerda.

### Trabalho
- revisar `TASK.md`;
- ajustar qualquer detalhe que o usuário pedir;
- obter aprovação explícita do brief e do generation prompt.

### Gate
**D1 — aprovação do usuário.**

### Critério de aceite
O usuário consegue responder “aprovado” sem que o gerador ainda tenha sido chamado.

**Checkpoint atual:** aqui.

---

## B2 — Deca: preparar referências diretas

### Objetivo
Eliminar ambiguidade dos produtos.

### Trabalho
- localizar/confirmar imagem oficial correta de cada SKU;
- preferir packshots limpos e em boa resolução;
- mapear Image 1–4 exatamente como `TASK.md`;
- garantir que não há imagem errada, variante errada ou acabamento incorreto.

### Critério de aceite
Quatro imagens prontas para serem anexadas diretamente à sessão de geração, cada uma com função explícita.

---

## B3 — Deca: geração base

### Objetivo
Gerar apenas **ambiente + integração dos produtos**, sem branding.

### Trabalho
- abrir sessão de imagem;
- anexar as quatro referências diretamente;
- usar o prompt aprovado;
- gerar a composição numa tarefa Codex separada, com arquivos versionados no workspace;
- produzir uma prévia recortada em 1920×320 antes da avaliação visual;
- não pedir logo/copy ao modelo.

### Gate
**D2 — aprovação visual da geração base e da prévia recortada.**

### Reprovar se
- faltar produto;
- produto estiver irreconhecível;
- houver substituição/duplicação;
- bacia tocar/sair da direita;
- composição virar colagem;
- ambiente dominar produtos;
- negative space da esquerda não funcionar;
- produto hero perder hierarquia;
- o recorte 1920×320 cortar ou comprimir visualmente qualquer produto obrigatório.

---

## B4 — Deca: pós-produção

### Objetivo
Transformar a geração aprovada em banner de produção.

### Trabalho
- aplicar logo Deca oficial;
- aplicar headline/supporting;
- ajustar hierarquia tipográfica;
- recortar/redimensionar exatamente para 1920×320;
- exportar master;
- otimizar formato/peso;
- garantir ≤ 1 MB.

### Gate
**D3 — aprovação da arte final.**

### Critério de aceite
Arquivo visualmente final, sem texto de IA e sem logo recriada.

---

## B5 — Deca: teste real na JET

### Objetivo
Validar UX, não apenas a imagem isolada.

### Trabalho
- carregar/testar na página real de marca;
- observar desktop no contexto real;
- verificar quanto da grade de produtos aparece acima/na primeira dobra;
- validar legibilidade de logo/copy;
- validar cortes e safe area;
- validar qualidade após compressão/upload;
- se necessário, comparar 320 px com pequena variação de altura, sem assumir regra antes do teste.

### Gate
**D4 — decisão da altura e composição de produção.**

### Critério de aceite
A página parece uma página de e-commerce premium e o banner não impede acesso visual rápido aos produtos.

### Saída possível
- manter 1920×320;
- ou recalibrar a altura com evidência real da JET.

---

## B6 — Consolidar learnings na skill

### Objetivo
Generalizar somente o que foi provado.

### Trabalho
- revisar o ciclo Deca;
- identificar o que é:
  - regra geral;
  - regra de categoria;
  - escolha específica Deca;
  - limitação técnica JET;
- atualizar skill/references apenas quando necessário;
- evitar acumular histórico experimental.

### Gate
**D5 — método Deca congelado como primeira validação.**

### Critério de aceite
A skill fica mais útil para a próxima marca sem ficar “Deca-shaped”.

---

## B7 — Docol: teste de generalização

### Objetivo
Provar que o método funciona numa segunda marca sem copiar Deca.

### Trabalho
1. entender identidade/categoria Docol;
2. selecionar produtos reais;
3. resolver referências oficiais;
4. definir Product Story própria;
5. criar novo brief;
6. criar novo prompt;
7. gerar;
8. pós-produzir;
9. validar na JET;
10. comparar o processo, não a aparência.

### Pergunta de teste
“Se removermos a logo, esta peça ainda parece uma história coerente dos produtos Docol, ou apenas uma versão do banner Deca com outra marca?”

### Critério de aceite
Mesma disciplina e qualidade; linguagem visual suficientemente própria.

---

## B8 — Escalar para o portfólio de marcas

### Objetivo
Produzir banners das demais marcas com o método estabilizado.

### Famílias de direção já reconhecidas

- **Metais / louças / cozinha:** arquitetura + produtos reais.
- **Revestimentos / superfícies:** arquitetura + materialidade.
- **Madeira:** interior + veio + calor.
- **Wellness:** água + atmosfera + relaxamento.
- **Acessórios / ferragens:** detalhe escultórico + interior refinado.

### Regras
- escolher Product Story por marca;
- não copiar cena anterior;
- produto sempre controlado;
- branding sempre oficial;
- QA antes do upload;
- teste real quando a categoria trouxer nova condição de layout.

---

## B9 — Operação repetível

### Objetivo
Fazer o processo deixar de depender de uma sessão específica de ChatGPT/Codex.

### Possíveis artefatos depois da validação multi-brand
- template mínimo de brief;
- checklist operacional;
- padrão de nomenclatura de assets;
- pasta/referência por marca;
- convenção de master/final;
- eventualmente automação de resize/compressão.

### Restrição
Não automatizar cedo demais. Primeiro provar Deca + Docol.

---

## Sequência resumida

```text
B0 Método
  ↓
B1 Deca brief 320px — D1
  ↓
B2 Referências reais
  ↓
B3 Geração sem branding + prévia recortada — D2
  ↓
B4 Pós-produção — D3
  ↓
B5 Teste real JET — D4
  ↓
B6 Generalizar learnings — D5
  ↓
B7 Docol
  ↓
B8 Outras marcas
  ↓
B9 Operacionalizar/automatizar
```

## Regra de avanço

Não pular um gate porque a ferramenta “consegue gerar”.

A qualidade do programa vem de:
`produto correto → story correta → geração controlada → pós determinística → validação real`.

## Estado de retomada

Para a próxima sessão/Codex:

**começar em B1 / Gate D1**.

O brief e o prompt candidatos estão em `TASK.md`. Não gerar Deca até aprovação explícita do usuário.
