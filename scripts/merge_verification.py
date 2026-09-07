#!/usr/bin/env python3
"""
Fusiona data/selected_pre_verification.json (filtrado+rankeado, sin llamadas API)
con data/verification_promotions.json (resultado real de get_channel_promotions
para cada canal finalista) y produce data/latest.json, el snapshot final que
build_dashboard.py consume.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    selected = json.loads((ROOT / "data" / "selected_pre_verification.json").read_text())
    promos = json.loads((ROOT / "data" / "verification_promotions.json").read_text())

    for sid, channels in selected["sections"].items():
        for ch in channels:
            p = promos.get(ch["channel_id"], {"scraped": False})
            ch["promotions_data_scraped"] = p.get("scraped", False)
            external = bool(p.get("sells")) or (p.get("sponsorCount", 0) or 0) > 0 or (p.get("selfPromoCount", 0) or 0) > 0
            ch["external_monetization_signals"] = external if p.get("scraped") else False
            ch["nexlev_estimated_revenue_per_month"] = p.get("estRevPerMonth")
            # limpieza de campos internos de ranking no necesarios en el HTML
            ch.pop("_ranking_components", None)

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sections": selected["sections"],
    }
    (ROOT / "data" / "latest.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print("data/latest.json escrito con", sum(len(v) for v in out["sections"].values()), "canales")


if __name__ == "__main__":
    main()
