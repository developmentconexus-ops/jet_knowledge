# Uncertainty Register

Itens que NÃO devem ser tratados como fatos confirmados por humanos, documentos futuros ou agentes.

- `UNC-001` — Frequência de atualização do sitemap: o instrutor citou 12 ou 24 horas sem confirmar.
- `UNC-002` — Automação de “Quem comprou, comprou também”: o instrutor disse precisar validar; naquele momento, afirmou ser 100% manual.
- `UNC-003` — Conversão m²/caixa já implementada ou ainda a implementar por Rodrigo: não confirmada.
- `UNC-004` — Existência/mapeamento de cross docking no Sankhya: o instrutor demonstrou incerteza.
- `UNC-005` — Exemplos sobre concorrentes/produtos feitos explicitamente como chute/opinião não são fatos.
- `UNC-006` — Afirmações jurídicas/LGPD feitas no treinamento exigem validação jurídica externa antes de virarem regras de compliance.
- `UNC-007` — Afirmações comparativas sobre modelos de IA feitas pelo instrutor são opinião do treinamento, não fato técnico canônico.
- `UNC-008` — Comportamento exato de primeiro acesso/e-mail antes e depois da publicação: o treinamento usa `Recuperar Senha` enquanto a loja está em projeto, mas também exige remetente padrão antes da publicação. A fronteira entre infraestrutura de disparo, senha temporária e remetente não ficou tecnicamente demonstrada.
- `UNC-009` — Estado atual da passagem de bastão para o suporte JET: no Módulo 1 ela ainda não havia ocorrido; nenhum transcript posterior confirma conclusão. Ver `PEN-038`.
- `UNC-010` — Estado atual de funcionalidades descritas como “sendo descontinuadas”, especialmente Comentários de Clientes sobre o Produto: a fala é temporal e deve ser revalidada antes de aparecer como fato atual em manual/agente.

## Regra de consumo

1. Agentes e documentos devem preferir `UNKNOWN`/`REQUIRES_EXTERNAL_VERIFICATION` a completar lacunas por inferência.
2. Uma fala temporal (“hoje”, “está sendo descontinuado”, “ainda não”) não deve ser automaticamente promovida a fato atual permanente.
3. Quando uma incerteza for resolvida, preservar o ID e registrar evidência/data de resolução em vez de apagar silenciosamente o histórico.