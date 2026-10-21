#!/usr/bin/env python3
"""Renderiza dashboard-nexlev.html desde data/nexlev_busqueda_2026-10-21.json (sin llamadas a API)."""
import json, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / "data" / "nexlev_busqueda_2026-10-21.json", encoding="utf-8"))
e = html.escape
f = lambda n: "-" if n is None else f"{n:,}".replace(",", ".")
fd = lambda x: str(x).replace(".", ",")


def canal(c):
    subs = c["subs"]
    top = "".join(
        f'<tr><td>{e(t)}</td><td>{f(v)}</td><td>{fd(round(v / subs, 1))}x</td></tr>' for t, v in c["top"]
    )
    return (
        f'<h3><a href="{e(c["url"])}">{e(c["nombre"])}</a></h3>'
        f'<table class="kv"><tr><th>Subs</th><td>{f(subs)}</td><th>Creado</th><td>{c["creado"]}</td>'
        f'<th>Antigüedad</th><td>1.º vídeo {c["primer_video"]}</td></tr>'
        f'<tr><th>Vis. medias</th><td>{f(c["media_vistas"])} ({fd(round(c["media_vistas"] / subs, 1))}x subs)</td>'
        f'<th>Mediana</th><td>{f(c["mediana_vistas"])}</td><th>Vídeos</th><td>{c["videos"]} ({fd(c["subidas_semana"])}/sem)</td></tr>'
        f'<tr><th>RPM est.</th><td>{fd(c["rpm"])} $</td><th>Ingresos/mes est.</th><td>{f(c["ingresos_mes_est"])} $</td>'
        f'<th>Faceless / monetizado</th><td>{e(c["faceless"])} / {e(c["monetizado"])}</td></tr></table>'
        f'<table><tr><th>Mejores vídeos</th><th>Visitas</th><th>Vis/sub</th></tr>{top}</table>'
    )


A = "".join(
    f'<h2>A{i + 1}. {e(n["nombre"])} <small>({e(n["idioma"])})</small></h2>'
    f'<p><b>{e(n["veredicto"])}</b></p>'
    + "".join(canal(c) for c in n["canales"])
    + f'<p><b>Competidores detectados:</b> {e(n["competidores"])}</p>'
    f'<p><b>Por qué es una oportunidad:</b> {e(n["por_que"])}</p>'
    f'<p class="n"><b>Riesgos:</b> {e(n["riesgos"])}</p>'
    for i, n in enumerate(d["lista_A"])
)

B = d["lista_B"]
cm = B["casi_pasa"]
ev = "".join(
    f'<tr><td><a href="{e(u)}">{e(n)}</a></td><td>{f(s)}</td><td>{e(t)}</td><td>{f(v)}</td><td>{fd(round(v / s))}x</td></tr>'
    for n, u, s, t, v in cm["evidencia"]
)
Bhtml = (
    f'<p><b>Ningún nicho entregable.</b> {e(B["nota"])}</p>'
    f'<h3>Casi pasa: {e(cm["nombre"])} <small>({e(cm["idioma"])})</small></h3>'
    f'<table><tr><th>Canal</th><th>Subs</th><th>Mejor vídeo</th><th>Visitas</th><th>Vis/sub</th></tr>{ev}</table>'
    f'<p><b>Competencia en inglés/español:</b> {e(cm["competencia_en_es"])}</p>'
    f'<p class="n"><b>Por qué no se entrega:</b> {e(cm["por_que_no_entrega"])}</p>'
)

desc = "".join(
    f'<tr><td>{e(x["nicho"])}</td><td>{x["canales"] if x["canales"] else "-"}</td><td>{e(x["motivo"])}</td></tr>'
    for x in d["descartes"]
)
R = d["recomendacion"]
rec = (
    f'<h2>Recomendación: {e(R["nicho"])}</h2><ul>'
    + "".join(f"<li>{e(x)}</li>" for x in R["por_que"])
    + f'</ul><p><b>Primeros pasos:</b> {e(R["primeros_pasos"])}</p><p class="n">{e(R["alternativa"])}</p>'
)

open(ROOT / "dashboard-nexlev.html", "w", encoding="utf-8").write(f"""<!doctype html><html lang="es"><meta charset="utf-8"><title>Búsqueda profunda Nexlev</title>
<style>body{{font:14px system-ui;max-width:1100px;margin:2em auto;padding:0 1em}}table{{border-collapse:collapse;width:100%;margin:.4em 0 1em}}td,th{{border-bottom:1px solid #ccc;padding:4px 6px;text-align:left}}.kv th{{color:#666;font-weight:normal;width:1%;white-space:nowrap}}.n,small{{color:#666}}.rec{{background:#eaf6ea;padding:.5em 1em;border-radius:6px}}</style>
<h1>Búsqueda profunda de nichos faceless (Nexlev)</h1>
<p><b>Fuente: Nexlev MCP</b> · {d["fecha"]}. Filtros: &lt;50K subs, creado hace poco, vistas desproporcionadas en varios vídeos, faceless y monetizado verificados con check_faceless_channel / check_channel_monetization, baja competencia.</p>
<ul>{"".join(f"<li>{e(m)}</li>" for m in d["metodo"])}</ul>
<p class="n"><b>Avisos:</b> {" ".join(e(a) for a in d["avisos"])}</p>
<h1>Lista A · Baja competencia en español/inglés</h1>{A}
<h1>Lista B · Vacíos de mercado (funcionan en otro idioma, inexistentes en es/en)</h1>{Bhtml}
<div class="rec">{rec}</div>
<h1>Descartados</h1>
<table><tr><th>Nicho</th><th>Canales</th><th>Motivo</th></tr>{desc}</table>
</html>""")
print("dashboard-nexlev.html escrito")
