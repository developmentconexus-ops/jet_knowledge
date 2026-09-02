# Campanhas promocionais, JET Search e Venda Assistida

Módulo 3 do treinamento. O Fabrício não gravou vídeo — entregou a lista de temas
com os tutoriais oficiais correspondentes (`video/MOD3/MOD3.txt`). Este documento
é a leitura desses 20 tutoriais em 02/09/2026, escrita com as nossas palavras.

Cobre as áreas que o `admin-module-inventory.md` marcava como lacuna: os 8
módulos de campanha promocional, os 4 de Jet Search, Venda Assistida e as
ferramentas do Google. É a matéria-prima do futuro **agente de campanha** e do
**agente de SEO**.

Fonte de cada afirmação: o tutorial correspondente em `experience.jet.com.br`,
catalogado em `docs/sources/experience-index.md`. Conteúdo do portal não é
reproduzido — o portal proíbe.

---

## 1. Antes de tudo: o que o plano libera

Três ferramentas declaram exigência de plano nos próprios tutoriais:

| Ferramenta | Plano declarado no tutorial |
|---|---|
| Desconto progressivo | Evolution Pro **ou NEO** |
| Oferta relâmpago | **somente Evolution Prime** |
| Gestão de brindes | **somente Evolution**, e exige implementação pela JET |

A loja `metalnobre` roda na **NEO**, e os três módulos **aparecem no menu**
do painel. Aparecer no menu não prova que está contratado: a JET costuma exibir
a entrada e bloquear na tela.

→ `UNC-011`. Resolver com o Fabrício antes de planejar qualquer campanha em cima
dessas três. Planejar Black Friday com oferta relâmpago que o plano não cobre é
descobrir tarde.

## 2. Incompatibilidades e armadilhas — leia isto antes das tabelas

Esta é a parte que economiza retrabalho.

**1. Frete grátis por cupom não funciona com hub de frete.** O tutorial de cupom
exclusivo declara: a opção "Frete Grátis" do cupom **não é compatível** com
Frenet, Intelipost e LogControl. A **Frenet está ativa em produção** na nossa
loja (`estado-da-loja-2026-09-02.md`). Ou seja: hoje, cupom com frete grátis não
entrega frete grátis.

Atenção à distinção — o módulo **Campanha de frete grátis** é outro, tem regra
própria por faixa de CEP e escolha da forma de envio, e **não** declara essa
incompatibilidade. Se a Metal Nobre quiser frete grátis, o caminho é esse
módulo, não a flag do cupom.

**2. "Valor por compra" e "Quantidade de produtos" olham a loja inteira.** Em
Desconto em produtos, esses dois limites são avaliados sobre **todos** os
produtos do carrinho, não só os participantes. O desconto, porém, cai só nos
participantes. Uma campanha com mínimo de R$ 150 em porcelanato dispara se o
cliente fizer R$ 150 com qualquer coisa da loja.

**3. Campanha usada não se apaga.** Cupom, Leve X Pague Y, desconto progressivo,
oferta relâmpago, brinde e frete grátis: todos bloqueiam exclusão depois do
primeiro pedido. O caminho é **inativar**, não excluir. Consequência para um
agente: criar campanha é ação praticamente irreversível.

**4. Duas funções dependem da versão do front-end.**

| Recurso | Versão mínima declarada |
|---|---|
| Etiqueta de produto na vitrine (Leve X Pague Y) | front-end 2.71.72 |
| Dica e imagem promocional na PDP (Desconto progressivo) | layout NEO 2.71.49 |

Não sabemos em que versão a nossa loja está → `UNC-012`, pergunta para o
Fabrício. Já temos scripts customizando o checkout, então a versão importa.

**5. O percentual que o cliente vê é uma soma.** Na oferta relâmpago, o
percentual exibido na vitrine e na PDP é a **soma** do desconto da forma de
pagamento com o desconto calculado entre "De" e "Por". O número da vitrine não é
o desconto da campanha isolado — e é ele que o cliente compara com o concorrente.

**6. Produto brinde precisa de estoque e status ativo.** Brinde sem estoque
quebra a campanha silenciosamente. Como o estoque vem do Sankhya, um brinde é um
produto do ERP que precisa ser mantido — não é um item virtual.

---

## 3. Campanhas promocionais — o que cada ferramenta faz

Caminho comum: **Marketing > Campanhas promocionais**.

| Ferramenta | Onde o desconto incide | Segmentação de produto | Cumulativa com cupom | Nota |
|---|---|---|---|---|
| **Cupom — Cliente exclusivo** | qualquer produto da loja | — (vale para tudo) | — | uso único, amarrado a nome + e-mail do cliente; período em dias |
| **Cupom — Desconto em produtos** | todos ou produtos específicos | produto, categoria, marca, grupo | configurável, inclusive múltiplos cupons | geração em lote; limite por pedido e por cliente; segmento B2C/B2B |
| **Leve X Pague Y** | valor total do pedido | produto, categoria, marca, grupo | flag própria | ativa sozinha no carrinho quando as regras batem; aceita mais de uma regra |
| **Desconto progressivo** | preço **"De"** ou **"Por"** (escolha na campanha) | produto, categoria, marca, grupo | flag própria | permite marcar produto como **exceção**: conta para a faixa mas não recebe desconto |
| **Oferta relâmpago** | **escreve no preço "Por"** | todos ou produtos específicos | flag própria | temporizador na vitrine e no mini-carrinho |
| **Campanha de frete grátis** | frete | por região e/ou categoria | — | faixa de CEP início/fim; escolhe quais formas de envio recebem |
| **Gestão de brindes** | produto adicional grátis | por valor mínimo, ou por modal (formulário na PDP) | — | brinde exclusivo via flag "Produto brinde" nas Configurações adicionais do produto |
| **Vale compra** | forma de pagamento no checkout | — | combina com outra forma de pagamento | crédito/débito por cliente, com validade; importação em lote |

### Empilhamento de descontos

Nos cupons percentuais existe uma escolha explícita de base de cálculo:

- **sobre o carrinho com outros descontos** — desconto sobre desconto, considera
  campanhas já aplicadas (Leve X Pague Y, progressivo);
- **sobre o valor total dos produtos** — ignora os descontos das outras campanhas.

Esta é a alavanca que define se as campanhas se somam ou se anulam. Sem uma
regra escrita, cada campanha nova é uma aposta na margem.

### Frete grátis por cupom — ordem de escolha

Quando o cupom concede frete grátis, a JET escolhe qual frete zerar nesta ordem:
menor valor → em empate, maior prazo → em novo empate, tabela personalizada mais
antiga. (Lembrando o item 1 acima: com hub de frete ativo, isso não se aplica.)

### Vale compra — parâmetros fora da tela da campanha

Duas configurações moram em **Minha Loja > Opções da loja > Editar dados da loja**:

- **base do saldo**: valor total do pedido (inclui frete) ou valor total dos
  produtos (exclui frete);
- **limite de uso por pedido**: percentual, padrão **100%**.

Isso conecta o vale compra ao `PEN-018` (parametrizações da loja) — mexer lá
muda o comportamento do vale sem passar pela ferramenta de vale.

---

## 4. Conflito de autoridade com o Sankhya

O preço da Metal Nobre vive no Sankhya (`TGFEXC.VLRVENDA`, `CODTAB 0`). Três
ferramentas de campanha escrevem sobre preço dentro da JET:

| Ferramenta | O que faz com o preço | Risco |
|---|---|---|
| Oferta relâmpago | grava desconto **no preço "Por"** | a próxima sincronização do Sankhya pode sobrescrever e derrubar a campanha no meio |
| Desconto progressivo (%) | incide sobre "De" ou "Por" | se a integração alimenta só um dos dois campos, a escolha muda o resultado |
| Desconto em produtos | desconto no carrinho, não no cadastro | menor risco — não toca o cadastro do produto |

Pergunta não resolvida, e ela é a decisão central antes de qualquer agente de
campanha: **a integração alimenta o preço "De", o "Por", ou os dois?** Enquanto
não houver resposta, nenhuma campanha percentual tem resultado previsível.

→ `UNC-013`. Resolver com a BLP, e registrar como `MN-DEC`.

Regra de segurança que deriva daí: campanha que **grava no cadastro do produto**
(oferta relâmpago) é território disputado com o ERP. Campanha que age **no
carrinho** (cupom, Leve X Pague Y, progressivo por valor, frete grátis, brinde,
vale compra) não disputa. Preferir a segunda família enquanto a autoridade de
preço não estiver escrita.

---

## 5. Jet Search — a alavanca de conversão do catálogo técnico

Caminho: **Jet Search**. Quatro ferramentas que se alimentam entre si.

| Ferramenta | O que faz |
|---|---|
| **Termos mais buscados** | mostra o que o cliente digitou, **incluindo buscas que não retornaram produto** |
| **Configurações de sinônimos** | agrupa palavras equivalentes; até **200 sinônimos ativos**; leva até **10 minutos** para propagar |
| **Relevância da busca** | define o peso de cada campo do produto (nome, descrição, etc.) no ranking, e permite desligar campos |
| **Impulsionar produtos** | destaca produtos na busca e também em vitrine, categorias, marcas e grupos |

O ciclo operacional é: ler os termos sem resultado → criar sinônimo → o termo
passa a achar produto. Erro de digitação e vocabulário do cliente ("vetidos" no
exemplo do tutorial; no nosso caso "porcelanato bege" contra
`POC.AV.AC120X120`) deixam de ser venda perdida.

**Por que isso importa mais aqui do que na média.** Nosso catálogo é nomeado em
código técnico. A relevância da busca pondera **campos do produto** — quer
dizer, o resultado depende diretamente de `AD_NOME_ECOM` e `AD_DESC_ECOM`
estarem preenchidos e escritos na linguagem do cliente. O trabalho de
enriquecimento (`PEN-007`) não é cosmético: é o que faz a busca funcionar.

Os 200 sinônimos são um teto real. Vale gastá-los guiado por dado dos Termos
mais buscados, não por palpite.

---

## 6. Venda Assistida

Dois papéis, dois tutoriais: cadastro/gestão de vendedores no painel, e a
atuação do vendedor na loja. O painel expõe **Gestão de vendedores** e
**Carteiras de clientes** sob Pedidos.

A Metal Nobre tem loja física e balcão. Venda assistida é a ponte entre o
vendedor de balcão e o e-commerce — pedido feito pelo vendedor em nome do
cliente, com carteira própria. Nenhuma decisão registrada sobre usar ou não.

Consequência que precisa ser pensada antes, não depois: se o vendedor de balcão
passa a lançar pedido pela JET, o pedido entra no Sankhya pela mesma esteira do
e-commerce (TOP 313), e a apuração por canal deixa de separar loja de online.
Isso afeta comissão, meta e o relatório por canal.

---

## 7. Ferramentas do Google e Meta

| Ferramenta | Situação hoje | Pendência |
|---|---|---|
| Rastreamento e conversão (GA4 / GTM) | não configurado | `PEN-034` |
| Search Console | não verificado | insumo do agente de SEO |
| Google Merchant / Shopping | não configurado | `PEN-028` |
| reCAPTCHA | **não ativado** | `PEN-051` |
| Pixel do Facebook / Meta | não configurado | — |

O caminho do GTM é **Marketing > Ferramentas do Google**, não Scripts
personalizados — a própria tela de scripts avisa isso.

---

## 8. Decisões pendentes que este documento revela

1. **Quais ferramentas de campanha a Metal Nobre vai usar** — 8 disponíveis,
   zero decididas. Sem isso, o agente de campanha não tem escopo.
2. **Autoridade do preço "De" / "Por"** entre JET e Sankhya (`UNC-013`).
3. **Regra de empilhamento** de descontos — base de cálculo e piso de margem.
4. **Frete grátis**: pelo módulo de campanha (funciona com Frenet) e não pela
   flag do cupom (não funciona).
5. **Venda Assistida**: usar ou não, e como separar canal na apuração.
6. **Confirmar com o Fabrício** o que o plano NEO libera (`UNC-011`) e a versão
   do front-end (`UNC-012`).

## 9. Incertezas abertas por esta leitura

| ID | Incerteza | Como resolver |
|---|---|---|
| `UNC-011` | Oferta relâmpago (Evolution Prime), Gestão de brindes (Evolution) e Desconto progressivo (Evolution Pro/NEO) estão contratados no nosso plano? Aparecem no menu, o que não prova acesso. | Fabrício / JET |
| `UNC-012` | Versão do front-end/layout da loja, que gatilha etiqueta de vitrine (≥2.71.72) e imagem promocional na PDP (≥2.71.49). | Fabrício / JET |
| `UNC-013` | A integração alimenta o preço "De", o "Por" ou ambos? Define o resultado de toda campanha percentual e o risco de sobrescrita da oferta relâmpago. | BLP + teste real |

## Método e validade

Lido dos tutoriais oficiais em 02/09/2026. Tutorial descreve **capacidade da
plataforma**, não configuração da nossa loja e não decisão da Metal Nobre
(guardrails 4 e 5). Nenhum módulo desta lista foi aberto no painel ainda — o
estado real de cada um continua por confirmar.
