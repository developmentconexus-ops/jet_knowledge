# Cronograma de go-live — proposta de 02/09/2026

**Data-alvo proposta: terça-feira, 06/10/2026.** Go/No-Go em 01/10. Freeze de
configuração em 30/09. Hypercare de 06 a 13/10.

Este documento é a proposta que fecha `PEN-031`. Ele **não substitui o Trello**:
status vive lá. Aqui vive a lógica — por que esta ordem, por que esta data, e o
que derruba a data se atrasar.

## Por que 06/10 e não antes

A data não é limitada por pagamento nem frete — os dois estão integrados. É
limitada por **catálogo**. A loja tem 8 produtos ativos. Não existe auditoria de
experiência (`PEN-046`) com valor em cima de 8 produtos, e sem auditoria não há
relatório para o Fabrício (`PEN-050`), e sem as correções dele não há E2E
confiável (`PEN-035`). Essa é a cadeia crítica:

```
sortimento (047) → enriquecimento (007) + categorias (002) → carga
   → auditoria UX (046) → relatório Fabrício (050) + layout (059)
   → E2E (035) → Go/No-Go (036) → cutover (032) → hypercare (037)
```

Cinco semanas é o mínimo para essa cadeia com um sortimento de **piloto** —
não o catálogo inteiro. Se a decisão for lançar com catálogo completo, a data
não se sustenta.

**A data cai se:** sortimento não estiver decidido até 09/09; ou a BLP não
entregar m²×caixa + peso do porcelanato até 18/09; ou o Fabrício não devolver
as correções de layout até 30/09.

## As três decisões que destravam tudo — esta semana

| Decisão | Card | Dono | Até |
|---|---|---|---|
| Sortimento do piloto: quais produtos entram no go-live | PEN-047 | Leandro | **09/09** |
| Peso efetivo do porcelanato para a regra de frete | PEN-045 | Ricardo | **09/09** |
| PIX: fica no Pagar.me pagando taxa, ou vai para outro gateway | PEN-060 | Leandro + Pagar.me | **11/09** |

Nenhuma das três é técnica. As três travam trabalho de outras pessoas: sem
sortimento o enriquecimento não tem alvo; sem peso a BLP não aplica a regra;
sem PIX decidido o teste de pagamento em produção testa a coisa errada.

## Semana a semana

### S1 — 02 a 06/09 · Decidir e destravar

| Card | O quê | Dono |
|---|---|---|
| PEN-031 | Fechar esta data e os critérios de readiness | Leandro |
| PEN-047 | Sortimento do piloto | Leandro |
| PEN-045 | Peso do porcelanato → repassar à BLP | Ricardo |
| PEN-056 | Decidir Multi-CD (um CD só = registrar e encerrar) — antes da carga | Leandro |
| PEN-054 | Regra: entrega própria com Exclusões + peso inflado no hub | Leandro + Rafael |
| PEN-033 | Escopo de permissão dos 4 usuários, em especial `blpintegracao` | Leandro |
| PEN-051 | Ativar reCAPTCHA | Leandro (15 min) |
| PEN-009/010 | Cobrar reimportação dos 4 pedidos de teste; rodar `comparar_pedido.py` | BLP → Leandro |

### S2 — 07 a 13/09 · Catálogo e regras

| Card | O quê | Dono |
|---|---|---|
| PEN-007 | Enriquecimento do sortimento do piloto (nome, descrição, peso, dimensões, fotos) | Leandro + pipeline |
| PEN-002 | Fechar árvore de categorias no Sankhya | Leandro + Rodrigo |
| PEN-008 | Validar mapeamento de imagens | Rodrigo |
| PEN-005 / PEN-006 | Marcas: agrupamento na integração + cadastro na JET | Rodrigo / Leandro |
| PEN-043 | BLP aplica regra de peso; validar cotação com CEP dentro e fora da área | BLP → Leandro |
| PEN-060 | Fechar decisão do PIX | Leandro |
| PEN-052 | Resposta do Pagar.me sobre antifraude | Leandro |
| PEN-014 / 018 / 019 | Remetente, parâmetros da loja, dados e logo | Leandro |
| PEN-020 | Política de privacidade — texto validado + publicada | Leandro + jurídico |

### S3 — 14 a 20/09 · Carga e integração validada

| Card | O quê | Dono |
|---|---|---|
| PEN-007 | Carga final do piloto na JET | Leandro |
| PEN-026 | Limpar produtos de teste, preservar grupos fixos da home | Leandro |
| PEN-049 | Modalidades de entrega e agendamento configuradas | Leandro |
| PEN-042 | Teste de pagamento **em produção** (PIX, crédito 1x e 10x, débito) | Leandro |
| PEN-024 | Páginas institucionais | Leandro / marketing |
| PEN-015 / 016 / 017 | E-mails: remetentes por evento, Fale Conosco, templates | Leandro / marketing |
| PEN-004 / PEN-003 | Categorias visíveis, "Ver todos", hover | Leandro + Fabrício |
| PEN-041 / PEN-040 | Custo variável nas TOP 313/306 + frete no custo | Leandro (Sankhya) |

### S4 — 21 a 27/09 · Auditoria e correções

| Card | O quê | Dono |
|---|---|---|
| PEN-046 | Auditoria completa como cliente — desktop e mobile | Leandro + Laura |
| PEN-050 | Relatório consolidado para o Fabrício, com evidência por achado | Leandro |
| PEN-059 | Cobrar os 8 ajustes de layout de 01/09 | Fabrício |
| PEN-011 | Layout da calculadora de porcelanato | Fabrício |
| PEN-022 / PEN-023 | Banners: dimensões oficiais + organizar existentes | Laura |
| PEN-034 | GA4 / GTM via Marketing > Google | Leandro |
| PEN-035 | **E2E**: pedido real por forma de pagamento → Sankhya → validação automática | Leandro + BLP |

### S5 — 28/09 a 02/10 · Freeze e Go/No-Go

| Data | O quê | Card |
|---|---|---|
| 28–29/09 | Correções finais do Fabrício; reteste do que mudou | PEN-059, PEN-050 |
| 30/09 | **Freeze** — nada muda na loja sem registro | PEN-032 |
| 01/10 | **Go/No-Go** com checklist de cutover | PEN-036 |
| 02/10 | Plano de DNS/domínio, comunicação, rollback | PEN-032 |

### Go-live — 06/10 (terça)

| Período | O quê | Card |
|---|---|---|
| 06/10 | Publicação e cutover | PEN-032 |
| 06–13/10 | Hypercare: pedidos, checkout, frete, integração, e-mails, 404 | PEN-037 |
| 07/10 | Passagem de bastão para suporte JET confirmada | PEN-038 |

## Fica para depois do go-live

| Card | Por quê |
|---|---|
| PEN-061 B2B | decisão do Leandro em 02/09: não agora; depende da arquitetura de preço no Sankhya |
| PEN-012 Produto Semelhante | merchandising; precisa de catálogo maior |
| PEN-025 SEO | precisa de catálogo e de Search Console; começar na S4 só o básico (loja + categorias) |
| PEN-027 Produtos Aguardados | processo de lead; precisa de tráfego |
| PEN-028 De/para marketplace | fase 2 |
| PEN-021 Redes sociais | não bloqueia venda |
| PEN-053 Webhooks × polling | decisão de arquitetura; polling funciona para o volume inicial |
| PEN-055 Contrato Correios | decisão de custo; precisa de volume real |
| PEN-057 Varredura de módulos | cérebro; não bloqueia loja |
| PEN-058 Reconciliação Analytics | precisa de venda real para reconciliar |
| PEN-013 / PEN-048 | otimização |

## Dependências externas — quem pode atrasar a data

| Pessoa | Depende dele | Cards |
|---|---|---|
| **BLP** (integradora) | m²×caixa, peso inflado, CIF/FOB, tipo de negociação, `AD_NUMPEDIDO_ECOM` | 009, 010, 043, 035 |
| **Fabrício** (JET) | 8 ajustes de layout, calculadora, hover, plano (`UNC-011`), versão do front (`UNC-012`) | 059, 011, 003, 050 |
| **Rafael** (JET) | regra do porcelanato aplicada com a integração | 043, 054 |
| **Ricardo** | peso do porcelanato; estoque exibido | 045, 044 |
| **Rodrigo** | categorias, imagens, marcas | 002, 008, 005 |
| **Pagar.me** | antifraude; taxa do PIX | 052, 060 |

Regra de gestão: dependência externa com prazo vencido vira **risco nomeado**
no Go/No-Go, não surpresa.

## Critérios de readiness (o que o Go/No-Go confere)

1. Sortimento do piloto 100% carregado, com foto, peso, dimensão e categoria.
2. Quatro pedidos reais (PIX, crédito 1x, crédito 10x, débito) fechados na loja
   e validados no Sankhya pelo `comparar_pedido.py` sem falha.
3. Porcelanato cotado com CEP dentro da área mostra só entrega própria; CEP fora
   mostra aviso de região não atendida.
4. reCAPTCHA ativo, política de privacidade publicada, remetente de e-mail
   configurado e testado.
5. Os 8 ajustes de layout do Fabrício aplicados e conferidos.
6. Auditoria UX sem defeito crítico aberto.
7. Plano de rollback escrito.

## Estado a confirmar com o Leandro

Cinco cards cujo estado real eu não consegui verificar; o cronograma assume
que estão **abertos**:

| Card | Pergunta |
|---|---|
| PEN-007 | quantos produtos enriquecidos hoje e meta do piloto |
| PEN-002 | árvore de categorias já subiu? |
| PEN-009/010 | BLP já reimportou os 4 pedidos de teste? |
| PEN-014/018/019/020 | alguém já configurou remetente, parâmetros, logo, privacidade? |
| PEN-045 | Ricardo já deu o peso? |

Se algum estiver fechado, a semana correspondente fica mais folgada — a data
não muda, a folga vira reserva.
