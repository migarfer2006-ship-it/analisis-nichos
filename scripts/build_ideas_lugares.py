#!/usr/bin/env python3
"""Renderiza dashboard-lugares.html desde data/ideas_lugares.json (sin llamadas a API)."""
import json, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / "data" / "ideas_lugares.json"))
f = lambda n: "-" if n is None else f"{n:,}".replace(",", ".")
sec = []
for i, r in d["ideas"].items():
    v = r["videos"]; n_out = sum(x["outlier5x"] for x in v)
    rows = "".join(
        f'<tr class="{"out" if x["outlier5x"] else ""}"><td>{html.escape(x["titulo"][:80])}</td><td>{html.escape(x["canal"])}</td>'
        f'<td>{f(x["subs"]) if x["subs"] is not None else "oculto"}</td><td>{f(x["visitas"])}</td><td>{x["dias"]} d</td><td>{x["min"]} min</td>'
        f'<td>{x["vps"] if x["vps"] is not None else "-"}</td><td>{f(x["vpd"])}</td><td>{"★ 5x" if x["outlier5x"] else ""}</td></tr>'
        for x in v[:3])
    sec.append(f'<h2>{i}. {html.escape(r["nombre"])} <small>({len(v)} vídeos, {n_out} con señal 5x)</small></h2>'
               + (f'<p class="n">{html.escape(r["nota"])}</p>' if r.get("nota") else "")
               + f'<table><tr><th>Vídeo</th><th>Canal</th><th>Subs</th><th>Visitas</th><th>Antigüedad</th><th>Duración</th><th>Vis/sub</th><th>Vis/día</th><th>Outlier~</th></tr>{rows}</table>')
open(ROOT / "dashboard-lugares.html", "w", encoding="utf-8").write(f"""<!doctype html><html lang="es"><meta charset="utf-8"><title>Lugares inaccesibles</title>
<style>body{{font:14px system-ui;max-width:1100px;margin:2em auto;padding:0 1em}}table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #ccc;padding:4px 6px;text-align:left}}tr.out{{background:#fff3c4}}.n,small{{color:#666}}</style>
<h1>Validación: canal de lugares inaccesibles</h1>
<p><b>Fuente: YouTube Data API (aproximación)</b> · {d["fecha"]} · {d["unidades"]} unidades de cuota.
Outlier~ = canal &lt;50.000 subs con visitas &gt; 5× sus suscriptores; <b>no es el outlier de Nexlev</b>.
Búsqueda: order=viewCount, últimos 12 meses, duración &gt;20 min (el filtro "long" de la API); el idioma de búsqueda es una pista, no garantiza el idioma del vídeo.</p>
{"".join(sec)}</html>""")
