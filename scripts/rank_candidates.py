#!/usr/bin/env python3
"""
Filtra, deduplica y rankea los canales candidatos obtenidos de
search_niche_finder_channels (guardados en data/raw_candidates.json),
usando los umbrales y pesos de config.json.

No llama a ninguna API. Produce data/selected_pre_verification.json con
los canales finalistas por seccion, listos para la fase de verificacion
(get_daily_analytics + get_channel_promotions) que si requiere llamadas MCP.
"""
import json
import statistics
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.now(timezone.utc)

CATEGORY_BUCKETS = {
    "high": {
        "personal finance", "investing", "cryptocurrency", "health", "medicine",
        "mental health", "healthcare industry", "insurance",
        "court cases & legal proceedings", "real estate", "nutrition",
        "men's health", "woman's health", "weight loss", "alternative medicine",
        "longevity", "reproductive health", "conditions and diseases",
    },
    "medium_high": {
        "tech", "tech gadgets", "business", "programming", "online business",
        "artificial intelligence", "software", "data science", "engineering",
        "computers", "robotics", "e-commerce", "small business",
        "retail business", "affiliate marketing", "hacking", "virtual reality",
        "automotive business", "aerospace business", "ev car business",
        "major companies",
    },
    "medium": {
        "history", "crime", "horror stories", "myths and folktales", "paranormal",
        "space & exploration", "science", "police bodycam", "crime interrogations",
        "disaster stories", "disaster and accidents", "urban legends", "folklore",
        "investigative documentaries", "investigative journalism", "life stories",
        "reddit stories", "scifi stories", "society", "culture", "psychology",
        "philosophy", "royalty", "celebrity", "pop news & gossip",
        "movie star news & gossip", "news", "geo politics", "politics",
        "usa politics", "military", "aviation", "wildlife", "biology",
        "earth sciences", "physics", "chemistry", "math",
        "anomalies and alternative science", "environment", "weather",
    },
}

RPM_BUCKET_KEY = {
    "high": "finanzas_legal_seguros_salud",
    "medium_high": "tecnologia_negocios",
    "medium": "entretenimiento_historia_curiosidades",
    "low": "otros",
}


def category_bucket(cat_name: str) -> str:
    cat_name = (cat_name or "").lower()
    for bucket, names in CATEGORY_BUCKETS.items():
        if cat_name in names:
            return bucket
    return "low"


def days_since(date_str: str) -> int:
    d = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return max((TODAY - d).days, 0)


def sustained_vph(videos: list) -> float:
    """VPH medio de hasta 5 videos recientes, recortando el maximo (evita picos)."""
    vphs = []
    for v in videos[:6]:
        try:
            upload = datetime.fromisoformat(v["video_upload_date"].replace("Z", "+00:00"))
        except Exception:
            continue
        hours = max((TODAY - upload).total_seconds() / 3600.0, 1.0)
        if hours < 20:
            continue  # muy reciente, VPH poco fiable
        vphs.append(v.get("video_view_count", 0) / hours)
    if not vphs:
        return 0.0
    if len(vphs) >= 4:
        vphs.sort()
        vphs = vphs[:-1]  # descarta el pico mas alto
    return statistics.mean(vphs)


def upload_consistency(videos: list) -> float:
    """Menor desviacion entre subidas = mas consistente. Devuelve score crudo (dias std, menor=mejor)."""
    dates = []
    for v in videos:
        try:
            dates.append(datetime.fromisoformat(v["video_upload_date"].replace("Z", "+00:00")))
        except Exception:
            continue
    dates.sort()
    if len(dates) < 3:
        return 999.0  # penaliza datos insuficientes
    gaps = [(dates[i + 1] - dates[i]).total_seconds() / 86400.0 for i in range(len(dates) - 1)]
    if len(gaps) < 2:
        return 999.0
    return statistics.pstdev(gaps)


def normalize(values: list) -> list:
    """Min-max a 0-10. Si todos iguales, devuelve 5 para todos."""
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi - lo < 1e-9:
        return [5.0 for _ in values]
    return [10.0 * (v - lo) / (hi - lo) for v in values]


def build_record(ch: dict, section_criteria: dict) -> dict:
    stats = ch["stats"]
    days = days_since(ch["channelCreationDate"])
    subs = max(stats.get("subscribers", 0), 1)
    views30 = stats.get("monthlyViews", 0)
    ratio = views30 / subs
    vph = sustained_vph(ch.get("lastUploadedVideos", []))
    consistency_raw = upload_consistency(ch.get("lastUploadedVideos", []))
    bucket = category_bucket(ch.get("category", {}).get("name", ""))
    rpm_key = RPM_BUCKET_KEY[bucket]

    return {
        "channel_id": ch["ytChannelId"],
        "name": ch["title"],
        "url": f"https://www.youtube.com/channel/{ch['ytChannelId']}",
        "days_since_creation": days,
        "views_30d": views30,
        "subscribers": stats.get("subscribers", 0),
        "category_bucket": rpm_key,
        "rpm_category_raw": ch.get("category", {}).get("name", ""),
        "is_monetized": bool(ch.get("isMonetizationEnabled")),
        "is_faceless": bool(ch.get("isFaceless")),
        "is_ai_channel": bool(ch.get("isAiChannel")),
        "avg_video_duration_min": round(stats.get("avgVideoLength", 0) / 60, 1),
        "upload_cadence_per_week": stats.get("uploadsPerWeek", 0),
        "vph_recent_avg": round(vph, 1),
        "upload_consistency_raw_days_std": round(consistency_raw, 2),
        "views_subscribers_ratio": round(ratio, 2),
        "quality": ch.get("quality"),
        "outlier_score": ch.get("outlierScore"),
        "nexlev_monthly_revenue_reported": stats.get("monthlyRevenue"),
        "nexlev_rpm_total": stats.get("rpm", {}).get("total"),
    }


def apply_hard_filters(records: list, criteria: dict) -> list:
    out = []
    for r in records:
        if "video_duration_min_minutes" in criteria and r["avg_video_duration_min"] < criteria["video_duration_min_minutes"]:
            continue
        if "video_duration_max_minutes" in criteria and r["avg_video_duration_min"] > criteria["video_duration_max_minutes"]:
            continue
        if "views_last_30_days_min" in criteria and r["views_30d"] < criteria["views_last_30_days_min"]:
            continue
        if "views_per_month_min" in criteria and r["views_30d"] < criteria["views_per_month_min"]:
            continue
        if "channel_age_max_days" in criteria and r["days_since_creation"] > criteria["channel_age_max_days"]:
            continue
        if "channel_age_min_days" in criteria and r["days_since_creation"] < criteria["channel_age_min_days"]:
            continue
        if criteria.get("requires_ai_signals") and not (r["is_ai_channel"] or r["upload_cadence_per_week"] >= 5):
            continue
        out.append(r)
    return out


def rank_section(records: list, weights: dict) -> list:
    if not records:
        return records
    ratio_n = normalize([r["views_subscribers_ratio"] for r in records])
    vph_n = normalize([r["vph_recent_avg"] for r in records])
    # consistency: menor std = mejor -> invertimos
    std_vals = [r["upload_consistency_raw_days_std"] for r in records]
    cons_n_raw = normalize(std_vals)
    cons_n = [10.0 - v for v in cons_n_raw]
    rev_mid = [(r.get("_rev_min", 0) + r.get("_rev_max", 0)) / 2 for r in records]
    rev_n = normalize(rev_mid)

    for i, r in enumerate(records):
        score = (
            ratio_n[i] * weights["views_subscribers_ratio"]
            + vph_n[i] * weights["sustained_vph_last_5_10_videos"]
            + cons_n[i] * weights["upload_consistency"]
            + rev_n[i] * weights["estimated_revenue"]
        )
        r["ranking"] = max(1, min(10, round(score)))
        r["_ranking_components"] = {
            "views_subs_ratio_norm": round(ratio_n[i], 2),
            "vph_norm": round(vph_n[i], 2),
            "consistency_norm": round(cons_n[i], 2),
            "revenue_norm": round(rev_n[i], 2),
        }
    records.sort(key=lambda r: r["ranking"], reverse=True)
    return records


def apply_revenue(records: list, rpm_table: dict):
    for r in records:
        rpm = rpm_table[r["category_bucket"]]
        views = r["views_30d"]
        r["est_revenue_min_usd"] = round(views / 1000 * rpm["min"])
        r["est_revenue_max_usd"] = round(views / 1000 * rpm["max"])
        r["_rev_min"] = r["est_revenue_min_usd"]
        r["_rev_max"] = r["est_revenue_max_usd"]


def main():
    config = json.loads((ROOT / "config.json").read_text())
    raw = json.loads((ROOT / "data" / "raw_candidates.json").read_text())
    weights = config["ranking_weights"]
    rpm_table = config["rpm_table_usd_per_1000_views"]
    target = config["target_channels_per_section"]

    section_cfg = {s["id"]: s for s in config["sections"]}
    priority = config["dedup_priority_order"]

    used_ids = set()
    selected = {}
    stats_report = {}

    for sid in priority:
        crit = section_cfg[sid]["criteria"]
        raw_channels = raw.get(sid, [])
        records = [build_record(ch, crit) for ch in raw_channels]
        filtered = apply_hard_filters(records, crit)
        apply_revenue(filtered, rpm_table)
        ranked = rank_section(filtered, weights)
        deduped = [r for r in ranked if r["channel_id"] not in used_ids]
        chosen = deduped[:target]
        for r in chosen:
            used_ids.add(r["channel_id"])
            r.pop("_rev_min", None)
            r.pop("_rev_max", None)
        selected[sid] = chosen
        stats_report[sid] = {
            "raw_candidates": len(raw_channels),
            "passed_filters": len(filtered),
            "available_after_dedup": len(deduped),
            "selected": len(chosen),
        }

    (ROOT / "data" / "selected_pre_verification.json").write_text(
        json.dumps({"sections": selected}, indent=2, ensure_ascii=False)
    )
    print(json.dumps(stats_report, indent=2))


if __name__ == "__main__":
    main()
