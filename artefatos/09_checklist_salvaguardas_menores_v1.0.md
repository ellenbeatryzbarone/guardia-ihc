# Lista de Verificação de Salvaguardas para Crianças e Adolescentes — GuardIA

| Campo | Valor |
|---|---|
| **Versão** | 1.0 |
| **Data** | 02/10/2026 |
| **Responsável** | Equipe GuardIA (Ellen Beatryz · Luana Cavalcanti · Márcia Rejane) |
| **Riscos tratados** | **E6 Tratamento de dados de menores sem salvaguardas específicas** · E5 Rotulação e estigmatização · T07 Privacidade |
| **Requisitos** | RF01, RF02, RF03, RF04 |
| **Base** | LGPD art. 14 (melhor interesse; consentimento específico e em destaque); ECA Digital (Lei nº 15.211/2025); Enunciado da ANPD sobre dados de crianças e adolescentes |

> **Como usar:** cada linha é uma salvaguarda com a evidência que qualquer pessoa pode abrir. O status é **honesto**: "Comprovado no protótipo" significa que o teste automatizado (artefato 10) passou; "A definir" significa que ainda não existe controle comprovado. Esta lista deve ser revisada antes de qualquer piloto com dados reais.

## 1. Salvaguardas

| ID | Salvaguarda | Tipo | Onde está | Evidência | Como verificar | Status |
|---|---|---|---|---|---|---|
| SG01 | Cadastro limitado a 6–17 anos | Preventiva | `index.html` (cadastro) | Teste S1 | Executar `teste_salvaguardas_menores.py` | Comprovado no protótipo |
| SG02 | Consentimento do responsável ativo, sem caixa pré-marcada, obrigatório para criar a conta | Governança | Termo v1.1; `index.html` | Testes S2a, S2b | Tentar cadastrar sem marcar a caixa | Comprovado no protótipo |
| SG03 | Versão do termo, da política e data do aceite registradas | Governança | `index.html` (campo `consent`) | Teste S3 | Inspecionar o registro da conta de teste | Comprovado no protótipo |
| SG04 | Registro do propósito declarado pela criança (RF07) desativado por padrão | Preventiva | Tela de privacidade | Teste S4; tela 07 | Abrir a aba Privacidade em conta nova | Comprovado no protótipo |
| SG05 | Uso de correções para melhoria desativado por padrão | Preventiva | Tela de privacidade | Teste S5; tela 07 | Idem | Comprovado no protótipo |
| SG06 | Explicação em linguagem simples para o jovem (e leitura conjunta de 6 a 9 anos) | Governança | Tela de privacidade; Política v1.1 | Teste S6; tela 07 | Ler o bloco "Para [nome]" | Comprovado no protótipo |
| SG07 | Texto de conversa não é armazenado nem exibido | Preventiva | Prompt v1.1 (regras 1 e 12); política (seção 2) | Teste S7 e S8; relatório 05 | Inspecionar o armazenamento e os alertas | Comprovado no protótipo (o protótipo não recebe conversas reais) |
| SG08 | Dado pessoal que escapar do filtro não é repetido e vai para revisão humana | Humana | Prompt v1.1 (regra 12, caso C8) | Log, CASO-024 | Rodar o caso C8 e conferir o log | Em andamento (depende do LLM contratado) |
| SG09 | Nenhuma ação punitiva ou bloqueio automático | Preventiva | `index.html` (ações do alerta) | Teste S9; log, CASO-018 | Conferir as 5 ações do alerta | Comprovado no protótipo |
| SG10 | Canal para o jovem contestar, com revisão humana | Humana | `index.html` (botão Contestar) | Tela 08; log, CASO-021 | Contestar um alerta e consultar o log | Comprovado no protótipo (fila de revisão ainda simulada) |
| SG11 | Exclusão do perfil e dos dados pelo responsável | Preventiva | Tela de privacidade | Teste S10 | Excluir conta de teste e conferir o armazenamento | Comprovado no protótipo |
| SG12 | Indicadores expiram em 60 dias; texto bruto com retenção zero | Preventiva | Política v1.1 (seção 2) | Política; tela 07 | Revisar a política de retenção | A definir (a expiração não está implementada no protótipo) |
| SG13 | Sem treino de modelos de terceiros com dados da criança | Governança | Política (seção 3); bases (F1) | Lista de bases v1.1 | Revisar contrato do fornecedor | A definir (não há fornecedor contratado) |
| SG14 | Autenticação forte, hash de senha, criptografia em trânsito e em repouso | Preventiva | — | — | Revisão de segurança | **A definir. NÃO atendido no protótipo** (a senha fica em texto simples no `localStorage`; serve só para demonstração) |
| SG15 | Avaliação do melhor interesse e mapeamento de fluxos antes de piloto com dados reais | Governança | Análise de Riscos (T07) | — | Revisão jurídica e ética | A definir |
| SG16 | Sem rotulação, comparação ou perfil permanente (E5) | Detectiva | Prompt v1.1 (regra 11); `index.html` | Varredura (artefato 10) | Rodar `verificacao_linguagem_rotulante.py` | Comprovado no protótipo |

## 2. Resumo

Das 16 salvaguardas, **11 estão comprovadas no protótipo** (SG01 a SG07, SG09, SG10, SG11 e SG16), **1 está em andamento** (SG08, depende do LLM contratado) e **4 estão a definir** (SG12, SG13, SG14 e SG15). Em SG10, a fila de revisão humana ainda é simulada. Nenhuma delas autoriza piloto com dados reais.

## 3. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 02/10/2026 | Equipe GuardIA | Versão inicial |
