# Política de Privacidade do GuardIA

| Campo | Valor |
|---|---|
| **Versão** | 1.1 (rascunho para validação jurídica) |
| **Data** | 02/10/2026 |
| **Responsável** | Equipe GuardIA (Ellen Beatryz · Luana Cavalcanti · Márcia Rejane · Deivison Amorim · Denilson Lima) |
| **Riscos tratados** | T07 Privacidade · T04 Transparência · E5 Rotulação · E6 Dados de menores |
| **Requisitos** | RF01, RF02, RF03 |
| **Base normativa** | LGPD (Lei nº 13.709/2018), art. 14; ECA Digital (Lei nº 15.211/2025); Enunciado da ANPD sobre dados de crianças e adolescentes |

> Este é um documento de projeto acadêmico. O GuardIA é um protótipo e **nenhum dado real de crianças é tratado nesta fase**. Antes de qualquer piloto, esta política deve ser revisada por assessoria jurídica e pelo encarregado de dados.

---

## Versão resumida (para responsáveis)

1. **Não lemos nem mostramos as conversas.** O painel só mostra categorias (escola, entretenimento, socialização, apoio emocional), tempo e variação semanal.
2. **O texto das conversas é apagado** assim que a categoria é identificada.
3. **A classificação pode errar.** Você pode corrigi-la, e o seu filho ou filha também pode contestar.
4. **Nada é bloqueado ou punido automaticamente.**
5. **Você pode excluir o perfil e os dados** da criança quando quiser.

## Versão resumida (para crianças e adolescentes)

- Seus pais **não veem** o que você escreve para a IA. Eles veem só o assunto geral (como "escola") e quanto tempo você usou.
- O app **não faz diagnóstico** e **não castiga**. Ele só ajuda a família a conversar.
- Se o app errar sobre você, **você pode explicar o que aconteceu** em "Contestar".
- Você participa de combinados como os horários.

---

## 1. Quem trata os dados

Controlador: equipe do projeto GuardIA (PPGEC, disciplina Interação Humano-Computador). Contato do encarregado: **[a definir, e-mail institucional]**.

## 2. Quais dados são tratados

| Dado | Quem fornece | Finalidade | Retenção proposta* |
|---|---|---|---|
| Nome, e-mail e senha (hash) do responsável | Responsável | Autenticação e vínculo | Enquanto a conta existir |
| Nome e idade da criança | Responsável | Vínculo e ajuste da faixa etária | Enquanto a conta existir |
| Faixa etária, horários, temas acompanhados | Responsável e criança | Configuração da supervisão (RF02) | Enquanto a conta existir |
| Categoria de uso, tempo e frequência (agregados semanais) | Gerado pelo sistema | Painel e alertas (RF03, RF04) | 60 dias |
| Ações no alerta (conversar, ignorar, corrigir, contestar) | Responsável e criança | Melhorar classificação e revisão humana | 6 meses |
| Registros de acesso (quem viu o quê) | Gerado pelo sistema | Auditoria de segurança | 6 meses |
| Texto bruto das conversas | — | Usado só em memória para classificar | **Zero: descartado após classificação** |

\*Prazos propostos pela equipe e sujeitos a validação jurídica.

## 3. O que o GuardIA NÃO faz

- Não exibe, armazena ou envia conversas integrais ao responsável.
- Não faz diagnóstico de saúde mental nem infere saúde, religião, raça, orientação sexual ou situação familiar.
- Não bloqueia nem sanciona automaticamente com base em classificação.
- Não usa dados da criança para treinar modelos de terceiros.
- Não vende nem compartilha dados com fins publicitários.
- O registro do propósito declarado pela criança (RF07) fica **desativado por padrão**.

## 4. Base legal e melhor interesse

O tratamento observa o **melhor interesse** da criança e do adolescente (LGPD, art. 14). Para crianças, exige **consentimento específico e em destaque** de ao menos um dos pais ou responsáveis (ver Termo de Consentimento v1.1). Adolescentes são informados em linguagem adequada e participam da configuração.

## 5. Compartilhamento e fornecedores

Ver "Lista de bases e fornecedores utilizados" (artefato 04). Todo fornecedor de IA deve ter contrato que proíba uso dos dados para treinamento próprio e exija exclusão sob solicitação. Enquanto não houver esse contrato, a classificação roda apenas em dados sintéticos.

## 6. Segurança

Autenticação com senha mínima e verificação de e-mail; vínculo responsável-criança confirmado; criptografia em trânsito e em repouso; controle de acesso por vínculo; registro de acessos.

## 7. Direitos do titular

Acesso, correção, exclusão, revogação do consentimento e informação sobre compartilhamento, a qualquer momento, no app (Configurações) ou por e-mail do encarregado. A exclusão do perfil remove os dados associados em até **30 dias** (prazo proposto).

## 8. Incidentes

Em caso de incidente de segurança com risco relevante, responsáveis e a ANPD serão comunicados conforme a LGPD.

## 9. Salvaguardas específicas para crianças e adolescentes (E6)

1. **Consentimento específico e em destaque** de ao menos um dos pais ou responsável, sem caixa pré-marcada, com versão e data registradas.
2. **Melhor interesse da criança** acima de qualquer finalidade de negócio ou de vigilância. Em caso de conflito, prevalece a proteção da criança.
3. **Minimização:** só categoria agregada, confiança e período. Nenhum texto de conversa, nome, escola, endereço ou foto é armazenado.
4. **Opcionais desativados por padrão**, inclusive o registro do propósito declarado pela criança (RF07).
5. **Linguagem adequada à idade:** versão para jovens e leitura conjunta com o responsável para 6 a 9 anos.
6. **Participação do jovem:** configuração combinada em conjunto e canal de contestação com revisão humana.
7. **Sem publicidade, sem perfilamento comercial e sem treino de modelos de terceiros.**
8. **Controle:** lista de verificação das salvaguardas (artefato 09) e teste automatizado (artefato 10).

## 10. Compromisso contra rotulação e estigmatização (E5)

- Os indicadores descrevem **padrões de uso em um período**, nunca a pessoa. O GuardIA não cria rótulos, pontuações, rankings nem perfil permanente de comportamento.
- Não há comparação entre crianças, irmãos ou com "médias".
- Indicadores por categoria **expiram em 60 dias** e não formam histórico de conduta.
- Textos ao responsável passam por varredura automática de termos rotulantes (artefato 10) e por revisão humana.
- O jovem pode contestar qualquer alerta e a decisão da revisão fica registrada (artefato 06).

## 11. Como verificar o cumprimento

| Compromisso | Verificação |
|---|---|
| Painel e API sem texto de conversa | Inspeção do painel e da API; teste automatizado |
| Texto bruto descartado | Revisão de código e teste em ambiente de teste |
| Acesso por vínculo | Teste de acesso entre contas de famílias diferentes |
| Exclusão em 30 dias | Teste de exclusão confirmado em ambiente de teste |
| Salvaguardas de menores (seção 9) | Lista de verificação (artefato 09) e teste S1 a S11 (artefato 10) |
| Sem rotulação (seção 10) | Varredura de linguagem rotulante: 15 termos proibidos, 6 frases obrigatórias (artefato 10) |

## 12. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 02/10/2026 | Equipe GuardIA | Versão inicial (rascunho) |
| 1.1 | 02/10/2026 | Equipe GuardIA | Inclusão das seções 9 (E6) e 10 (E5) |
