#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def rebuild_all():
    # Sections to include in order
    phases = [
        # "templates/fase_5_hero.json", # Hero (I'll use the harmonized version logic)
        "templates/fase_6_trust_cards.json",
        "templates/fase_7_especialidades.json"
    ]
    
    # 1. Start with the harmonized Hero (I need to get it from the page or a file)
    # Actually, I'll just fetch whatever is on the page right now and ensure F6 and F7 are appended correctly.
    
    url_get = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit" # context=edit to be sure
    resp_get = requests.get(url_get, auth=HTTPBasicAuth(USER, PASS))
    current_page = resp_get.json()
    
    # Get current sections
    elementor_data_raw = current_page.get("meta", {}).get("_elementor_data", "[]")
    full_data = json.loads(elementor_data_raw)
    
    print(f"DEBUG: Current sections count: {len(full_data)}")
    
    # 2. Add Phase 6 (Trust Cards) if missing
    with open("templates/fase_6_trust_cards.json", "r") as f:
        f6 = json.load(f)
    if not any(s.get("id") == "f6" for s in full_data):
        print("Adding Phase 6...")
        full_data.extend(f6)
    
    # 3. Add Phase 7 (Specialties)
    with open("templates/fase_7_especialidades.json", "r") as f:
        f7 = json.load(f)
    if not any(s.get("id") == "f7" for s in full_data):
        print("Adding Phase 7...")
        full_data.extend(f7)

    # 4. Push back
    url_post = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {
        "meta": {
            "_elementor_data": json.dumps(full_data)
        }
    }
    
    resp_post = requests.post(
        url_post,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    
    if resp_post.status_code == 200:
        print(f"✅ Rebuild completo inyectado. Total secciones: {len(full_data)}")
    else:
        print(f"❌ Error: {resp_post.status_code}")
        print(resp_post.text)

if __name__ == "__main__":
    rebuild_all()
