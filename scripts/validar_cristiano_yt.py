#!/usr/bin/env python3
"""Validacion de 3 ideas del canal cristiano con YouTube Data API. Salida: data/ideas_cristiano.json"""
import json, sys, re, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
KEY = dict(l.strip().split("=", 1) for l in open(ROOT / ".env") if "=" in l)["YOUTUBE_API_KEY"]
units = 0
def api(ep, **p):
    global units
    p["key"] = KEY
    try:
        with urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/{ep}?" + urllib.parse.urlencode(p), timeout=30) as r: d = json.load(r)
    except urllib.error.HTTPError as e:
        print("ERROR", e.code, e.read()[:200].decode().replace(KEY, "***"), units); sys.exit(1)
    units += 100 if ep == "search" else 1; return d
def dur(s):
    h, m, se = (int(x or 0) for x in re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s).groups()); return h*60 + m + se/60
Q = {1: ["hablar en lenguas es para todos los cristianos", "don de lenguas Espíritu Santo"],
     2: ["cómo saber si es Dios o eres tú voz del Espíritu Santo", "reconocer la voz de Dios Espíritu Santo"],
     3: ["Espíritu Santo intercede cuando no sabes qué orar Romanos 8:26", "Romanos 8:26 Espíritu Santo ora por nosotros"]}
now = datetime.now(timezone.utc); after = (now - timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")
out = {"fecha": now.strftime("%Y-%m-%d"), "ideas": {}}
for i, qs in Q.items():
    vs = {}
    for q in qs:
        s = api("search", part="snippet", q=q, type="video", order="viewCount", publishedAfter=after, videoDuration="long", relevanceLanguage="es", maxResults=15)
        ids = [x["id"]["videoId"] for x in s.get("items", [])]
        if not ids: continue
        v = api("videos", part="snippet,statistics,contentDetails", id=",".join(ids))
        c = api("channels", part="statistics", id=",".join(sorted({x["snippet"]["channelId"] for x in v["items"]})))
        subs = {x["id"]: (None if x["statistics"].get("hiddenSubscriberCount") else int(x["statistics"]["subscriberCount"])) for x in c["items"]}
        for it in v["items"]:
            pub = datetime.fromisoformat(it["snippet"]["publishedAt"].replace("Z", "+00:00")); views = int(it["statistics"].get("viewCount", 0)); sb = subs.get(it["snippet"]["channelId"])
            vs[it["id"]] = dict(id=it["id"], titulo=it["snippet"]["title"], canal=it["snippet"]["channelTitle"], subs=sb, visitas=views, dias=max((now-pub).days, 1), min=round(dur(it["contentDetails"]["duration"])),
                lang=it["snippet"].get("defaultAudioLanguage"), vps=round(views/sb, 2) if sb else None, outlier5x=bool(sb is not None and sb < 50000 and views > 5*sb))
    out["ideas"][i] = sorted(vs.values(), key=lambda x: -x["visitas"])
out["unidades"] = units
(ROOT / "data" / "ideas_cristiano.json").write_text(json.dumps(out, ensure_ascii=False, indent=1)); print("OK", units)
