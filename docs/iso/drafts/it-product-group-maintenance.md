# Rascunho de conhecimento operacional — Manutenção de grupos de produtos na JET

> **Status:** rascunho de conhecimento / não liberado como IT ISO controlada.
>
> Este documento consolida somente o que os materiais analisados sustentam sobre manutenção de grupos de produtos. Não define ainda responsável, periodicidade, aprovação, nomenclatura documental ou calendário de merchandising.

## Objetivo

Registrar o fluxo seguro para manter grupos de produtos existentes na JET, alterar seu conteúdo e criar grupos novos para páginas/campanhas, preservando os grupos da home que estão vinculados ao layout por ID.

## Regra crítica antes de qualquer alteração

No treinamento da Metal Nobre, os grupos já existentes na home estavam associados a posições específicas do layout por **ID**.

Por isso:

> **Não excluir os grupos existentes que estão vinculados ao layout da home.**

A exclusão pode quebrar o vínculo que faz o grupo aparecer naquela posição do layout.

Referências: `JET-KB-030`, `JET-RULE-005`, `MOD2-VIS-009`.

## Conceito operacional

Um grupo de produtos na JET pode servir para:

- formar uma seção/vitrine da home quando o layout está vinculado ao grupo;
- criar uma página própria com URL;
- agrupar produtos por campanha, tema ou curadoria;
- ser destino de banner, e-mail ou outro link de campanha.

Um grupo novo **não passa a aparecer automaticamente na home**. Para isso, o layout precisa ser alterado/configurado para usar esse grupo.

Referência: `JET-KB-031`.

## Manutenção de um grupo existente da home

### 1. Acessar Grupos de Produtos

Caminho demonstrado no treinamento:

`Produtos → Configurações do catálogo → Grupo de produtos`

A interface mostrava os grupos já cadastrados para a Metal Nobre naquele momento.

### 2. Identificar se o grupo é um grupo fixo do layout

Antes de editar, confirmar se o grupo é um dos grupos utilizados pela home/layout.

No treinamento, a explicação é que cada grupo da home estava fixado a uma posição por ID.

Se houver dúvida sobre o vínculo do grupo com o layout, **não excluir**.

### 3. Editar os dados do grupo

No menu do grupo, usar `Editar grupo`.

O treinamento demonstra que é possível alterar/manter:

- nome do grupo;
- URL;
- título/descrição de SEO;
- texto da página do grupo;
- opção `Exibir na home`.

### 4. Ao renomear, revisar também a URL

O instrutor chama atenção para o fato de que alterar somente o nome pode deixar a URL com o slug/nome anterior.

Portanto, quando o nome do grupo mudar, revisar deliberadamente se a URL também deve ser atualizada.

Não alterar URL automaticamente sem entender os links/campanhas que já apontam para ela; essa checagem é um controle operacional derivado, não uma regra demonstrada no treinamento.

### 5. Preservar `Exibir na home = Sim` nos grupos que compõem a home

Para os grupos que já fazem parte da home, o treinamento orienta manter `Exibir na home` como `Sim`.

Se for colocado `Não`, o grupo deixa de aparecer na home.

Essa regra não significa que todo grupo novo deve ter `Sim`; grupos novos não entram automaticamente no layout.

### 6. Salvar as alterações do grupo

Após revisar nome, URL, SEO, texto e exibição, salvar.

## Manutenção dos produtos vinculados

### 1. Abrir `Editar produtos vinculados`

No grupo desejado, acessar a função de edição dos produtos vinculados.

### 2. Entender os dois lados da seleção

No treinamento:

- o lado direito contém os produtos já vinculados ao grupo;
- o lado esquerdo é usado para localizar produtos a adicionar.

### 3. Pesquisar produtos

A pesquisa pode ser feita por:

- nome;
- código.

### 4. Remover produtos de teste ou que não devem mais compor a curadoria

Produtos que foram inseridos para teste podem ser removidos do grupo.

A regra crítica é remover **produtos do grupo**, não excluir o próprio grupo fixo do layout.

### 5. Adicionar os produtos desejados

Pesquisar, selecionar e adicionar os produtos que devem compor a vitrine/página do grupo.

### 6. Salvar os vínculos

Salvar após concluir a curadoria.

## Criação de um grupo novo

A JET permite criar grupos adicionais.

Exemplo dado no treinamento: um grupo de campanha `Black Friday`.

### O que um grupo novo entrega

Depois de criado e com produtos vinculados, o grupo possui uma página/URL própria que pode ser usada em:

- banner;
- e-mail;
- divulgação direta de link;
- outras ações de redirecionamento.

### O que um grupo novo NÃO faz sozinho

Ele **não aparece automaticamente na home** apenas porque foi criado ou porque a opção de exibição existe.

Para ocupar uma posição da home, o layout precisa ser alterado/configurado para referenciar o grupo.

## Verificação pós-alteração

Controles operacionais derivados do comportamento demonstrado:

### Grupo fixo da home

Após alteração:

1. confirmar que o grupo continua aparecendo na posição esperada da home;
2. confirmar que `Exibir na home` permanece coerente com o uso do grupo;
3. abrir a página do grupo e conferir nome/URL/conteúdo;
4. conferir se os produtos esperados aparecem e se produtos de teste/indesejados foram removidos.

### Grupo novo

Após criação:

1. confirmar que a página/URL do grupo abre;
2. conferir os produtos vinculados;
3. se houver campanha, validar o banner/e-mail/link que aponta para a página;
4. não interpretar ausência na home como erro se o layout ainda não foi configurado para o grupo.

## Ações proibidas / guardrails

- Não excluir grupos existentes vinculados à home por ID.
- Não usar exclusão de grupo como forma de “limpar produtos de teste”; editar os produtos vinculados.
- Não colocar `Exibir na home = Não` em grupo fixo da home sem uma decisão consciente de remover aquela vitrine.
- Não assumir que criar um novo grupo adiciona automaticamente uma nova seção à home.
- Não assumir que o ID demonstrado em treinamento é um ID permanente/canônico atual; validar o ambiente atual antes de qualquer manutenção de layout.

## Se um grupo fixo for excluído por engano

O treinamento indica que o time deveria ser avisado, mas não apresenta um procedimento técnico completo de restauração.

Portanto, a resposta canônica atual é:

1. interromper novas alterações relacionadas;
2. registrar qual grupo foi afetado;
3. escalar para JET/layout/suporte responsável;
4. não recriar às cegas presumindo que um novo grupo receberá o mesmo ID ou vínculo de layout.

A recuperação exata deve ser documentada quando houver evidência real do processo.

## Evidência e rastreabilidade

- Transcript MOD2: `01:40:48–01:44:19`.
- Evidência visual: `MOD2-VIS-009` — `VERIFIED`.
- Knowledge Base: `JET-KB-030`, `JET-KB-031`.
- Guardrail: `JET-RULE-005`.
- Pendência relacionada à limpeza real da home: `PEN-026`.

## O que observar quando reassistirmos a aula

Na segunda passada, validar especificamente:

1. nomes e IDs dos grupos existentes naquele momento, separando exemplo histórico de configuração atual;
2. se todos os grupos da home são realmente vinculados por ID ou apenas os demonstrados;
3. caminho e nomes atuais de `Editar grupo` e `Editar produtos vinculados`;
4. todos os campos presentes no cadastro do grupo;
5. efeito exato da opção `Exibir na home` no layout atual da Metal Nobre;
6. se existe ordem própria dos produtos dentro do grupo e como ela é alterada;
7. se há limite de quantidade de produtos por grupo;
8. comportamento ao alterar a URL de um grupo que já possui links externos;
9. procedimento real de recuperação se um grupo fixo for apagado;
10. como o time de layout associa um grupo novo a uma posição da home;
11. se um grupo pode ser reutilizado em mais de uma posição/componente do layout;
12. quais grupos de teste precisam ser limpos antes do go-live.

## Limite deste rascunho

Este documento não define a curadoria comercial que deve entrar em cada grupo, porque isso é uma decisão de merchandising da Metal Nobre e pode mudar ao longo do tempo.

Também não define quem pode alterar grupos, quem aprova campanhas ou quais posições da home são permanentes; essas regras devem ser estabelecidas quando o processo for formalizado.
