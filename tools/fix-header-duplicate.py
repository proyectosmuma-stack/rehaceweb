import json, requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    # 1. Hide the theme's default header and footer to avoid duplicates
    # and make our custom header 100% width.
    # Also set page template to Elementor Canvas which is the cleanest way.
    
    print("🔧 Fixing header: eliminating duplicates and setting 100% width...")
    
    # Update Page Template to Elementor Canvas
    resp_tpl = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "template": "elementor_canvas"
    })
    
    if resp_tpl.status_code == 200:
        print("✅ Page template set to 'Elementor Canvas' (removes theme header/footer).")
    else:
        print(f"⚠️ Could not set template: {resp_tpl.status_code}")

    # 2. Fetch data to ensure our injected header is Full Width
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    data = r.json()
    meta = data.get("meta", {})
    el_data_str = meta.get("_elementor_data", "[]")
    el_data = json.loads(el_data_str)
    
    changed = False
    for section in el_data:
        # Looking for the topbar or header containers
        # My previous deploy used 'rh-v2-header' or similar logic
        s_str = json.dumps(section)
        if "site-header" in s_str or "topbar" in s_str:
            print(f"Updating container {section.get('id')} to Full Width...")
            section["settings"]["content_width"] = "full"
            section["settings"]["width"] = {"unit": "%", "size": 100}
            section["settings"]["gap"] = "no"
            changed = True
            
    # Inject Global CSS to ensure 100% width and clean up potential Astra conflicts
    css_fix = """
    <style>
    /* Force 100% width for our custom header containers */
    .elementor-section-filled, .elementor-section-full_width { width: 100% !important; left: 0 !important; }
    #site-header { width: 100% !important; max-width: 100% !important; }
    .topbar { width: 100% !important; }
    body.elementor-canvas .elementor-section.elementor-section-boxed > .elementor-container { max-width: 100% !important; width: 100% !important; }
    
    /* Ensure our sticky header works */
    .site-header { position: sticky; top: 0; z-index: 9999; background: #fff; width: 100% !important; }
    </style>
    """
    
    # We find the CSS section (index 0 usually in my v2 script)
    if el_data and el_data[0].get("id") == "rh-v2-css-section" or "style" in json.dumps(el_data[0]):
        el_data[0]["settings"]["html"] += css_fix
        changed = True

    if changed:
        resp = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
            "meta": {
                "_elementor_data": json.dumps(el_data)
            }
        })
        if resp.status_code == 200:
            print("✅ Elementor data updated with Full Width settings.")
        else:
            print(f"❌ Error updating data: {resp.status_code}")
    else:
        print("No header sections found to modify.")

if __name__ == "__main__":
    main()
