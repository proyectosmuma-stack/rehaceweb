#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def inject_phase_6():
    # 1. Load Current Page Data (already has Hero)
    with open("current_elementor_data.json", "r") as f:
        current_data = json.load(f)

    # 2. Load Phase 6 Template
    with open("templates/fase_6_trust_cards.json", "r") as f:
        fase_6_template = json.load(f) # This is a list with one section

    # 3. Check if f6 is already there to avoid duplicates
    if any(section.get("id") == "f6" or section.get("id") == "trust-cards-section" for section in current_data):
        print("⚠️ Fase 6 ya parece estar en la página. Sobrescribiendo...")
        current_data = [s for s in current_data if s.get("id") not in ["f6", "trust-cards-section"]]

    # 4. Append
    current_data.extend(fase_6_template)

    # 5. POST back to WP
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {
        "meta": {
            "_elementor_data": json.dumps(current_data)
        }
    }
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    
    if response.status_code == 200:
        print(f"✅ FASE 6 (Trust Cards) inyectada con éxito en la página {PAGE_ID}.")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    inject_phase_6()
