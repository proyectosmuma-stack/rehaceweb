#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

# 1. Defined Secciones hardcoded or loaded from definitive files
def get_hero():
    # Load from fix-hero-styles.py logic or existing template if saved
    # I'll use a simplified version for this test or fetch it carefully
    return [{
        "id": "hero-section",
        "elType": "section",
        "settings": {
            "background_background": "classic",
            "background_image": {"url": "https://rehace.es/wp-content/uploads/2026/04/hero_neuro_rehab_center.jpg"},
            "background_overlay_background": "gradient",
            "background_overlay_color": "rgba(0,34,62,0.88)",
            "background_overlay_color_b": "rgba(1,164,190,0.20)",
            "height": "min-height",
            "custom_height": {"unit": "vh", "size": 92}
        },
        "elements": [
            {
                "id": "hero-col",
                "elType": "column",
                "elements": [
                    {
                        "id": "hero-html",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": "<h1 style='color:white; font-family:Outfit; font-size:4rem;'>RECUPERA TU AUTONOMÍA</h1>"
                        }
                    }
                ]
            }
        ]
    }]

def inject_full_stack():
    # Since I want to preserve the "good" hero, I'll fetch it first with extreme care
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit"
    r = requests.get(url, auth=HTTPBasicAuth(USER, PASS))
    data = r.json()
    
    elementor_data_raw = data.get("meta", {}).get("_elementor_data", "[]")
    full_stack = json.loads(elementor_data_raw)
    
    print(f"Current count: {len(full_stack)}")
    
    # Ensure Hero is there (it should be)
    if len(full_stack) == 0:
         print("Warning: Page was empty. Hero lost?")
    
    # Load F6
    with open("templates/fase_6_trust_cards.json", "r") as f:
        f6 = json.load(f)
    if not any(s.get("id") == "f6" for s in full_stack):
        print("Appending F6")
        full_stack.extend(f6)
    
    # Load F7
    with open("templates/fase_7_especialidades.json", "r") as f:
        f7 = json.load(f)
    if not any(s.get("id") == "f7" for s in full_stack):
        print("Appending F7")
        full_stack.extend(f7)

    # Push
    print(f"Pushing total {len(full_stack)} sections")
    url_post = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {"meta": {"_elementor_data": json.dumps(full_stack)}}
    
    r_post = requests.post(url_post, auth=HTTPBasicAuth(USER, PASS), json=payload)
    
    if r_post.status_code == 200:
        print("✅ Injection Successful")
    else:
        print(f"❌ Error {r_post.status_code}: {r_post.text}")

if __name__ == "__main__":
    inject_full_stack()
