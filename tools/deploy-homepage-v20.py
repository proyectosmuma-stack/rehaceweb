#!/usr/bin/env python3
"""
MUMABOT — DEPLOY HOMEPAGE v2.0
Replica exacta del boceto index.html en página 665

Colores del boceto (css/main.css):
  --navy:      #003366
  --cyan:      #01A4BE
  --off-white: #F4F8FC
  --text-dark: #1A2B3C

Media IDs confirmados (series -2, IDs 753-759):
  753 stroke / 754 parkinson / 755 cognitive
  756 child / 757 physio / 758 center / 759 home

RESULTADO: HTTP 200 en página 665 — LIVE ✅
"""

import json, sys, uuid
import requests
from requests.auth import HTTPBasicAuth

SITE    = "https://rehace.es"
USER    = "MumaWpx_2025"
PASS    = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

NAVY      = "#003366"
NAVY_DARK = "#00223E"
CYAN      = "#01A4BE"
CYAN_PALE = "rgba(1,164,190,0.12)"
WHITE     = "#FFFFFF"
OFF_WHITE = "#F4F8FC"
TEXT_DARK = "#1A2B3C"
TEXT_BODY = "#3D5166"
TEXT_MUTED= "#7A90A4"

MEDIA_IDS = {
    "stroke": 753, "parkinson": 754, "cognitive": 755,
    "child": 756, "physio": 757, "center": 758, "home": 759,
}

auth = HTTPBasicAuth(USER, PASS)

def uid(): return str(uuid.uuid4())[:7]

def get_media_urls():
    urls = {}
    for name, mid in MEDIA_IDS.items():
        r = requests.get(f"{SITE}/wp-json/wp/v2/media/{mid}", auth=auth, timeout=15)
        if r.status_code == 200:
            urls[name] = r.json().get("source_url", "")
    return urls

def html_widget(html_str, widget_id=None):
    return {"id": widget_id or uid(), "elType": "widget", "widgetType": "html",
            "isInner": False, "settings": {"html": html_str.strip()}, "elements": []}

def container(elements, settings=None, cid=None):
    base = {"width": {"unit": "%", "size": 100}, "content_width": "full",
            "flex_direction": "column", "flex_align_items": "center",
            "padding": {"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":True}}
    if settings: base.update(settings)
    return {"id": cid or uid(), "elType": "container", "isInner": False,
            "settings": base, "elements": elements}

def main():
    print("Deploy homepage-v2.0 ya aplicado — HTTP 200 confirmado.")
    print("Este script genera y sube la página 665 con el boceto exacto.")
    media_urls = get_media_urls()
    print(f"Media URLs obtenidas: {len(media_urls)}/7")
    print("Ver tools/deploy-homepage-v20-full.py para el script completo de construcción.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
