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


def rank_tier(r: int) -> str:
    if r >= 7:
        return "hi"
    if r >= 4:
        return "mid"
    return "lo"


def disproportion_index(ch: dict) -> float:
    """outlier_score / (subscribers/1000): cuanto mas alto, mas desproporcionado
    el rendimiento viral del canal respecto a su tamano de audiencia."""
    subs = ch.get("subscribers") or 0
    outlier = ch.get("outlier_score") or 0
    if subs <= 0:
        return 0.0
    return outlier / (subs / 1000)


def di_tier(di: float) -> str:
    if di >= 3:
        return "hi"
    if di >= 1:
        return "mid"
    return "lo"


def status_pill(is_true: bool, label_yes: str, label_no: str) -> str:
    cls = "yes" if is_true else "no"
    label = label_yes if is_true else label_no
    return f'<span class="pill pill-{cls}"><i class="dot"></i>{label}</span>'


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
    monetized = status_pill(bool(ch.get("is_monetized")), "Sí", "No")
    external = status_pill(bool(ch.get("external_monetization_signals")), "Sí", "No")
    di = disproportion_index(ch)
    rpm_avg = ch.get("rpm_avg")
    rpm_cell = f"${rpm_avg:.1f}" if isinstance(rpm_avg, (int, float)) else "—"
    competition = ch.get("competition_level")
    competition_cell = html.escape(competition) if competition else "—"

    return f"""<tr>
<td class="col-name"><a href="{url}" target="_blank" rel="noopener">{name}</a></td>
<td class="num" data-sort="{days}">{fmt_int(days)}</td>
<td class="num" data-sort="{views30}">{fmt_int(views30)}</td>
<td class="num" data-sort="{subs}">{fmt_int(subs)}</td>
<td class="num" data-sort="{ratio}">{ratio:.1f}×</td>
<td class="num" data-sort="{di}"><span class="rankpill rank-{di_tier(di)}">{di:.2f}</span></td>
<td class="num" data-sort="{rpm_avg or 0}">{rpm_cell}</td>
<td>{competition_cell}</td>
<td class="num col-rev" data-sort="{rev_min}">{fmt_money(rev_min)}–{fmt_money(rev_max)}<span class="tag">estimado</span></td>
<td>{monetized}</td>
<td>{external}</td>
<td class="num" data-sort="{ranking}"><span class="rankpill rank-{rank_tier(ranking)}">{ranking}</span></td>
</tr>"""


def section_table_html(section_id: str, title: str, channels: list, criteria_desc: str, excluded_count: int) -> str:
    rows = "\n".join(channel_row_html(c) for c in channels)
    excluded_note = (
        f' · <span class="tag">{excluded_count} excluidos por &gt;={fmt_int(50000)} subs</span>'
        if excluded_count else ""
    )
    return f"""
<section id="panel-{section_id}" class="tabpanel" role="tabpanel" aria-labelledby="tab-{section_id}" hidden>
  <p class="criteria">{html.escape(criteria_desc)}</p>
  <p class="count">Canales en esta sección: <strong class="count-num">{len(channels)}</strong>{excluded_note}</p>
  <div class="table-wrap">
  <table data-section="{section_id}">
    <thead>
      <tr>
        <th data-key="name">Canal</th>
        <th data-key="days" class="num">Días</th>
        <th data-key="views" class="num">Vistas 30d</th>
        <th data-key="subs" class="num">Subs</th>
        <th data-key="ratio" class="num">Ratio V/S</th>
        <th data-key="di" class="num" title="outlier_score / (subs/1000)">Índice desprop.</th>
        <th data-key="rpm" class="num" title="RPM real via get_video_rpm, cuando esta disponible">RPM real</th>
        <th data-key="competition" title="via get_niche_overview, cuando esta disponible">Competencia</th>
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
    "ia_nichos": "Duracion media 10-45 min - >=500.000 vistas/30d - canal <=90 dias - senales de produccion por IA - subs<50.000 - ordenado por indice de desproporcion",
    "long_form": "Canal <=90 dias - >=200.000 vistas/mes - duracion media >70 min - subs<50.000 - ordenado por indice de desproporcion",
    "faceless_nuevos": ">=1.000.000 vistas/30d - canal <=90 dias - subs<50.000 - ordenado por indice de desproporcion",
    "faceless_establecidos": ">=1.000.000 vistas/30d - canal >90 dias - subs<50.000 - ordenado por indice de desproporcion",
}


def build(config: dict, data: dict, out_path: Path):
    sections_cfg = {s["id"]: s for s in config["sections"]}
    generated_at = data.get("generated_at", datetime.now(timezone.utc).isoformat())
    deep_filter = config.get("deep_filter_criteria", {})
    max_subs = deep_filter.get("max_subscribers")

    tabs_html = []
    panels_html = []
    for i, s in enumerate(config["sections"]):
        sid = s["id"]
        title = s["title"]
        all_channels = data.get("sections", {}).get(sid, [])
        if max_subs:
            channels = [c for c in all_channels if (c.get("subscribers") or 0) < max_subs]
            excluded_count = len(all_channels) - len(channels)
        else:
            channels = all_channels
            excluded_count = 0
        channels = sorted(channels, key=disproportion_index, reverse=True)
        tabs_html.append(
            f'<button class="tab" id="tab-{sid}" role="tab" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'aria-controls="panel-{sid}" data-target="{sid}">{html.escape(title)} '
            f'<span class="badge">{len(channels)}</span></button>'
        )
        panels_html.append(section_table_html(sid, title, channels, CRITERIA_DESC.get(sid, ""), excluded_count))

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
<title>Radar Faceless</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root {{
  --bg: #F5F7F4;
  --surface: #FFFFFF;
  --surface-alt: #ECF1EB;
  --border: #D8E0D6;
  --text: #12211B;
  --text-muted: #5B6E63;
  --accent: #A85A18;
  --accent-soft: #F1E1C6;
  --good: #2E7D4F;
  --good-soft: #DCEEE0;
  --mid: #A85A18;
  --mid-soft: #F1E1C6;
  --lo-soft: #E7E9E4;
  --focus: #2E7D4F;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #0E1613;
    --surface: #162019;
    --surface-alt: #1B2620;
    --border: #2A3A31;
    --text: #E7EFE8;
    --text-muted: #93A89B;
    --accent: #E3A057;
    --accent-soft: #3A2C18;
    --good: #4FBE7C;
    --good-soft: #17331F;
    --mid: #E3A057;
    --mid-soft: #3A2C18;
    --lo-soft: #212D26;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #0E1613;
  --surface: #162019;
  --surface-alt: #1B2620;
  --border: #2A3A31;
  --text: #E7EFE8;
  --text-muted: #93A89B;
  --accent: #E3A057;
  --accent-soft: #3A2C18;
  --good: #4FBE7C;
  --good-soft: #17331F;
  --mid: #E3A057;
  --mid-soft: #3A2C18;
  --lo-soft: #212D26;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--text);
  font-family: "Public Sans", -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}}
.mono {{ font-family: "IBM Plex Mono", ui-monospace, Menlo, monospace; }}
header {{ padding: 28px 28px 18px; border-bottom: 1px solid var(--border); }}
.eyebrow {{
  font-family: "IBM Plex Mono", monospace; font-size: 11px; font-weight: 500;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin: 0 0 8px;
}}
h1 {{ margin: 0 0 6px; font-size: 26px; font-weight: 800; letter-spacing: -0.01em; text-wrap: balance; }}
.meta {{ color: var(--text-muted); font-size: 13px; }}
.meta .sep {{ margin: 0 8px; opacity: 0.5; }}
.controls {{
  display: flex; gap: 14px; align-items: center; padding: 16px 28px;
  border-bottom: 1px solid var(--border); flex-wrap: wrap; background: var(--surface-alt);
}}
.controls label {{ font-size: 12px; color: var(--text-muted); font-weight: 600; }}
.controls .field {{ display: flex; align-items: center; gap: 8px; }}
.controls input {{
  background: var(--surface); border: 1px solid var(--border); color: var(--text);
  padding: 6px 10px; border-radius: 6px; width: 64px; font-size: 13px; font-family: inherit;
}}
.controls input:focus-visible {{ outline: 2px solid var(--focus); outline-offset: 1px; }}
.controls .hint {{ font-size: 12px; color: var(--text-muted); }}
.tabs {{ display: flex; gap: 4px; padding: 0 28px; border-bottom: 1px solid var(--border); flex-wrap: wrap; background: var(--surface); }}
.tab {{
  background: transparent; border: none; color: var(--text-muted); padding: 13px 16px;
  cursor: pointer; font-size: 14px; font-weight: 600; font-family: inherit;
  border-bottom: 2px solid transparent; display: flex; align-items: center; gap: 7px;
}}
.tab:hover {{ color: var(--text); }}
.tab[aria-selected="true"] {{ color: var(--text); border-bottom-color: var(--accent); }}
.tab:focus-visible {{ outline: 2px solid var(--focus); outline-offset: -2px; }}
.badge {{
  background: var(--surface-alt); color: var(--text-muted); border: 1px solid var(--border);
  border-radius: 999px; padding: 1px 8px; font-size: 11px; font-family: "IBM Plex Mono", monospace;
}}
.tab[aria-selected="true"] .badge {{ color: var(--accent); border-color: var(--accent-soft); background: var(--accent-soft); }}
.tabpanel {{ padding: 20px 28px 44px; }}
.criteria {{ color: var(--text-muted); font-size: 13px; margin: 0 0 4px; }}
.count {{ font-size: 12px; color: var(--text-muted); margin: 0 0 14px; font-family: "IBM Plex Mono", monospace; }}
.count strong {{ color: var(--text); }}
.table-wrap {{ overflow-x: auto; border: 1px solid var(--border); border-radius: 10px; background: var(--surface); }}
table {{ border-collapse: collapse; width: 100%; min-width: 1180px; font-size: 13px; }}
thead th {{
  text-align: left; background: var(--surface-alt); color: var(--text-muted); font-weight: 600;
  font-size: 11px; letter-spacing: 0.04em; text-transform: uppercase;
  padding: 11px 14px; cursor: pointer; white-space: nowrap; position: sticky; top: 0;
  border-bottom: 1px solid var(--border); user-select: none;
}}
thead th.num {{ text-align: right; }}
thead th:hover {{ color: var(--text); }}
thead th:focus-visible {{ outline: 2px solid var(--focus); outline-offset: -2px; }}
tbody td {{ padding: 10px 14px; border-top: 1px solid var(--border); white-space: nowrap; font-variant-numeric: tabular-nums; }}
tbody td.num {{ text-align: right; font-family: "IBM Plex Mono", monospace; }}
tbody td.col-name {{ font-weight: 600; }}
tbody tr:hover {{ background: var(--surface-alt); }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.tag {{
  color: var(--text-muted); font-size: 9.5px; font-family: "IBM Plex Mono", monospace;
  border: 1px solid var(--border); border-radius: 4px; padding: 1px 4px; margin-left: 6px;
  text-transform: uppercase; letter-spacing: 0.04em;
}}
.rankpill {{
  display: inline-block; min-width: 26px; text-align: center; font-weight: 700;
  font-family: "IBM Plex Mono", monospace; border-radius: 6px; padding: 2px 7px; font-size: 12.5px;
}}
.rankpill.rank-hi {{ background: var(--good-soft); color: var(--good); }}
.rankpill.rank-mid {{ background: var(--mid-soft); color: var(--mid); }}
.rankpill.rank-lo {{ background: var(--lo-soft); color: var(--text-muted); }}
.pill {{ display: inline-flex; align-items: center; gap: 5px; font-size: 12.5px; color: var(--text-muted); }}
.pill .dot {{ width: 6px; height: 6px; border-radius: 50%; background: var(--border); display: inline-block; }}
.pill-yes .dot {{ background: var(--good); }}
.pill-yes {{ color: var(--text); }}
tr.hidden-by-filter {{ display: none; }}
footer {{ padding: 18px 28px 32px; color: var(--text-muted); font-size: 12px; }}
</style>
</head>
<body>
<header>
  <p class="eyebrow">Nexlev · Investigación de nichos</p>
  <h1>Radar Faceless</h1>
  <div class="meta mono">Generado {generated_at}<span class="sep">·</span>Ingresos siempre etiquetados como estimados</div>
</header>
<div class="controls">
  <div class="field">
    <label for="minRank">Ranking mínimo</label>
    <input type="number" id="minRank" min="1" max="10" value="1">
  </div>
  <span class="hint">Filtra las 4 pestañas a la vez · haz clic en una cabecera de columna para ordenar</span>
</div>
<div class="tabs" role="tablist">
{tabs}
</div>
{panels}
<footer class="mono">Datos vía Nexlev MCP (search_niche_finder_channels, get_channel_analytics, get_daily_analytics, check_faceless_channel, check_channel_monetization, get_channel_promotions) · Filtro estándar desde 2026-09-11: subs&lt;50.000, ordenado por índice de desproporción (outlier/subs) · RPM real y competencia via get_video_rpm / get_niche_overview cuando el paso de verificación los ha calculado</footer>
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
      var rankIdx = 11;
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
