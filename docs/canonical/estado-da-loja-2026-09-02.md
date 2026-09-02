# Estado real da loja `metalnobre` — 02/09/2026

Leitura direta do painel autenticado, módulo a módulo. **Nada foi alterado** —
só leitura, conforme a guardrail 1 (não existe sandbox).

Serve para uma coisa: separar o que o board *diz* do que a plataforma *está*.
Vários cards marcados como pendentes já estão configurados, e há configuração em
produção que nenhum card cobre.

## Arquitetura do painel

O admin não é um sistema só. É um conjunto de microserviços com hosts próprios,
mais um painel legado que ainda responde por várias telas:

| Host | Área |
|---|---|
| `gestaodeprodutos.plataformaneo.com.br` | home e produtos |
| `gestaodepedidos.plataformaneo.com.br` | pedidos |
| `gestaodeloja.plataformaneo.com.br` | minha loja |
| `gestaodemarketing.plataformaneo.com.br` | marketing |
| `configuracoes.plataformaneo.com.br` | configurações |
| `painel2.plataformaneo.com.br` | **painel legado** — frete, pagamento, dados da loja e telas `painel-novo.asp?idMenu=###` |

Consequência prática: a mesma sessão navega entre hosts, e um link de módulo pode
levar do painel novo para o legado sem aviso. É a materialização do `RCN-002`
(migração de layout antigo/novo). Documentação com print precisa dizer em qual
painel a tela vive, senão ninguém acha de novo.

Storefront: `https://metalnobre.plataformaneo.com.br/`

## Pagamento — `PEN-042`

| Gateway | Estado |
|---|---|
| **Pagar.me PSP** | ✅ ativo, ambiente **Produção** |
| **Pagamento (Offline)** | ✅ ativo, ambiente **Produção** |
| Antifraude | **nenhum provedor ativo** |

O gateway escolhido em `MN-DEC-011` **já está integrado e em produção**. O card
`PEN-042` está em "Em andamento" descrevendo a integração como pendente — a
configuração acabou; o que resta é a validação ponta a ponta (`PEN-035`).

Pagamento Offline ativo explica os pedidos de porcelanato de teste que chegaram
ao Sankhya sem tipo de negociação da série e-commerce.

Aba de antifraude vazia. A JET oferece ClearSale, Braspag e outros. Antes de
publicar, é preciso responder se o antifraude do próprio Pagar.me cobre o risco
ou se falta contratar camada — não é uma pergunta que se responde por print.

## Frete — `PEN-043`

CEP de origem: **38.405-105** — Rua Ásia, Tibery, Uberlândia/MG.

| Transportadora / hub | Estado |
|---|---|
| **Frenet** | ✅ **ativa, ambiente Produção** |
| Entrega personalizada | 3 tabelas ativas |
| JET Envios (Smart Envios) | inativa (ambiente Produção) |
| Intelipost | inativa (ambiente Homologação) |
| Ship Smart | inativa |
| Lincros | inativa |
| Correios | contrato com Correios: **Não** |

Frenet, escolhida em `MN-DEC-012`, **está ativa em produção**. Mesma situação do
Pagar.me: o card descreve como pendente algo que já foi feito.

Dois pontos que merecem decisão explícita e não estão em card nenhum:

1. **Correios sem contrato.** Os pedidos de teste cotaram Sedex Contrato (03220)
   via Frenet. Cotar Correios pela Frenet e ter contrato próprio com os Correios
   são coisas diferentes, com preço diferente. Qual é o modelo pretendido?
2. **Entrega personalizada com 3 tabelas ativas** convivendo com a Frenet. Se as
   duas cotarem a mesma região, qual ganha? Sem regra explícita, o cliente vê o
   que a plataforma decidir, não o que a Metal Nobre decidiu.

## Integração

| Item | Estado |
|---|---|
| Webhooks cadastrados | **nenhum** |
| Status de pedido personalizados | **nenhum** (01 a 09 são padrão da plataforma e não podem ser excluídos) |
| Reserva e liberação de estoque | nenhum registro pendente |
| Credenciais de integração | em uso pela integradora |

**Nenhum webhook** significa que a integração hoje funciona por *polling* de
fila. A JET oferece notificação por evento. Isso não é defeito — é uma escolha
de arquitetura que ninguém registrou como escolha, e que muda o tempo de reação
a pedido novo, mudança de status e cancelamento.

A ausência de status personalizados fecha uma questão aberta: os status que a
integração enxerga são os 01–09 padrão da plataforma. Qualquer combinação com o
`STATUSNOTA` do Sankhya é mapeamento da integradora, não da JET.

## Catálogo e loja

| Item | Estado |
|---|---|
| Produtos ativos | **8** |
| Pedidos | 8 |
| Clientes cadastrados | **0** |
| Centros de distribuição (Multi-CD) | **nenhum** |
| Personalização de produto | nenhuma |
| Scripts personalizados | 3 ativos |
| reCAPTCHA | **não ativado** |

### Correção a `admin-module-inventory.md`

O módulo **"Campos personalizados no produto"** não é o que o nome sugere. A tela
se chama **Personalização** e serve para o *cliente escolher* uma personalização
na página do produto (gravação, cor, etc.). **Não é** um repositório de atributos
de dado, e portanto **não é** candidato a receber os campos `AD_*` do Sankhya.
O caminho para atributo de dado continua sendo Atributos Únicos (`PEN-009`).

Restrição registrada na própria tela: campos de personalização não aparecem em
"Compre Junto" nem em "Kits de Produtos".

### Multi-CD — incompatibilidades declaradas pela plataforma

A tela avisa que Multi-CD **não é compatível** com: Kit de Produtos, Lista de
Eventos, Compra Automática, Produto com Entrega Restrita e **Importação de
Produtos em lote**.

Isso importa antes de qualquer decisão sobre operar mais de um CD: perder
importação em lote de produtos é caro para um catálogo que ainda vai ser
carregado. A decisão de Multi-CD precisa vir *antes* da carga do catálogo, não
depois.

### Scripts ativos na loja

| Script | Local | Tipo | Desde |
|---|---|---|---|
| Whatsapp flutuante | Footer | Javascript | 11/08/2026 |
| Script de estilização do checkout | Footer | CSS | 10/08/2026 |
| Script de layout do checkout | Footer | Javascript | 10/08/2026 |

O checkout já recebeu customização visual por script. Quem for auditar a
experiência (`PEN-046`) precisa saber disso: comportamento estranho no checkout
pode vir daqui, não do produto padrão da JET.

GA4/GTM **não** estão aqui. A própria tela orienta a usar Marketing > Google —
relevante para `PEN-034`.

## Usuários administradores — `PEN-033`

| Nome | Login | E-mail | Status |
|---|---|---|---|
| Metal Nobre | `metalnobre` | leandro.theodoro@… | Ativo (conta mestre) |
| BLP Integração | `blpintegracao` | integracao@blpit.com.br | Ativo |
| Vinicius Theodoro Cruz Andrade | `vinicius.theodoro` | vinicius@… | Ativo |
| Laura André | `laura.andre` | marketing@… | Ativo |

Quatro usuários. A integradora (**BLP**) tem usuário administrativo próprio desde
15/07/2026 — o que é correto para rastreabilidade, e torna o escopo de permissão
dela uma decisão de segurança, não um detalhe. `PEN-033` continua válido, mas a
pergunta certa não é "quantos usuários existem" e sim **"qual escopo cada um
tem"**, que exige abrir o perfil de cada conta.

## Impacto no board

| Card | Estado no board | Estado real | Ação |
|---|---|---|---|
| `PEN-042` Pagar.me | Em andamento, blocker | gateway ativo em produção | reduzir escopo para validação E2E |
| `PEN-043` Frenet | Em andamento, blocker | hub ativo em produção | reduzir escopo para validação E2E |
| `PEN-033` usuários | Próximo, blocker | 4 usuários, escopos não auditados | manter; refocar em permissões |
| `PEN-046` auditoria UX | Próximo | loja com 8 produtos e 0 clientes | registrar dependência de `PEN-007`/`PEN-047` |

## Pendências que a varredura revelou e o board não cobre

1. reCAPTCHA não ativado em loja que vai a público.
2. Antifraude sem provedor — decisão pendente sobre a cobertura do Pagar.me.
3. Webhooks vs polling — arquitetura de integração nunca decidida explicitamente.
4. Precedência entre Frenet e Entrega personalizada na cotação.
5. Contrato próprio com Correios — sim ou não.
6. Multi-CD precisa ser decidido antes da carga de catálogo, pelas
   incompatibilidades declaradas.
7. Escopo de permissão do usuário da integradora.

## Método e validade

Levantado em 02/09/2026 por leitura do painel com a conta mestre. Outro perfil
pode enxergar menos. Estado de plataforma muda sem aviso — este documento é uma
fotografia datada, não uma afirmação permanente (guardrail 6).
