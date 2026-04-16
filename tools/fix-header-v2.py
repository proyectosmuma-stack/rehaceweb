import json, requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🚀 Fixing header and removing duplicates (Elementor Canvas)...")
    
    # 1. Force Elementor Canvas Template (Removes Astra Header/Footer)
    requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={"template": "elementor_canvas"})
    
    # 2. Fetch and modify existing sections
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    el_data = json.loads(r.json().get("meta", {}).get("_elementor_data", "[]"))
    
    for section in el_data:
        s_id = section.get("id", "")
        # Apply full width to specific header containers
        if s_id in ["rh-v2-topbar", "rh-v2-header", "rh-v2-css-section"]:
            section["settings"]["content_width"] = "full"
            section["settings"]["width"] = {"unit": "%", "size": 100}
            if "padding" in section["settings"]:
                section["settings"]["padding"] = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}

    # 3. Update the page
    resp = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "meta": {
            "_elementor_data": json.dumps(el_data)
        }
    })
    
    if resp.status_code == 200:
        print("✅ Header is now 100% width and Astra headers are removed.")
    else:
        print(f"❌ Error: {resp.status_code}")

if __name__ == "__main__":
    main()
