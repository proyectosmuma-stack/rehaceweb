#!/usr/bin/env python3
import os
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"

IMAGES = [
    "rehab_center_modern_1775656504951.png",
    "therapy_home_visit_1775659496678.png",
    "therapy_session_physio_1775656527885.png",
    "treatment_child_neuro_1775657348721.png",
    "treatment_cognitive.png",
    "treatment_parkinson.png",
    "treatment_stroke.png"
]

def upload_image(filename):
    url = f"{SITE}/wp-json/wp/v2/media"
    headers = {
        "Content-Disposition": f"attachment; filename={filename}",
        "Content-Type": "image/png"
    }
    with open(filename, "rb") as f:
        resp = requests.post(url, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=f)
    if resp.status_code in [200, 201]:
        data = resp.json()
        print(f"✅ Subido: {filename} -> {data['source_url']}")
        return data['source_url']
    else:
        print(f"❌ Error subiendo {filename}: {resp.status_code} {resp.text}")
        return None

if __name__ == "__main__":
    mapping = {}
    for img in IMAGES:
        if os.path.exists(img):
            url = upload_image(img)
            if url:
                mapping[img] = url
        else:
            print(f"⚠ Archivo no encontrado: {img}")
    
    with open("media_mapping.json", "w") as f:
        json.dump(mapping, f, indent=2)
    print("\nMapping guardado en media_mapping.json")
