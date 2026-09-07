#!/usr/bin/env python3
"""
Genera dashboard.html a partir de data/latest.json + config.json.
No llama a ninguna API externa ni a herramientas MCP: solo formatea
datos ya recolectados. La recoleccion de datos (que si requiere las
herramientas MCP de Nexlev) la hace el agente de Claude Code antes de
invocar este script - ver docs/research_playbook.md.

Uso:
    python3 build_dashboard.py [--config CONFIG] [--data DATA] [--out OUT]
"""
import argparse
import json
import html
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fmt_int(n):
    try:
        return f"{int(n):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "-"


def fmt_money(n):
    try:
        return f"${int(n):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "-"


def channel_row_html(ch: dict) -> str:
    name = html.escape(ch.get("name", "?"))
    url = html.escape(ch.get("url", "#"))
    days = ch.get("days_since_creation", 0)
    views30 = ch.get("views_30d", 0)
    subs = ch.get("subscribers", 0)
    rev_min = ch.get("est_revenue_min_usd", 0)
    rev_max = ch.get("est_revenue_max_usd", 0)
    ranking = ch.get("ranking", 0)
    ratio = ch.get("views_subscribers_ratio", 0)
    monetized = "Si" if ch.get("is_monetized") else "No"
    external = "Si" if ch.get("external_monetization_signals") else "No"

    return f"""<tr>
<td><a href="{url}" target="_blank" rel="noopener">{name}</a></td>
<td data-sort="{days}">{fmt_int(days)}</td>
<td data-sort="{views30}">{fmt_int(views30)}</td>
<td data-sort="{subs}">{fmt_int(subs)}</td>
<td data-sort="{ratio}">{ratio:.1f}</td>
<td data-sort="{rev_min}">{fmt_money(rev_min)} - {fmt_money(rev_max)} <span class="tag">estimado</span></td>
<td>{monetized}</td>
<td>{external}</td>
<td data-sort="{ranking}" class="rank rank-{ranking}">{ranking}</td>
</tr>"""


def section_table_html(section_id: str, title: str, channels: list, criteria_desc: str) -> str:
    rows = "\n".join(channel_row_html(c) for c in channels)
    return f"""
<section id="panel-{section_id}" class="tabpanel" role="tabpanel" aria-labelledby="tab-{section_id}" hidden>
  <p class="criteria">{html.escape(criteria_desc)}</p>
  <p class="count">Canales: <strong class="count-num">{len(channels)}</strong></p>
  <div class="table-wrap">
  <table data-section="{section_id}">
    <thead>
      <tr>
        <th data-key="name">Canal</th>
        <th data-key="days" class="num">Dias</th>
        <th data-key="views" class="num">Vistas 30d</th>
        <th data-key="subs" class="num">Subs</th>
        <th data-key="ratio" class="num">Ratio V/S</th>
        <th data-key="revenue" class="num">Ingresos est.</th>
        <th data-key="monetized">Monetiza</th>
        <th data-key="external">Ingr. externos</th>
        <th data-key="rank" class="num">Ranking</th>
      </tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
</section>"""


CRITERIA_DESC = {
    "ia_nichos": "Duracion media 10-45 min - >=500.000 vistas/30d - canal <=90 dias - senales de produccion por IA",
    "long_form": "Canal <=90 dias - >=200.000 vistas/mes - duracion media >70 min",
    "faceless_nuevos": ">=1.000.000 vistas/30d - canal <=90 dias",
    "faceless_establecidos": ">=1.000.000 vistas/30d - canal >90 dias",
}


def build(config: dict, data: dict, out_path: Path):
    sections_cfg = {s["id"]: s for s in config["sections"]}
    generated_at = data.get("generated_at", datetime.now(timezone.utc).isoformat())

    tabs_html = []
    panels_html = []
    for i, s in enumerate(config["sections"]):
        sid = s["id"]
        title = s["title"]
        channels = data.get("sections", {}).get(sid, [])
        tabs_html.append(
            f'<button class="tab" id="tab-{sid}" role="tab" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'aria-controls="panel-{sid}" data-target="{sid}">{html.escape(title)} '
            f'<span class="badge">{len(channels)}</span></button>'
        )
        panels_html.append(section_table_html(sid, title, channels, CRITERIA_DESC.get(sid, "")))

    html_out = TEMPLATE.format(
        generated_at=html.escape(generated_at),
        tabs="\n".join(tabs_html),
        panels="\n".join(panels_html),
    )
    out_path.write_text(html_out, encoding="utf-8")
    return out_path


TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dashboard Nichos YouTube Faceless</title>
<style>
:root {{
  --bg: #0b0d12; --panel: #12151c; --border: #232838; --text: #e6e9f0;
  --muted: #8891a7; --accent: #5b8cff; --good: #35c88a; --warn: #f2b84b;
}}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font-family: -apple-system, Segoe UI, Roboto, Arial, sans-serif; }}
header {{ padding: 20px 24px 8px; }}
h1 {{ margin: 0 0 4px; font-size: 20px; }}
.meta {{ color: var(--muted); font-size: 13px; }}
.controls {{ display:flex; gap:12px; align-items:center; padding: 12px 24px; flex-wrap: wrap; }}
.controls label {{ font-size: 13px; color: var(--muted); }}
.controls input {{ background: var(--panel); border:1px solid var(--border); color:var(--text); padding:6px 10px; border-radius:6px; width:70px; }}
.tabs {{ display:flex; gap:6px; padding: 0 24px; border-bottom:1px solid var(--border); flex-wrap:wrap; }}
.tab {{ background:transparent; border:none; color:var(--muted); padding:10px 14px; cursor:pointer; font-size:14px; border-bottom:2px solid transparent; }}
.tab[aria-selected="true"] {{ color:var(--text); border-bottom-color:var(--accent); }}
.badge {{ background:var(--border); color:var(--muted); border-radius:10px; padding:1px 7px; font-size:11px; margin-left:4px; }}
.tabpanel {{ padding: 16px 24px 40px; }}
.criteria {{ color: var(--muted); font-size: 13px; margin: 4px 0 10px; }}
.count {{ font-size: 13px; color: var(--muted); margin-bottom: 10px; }}
.table-wrap {{ overflow-x: auto; border:1px solid var(--border); border-radius:8px; }}
table {{ border-collapse: collapse; width: 100%; min-width: 900px; font-size: 13px; }}
thead th {{ text-align:left; background: var(--panel); color: var(--muted); font-weight:600; padding:10px 12px; cursor:pointer; white-space:nowrap; position: sticky; top:0; }}
thead th.num {{ text-align:right; }}
thead th:hover {{ color: var(--text); }}
tbody td {{ padding:9px 12px; border-top:1px solid var(--border); white-space:nowrap; }}
tbody td:nth-child(n+2) {{ text-align:right; }}
tbody tr:hover {{ background: rgba(255,255,255,0.03); }}
a {{ color: var(--accent); text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
.tag {{ color: var(--warn); font-size:10px; border:1px solid var(--warn); border-radius:4px; padding:1px 4px; margin-left:4px; }}
.rank {{ font-weight:700; }}
.rank-9, .rank-10 {{ color: var(--good); }}
.rank-1, .rank-2, .rank-3 {{ color: var(--muted); }}
tr.hidden-by-filter {{ display:none; }}
</style>
</head>
<body>
<header>
  <h1>Dashboard de Nichos YouTube Faceless</h1>
  <div class="meta">Generado: {generated_at} - Fuente: Nexlev MCP - Ingresos siempre etiquetados como estimados</div>
</header>
<div class="controls">
  <label for="minRank">Ranking minimo</label>
  <input type="number" id="minRank" min="1" max="10" value="1">
</div>
<div class="tabs" role="tablist">
{tabs}
</div>
{panels}
<script>
(function() {{
  var tabs = document.querySelectorAll('.tab');
  var panels = document.querySelectorAll('.tabpanel');
  function activate(id) {{
    tabs.forEach(function(t) {{
      var on = t.dataset.target === id;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    }});
    panels.forEach(function(p) {{
      p.hidden = p.id !== 'panel-' + id;
    }});
  }}
  tabs.forEach(function(t) {{
    t.addEventListener('click', function() {{ activate(t.dataset.target); }});
  }});
  if (tabs.length) activate(tabs[0].dataset.target);

  document.querySelectorAll('table').forEach(function(table) {{
    var state = {{ key: null, dir: 1 }};
    table.querySelectorAll('thead th').forEach(function(th, idx) {{
      th.addEventListener('click', function() {{
        var tbody = table.querySelector('tbody');
        var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
        var dir = (state.key === idx) ? -state.dir : 1;
        state.key = idx; state.dir = dir;
        rows.sort(function(a, b) {{
          var ca = a.children[idx], cb = b.children[idx];
          var va = ca.dataset.sort !== undefined ? parseFloat(ca.dataset.sort) : ca.textContent.trim().toLowerCase();
          var vb = cb.dataset.sort !== undefined ? parseFloat(cb.dataset.sort) : cb.textContent.trim().toLowerCase();
          if (va < vb) return -1 * dir;
          if (va > vb) return 1 * dir;
          return 0;
        }});
        rows.forEach(function(r) {{ tbody.appendChild(r); }});
      }});
    }});
  }});

  var minRank = document.getElementById('minRank');
  function applyFilter() {{
    var min = parseInt(minRank.value, 10) || 1;
    document.querySelectorAll('table').forEach(function(table) {{
      var rankIdx = 8;
      table.querySelectorAll('tbody tr').forEach(function(row) {{
        var cell = row.children[rankIdx];
        var val = cell ? parseFloat(cell.dataset.sort) : 0;
        row.classList.toggle('hidden-by-filter', val < min);
      }});
      var panel = table.closest('.tabpanel');
      var countEl = panel.querySelector('.count-num');
      var visible = table.querySelectorAll('tbody tr:not(.hidden-by-filter)').length;
      if (countEl) countEl.textContent = visible;
    }});
  }}
  minRank.addEventListener('input', applyFilter);
}})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(ROOT / "config.json"))
    ap.add_argument("--data", default=None, help="Por defecto usa data_snapshot_path del config")
    ap.add_argument("--out", default=None, help="Por defecto usa output_html_path del config")
    args = ap.parse_args()

    config = load_json(Path(args.config))
    data_path = Path(args.data) if args.data else ROOT / config["data_snapshot_path"]
    out_path = Path(args.out) if args.out else ROOT / config["output_html_path"]

    data = load_json(data_path)
    result = build(config, data, out_path)
    print(f"Dashboard generado: {result}")


if __name__ == "__main__":
    main()
