# Rascunho de conhecimento operacional — Atualização massiva de campos de produto gerenciados pela JET

> **Status:** rascunho de conhecimento / não liberado como IT ISO controlada.
>
> Este documento registra o que já é suficientemente sustentado pelos treinamentos, pela camada canônica e pela evidência visual. Ele não define responsável, periodicidade, aprovação ou código documental oficial.

## Objetivo

Registrar o fluxo seguro para atualizar em lote, via planilha da JET, **somente campos que são legitimamente gerenciados na JET** para produtos que já existem na plataforma.

O treinamento demonstra que a ferramenta `Importar produtos` possui capacidade de cadastrar e atualizar em lote, mas a orientação específica para a Metal Nobre é **não usar a planilha para criar o cadastro principal dos produtos**, pois esse cadastro vem do Sankhya/upstream. O uso aplicável é a atualização massiva de informações locais da JET.

## Regra de autoridade antes de começar

Antes de preencher qualquer coluna, responder:

> **Este campo é JET-local ou é mandado pelo Sankhya/upstream?**

Se o campo for mandado pelo Sankhya/upstream, **não usar a planilha para criar uma segunda fonte de verdade**.

Exemplos demonstrados/compatíveis com uso local na JET:

- etiqueta;
- disponibilidade/mensagem de disponibilidade;
- SEO Title;
- Meta Description;
- outros campos que a Integration Authority Matrix classificar explicitamente como JET-managed.

Exemplos que **não devem ser usados para contornar a integração** no modelo atual:

- nome do produto;
- GTIN;
- NCM;
- código do produto;
- estoque;
- preço;
- categoria;
- demais campos definidos como upstream/Sankhya.

Referências: `JET-KB-013`, `JET-KB-017`, `JET-KB-032`, `JET-KB-033`, `JET-RULE-002`, `JET-RULE-006`.

## Quando usar

Usar quando houver necessidade de alterar **vários produtos já cadastrados** em um campo JET-local.

Exemplos dados no treinamento:

- aplicar uma etiqueta, como uma campanha de Black Friday, em muitos produtos;
- alterar disponibilidade em lote;
- preencher SEO em lote.

Não usar este fluxo como atalho para corrigir na JET um dado cuja origem correta é Sankhya/upstream.

## Procedimento conhecido

### 1. Acessar `Importar produtos`

No cadastro/lista de produtos, acessar a função `Importar produtos`.

A interface demonstrada apresenta duas finalidades da ferramenta:

1. cadastro de produtos em lote;
2. atualização de produtos já cadastrados.

Para a Metal Nobre, o fluxo aqui documentado é o **segundo**.

### 2. Baixar a planilha modelo atual da JET

Baixar o modelo diretamente da JET para a execução atual.

Não reutilizar um modelo antigo presumindo que o schema permaneceu igual.

### 3. Consultar o tutorial/instruções da própria ferramenta

O treinamento demonstra acesso a um tutorial associado ao importador. A função desse tutorial é explicar o significado e a regra de preenchimento de cada coluna.

Quando houver dúvida sobre um valor aceito, consultar a instrução do campo em vez de inventar formato.

### 4. Preservar integralmente a estrutura da planilha

Não alterar:

- formatação do modelo;
- nome das colunas;
- ordem das colunas.

A planilha deve ser preenchida, não redesenhada.

### 5. Informar obrigatoriamente o código do produto

No fluxo de atualização demonstrado, o `Código` é o identificador obrigatório para a JET saber qual produto deve ser atualizado.

Cada linha de atualização deve apontar para o produto correto.

### 6. Preencher somente o que deve ser alterado

Para uma atualização:

- preencher o código do produto;
- preencher apenas a(s) coluna(s) do que se pretende alterar;
- deixar em branco as demais colunas quando não houver intenção de alterá-las.

Não preencher campos “só porque existem na planilha”.

### 7. Respeitar valores exatos esperados pela JET

O treinamento mostra que alguns campos dependem de correspondência exata com valores já existentes.

Exemplo demonstrado: etiqueta `Frete Grátis`.

O instrutor orienta copiar o nome exatamente, incluindo:

- acentuação;
- maiúsculas/minúsculas;
- grafia.

Portanto, quando o campo referenciar uma entidade/valor já cadastrado na JET, preferir copiar o valor existente em vez de redigitá-lo de memória.

### 8. Salvar a planilha e fazer o upload

Após o preenchimento:

1. salvar o arquivo;
2. retornar a `Importar produtos`;
3. enviar a planilha pela ferramenta.

### 9. Ler o resultado da importação

O treinamento demonstra que, ao final, a JET informa quantas linhas foram processadas com sucesso e quais falharam.

Quando uma linha falha, a ferramenta pode indicar o motivo associado ao campo/valor esperado.

Exemplo didático do treinamento: erro por tipo de dado incompatível em uma coluna.

### 10. Corrigir somente o erro apontado e reprocessar o necessário

Se houver falha:

- identificar linha/coluna;
- consultar a regra do campo;
- corrigir o valor ou formato;
- reenviar conforme necessário.

Não transformar uma falha de importação em justificativa para alterar a estrutura do modelo.

## Verificação pós-execução

O treinamento comprova o relatório de sucesso/falha do importador. Como controle operacional derivado, uma execução massiva deve ser considerada verificada somente depois de:

1. conferir o resultado informado pela JET;
2. investigar todas as linhas com erro;
3. abrir uma amostra dos produtos alterados e confirmar que o campo pretendido recebeu o valor correto;
4. confirmar que campos upstream não foram usados para criar divergência com o Sankhya.

Os itens 3 e 4 são controles operacionais derivados da matriz de autoridade; não foram apresentados pelo instrutor como um checklist formal.

## Ações proibidas / guardrails

- Não mudar nomes/ordem/formatação das colunas do modelo.
- Não preencher campos sem necessidade de alteração.
- Não usar a planilha para contornar o Sankhya em campos upstream.
- Não assumir que um valor textual aproximado será aceito quando a JET espera correspondência exata.
- Não considerar uma importação concluída ignorando linhas que a JET reportou como erro.
- Não assumir que o modelo visto no treinamento é o modelo atual; baixar o modelo vigente.

## Falhas e diagnóstico já conhecidos

### Valor não reconhecido

Possível causa: texto diferente do valor esperado/cadastrado, inclusive grafia ou acentuação.

Ação: consultar a regra do campo e copiar o valor canônico existente na JET quando aplicável.

### Tipo/formato inválido

Possível causa: a coluna exige determinado tipo de dado e recebeu outro.

Ação: seguir a mensagem da importação e a documentação/tutorial do campo.

### Campo upstream alterado por engano

Este caso não foi demonstrado como erro técnico do importador. O risco é **operacional**: criar divergência temporária ou um valor que depois será sobrescrito pela integração.

Ação: tratar pela Integration Authority Matrix e corrigir no sistema de origem quando esse for o mandante.

## Evidência e rastreabilidade

- Transcript MOD2: `01:15:27–01:20:00`.
- Evidência visual: `MOD2-VIS-006` — `VERIFIED`.
- Knowledge Base: `JET-KB-032`, `JET-KB-033`.
- Guardrails: `JET-RULE-002`, `JET-RULE-006`.
- Matriz: `docs/canonical/integration-authority-matrix.md`.

## O que observar quando reassistirmos a aula

Na segunda passada, validar especificamente:

1. caminho exato e nome atual da função `Importar produtos`;
2. se o modelo atual ainda usa a mesma organização demonstrada (incluindo exemplos de produto sem variação e com variação);
3. quais campos JET-local aparecem hoje na planilha;
4. se existem campos obrigatórios adicionais além do código para atualização;
5. se a ferramenta atual oferece arquivo/relatório de erros para download ou apenas retorno em tela;
6. comportamento de reenvio parcial após erros;
7. se há limites de quantidade/tamanho de arquivo não capturados no treinamento;
8. se há qualquer mecanismo de pré-validação antes de aplicar a importação;
9. confirmar se SEO Title e Meta Description continuam disponíveis no modelo atual;
10. qualquer diferença de interface que precise entrar na futura IT visual.

## Limite deste rascunho

Este documento não define responsável, aprovação, periodicidade, retenção de planilhas ou nomenclatura de arquivos porque essas regras não foram estabelecidas pelos materiais analisados.

Esses elementos devem ser definidos quando o fluxo for convertido em uma IT formal da Metal Nobre.
