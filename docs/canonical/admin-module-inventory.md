# Inventário de módulos do painel JET — loja `metalnobre`

Levantamento direto do menu do painel em **02/09/2026**, sessão real da loja
`metalnobre` (`gestaodeprodutos.plataformaneo.com.br`). Storefront:
`https://metalnobre.plataformaneo.com.br/`.

Este documento responde uma pergunta só: **o que existe no painel**. Não diz o
que está configurado, nem quem é dono do dado — para isso, `platform-map.md` e
`integration-authority-matrix.md`.

## Por que ele existe

O `platform-map.md` foi derivado dos treinamentos e cobre 44 capabilities. O
painel tem **92 módulos**. A diferença não é detalhe: são áreas inteiras que
nenhum documento canônico menciona — JET Analytics (7 relatórios), Jet Search
(4 módulos), campanhas promocionais (8 módulos), campos personalizados de
cliente/pedido, webhooks, multi centro de distribuição, log de produtos.

Um agente que só leia o platform-map vai concluir que essas coisas não existem.

## Legenda de cobertura

- `COBERTO` — a capability aparece no `platform-map.md`.
- `PARCIAL` — aparece, mas o módulo real do painel é mais amplo que a linha do mapa.
- `LACUNA` — não existe em nenhum documento canônico.
- `⚠` — lacuna de alto impacto: mexe em preço, estoque, autoridade de dado, auditoria ou segurança.

## Produtos

| Módulo | Cobertura | Nota |
|---|---|---|
| Meus produtos | COBERTO | `PEN-007` |
| Categorias | COBERTO | `PEN-001`, `PEN-002` |
| Etiqueta (flag) | COBERTO | `JET-RULE-006` |
| Marcas | COBERTO | `PEN-005`, `PEN-006` |
| Variações de produtos (grade) | COBERTO | não é a estratégia atual (`MN-DEC-002`) |
| Disponibilidade de produto | COBERTO | — |
| Campos personalizados no produto | ⚠ LACUNA | candidato natural para os campos `AD_*` do Sankhya; exige decisão de autoridade antes de qualquer uso |
| Sugestões de conjuntos | COBERTO | — |
| Ordenação de produtos | LACUNA | afeta merchandising de vitrine e listagem |
| Kits de produtos | COBERTO | — |
| Atributos únicos | COBERTO | `PEN-009` m²/caixa |
| Produtos semelhantes | COBERTO | `PEN-012` |
| Grupo de produtos | COBERTO | `JET-RULE-005`, `PEN-026` |
| Gestão B2B | LACUNA | a plataforma tem capability B2B; não há decisão Metal Nobre registrada |
| Reajuste de preço em lote | ⚠ LACUNA | preço é do Sankhya. Módulo que escreve preço direto na JET é candidato a guardrail de bloqueio |
| Produtos aguardados | COBERTO | `PEN-027` |
| Limite de compra por produto e valor | LACUNA | controle de abuso / compra atacado no varejo |
| Log de Produtos | ⚠ LACUNA | trilha de auditoria. É o que permite provar o que um agente ou a integração alterou |

## Pedidos

| Módulo | Cobertura | Nota |
|---|---|---|
| Meus pedidos | PARCIAL | coberto pelo lado da integração, não pelo lado operacional do painel |
| Gestão de vendedores (Venda Assistida) | LACUNA | — |
| Carteiras de clientes (Venda Assistida) | LACUNA | — |
| Gestão de trocas / devoluções | ⚠ LACUNA | a política de troca/devolução está em aberto; o módulo que a executa não está documentado |
| Carrinhos abandonados | ⚠ LACUNA | alavanca direta de conversão e insumo do futuro agente de campanha |
| Pedidos em aprovação a mais de 48 horas | LACUNA | fila de exceção operacional |
| Reserva e liberação de estoque | ⚠ LACUNA | toca diretamente `PEN-044` (estoque simultâneo) |
| Gerenciar status de pedido | ⚠ LACUNA | relacionado à questão aberta do status `A` vs `L` na integração Sankhya |

## Clientes

| Módulo | Cobertura | Nota |
|---|---|---|
| Meus clientes | LACUNA | 0 clientes na loja hoje |
| Caixa de entrada - Fale conosco | COBERTO | `PEN-016` |
| Integração CNPJ.ws | LACUNA | enriquecimento automático de cadastro PJ |

## Minha Loja

| Módulo | Cobertura | Nota |
|---|---|---|
| Editar dados da loja | COBERTO | `PEN-018` |
| Redes sociais | COBERTO | `PEN-021` |
| Ativar login social | LACUNA | impacta cadastro e checkout |
| Instagram na vitrine | COBERTO | `PEN-021` |
| Redirecionamento 301 de url | COBERTO | `MN-DEC-007` |
| Banners | COBERTO | `PEN-022`, `PEN-023` |
| Comentários dos clientes | COBERTO | `UNC-010` (status de descontinuação) |
| Rodapé e selos | LACUNA | selos de segurança pesam em conversão |
| Páginas personalizadas | COBERTO | `PEN-024` |
| Perguntas frequentes | LACUNA | — |
| Geolocalização | LACUNA | — |
| Aparência da loja - layout | ⚠ LACUNA | é a superfície de `PEN-046` e `PEN-050`; auditar experiência sem conhecer este módulo gera relatório sem endereço |
| Scripts personalizados | ⚠ LACUNA | é por onde entram GA4/GTM (`PEN-034`) e qualquer script de terceiro |

## Marketing

| Módulo | Cobertura | Nota |
|---|---|---|
| Cupons de desconto | LACUNA | — |
| Oferta relâmpago | LACUNA | — |
| Gestão de brindes | LACUNA | — |
| Campanha de frete grátis | ⚠ LACUNA | frete grátis é decisão de margem, não de marketing; precisa de regra antes de existir |
| Desconto progressivo | LACUNA | — |
| Leve x pague y | LACUNA | — |
| Desconto em produtos | ⚠ LACUNA | desconto na JET vs preço do Sankhya: autoridade não resolvida |
| Temporizador de produtos no carrinho | LACUNA | — |
| Vale compra para clientes | LACUNA | — |
| E-mails de newsletter | LACUNA | — |
| Rastreamento e conversão (Google) | PARCIAL | `PEN-034` cita instrumentação, não o módulo |
| Search Console (Google) | LACUNA | insumo do futuro agente de SEO |
| Google Merchant / Shopping | PARCIAL | `PEN-028` trata do de/para de categorias |
| ReCaptcha | ⚠ LACUNA | **não ativado hoje** — o próprio painel avisa na home |
| CRM Bônus | LACUNA | — |
| RD Station | LACUNA | — |
| Lista de eventos | LACUNA | — |
| Facebook | LACUNA | — |
| Edrone | LACUNA | — |
| XML de Produtos | COBERTO | `PEN-028` |

Todo o bloco de campanhas promocionais (8 módulos) é a matéria-prima do futuro
agente de campanha e hoje não tem uma linha de documentação nem uma decisão da
Metal Nobre associada.

## JET Analytics

| Módulo | Cobertura |
|---|---|
| Faturamento | ⚠ LACUNA |
| Pedidos | ⚠ LACUNA |
| Análise RFM | ⚠ LACUNA |
| Análise oportunidades de venda | ⚠ LACUNA |
| Torre de controle | ⚠ LACUNA |
| Produtos | ⚠ LACUNA |
| Clientes | ⚠ LACUNA |

Área inteira ausente do cérebro. Importa duas vezes: é o que mede o resultado do
e-commerce, e é onde um número da JET pode divergir do faturamento apurado pelo
Sankhya — que tem regra própria de TOP e devolução. A divergência entre os dois
vai aparecer, e precisa de uma regra de reconciliação antes de aparecer.

## Configurações

| Módulo | Cobertura | Nota |
|---|---|---|
| Criar emails de alerta | COBERTO | `PEN-015` |
| Gerenciar usuários administradores | COBERTO | `PEN-033` |
| Personalizar e-mails | COBERTO | `PEN-017` |
| Campos personalizados — Clientes | ⚠ LACUNA | — |
| Campos personalizados — Pedidos | ⚠ LACUNA | é onde pode viver a chave de reconciliação com `TGFCAB.AD_NUMPEDIDO_ECOM` |
| Gerenciar credenciais de integração | COBERTO | `JET-RULE-004` |
| Gerenciar Webhooks | ⚠ LACUNA | alternativa ao polling de fila; muda a arquitetura da integração |
| Gestão de frete | COBERTO | `PEN-043` |
| Reajuste de preço do frete | LACUNA | `PEN-040`/`PEN-041` tratam de custo, não deste módulo |
| Gestão de pagamento | COBERTO | `PEN-042` |
| Gestão de taxas por produto / região | LACUNA | — |
| Gestão multi centro de distribuição | ⚠ LACUNA | relaciona `UNC-004` (cross-docking) e o local 10101 do Sankhya |
| Forma de pagamento por produto | LACUNA | — |
| Credenciais OpenAPI (V 1.0) | LACUNA | segunda superfície de API além da usada hoje |
| Rits Compra recorrente | LACUNA | app de terceiro |

## Marketplaces, App Store e Busca

| Módulo | Cobertura | Nota |
|---|---|---|
| JETHUB | PARCIAL | `PEN-028` trata do de/para, não do hub |
| App store — parceiros | LACUNA | catálogo de integrações de terceiro disponíveis |
| Jet Search — Configurações de sinônimos | ⚠ LACUNA | busca interna: maior alavanca de conversão em catálogo técnico |
| Jet Search — Impulsionar produtos | ⚠ LACUNA | — |
| Jet Search — Termos mais buscados | ⚠ LACUNA | insumo direto do agente de SEO e do sortimento (`PEN-047`) |
| Jet Search — Relevância da busca | ⚠ LACUNA | — |

## Estado da loja em 02/09/2026

Números da home do painel: **8 pedidos**, **8 produtos ativos**, **0 clientes**.

Consequência operacional: `PEN-046` (auditoria de experiência como usuário) não
pode ser executado com valor hoje — o próprio card exige produtos reais
representativos. A auditoria depende de `PEN-007` e `PEN-047` avançarem antes.

## Achados imediatos

| # | Achado | Encaminhamento |
|---|---|---|
| 1 | reCAPTCHA não ativado — alerta na home do painel | pendência nova, pré-go-live: loja pública sem proteção contra bot em formulário e login |
| 2 | 92 módulos no painel contra 44 capabilities no mapa canônico | varredura módulo a módulo das lacunas `⚠` antes de definir o time de agentes |
| 3 | Loja com 8 produtos e 0 clientes | `PEN-046` fica bloqueado por `PEN-007`/`PEN-047`; a dependência não está registrada no board |
| 4 | Nem admin nem storefront tinham URL registrada em nenhum documento | registradas neste documento |

## Canais de suporte da JET expostos no painel

| Canal | Endereço |
|---|---|
| Base de conhecimento (JET Experience) | `https://experience.jet.com.br/` |
| Central de atendimento / workspace | `https://workspace.jet.com.br/portal` |
| Central de suporte (chamados) | `https://jet.topdesk.net/tas/public/login/form` |
| Telefone | (11) 3512-9880 |
| WhatsApp | `wa.me/5516997277511` |

Relevante para `PEN-038` / `UNC-009`: os canais existem e estão publicados no
painel. Isso não resolve a incerteza — ela é sobre quem é o dono da conta e qual
a rota de escalonamento acordada, não sobre a existência do canal.

## Método

Inventário extraído do próprio menu do painel autenticado, não de treinamento.
Reflete o que a loja `metalnobre` enxerga com o perfil usado — outro perfil
administrativo pode ver menos (`PEN-033`). Reexecutar após qualquer mudança de
plano, contratação de app ou migração de layout da JET.
