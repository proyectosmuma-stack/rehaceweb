#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def inject_phase(phase_id, file_path):
    print(f"🚀 Iniciando inyección de la Fase {phase_id}...")
    
    # 1. Fetch current data from the page to ensure we have the latest (including previous phases)
    url_get = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    resp_get = requests.get(url_get, auth=HTTPBasicAuth(USER, PASS))
    if resp_get.status_code != 200:
        print(f"❌ Error al obtener datos de la página: {resp_get.status_code}")
        return
    
    page_data = resp_get.json()
    elementor_data_json = page_data.get("meta", {}).get("_elementor_data", "[]")
    current_data = json.loads(elementor_data_json)

    # 2. Load Phase Template
    with open(file_path, "r") as f:
        phase_template = json.load(f)

    # 3. Clean existing if needed (using id from template)
    template_ids = [s.get("id") for s in phase_template if s.get("id")]
    unique_ids = list(set(template_ids))
    
    current_data = [s for s in current_data if s.get("id") not in unique_ids]

    # 4. Append
    current_data.extend(phase_template)

    # 5. POST back
    url_post = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {
        "meta": {
            "_elementor_data": json.dumps(current_data)
        }
    }
    
    resp_post = requests.post(
        url_post,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    
    if resp_post.status_code == 200:
        print(f"✅ FASE {phase_id} ({file_path}) inyectada con éxito.")
    else:
        print(f"❌ Error: {resp_post.status_code}")
        print(resp_post.text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python3 inject-phase.py <id> <file_path>")
    else:
        inject_phase(sys.argv[1], sys.argv[2])
