#!/usr/bin/env python3
import json
import random
import string
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

# Live asset URLs
URLS = {
    "rehab_center_modern.png": "https://rehace.es/wp-content/uploads/2026/04/rehab_center_modern_1775656504951-1.jpg",
    "therapy_session_physio.png": "https://rehace.es/wp-content/uploads/2026/04/therapy_session_physio_1775656527885-1.jpg",
    "treatment_stroke.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_stroke-1.jpg",
    "treatment_parkinson.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_parkinson-1.jpg",
    "treatment_cognitive.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_cognitive-1.jpg",
    "treatment_child_neuro.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_child_neuro_1775657348721-1.jpg",
    "hero_neuro_rehab_center.jpg": "https://rehace.es/wp-content/uploads/2026/04/hero_neuro_rehab_center.jpg"
}

def gen_id(): return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def process_live_urls(content):
    if isinstance(content, str):
        for k, v in URLS.items(): content = content.replace(f"https://rehace.es/wp-content/uploads/2026/04/{k}", v).replace(k, v)
        return content
    elif isinstance(content, list): return [process_live_urls(i) for i in content]
    elif isinstance(content, dict): return {k: process_live_urls(v) for k, v in content.items()}
    return content

def process_ids(section):
    """Recursively update IDs and settings for new sections (Ph 6-9)"""
    section['id'] = gen_id()
    for col in section.get('elements', []):
        col['id'] = gen_id()
        for widget in col.get('elements', []):
            widget['id'] = gen_id()
            if widget.get('elType') == 'section' or widget.get('elType') == 'container': process_ids(widget)
            elif widget.get('settings'): widget['settings'] = process_live_urls(widget['settings'])
    return section

def harmonize_hero_container(hero):
    """Apply the brand styling to the user's native container-based Hero"""
    try:
        def apply_styles(elements):
            if not isinstance(elements, list): return
            for el in elements:
                if not isinstance(el, dict): continue
                settings = el.get("settings", {})
                if not isinstance(settings, dict): settings = {}
                
                # Main Heading (b58dd15)
                if el.get("id") == "b58dd15":
                    settings.update({"typography_font_family": "Outfit", "typography_font_weight": "900", "typography_font_size": {"unit": "rem", "size": 3.8}, "typography_line_height": {"unit": "em", "size": 1.1}, "title_color": "#ffffff"})
                # Flexbox buttons (97c887b)
                if el.get("id") == "97c887b":
                    settings.update({"flex_direction": "row", "flex_gap": {"size": 24, "unit": "px"}, "flex_wrap": "wrap", "flex_align_items": "center"})
                    for btn in el.get("elements", []):
                        if not isinstance(btn, dict): continue
                        b_settings = btn.get("settings", {})
                        if not isinstance(b_settings, dict): b_settings = {}
                        if btn.get("id") == "2465aab": # Primary button
                            b_settings.update({"typography_font_family": "Outfit", "typography_font_weight": "700", "background_color": "#01A4BE", "color": "#FFFFFF", "border_radius": {"unit": "px", "top": 50, "right": 50, "bottom": 50, "left": 50}})
                        if btn.get("id") == "65b8e0b": # Outline button
                            b_settings.update({"typography_font_family": "Outfit", "typography_font_weight": "700", "background_color": "transparent", "color": "#FFFFFF", "border_border": "solid", "border_width": {"unit": "px", "top": 2, "right": 2, "bottom": 2, "left": 2}, "border_color": "rgba(255,255,255,0.6)", "border_radius": {"unit": "px", "top": 50, "right": 50, "bottom": 50, "left": 50}})
                        btn["settings"] = b_settings
                
                el["settings"] = settings
                if "elements" in el: apply_styles(el["elements"])

        apply_styles(hero.get("elements", []))
        # Ensure section background is correct
        h_settings = hero.get("settings", {})
        if isinstance(h_settings, dict):
            h_settings.update({
                "background_image": {"url": URLS["hero_neuro_rehab_center.jpg"]},
                "background_overlay_background": "gradient",
                "background_overlay_color": "#00223EED",
                "background_overlay_color_b": "rgba(1,164,190,0.20)",
                "background_overlay_gradient_angle": {"unit": "deg", "size": 110}
            })
            hero["settings"] = h_settings
    except Exception as e: print(f"⚠️ Warning during harmonization: {e}")
    return hero

def run_fix():
    print("🛠️ Restaurando el Hero original (Contenedores) y combinando con Fases 6-9...")
    
    # 1. Load User's Hero (The one they edited in the builder)
    with open("current_elementor_data.json", "r") as f:
        user_hero_list = json.load(f)
        user_hero = harmonize_hero_container(user_hero_list[0])
    
    # 2. Load the additional phases
    phases = ["templates/fase_6_trust_cards.json", "templates/fase_7_especialidades.json", "templates/fase_8_por_que_elegir.json", "templates/fase_9_cuatro_pasos.json"]
    additional_sections = []
    for p in phases:
        with open(p, "r") as f:
            sections = json.load(f)
            additional_sections.extend([process_ids(s) for s in sections])
    
    # 3. Combine
    final_data = [user_hero] + additional_sections
    
    # 4. Inject
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    auth = HTTPBasicAuth(USER, PASS)
    requests.post(url, auth=auth, json={"meta": {"_elementor_data": json.dumps(final_data), "_elementor_edit_mode": "builder"}})
    requests.post(url, auth=auth, json={"title": "Nueva Home - Fixed Hero Clash"})
    requests.post(url, auth=auth, json={"title": "Nueva Home - Propuesta Diseño"})
    print("✅ Stack restaurado. El Hero ahora usa los Contenedores nativos del usuario.")

if __name__ == "__main__": run_fix()
