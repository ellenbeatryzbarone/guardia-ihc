#!/usr/bin/env python3
"""GuardIA - E5 (rotulação e estigmatização): varredura de linguagem rotulante nos textos exibidos.
Uso: python3 verificacao_linguagem_rotulante.py ../../index.html
Falha (exit 1) se achar termo rotulante ou se faltar uma frase obrigatória.
"""
import re, sys, json, unicodedata
alvo = sys.argv[1] if len(sys.argv) > 1 else "../../index.html"
html = open(alvo, encoding="utf-8").read()
def n(t): return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")
txt = n(html)
PROIBIDOS = {  # rótulos que descrevem a criança, e não o padrão de uso
 "viciad":"rótulo de dependência", "vicio":"rótulo de dependência", "dependente":"rótulo de dependência",
 "problematic":"rótulo de conduta", "deprimid":"diagnóstico implícito", "suspeit":"presunção de culpa",
 "mau uso":"presunção de culpa", "comportamento de risco":"rótulo de conduta", "desajustad":"rótulo de conduta",
 "crianca de risco":"rótulo de risco", "adolescente de risco":"rótulo de risco", "perigos":"rótulo de risco",
 "pior que":"comparação entre crianças", "media das criancas":"comparação entre crianças", "ranking":"comparação entre crianças",
}
OBRIGATORIAS = [
 ("pode estar errada", "aviso de incerteza"),
 ("nao indica um problema de saude", "ausência de diagnóstico"),
 ("nao descreve quem seu filho ou filha e", "alerta descreve uso, não a pessoa"),
 ("nenhum rotulo e guardado", "sem perfil persistente"),
 ("expiram em 60 dias", "expiração dos indicadores"),
 ("contestar", "canal de contestação do jovem"),
]
achados = [{"termo": t, "motivo": m, "ocorrencias": txt.count(t)} for t, m in PROIBIDOS.items() if t in txt]
faltando = [{"frase": f, "motivo": m} for f, m in OBRIGATORIAS if f not in txt]
ok = not achados and not faltando
print(json.dumps({"arquivo": alvo, "termos_rotulantes_encontrados": achados, "frases_obrigatorias_ausentes": faltando,
                  "termos_verificados": len(PROIBIDOS), "frases_exigidas": len(OBRIGATORIAS), "resultado": "APROVADO" if ok else "REPROVADO"}, ensure_ascii=False, indent=1))
sys.exit(0 if ok else 1)
