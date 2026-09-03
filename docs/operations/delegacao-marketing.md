# O que o time de marketing pode absorver — 02/09/2026

Análise dos 62 cards do board contra a pergunta: **o que acelera se sair da mão
do Leandro?**

Resposta curta: **18 cards**, sendo um deles o gargalo do go-live inteiro.

## O gargalo é validação, não produção

Estado real do staging de catálogo (`data/catalogo.db`, lido em 02/09):

| | produtos |
|---|---|
| Total no escopo vendável | 4.715 |
| Prontos de verdade (nome + descrição + peso + imagem) | **2.056** |
| Enriquecidos aguardando validação humana | **1.952** |
| Já validados | 159 |
| Rejeitados | 55 |
| Sem enriquecimento (nome_gerado + pendente) | 2.549 |

O farol de validação automática já classificou o que está enriquecido:
**319 verde · 1.349 amarelo · 283 vermelho**.

O amarelo é o volume. Amarelo não é erro — é "passou, mas alguém precisa olhar".
São 1.349 fichas de olhar-e-decidir, com atalho de teclado, no viewer que já
existe. **Isso é trabalho de conferência, não de criação.** É o que o padrão 07
já previa delegar: "Leandro calibra primeiro → delega funcionário".

Enquanto essa fila não anda, o catálogo não carrega; sem catálogo não há
auditoria de UX; sem auditoria não há relatório para a JET. É a cadeia crítica
inteira presa numa fila de conferência.

## Recomendação de sortimento do piloto (`PEN-047`)

Cortes possíveis, com prontidão e faturamento 12 meses:

| Recorte | Produtos | Prontos | % | Faturamento 12m |
|---|---|---|---|---|
| **Núcleo** | 500 | **405** | **81%** | **R$ 19,9 mi** |
| Núcleo + giro | 1.717 | 1.039 | 60% | R$ 21,5 mi |
| Onda 1 | 2.665 | 1.588 | 59% | R$ 17,0 mi |
| Tier A | 3.050 | 1.439 | 47% | R$ 23,1 mi |
| Catálogo todo | 4.715 | 2.056 | 43% | R$ 24,3 mi |

**Recomendação: lançar com o núcleo.** 500 produtos — 11% do catálogo — carregam
**82% do faturamento**. E é o recorte mais pronto: 81% já tem nome, descrição,
peso e imagem.

O que falta nos 95 restantes do núcleo: 91 sem descrição, 77 sem nome, 50 sem
imagem, **zero sem peso**. É uma semana de trabalho, não um mês.

Ir para núcleo + giro dobra o esforço (mais 678 produtos a preparar) e adiciona
R$ 1,6 mi de faturamento. Não paga o atraso. Giro entra na onda 2, depois do
go-live, com a operação já rodando.

## Os 18 cards que marketing pode assumir

### Bloco 1 — Catálogo (o que destrava a data)

| Card | Tarefa | Por que serve ao marketing |
|---|---|---|
| `PEN-007` | **Validar o farol amarelo no viewer** — 782 no recorte núcleo+giro | conferência com atalho A/R, auditoria de quem validou; não exige Sankhya |
| `PEN-007` | **Caçar as 50 fotos faltantes do núcleo** | o OneDrive de fotos já é do marketing |
| `PEN-007` | Revisar as 91 descrições faltantes do núcleo | copy de produto é ofício deles |

Ordem: validar primeiro o **verde** (rápido, calibra a régua), depois o
**amarelo**. O **vermelho** volta para o Leandro — ali o problema costuma ser
dado, não texto.

### Bloco 2 — Conteúdo e vitrine

| Card | Tarefa |
|---|---|
| `PEN-022` | Confirmar dimensões oficiais dos banners com a JET |
| `PEN-023` | Organizar e produzir os banners de lançamento |
| `PEN-024` | Migrar/escrever as páginas institucionais |
| `PEN-006` | Marcas na JET: imagem, URL, texto e SEO por marca |
| `PEN-004` | Definir quais categorias aparecem no menu e o "Ver todos" |

### Bloco 3 — Comunicação com o cliente

| Card | Tarefa |
|---|---|
| `PEN-017` | Revisar os templates de e-mail transacional (texto e visual) |
| `PEN-019` | Logo e dados que saem nos e-mails |
| `PEN-016` | Fale Conosco: layout, campos e destinatários |
| `PEN-015` | Definir remetente e cópias por evento de e-mail |
| `PEN-020` | **Rascunhar** a política de privacidade — validação jurídica é externa |

### Bloco 4 — Presença e busca

| Card | Tarefa |
|---|---|
| `PEN-021` | Conectar redes sociais e vitrine do Instagram |
| `PEN-025` | SEO por prioridade: loja → categorias → produtos estratégicos |
| `PEN-046` | Auditoria de experiência como cliente, desktop e mobile |
| `PEN-050` | Alimentar o relatório para o Fabrício com os achados |

### Bloco 5 — Depois do go-live

`PEN-027` leads de Produtos Aguardados · `PEN-012` famílias de Produto
Semelhante · `PEN-057` varredura dos módulos de campanha.

## O que o marketing NÃO deve tocar

A conta `laura.andre` é administradora. Sem regra escrita, isso é um risco.

| Nunca | Por quê |
|---|---|
| Gestão de pagamento, Gestão de frete | mexe em dinheiro que entra e sai |
| Credenciais de integração, Webhooks, Usuários administradores | superfície de segurança |
| **Reajuste de preço em lote**, **Desconto em produtos** | preço é do Sankhya; a JET sobrescreve na próxima sincronização |
| Excluir ou reordenar categorias | reordenar muda hierarquia (`JET-RULE-003`) |
| Excluir grupos de produtos existentes | amarrados por ID no layout da home (`JET-RULE-005`) |
| Qualquer campanha promocional | não existe regra de margem definida (`PEN-057`) |
| Cadastro de produto direto na JET | o Sankhya é o dono; edição na JET se perde |

Regra de bolso para o time: **se a tela fala de dinheiro, de acesso ou de preço,
não é nossa.** Conteúdo, imagem, texto e conferência são.

Encaminhamento: `PEN-033` deve rebaixar a conta `laura.andre` para um perfil sem
acesso a pagamento, frete, credenciais e usuários. Guardrail escrito só vale se a
permissão acompanhar.

## Efeito no cronograma

Com marketing absorvendo o bloco 1 e o bloco 2 em paralelo, S2 e S3 deixam de ser
sequenciais para o Leandro. A data de **06/10** ganha folga, e as três decisões
da semana (sortimento, peso do porcelanato, PIX) voltam a ser o único caminho
crítico — que é onde elas deveriam estar.

O que **não** acelera com mais gente: `PEN-045` (Ricardo), `PEN-010` (BLP),
`PEN-059` (Fabrício). Dependência externa não paraleliza.
