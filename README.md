# GuardIA — protótipo e artefatos complementares (7 riscos · 02/10/2026)

**Riscos cobertos:** T03 Desempenho · T04 Explicabilidade · T05 Viés · T06 Supervisão humana · T07 Privacidade · **E5 Rotulação e estigmatização** (Educação) · **E6 Dados de menores sem salvaguardas específicas** (Educação).

| # | Arquivo | Tipo | Riscos | Requisitos |
|---|---|---|---|---|
| 01 | `01_prompt_classificador_v1.1.md` | Prompt (MD) | T07, T06, T04, T05, E5, E6 | RF03, RF04, RF05 |
| 02 | `02_politica_de_privacidade_v1.1.md` | Documento (MD) | T07, T04, E5, E6 | RF01, RF02, RF03 |
| 03 | `03_termo_de_consentimento_v1.1.md` | Documento (MD) | T07, T06, E5, E6 | RF01, RF02 |
| 04 | `04_lista_de_bases_utilizadas_v1.1.md` | Documento (MD) | T05, T07, T03, E5, E6 | RF03, RF04 |
| 05 | `05_relatorio_avaliacao_vieses_v1.1.pdf` | Relatório de teste (PDF) | T05, T03, T06, E5 | RF03, RF04 |
| 06 | `06_log_revisao_humana_v1.1.txt` | Log (TXT, sintético, 26 casos) | T03 a T07, E5, E6 | RF01, RF03, RF04, RF05 |
| 07 | `07_tela_configuracao_privacidade.png` | Tela (PNG) | T07, E6, E5 | RF01, RF03 |
| 08 | `08_tela_alerta_explicado.png` | Tela (PNG) | T06, T04, E5 | RF04 |
| 09 | `09_checklist_salvaguardas_menores_v1.0.md` | Documento (MD) | E6, E5, T07 | RF01 a RF04 |
| 10 | `10_relatorio_teste_E5_E6_v1.0.pdf` | Relatório de teste (PDF) | E5, E6 | RF01 a RF04 |
| — | `evidencias/` (scripts, dataset, resultados, gráfico) | Suporte aos relatórios 05 e 10 | T05, E5, E6 | RF03 |
| — | `index.html` (raiz do projeto) | Protótipo que gerou as telas 07 e 08 | T07, T06, T04, E5, E6 | RF01 a RF04 |

## Medidas por risco novo (mínimo: 3 medidas, 2 tipos)

| Risco | Medida | Tipo | Artefatos |
|---|---|---|---|
| E5 | Regra 11 do prompt (descrever uso, nunca a pessoa; sem comparação, ranking ou perfil) e expiração dos indicadores em 60 dias | Preventiva | 01, 02, 08 |
| E5 | Varredura automática de termos rotulantes e frases obrigatórias nos textos exibidos | Detectiva | 10, `evidencias/verificacao_linguagem_rotulante.py` |
| E5 | Contestação pelo jovem com revisão humana registrada | Humana | 06, 08 |
| E5 | Compromisso do responsável no termo (não rotular, comparar nem punir) | Governança | 03 |
| E6 | Consentimento ativo e versionado, opcionais desativados, explicação ao jovem, exclusão, texto de conversa não armazenado | Preventiva | 02, 07, 09 |
| E6 | Teste automatizado das salvaguardas (S1 a S11) | Detectiva | 10, `evidencias/teste_salvaguardas_menores.py` |
| E6 | Revisão humana de dado pessoal que escapar do filtro (regra 12 do prompt) | Humana | 01, 06 |
| E6 | Política, termo e lista de verificação das salvaguardas, com avaliação do melhor interesse antes de piloto | Governança | 02, 03, 09 |

## Equipe
Ellen Beatryz · Luana Cavalcanti · Márcia Rejane · Deivison Amorim · Denilson Lima

## Estrutura de pastas

```
guardia/
├── index.html        ← protótipo (abrir no navegador)
├── README.md
└── artefatos/
    ├── 01 a 10 (prompt, política, termo, bases, relatórios, log, telas, checklist)
    └── evidencias/   ← scripts e resultados dos testes
```

## Reprodução (executar dentro de `artefatos/evidencias/`)
- Viés: `python3 avaliacao_vieses.py` (script não incluído nesta entrega, ver nota abaixo)
- E5: `python3 verificacao_linguagem_rotulante.py ../../index.html`
- E6: `python3 teste_salvaguardas_menores.py ../../index.html` (requer `pip install playwright` e `playwright install chromium`)

Todos os dados são sintéticos; as telas usam o perfil fictício "Criança Demo".

## Nota sobre evidências ausentes
Os arquivos `avaliacao_vieses.py`, `dataset_sintetico_v1.0.csv`, `resultados_v1.0.json` e o gráfico de revocação, citados nos relatórios 05 e na lista de bases (B1, B2), não estavam entre os arquivos recebidos. Adicione-os em `artefatos/evidencias/` para completar a reprodução do relatório de viés.
