# Lista de Bases de Dados e Fornecedores Utilizados — GuardIA

| Campo | Valor |
|---|---|
| **Versão** | 1.1 |
| **Data** | 02/10/2026 |
| **Responsável** | Equipe GuardIA (Ellen Beatryz · Luana Cavalcanti · Márcia Rejane · Deivison Amorim · Denilson Lima) |
| **Riscos tratados** | T05 Viés · T07 Privacidade · T03 Desempenho · E5 Rotulação · E6 Dados de menores |
| **Requisitos** | RF03, RF04 |

> **Princípio:** nesta fase **nenhuma base contém dado real de crianças ou adolescentes**. Toda base abaixo é sintética, pública ou futura (condicionada a consentimento e avaliação).

## 1. Bases de dados

| ID | Base | Origem | Conteúdo | Dado pessoal? | Uso | Limites e lacunas | Local |
|---|---|---|---|---|---|---|---|
| B1 | Conjunto sintético de avaliação v1.0 | Escrito pela equipe | 72 mensagens, 4 categorias × 3 registros × 4 faixas etárias | **Não** | Teste de viés e desempenho (artefato 05) | Redigido por adultos; regionalismos limitados ao Nordeste; 6 exemplos por célula; sem áudio, emoji, abreviação de chat | `evidencias/dataset_sintetico_v1.0.csv` |
| B2 | Léxico de categorias v0.1 | Escrito pela equipe | ~60 termos em 4 categorias | Não | Protótipo de classificação por regras | Baseado em português padrão; sub-representa gíria e regionalismo (ver relatório) | `evidencias/avaliacao_vieses.py` |
| B3 | Casos sintéticos de revisão humana | Escrito pela equipe | 26 casos fictícios | Não | Log de revisão (artefato 06) | Demonstração de formato, não é amostra estatística | `06_log_revisao_humana_v1.1.txt` |
| B6 | Lista de termos rotulantes v1.0 | Escrita pela equipe | 15 termos e expressões proibidos e 6 frases obrigatórias | Não | Varredura automática de textos exibidos (E5, artefato 10) | Lista curta, em português; não detecta rotulação implícita nem ironia; ampliar com revisão de famílias e educadores | `evidencias/verificacao_linguagem_rotulante.py` |
| B4 | Dados de uso real das famílias | **Não utilizado** | — | Sim | Previsto apenas pós-piloto autorizado | Exige mapa de fluxos, base legal e avaliação do melhor interesse | — |
| B5 | Cenários consentidos de famílias | **A coletar (futuro)** | Cenários descritos voluntariamente | Possível | Ampliar diversidade da avaliação | Exige TCLE/TALE, parecer ético e proteção de menores | — |

## 2. Fornecedores e componentes

| ID | Componente | Papel | Dados que recebe | Treina com dados da criança? | Situação |
|---|---|---|---|---|---|
| F1 | LLM de classificação (a definir) | Classifica categoria e redige texto (artefato 01) | Somente texto anonimizado e faixa etária | **Não (exigência contratual)** | Não contratado; uso apenas com dados sintéticos |
| F2 | Hospedagem e banco de dados (a definir) | Armazena contas e indicadores agregados | Cadastro e agregados | Não se aplica | Protótipo roda no navegador (`localStorage`) |
| F3 | Fontes tipográficas Google Fonts | Exibição do painel | Endereço IP do navegador | Não se aplica | Em uso no protótipo; substituir por fontes locais em produção |

## 3. Fontes normativas e de referência

| Fonte | Uso no projeto |
|---|---|
| Lei nº 13.709/2018 (LGPD) | Base legal, art. 14 |
| Lei nº 15.211/2025 (ECA Digital) | Proteção de crianças e adolescentes em ambiente digital |
| Enunciado da ANPD sobre dados de crianças e adolescentes | Melhor interesse e bases legais |
| Análise de Riscos GuardIA v1 | Origem dos riscos T03 a T07 |
| Requisitos Funcionais GuardIA | Requisitos RF01 a RF06 |

## 4. Regras de governança das bases

1. Nenhuma base com dado real entra no projeto sem aprovação registrada.
2. Toda base nova recebe ID, origem, limites e lacunas antes do uso.
3. Mudanças nesta lista geram nova versão.

## 5. Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0 | 02/10/2026 | Equipe GuardIA | Versão inicial |
| 1.1 | 02/10/2026 | Equipe GuardIA | Inclusão da base B6 (E5) e dos riscos E5 e E6 |
