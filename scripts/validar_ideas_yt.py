#!/usr/bin/env python3
"""Validacion de ideas con YouTube Data API v3 (clave en .env). Salida: data/ideas_lugares.json"""
import json, sys, urllib.request, urllib.parse, re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = dict(l.strip().split("=", 1) for l in open(ROOT / ".env") if "=" in l)["YOUTUBE_API_KEY"]
units = 0

def api(ep, **p):
    global units
    p["key"] = KEY
    url = f"https://www.googleapis.com/youtube/v3/{ep}?" + urllib.parse.urlencode(p)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        print("ERROR", e.code, e.read()[:300].decode().replace(KEY, "***"), "unidades:", units); sys.exit(1)
    units += 100 if ep == "search" else 1
    return d

def dur(s):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s)
    h, mi, se = (int(x or 0) for x in m.groups()); return h*60 + mi + se/60

IDEAS = {
 1: ("Nueva Guinea / Foja / mundo perdido", "selva Nueva Guinea Montañas Foja mundo perdido", "New Guinea Foja mountains lost world jungle"),
 2: ("Lago Vostok", "Lago Vostok Antártida", "Lake Vostok Antarctica"),
 3: ("Hang Sơn Đoòng", "cueva Hang Son Doong", "Hang Son Doong cave"),
 4: ("Darién / Panamericana", "Darién Carretera Panamericana", "Darien Gap Pan-American Highway"),
 5: ("Cráter Batagaika", "cráter Batagaika", "Batagaika crater"),
 6: ("Danakil / Dallol", "Danakil Dallol", "Danakil Depression Dallol"),
 7: ("Fosa de las Marianas", "Fosa de las Marianas Challenger", "Mariana Trench Challenger Deep"),
 8: ("Tepuyes / mundo perdido", "tepuyes Venezuela El mundo perdido", "tepui lost world Venezuela"),
 9: ("Pozo de Kola", "Pozo de Kola", "Kola Superdeep Borehole"),
 10: ("Isla Sentinel del Norte", "isla Sentinel del Norte", "North Sentinel Island"),
}
after = (datetime.now(timezone.utc) - timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")
now = datetime.now(timezone.utc)
out = {"fecha": now.strftime("%Y-%m-%d"), "ideas": {}}
for i, (name, qes, qen) in IDEAS.items():
    res = {"nombre": name, "videos": []}
    for lang, q in (("es", qes), ("en", qen)):
        kw = dict(part="snippet", q=q, type="video", order="viewCount", publishedAfter=after, videoDuration="long", maxResults=10)
        if lang == "es": kw.update(relevanceLanguage="es")
        s = api("search", **kw)
        ids = [it["id"]["videoId"] for it in s.get("items", [])]
        if not ids: continue
        v = api("videos", part="snippet,statistics,contentDetails", id=",".join(ids))
        chids = sorted({it["snippet"]["channelId"] for it in v["items"]})
        c = api("channels", part="statistics", id=",".join(chids))
        subs = {x["id"]: (None if x["statistics"].get("hiddenSubscriberCount") else int(x["statistics"]["subscriberCount"])) for x in c["items"]}
        for it in v["items"]:
            pub = datetime.fromisoformat(it["snippet"]["publishedAt"].replace("Z", "+00:00"))
            views = int(it["statistics"].get("viewCount", 0)); sb = subs.get(it["snippet"]["channelId"])
            days = max((now - pub).days, 1)
            res["videos"].append(dict(id=it["id"], titulo=it["snippet"]["title"], canal=it["snippet"]["channelTitle"], idioma_busqueda=lang,
                subs=sb, visitas=views, dias=days, min=round(dur(it["contentDetails"]["duration"])),
                vps=round(views/sb, 2) if sb else None, vpd=round(views/days),
                outlier5x=bool(sb is not None and sb < 50000 and views > 5*sb)))
    seen = {}
    for x in res["videos"]: seen[x["id"]] = x
    res["videos"] = sorted(seen.values(), key=lambda x: -x["visitas"])
    out["ideas"][i] = res
out["unidades"] = units
(ROOT / "data" / "ideas_lugares.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print("OK unidades", units)
