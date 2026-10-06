#!/usr/bin/env python3
"""Ronda 2 Clave Biblica: calibracion + busquedas por dificultad. Salida: data/clave_biblica_r2.json"""
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
MUSIC = re.compile(r"adoraci|worship|alabanza|m[uú]sica|cantad|c[aá]ntico|canci[oó]n|bachata|jazz|himno|cumbia|reggae|gospel|salmos poderosos|oraci[oó]n de la ma|oraci[oó]n poderosa de la ma|morning prayer|oração|ora[cç][aã]o|terço|instrumental|lofi|piano", re.I)
PT = re.compile(r"\b(você|não|deus|senhor|até quando|oração|ouça|porque deus|igreja|palavra para)\b", re.I)
ES_OK = re.compile(r"\b(dios|por qu[eé]|el|la|los|las|de|que|qu[eé]|en|tu|sigo|cansad|explicad)\b", re.I)
def es(it):
    l = (it["snippet"].get("defaultAudioLanguage") or it["snippet"].get("defaultLanguage") or "").lower()
    if l: return l.startswith("es")
    return bool(ES_OK.search(it["snippet"]["title"])) and not PT.search(it["snippet"]["title"])
now = datetime.now(timezone.utc)
def run(q, days, n=50):
    after = (now - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    s = api("search", part="snippet", q=q, type="video", order="viewCount", publishedAfter=after, videoDuration="long", relevanceLanguage="es", maxResults=n)
    ids = [x["id"]["videoId"] for x in s.get("items", [])]
    if not ids: return []
    v = {it["id"]: it for it in api("videos", part="snippet,statistics,contentDetails", id=",".join(ids))["items"]}
    chids = sorted({it["snippet"]["channelId"] for it in v.values()})
    subs = {}
    for k in range(0, len(chids), 50):
        for x in api("channels", part="statistics", id=",".join(chids[k:k+50]))["items"]:
            subs[x["id"]] = None if x["statistics"].get("hiddenSubscriberCount") else int(x["statistics"]["subscriberCount"])
    out = []
    for pos, i in enumerate(ids, 1):
        it = v.get(i)
        if not it: continue
        pub = datetime.fromisoformat(it["snippet"]["publishedAt"].replace("Z", "+00:00")); views = int(it["statistics"].get("viewCount", 0)); sb = subs.get(it["snippet"]["channelId"])
        out.append(dict(pos=pos, id=i, titulo=it["snippet"]["title"], canal=it["snippet"]["channelTitle"], subs=sb, visitas=views, dias=max((now-pub).days, 1), min=round(dur(it["contentDetails"]["duration"])),
            musica=bool(MUSIC.search(it["snippet"]["title"])), es=es(it), vps=round(views/sb, 2) if sb else None, outlier5x=bool(sb is not None and sb < 50000 and views > 5*sb)))
    return out
res = {"fecha": now.strftime("%Y-%m-%d"), "calibracion": {}, "busquedas": {}}
for q, key in (("Habacuc explicado -música -alabanza -canción", "habacuc"), ("Gálatas 5:16 explicado -música -alabanza -canción", "galatas")):
    res["calibracion"][q] = run(q, 730)
Q = ["por qué Dios guarda silencio", "Dios no responde mis oraciones explicado", "por qué sigo cansado aunque oro", "cansancio espiritual Biblia explicado", "dónde está Dios cuando sufro",
     "Dios cerca del quebrantado de corazón explicado", "Habacuc explicado", "Mateo 11:28 explicado", "Salmo 34 explicado", "Salmo 13 explicado"]
for q in Q: res["busquedas"][q] = run(q + " -música -alabanza -canción", 365)
res["unidades"] = units
(ROOT / "data" / "clave_biblica_r2.json").write_text(json.dumps(res, ensure_ascii=False, indent=1)); print("OK", units)
