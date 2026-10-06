#!/usr/bin/env python3
"""Renderiza dashboard-lugares.html desde data/ideas_lugares.json (sin llamadas a API)."""
import json, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / "data" / "ideas_lugares.json"))
f = lambda n: "-" if n is None else f"{n:,}".replace(",", ".")
N = json.load(open(ROOT / "data" / "ideas_nuevas.json"))
_ang = lambda t: N["angulos"].get(t, "")
sec = []
for i, r in d["ideas"].items():
    v = r["videos"]; n_out = sum(x["outlier5x"] for x in v)
    rows = "".join(
        f'<tr class="{"out" if x["outlier5x"] else ""}"><td>{html.escape(x["titulo"])}</td><td>{html.escape(x["canal"])}</td>'
        f'<td>{f(x["subs"]) if x["subs"] is not None else "oculto"}</td><td>{f(x["visitas"])}</td><td>{x["dias"]} d</td><td>{x["min"]} min</td>'
        f'<td>{x["vps"] if x["vps"] is not None else "-"}</td><td>{f(x["vpd"])}</td><td>{"★ 5x" if x["outlier5x"] else ""}</td><td>{html.escape(_ang(x["titulo"]))}</td></tr>'
        for x in v[:3])
    sec.append(f'<h2>{i}. {html.escape(r["nombre"])} <small>({len(v)} vídeos, {n_out} con señal 5x)</small></h2>'
               + (f'<p class="n">{html.escape(r["nota"])}</p>' if r.get("nota") else "")
               + f'<table><tr><th>Vídeo</th><th>Canal</th><th>Subs</th><th>Visitas</th><th>Antigüedad</th><th>Duración</th><th>Vis/sub</th><th>Vis/día</th><th>Outlier~</th><th>Ángulo</th></tr>{rows}</table>')
M = json.load(open(ROOT / "data" / "mineria_canales.json"))
mi = []
for c in M["canales"]:
    rows = "".join(f'<tr><td>{html.escape(x["titulo"][:95])}</td><td>{f(x["visitas"])}</td><td>{x["vps"]}</td><td>{x["dias"]} d</td><td>{x["min"]} min</td></tr>' for x in c["top"])
    mi.append(f'<h3>{html.escape(c["canal"])} <small>({f(c["subs"])} subs, {c["n_videos"]} vídeos leídos)</small></h3><table><tr><th>Vídeo</th><th>Visitas</th><th>Vis/sub</th><th>Antigüedad</th><th>Duración</th></tr>{rows}</table>')
ni = "".join(f"<tr><td>{i+1}</td><td><b>{html.escape(a)}</b></td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>" for i, (a, b, c) in enumerate(N["ideas"]))
extra = f"""<h1>Minería de canales pequeños</h1><p>Fuente: YouTube Data API (aproximación), {M["fecha"]}, {M["unidades"]} unidades. Últimos ~100 vídeos por canal, ordenados por visitas/suscriptor.
Patrón: Cronotierra repite "Así viven estas tribus… | Documental Completo" (recopilatorios de 5 comunidades); Discovery 10 / Discovery Vault repiten listas "N descubrimientos…" y titulares de "IA demuestra…"; varios canales viven de 1-2 vídeos y el resto rinde 1-10x.</p>{"".join(mi)}
<h1>10 ideas nuevas</h1><p>Cada una con un vídeo real de esos canales. "Stock" = mi estimación del material disponible, no un dato medido. Las afirmaciones deben verificarse antes de escribir el guion.</p>
<table><tr><th>#</th><th>Título</th><th>Respaldo</th><th>Stock / reservas</th></tr>{ni}</table>
<p class="n">Darién: {html.escape(N["nota_darien"])}</p>"""
open(ROOT / "dashboard-lugares.html", "w", encoding="utf-8").write(f"""<!doctype html><html lang="es"><meta charset="utf-8"><title>Lugares inaccesibles</title>
<style>body{{font:14px system-ui;max-width:1100px;margin:2em auto;padding:0 1em}}table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #ccc;padding:4px 6px;text-align:left}}tr.out{{background:#fff3c4}}.n,small{{color:#666}}</style>
<h1>Validación: canal de lugares inaccesibles</h1>
<p><b>Fuente: YouTube Data API (aproximación)</b> · {d["fecha"]} · {d["unidades"]} unidades de cuota.
Outlier~ = canal &lt;50.000 subs con visitas &gt; 5× sus suscriptores; <b>no es el outlier de Nexlev</b>.
Búsqueda: order=viewCount, últimos 12 meses, duración &gt;20 min (el filtro "long" de la API); el idioma de búsqueda es una pista, no garantiza el idioma del vídeo.</p>
{"".join(sec)}{extra}</html>""")
