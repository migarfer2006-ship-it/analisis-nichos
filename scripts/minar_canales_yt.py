#!/usr/bin/env python3
"""Mineria de canales pequenos con señal 5x. Salida: data/mineria_canales.json (clave en .env)."""
import json, sys, re, urllib.request, urllib.parse
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
KEY = dict(l.strip().split("=", 1) for l in open(ROOT / ".env") if "=" in l)["YOUTUBE_API_KEY"]
units = 0
def api(ep, **p):
    global units
    p["key"] = KEY
    try:
        with urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/{ep}?" + urllib.parse.urlencode(p), timeout=30) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        print("ERROR", e.code, e.read()[:200].decode().replace(KEY, "***"), units); sys.exit(1)
    units += 1; return d
def dur(s):
    h, m, se = (int(x or 0) for x in re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s).groups()); return h*60 + m + se/60
ideas = json.load(open(ROOT / "data" / "ideas_lugares.json"))["ideas"]
vids = {v["id"]: v for r in ideas.values() for v in r["videos"]}
# canales <60K con señal 5x; prioridad: Cronotierra y mayor ratio
cand = {}
for v in vids.values():
    if v["outlier5x"] and v["subs"] < 60000 and v["subs"] >= 1000:
        c = cand.setdefault(v["canal"].strip(), dict(subs=v["subs"], vid=v["id"], best=0))
        c["best"] = max(c["best"], v["vps"])
names = sorted(cand, key=lambda n: (n != "Cronotierra", -cand[n]["best"]))[:8]
vd = api("videos", part="snippet", id=",".join(cand[n]["vid"] for n in names))
now = datetime.now(timezone.utc); out = {"fecha": now.strftime("%Y-%m-%d"), "canales": []}
for it in vd["items"]:
    ch = api("channels", part="contentDetails,statistics", id=it["snippet"]["channelId"])["items"][0]
    subs = int(ch["statistics"]["subscriberCount"]); pl = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, tok = [], None
    for _ in range(2):
        p = dict(part="contentDetails", playlistId=pl, maxResults=50)
        if tok: p["pageToken"] = tok
        r = api("playlistItems", **p); ids += [x["contentDetails"]["videoId"] for x in r["items"]]
        tok = r.get("nextPageToken")
        if not tok: break
    vs = []
    for k in range(0, len(ids), 50):
        for v in api("videos", part="snippet,statistics,contentDetails", id=",".join(ids[k:k+50]))["items"]:
            pub = datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z", "+00:00")); views = int(v["statistics"].get("viewCount", 0))
            vs.append(dict(id=v["id"], titulo=v["snippet"]["title"], visitas=views, min=round(dur(v["contentDetails"]["duration"])), dias=max((now-pub).days, 1), vps=round(views/subs, 2)))
    vs.sort(key=lambda x: -x["vps"])
    out["canales"].append(dict(canal=it["snippet"]["channelTitle"], channel_id=it["snippet"]["channelId"], subs=subs, n_videos=len(vs), top=vs[:10]))
out["unidades"] = units
(ROOT / "data" / "mineria_canales.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print("OK", units, [c["canal"] for c in out["canales"]])
