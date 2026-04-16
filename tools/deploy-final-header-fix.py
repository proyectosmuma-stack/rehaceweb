import json, requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🚀 Applying FIX 1, 2 & 3: Header 100% Width & Dual Conflict Resolution...")
    
    # FIX 3: Ensure Page Template is Elementor Canvas
    requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={"template": "elementor_canvas"})
    
    # Fetch current data
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    el_data = json.loads(r.json().get("meta", {}).get("_elementor_data", "[]"))
    
    # FIX 1: Elementor Section Configuration
    for section in el_data:
        s_id = section.get("id", "")
        if s_id in ["rh-v2-topbar", "rh-v2-header"] or "topbar" in s_id or "header" in str(section):
            print(f"Applying Elementor settings to section {s_id}...")
            section["settings"]["content_width"] = "full"
            section["settings"]["stretch_section"] = "section_stretched"
            section["settings"]["gap"] = "no"
            section["settings"]["padding"] = {"unit": "px", "top": "0", "right": "32", "bottom": "0", "left": "32", "isLinked": False}

    # FIX 2: CSS Adicional provided by USER
    custom_css = """
/* ── HEADER 100% ANCHO – FIX COMPLETO ── */

/* Elimina el max-width que Astra pone al header */
.site-header .ast-container,
.site-header .ast-flex,
#ast-fixed-header .ast-container,
header.site-header > .ast-container {
  max-width: 100% !important;
  width: 100% !important;
  padding-left: 32px !important;
  padding-right: 32px !important;
}

/* La sección Elementor del header también a 100% */
.elementor-section.elementor-section-stretched,
.elementor-section[data-settings*="stretch_section"] {
  left: 0 !important;
  width: 100% !important;
}

/* TopBar a 100% */
.topbar,
.elementor-top-bar,
.e-con.topbar-section {
  width: 100% !important;
  max-width: 100% !important;
  left: 0 !important;
  right: 0 !important;
}

/* Evita que Astra añada margen lateral automático */
.ast-page-builder-template .hfb-header,
.elementor-template-canvas .site-header {
  width: 100% !important;
  max-width: none !important;
}
"""
    
    # Inject CSS into the first section if it's our CSS section, or create a new header widget
    # Usually el_data[0] is rh-v2-css-section
    css_found = False
    for section in el_data:
        if section.get("id") == "rh-v2-css-section":
            for col in section.get("elements", []):
                for widget in col.get("elements", []):
                    if widget.get("widgetType") == "html":
                        widget["settings"]["html"] = f"<style>{custom_css}</style>\n" + widget["settings"]["html"]
                        css_found = True
                        break
                if css_found: break
            if css_found: break

    # Update Page
    resp = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "meta": {
            "_elementor_data": json.dumps(el_data)
        }
    })
    
    if resp.status_code == 200:
        print("✅ Header fix (Elementor + CSS + Canvas) applied successfully.")
    else:
        print(f"❌ Error: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    main()
