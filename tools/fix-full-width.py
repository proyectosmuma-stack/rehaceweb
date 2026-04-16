import json, requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🛠 Applying Full Width to ALL sections to ensure background coverage...")
    
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    el_data = json.loads(r.json().get("meta", {}).get("_elementor_data", "[]"))
    
    for section in el_data:
        if section.get("elType") == "section" or section.get("elType") == "container":
            print(f"Setting section {section.get('id')} to Full Width...")
            section["settings"]["content_width"] = "full"
            # Ensure no margins are boxing the section
            section["settings"]["margin"] = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
            
            # If it's the Topbar or Header, ensure zero padding as well
            if section.get("id") in ["rh-v2-topbar", "rh-v2-header"]:
                section["settings"]["padding"] = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}

    # Inject a robust CSS fix to override any theme containers
    css_override = """
    <style>
    :root { --content-max-width: 1280px; }
    
    /* Ensure the main container of Elementor Canvas occupies everything */
    #elementor-canvas #content { width: 100% !important; max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
    
    /* Force sections to stretch */
    .elementor-section.elementor-section-full_width {
        width: 100% !important;
        left: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    
    /* If content needs to be boxed inside a full-width section, 
       we'll handle it via the inner columns or a central wrapper CSS if needed,
       but for now, priority is background 100% */
    </style>
    """
    
    # Add CSS to the first section (usually my CSS block)
    if el_data and "settings" in el_data[0] and "html" in el_data[0]["settings"]:
        el_data[0]["settings"]["html"] += css_override
    elif el_data:
        # Fallback: traverse to find an HTML widget or add a new section
        found = False
        for s in el_data:
            for col in s.get("elements", []):
                for widget in col.get("elements", []):
                    if widget.get("widgetType") == "html":
                        widget["settings"]["html"] += css_override
                        found = True
                        break
                if found: break
            if found: break

    resp = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "meta": {
            "_elementor_data": json.dumps(el_data)
        }
    })
    
    if resp.status_code == 200:
        print("✅ ALL sections updated to Full Width.")
    else:
        print(f"❌ Error: {resp.status_code}")

if __name__ == "__main__":
    main()
