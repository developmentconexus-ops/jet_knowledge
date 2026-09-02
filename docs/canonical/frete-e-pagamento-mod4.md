# Frete e pagamento — sessão de configuração (Módulo 4)

Transcrito do vídeo `[Metal Nobre] Treinamento Módulo 4.mp4` (66 min, gravado em
28/08/2026), transcrito localmente em 02/09/2026 com Whisper. Transcrito em
`Videos/Treinamento_Ecommerce/resultados/AUDIO_COMPLETO_MOD4.*` (txt, srt, vtt,
tsv, json com timestamps).

Diferente dos módulos 1 e 2, este não é aula: é o Fabrício **configurando a loja
junto com o Leandro, ao vivo**. Então boa parte do conteúdo é estado real da
nossa loja, não capacidade genérica da plataforma.

---

## 1. O problema não resolvido do porcelanato

Este é o assunto central do vídeo e ele **terminou em aberto**.

**O que a Metal Nobre precisa:** porcelanato só sai por entrega própria, dentro
da região atendida. É frágil; se for por Jadlog ou Correios, chega quebrado.

**Por que a Frenet não resolve:** o hub **não conhece produto**. Ele recebe
volume, peso e dimensões. Não existe "este produto não vai pela Frenet". Se o
peso e as medidas couberem na regra da transportadora, ela aparece para o
cliente — e o cliente pode escolher.

**Por que limitar por CEP também não resolve:** o pedido é um só. Cliente que
compra torneira **e** porcelanato tem um frete só. Se a regra do porcelanato
bloqueia a região dele, o **pedido inteiro** fica sem opção de entrega — perde-se
a torneira junto. A disponibilidade do produto na vitrine é aberta: o cliente de
fora da área vê o produto, coloca no carrinho, e só descobre no frete.

**O que existe do lado JET e não existe do lado hub:** a ferramenta **Entrega
personalizada** tem uma aba **Exclusões** — lista de produtos que aquela tabela
de frete não transporta. Se o produto está no carrinho, aquela modalidade não
aparece. Isso é exatamente o controle por produto que falta na Frenet.

**Encaminhamento registrado no vídeo:** o Fabrício ficou de marcar com o
**Rafael** para desenhar a solução, e cogitou **Multi-CD com split de pedido**
como caminho — o que conflita com `PEN-056` (Multi-CD é incompatível com
importação de produtos em lote).

Consequência: `PEN-043` não está fechado, mesmo com a Frenet ativa em produção.
O que falta não é configuração, é **regra de negócio**.

## 2. Frenet — o que já está ativo

Confirmado na tela durante a sessão:

- token configurado, integração de pedido e de **etiqueta** ativas;
- a Frenet tem permissão para **alterar o status do pedido dentro da JET**:
  coleta/despacho → `tracking` (a caminho); recebimento → `concluído`;
- a JET dispara e-mail de rastreio com o código, mas o acompanhamento detalhado
  é do site da transportadora — o e-mail não é granular;
- dentro da Frenet já estavam ativos Correios e Jadlog.

Fato para a integração: **quem move o status do pedido na JET é a Frenet**, não
a integradora. Qualquer mapeamento de status no Sankhya precisa contar com isso.

**Contrato próprio com os Correios pela Frenet tem mensalidade.** Dado que
faltava no `PEN-055`.

**Limite dos Correios: 30 kg.** Jadlog aceita bem mais.

## 3. Entrega personalizada — como a ferramenta funciona

Caminho: **Configurações > Gestão de frete > Entrega personalizada > Cadastrar novo**.

| Campo | Comportamento |
|---|---|
| Tipo de cálculo | tabela por faixa, **ou** percentual sobre o valor dos produtos |
| Segmento | B2C / B2B |
| Descrição | texto livre exibido ao cliente antes da compra (ex.: horário de entrega) |
| Abrangência | país / estado / cidade, **ou** faixa de CEP personalizada (permite bairro) |
| Faixas de peso | mínimo e máximo por faixa, com preço próprio |
| Prazo | dias úteis, dias corridos ou imediato |
| Cadastro | manual ou **por planilha** (colunas: peso início, peso fim, CEP início, CEP fim) |
| Exclusões | produtos que esta modalidade **não** transporta |
| Agendamento | calendário para o cliente, ver abaixo |

**Armadilha das faixas de peso.** A faixa seguinte começa em `X,001`, não em `X`.
Faixa de 0 a 20 kg, a próxima começa em **20,001** — é assim que a plataforma
entende "acima de 20". Errar isso deixa buraco ou sobreposição na tabela.

**Agendamento de entrega.** Quando ativado, o cliente vê um mini-calendário no
checkout: escolhe **data** e **turno** (manhã / tarde / noite). Regras:

- só oferece datas a partir do **prazo cadastrado na tabela** — prazo de 7 dias
  significa que a primeira data disponível é d+7;
- dá para limitar quais turnos e quais dias da semana ficam habilitados;
- dá para **cobrar a mais por turno** (manhã custa mais caro, por exemplo);
- **dias diferentes por bairro exigem tabelas diferentes.** Não há como colocar
  "segunda e quarta no bairro X, terça e quinta no bairro Y" numa tabela só — são
  duas entregas próprias, cada uma com sua faixa de CEP. O cliente só enxerga a
  que casa com o CEP dele.

Isso conecta direto ao `PEN-049` (modalidades de entrega e agendamento).

## 4. Retirada na loja — a padrão da JET deve ser descartada

O "Retirada na loja" que vem com a plataforma é **legado e não recebe
melhorias**. O caminho correto é criar uma retirada nova pela ferramenta de
Entrega personalizada (marcando o tipo "retira na loja") e **excluir a antiga**.
Isso foi feito durante a sessão.

A retirada nova aceita: prazo em horas, CEP e endereço do ponto físico,
informações adicionais, abrangência (quem pode retirar — Brasil todo ou região)
e **exclusões de produto** (item que não pode ser retirado).

O Fabrício recomendou deixar a retirada aberta para o Brasil todo: cliente que
viaja, ou parente que retira e reenvia, é um caso real.

## 5. Reajuste de preço do frete

Caminho: **Configurações > Reajuste de preço do frete**. Aplica acréscimo em **%
ou R$** sobre as modalidades **personalizadas** (não sobre hub), e permite
escolher quais regiões cadastradas recebem o reajuste. É a ferramenta para
repassar combustível sem reeditar a planilha inteira.

## 6. Gestão de taxas por produto / região

Caminho: **Configurações > Gestão de taxas por produto / região**.

Cria uma taxa que pode ser aplicada **sobre o valor do frete** (o cliente não vê
a taxa, só o frete final) ou **sobre o valor do produto**.

⚠️ **Sobre o produto é território perigoso.** O Fabrício foi explícito: o preço
não pode mudar depois que o cliente digita o CEP — produto anunciado a R$ 10 que
vira R$ 15 ao informar o CEP é propaganda enganosa. Se a taxa for no produto, ela
precisa estar no preço desde o início. Na prática, quase todo mundo usa sobre o
frete.

Configuração: % ou valor; período de vigência opcional; abrangência por estado ou
faixa de CEP; e escopo por **todos os produtos**, ou por produto / categoria /
marca, com **planilha de exceção** para o caso "todos menos estes".

Uso possível para nós: embutir no frete o custo diferenciado de carga frágil,
já que não dá para distinguir porcelanato dentro do hub.

## 7. Pagamento — estado e decisões pendentes

### ⚠️ As credenciais do Pagar.me no painel podem ser fictícias

Fato dito na sessão: **o time da JET cadastra credenciais fictícias do Pagar.me
para montar o layout da loja**. Elas precisam ser trocadas pelas credenciais
reais.

Na varredura do painel em 02/09/2026 o Pagar.me PSP aparece **ativo em ambiente
Produção** — mas isso não prova que a credencial é a real. Verificar antes de
qualquer teste de pagamento valer como evidência.

O Fabrício também alertou: o Pagar.me normalmente entrega credencial de
produção, mas já houve caso de mandarem de homologação. Conferir o ambiente com
eles, não presumir.

### PIX — decisão em aberto

O Pagar.me **cobra taxa no PIX**. Na sessão foi testado usar o **Mercado Pago só
para o PIX**, mantendo o Pagar.me no cartão. Achados:

- **não é possível ter a mesma forma de pagamento ativa em dois gateways** — para
  ativar PIX no Mercado Pago é preciso desativar o PIX do Pagar.me;
- o Mercado Pago é ativado por **"Autorizar aplicação"** (login OAuth), não por
  chave;
- **o teste falhou**: o QR Code não foi gerado. A conta do Mercado Pago da Metal
  Nobre é a do Mercado Livre, e e-commerce é um segmento separado dentro do
  Mercado Pago — pode exigir habilitação ou plano próprio, e pode ter exigência
  de trabalhar cartão com eles.

Na varredura de 02/09 **o Mercado Pago não aparece entre os gateways ativos** —
ou seja, o teste não foi retomado. A decisão PIX continua aberta.

### Pagamento offline

É manual e **sem taxa**. Não é gateway: o pedido não muda para aprovado sozinho.
O lojista põe na descrição o QR Code estático e as instruções ("envie o
comprovante pelo WhatsApp") e valida na mão.

Risco declarado: QR estático **não carrega valor**, o cliente digita — e erra.

A forma "Pagamento offline" que vem criada por padrão deve ser **inativada**,
criando as suas próprias no lugar. Hoje ela está ativa em produção na nossa loja
e foi o que gerou os pedidos de porcelanato de teste sem tipo de negociação da
série e-commerce.

### Parâmetros de forma de pagamento

Cada forma aceita: perfil (PF / PJ / ambos), valor mínimo de compra, desconto %
com valor mínimo para aplicar, e parcelamento com **valor mínimo por parcela**.

**Grupos** existem para fundir várias formas numa só opção no checkout — o caso
clássico é boleto faturado 30/60/90 dias agrupado em "Boleto faturado".

**Cartão de crédito exige configurar bandeira por bandeira** (Mastercard, Visa,
Amex, Elo, Diners, Hipercard), cada uma com seu desconto, valor mínimo e número
de parcelas.

**Pagar.me suporta pagamento com dois cartões**; Mercado Pago e PagSeguro não.

### Tempo de expiração do PIX — regra com motivo

O PIX tem campo de **minutos até o vencimento**, e a recomendação é **1 hora**.

O motivo não é técnico, é defensivo: enquanto o pagamento está pendente, o
**estoque fica reservado**. O Fabrício relatou a prática de concorrente que, em
data comemorativa, compra todo o estoque do rival em boleto de 3 dias, deixa
vencer e tira o produto do ar no melhor momento de venda. Por isso boleto
faturado deve ficar em 2 a 3 dias no máximo, e PIX em uma hora.

Isso liga direto a `PEN-044` e à tela **Reserva e liberação de estoque**.

### 10x sem juros — a origem da decisão

Na sessão o Leandro observou que os concorrentes parcelam em **10x** (alguns 5 ou
6). É a origem do item de rodapé do documento de ajuste de layout de 01/09
(`PEN-059`), que troca 12x por 10x.

⚠️ Consequência para a integração: a série de `CODTIPVENDA` do e-commerce no
Sankhya vai até 12x (código 210). Se a loja comunica e vende em 10x, os códigos
209 (11x) e 210 (12x) não deveriam mais chegar em pedido nenhum.

## 8. B2B — e por que ele é uma questão de Sankhya, não de JET

O B2B da JET funciona por **área restrita com tabela de preço**: o cliente
comum vê o preço público; o cliente alocado numa tabela entra na área restrita e
vê o preço dela. Dá para ter várias tabelas (revenda, cliente estratégico,
construtora) e cada tabela define quais produtos e a que preço.

O Fabrício foi direto sobre a divisão de trabalho: **as tabelas devem existir
prontas no ERP e descer pela integração**; na JET só se **aloca o cliente na
tabela**.

Isso amarra com o modelo de preço do Sankhya (`TGFTAB.CODTAB` / `TGFEXC`): a
"tabela engenharia" citada na conversa é uma tabela do ERP. Ou seja, B2B na JET
não é decisão de e-commerce — é decisão de arquitetura de preço no Sankhya, e
depende do objetivo do campo de preço que ainda está em aberto.

O cadastro da loja aceita **CPF e CNPJ**; B2B não é o que permite PJ comprar, é o
que dá preço diferenciado a PJ selecionado.

## 9. Achados operacionais menores

- Cadastro de produto **exige peso maior que zero**. Dimensões são opcionais para
  retirada, mas não para frete calculado.
- Alteração de produto reflete **imediatamente na página de detalhe**; a home
  demora mais.
- Produto sem categoria não fica comprável — durante a sessão a loja estava sem
  categorias porque o Rodrigo estava subindo o catálogo.

## 10. O que este módulo muda no board

| Card | Impacto |
|---|---|
| `PEN-042` Pagar.me | credencial pode ser fictícia; PIX/expiração e bandeiras não configurados; decisão PIX aberta |
| `PEN-043` Frenet | configuração pronta, **regra do porcelanato não resolvida** — pendente com o Rafael |
| `PEN-054` precedência de frete | a Entrega personalizada tem **Exclusões** por produto; o hub não tem. É a chave do desenho |
| `PEN-049` modalidades e agendamento | mecânica de agendamento documentada aqui |
| `PEN-055` contrato Correios | contrato próprio pela Frenet **tem mensalidade** |
| `PEN-056` Multi-CD | foi cogitado como solução do porcelanato — decidir antes da carga do catálogo |
| `PEN-059` layout 12x→10x | origem da decisão registrada; conferir CODTIPVENDA 209/210 |
| `PEN-044` estoque | expiração de PIX/boleto é controle de reserva de estoque, não detalhe de checkout |

## Método e validade

Transcrição automática (Whisper `small`, português) de uma reunião gravada.
Nomes de ferramenta e números podem sair distorcidos no áudio ("frenete",
"Sunker" para Sankhya, "Pixie" para PIX, "GDLog" para Jadlog) — o sentido foi
reconstruído, mas **qualquer número crítico deve ser reconferido na tela** antes
de virar decisão. Estado de configuração descrito aqui é o de 28/08/2026 e já
divergiu em pelo menos um ponto (Mercado Pago).
