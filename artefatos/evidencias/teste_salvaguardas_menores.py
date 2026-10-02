#!/usr/bin/env python3
"""GuardIA - E6 (dados de menores sem salvaguardas específicas): testes automatizados no protótipo.
Uso: python3 teste_salvaguardas_menores.py ../../index.html   (requer: pip install playwright && playwright install chromium)
"""
import sys, json, pathlib
from datetime import datetime
from playwright.sync_api import sync_playwright
alvo = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../../index.html").resolve().as_uri()
R = []
def t(id_, desc, ok, det=""): R.append((id_, desc, bool(ok), det))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.on("dialog", lambda d: d.accept())
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(alvo); pg.click("#tab-signup")
    # S1 idade só 6 a 17
    ages = pg.eval_on_selector_all("#su-age option", "o=>o.map(x=>+x.value)")
    t("S1", "Cadastro aceita apenas idades de 6 a 17 anos", min(ages) == 6 and max(ages) == 17, f"{min(ages)}-{max(ages)}")
    # S2 consentimento não pré-marcado e obrigatório
    t("S2a", "Caixa de consentimento NÃO vem pré-marcada", not pg.is_checked("#su-consent"))
    pg.fill("#su-parent", "Responsável Teste"); pg.fill("#su-email", "teste@exemplo.com"); pg.fill("#su-pass", "senha123"); pg.fill("#su-child", "Criança Teste")
    pg.click("#form-signup button[type=submit]")
    t("S2b", "Cadastro é bloqueado sem consentimento", pg.is_visible("#screen-auth") and "consentimento" in pg.inner_text("#signup-error"))
    pg.check("#su-consent"); pg.click("#form-signup button[type=submit]"); pg.wait_for_selector("#screen-app", state="visible")
    acc = json.loads(pg.evaluate("localStorage.getItem('guardia_accounts')"))["teste@exemplo.com"]
    t("S3", "Versão do termo e da política e data do aceite são registradas", acc.get("consent", {}).get("termo") == "1.1" and acc["consent"].get("data"), json.dumps(acc.get("consent"), ensure_ascii=False))
    pg.click("#navtab-privacidade")
    t("S4", "Registro do propósito da criança (RF07) vem DESATIVADO por padrão", not pg.is_checked("#pv-proposito"))
    t("S5", "Uso de correções para melhoria vem DESATIVADO por padrão", not pg.is_checked("#pv-correcoes"))
    t("S6", "Existe explicação em linguagem simples para o jovem", "não veem" in pg.inner_text("#bloco-jovem").lower() or "não veem" in pg.inner_text("#bloco-jovem"))
    # S7 nenhum texto de conversa nas chaves armazenadas
    chaves = pg.evaluate("Object.keys(localStorage)")
    suspeitas = [k for k in chaves if any(w in k.lower() for w in ("conversa", "chat", "mensagem", "texto"))]
    t("S7", "Nenhuma chave de armazenamento guarda texto de conversa", not suspeitas, "chaves: " + ", ".join(chaves))
    # S8 painel e alertas sem texto literal (nenhum campo de entrada de conversa)
    pg.click("#navtab-alertas"); corpo = pg.inner_text("#view-alertas").lower()
    t("S8", "Alertas informam que não usam texto das conversas", "não usamos o texto das conversas" in corpo)
    t("S9", "Nenhum alerta oferece bloqueio ou punição (apenas conversar, ignorar, corrigir, contestar, orientação)",
      pg.eval_on_selector_all("#alert-list button", "b=>b.map(x=>x.innerText)")[:5] == ["Conversar", "Ignorar", "Corrigir classificação", "Contestar (para o jovem)", "Pedir orientação"])
    # S10 exclusão remove tudo
    pg.click("#navtab-privacidade"); pg.click("#btn-delete"); pg.wait_for_timeout(300)
    resto = pg.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('guardia_') && k!=='guardia_accounts')")
    contas = pg.evaluate("localStorage.getItem('guardia_accounts')")
    t("S10", "Exclusão remove conta, sessão, configurações, progresso e alertas", contas == "{}" and not resto, f"contas={contas} restos={resto}")
    t("S11", "Nenhum erro de JavaScript durante o fluxo", not errs, "; ".join(errs))
    b.close()
ok = all(r[2] for r in R)
out = [f"GuardIA - RESULTADO DO TESTE DE SALVAGUARDAS PARA MENORES (E6) | {datetime.now():%d/%m/%Y %H:%M} | arquivo testado: index.html", "-" * 110]
for i, d, o, det in R: out.append(f"[{'PASSOU' if o else 'FALHOU'}] {i:<4} {d}" + (f"  ({det})" if det and not o else ""))
out += ["-" * 110, f"RESUMO: {sum(r[2] for r in R)}/{len(R)} testes aprovados | resultado: {'APROVADO' if ok else 'REPROVADO'}", "Dados: 100% fictícios (conta de teste criada e excluída durante a execução)."]
print("\n".join(out)); sys.exit(0 if ok else 1)
