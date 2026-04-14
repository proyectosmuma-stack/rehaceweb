#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def update_hero_with_user_widgets():
    # 1. Load the current state to preserve user widgets (IDs and types)
    with open("current_elementor_data.json", "r") as f:
        data = json.load(f)

    # 2. Re-structure the logic: we want to keep the 1280px wrapper and section settings
    # but refine the widgets inside 'b198446' (the hero content column)
    
    # Hero content column found at data[0] -> elements[0] -> elements[0] -> elements[0]
    # Let's target it safely
    try:
        content_column = data[0]["elements"][0]["elements"][0]["elements"][0]
        # Remove the old HTML buttons widget (743531e) if it exists
        content_column["elements"] = [el for el in content_column["elements"] if el.get("id") != "743531e"]
        
        # Now style the user's native widgets to be brand-compliant
        for el in content_column["elements"]:
            # Style the eyebrow heading (171b4ca)
            if el.get("id") == "171b4ca":
                # Ensure it has the correct margin and style
                el["settings"]["_margin"] = {"unit": "px", "top": 0, "right": 0, "bottom": 28, "left": 0}
            
            # Style the main H1 (b58dd15)
            if el.get("id") == "b58dd15":
                el["settings"]["typography_font_size"] = {"unit": "rem", "size": 3.8}
                el["settings"]["typography_line_height"] = {"unit": "em", "size": 1.1}
            
            # Style the flexbox container for buttons (97c887b)
            if el.get("id") == "97c887b":
                el["settings"] = {
                    "flex_direction": "row",
                    "flex_gap": {"size": 24, "unit": "px"},
                    "flex_wrap": "wrap",
                    "flex_align_items": "center",
                    "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 40, "left": 0}
                }
                # Style the buttons inside the flexbox
                for btn in el.get("elements", []):
                    if btn.get("id") == "2465aab": # Solicitar Valoración
                        btn["widgetType"] = "button" # Ensure standard button for easier styling if e-button is tricky
                        btn["settings"] = {
                            "text": "Solicitar Valoración Gratuita",
                            "button_type": "success",
                            "typography_typography": "custom",
                            "typography_font_family": "Outfit",
                            "typography_font_weight": "700",
                            "background_color": "#01A4BE",
                            "color": "#FFFFFF",
                            "border_radius": {"unit": "px", "top": 50, "right": 50, "bottom": 50, "left": 50},
                            "typography_font_size": {"unit": "px", "size": 17},
                            "padding": {"unit": "px", "top": 16, "right": 35, "bottom": 16, "left": 35}
                        }
                    if btn.get("id") == "65b8e0b": # Ver especialidades
                        btn["widgetType"] = "button"
                        btn["settings"] = {
                            "text": "Ver especialidades →",
                            "typography_typography": "custom",
                            "typography_font_family": "Outfit",
                            "typography_font_weight": "700",
                            "background_color": "transparent",
                            "color": "#FFFFFF",
                            "border_border": "solid",
                            "border_width": {"unit": "px", "top": 2, "right": 2, "bottom": 2, "left": 2},
                            "border_color": "rgba(255,255,255,0.6)",
                            "border_radius": {"unit": "px", "top": 50, "right": 50, "bottom": 50, "left": 50},
                            "typography_font_size": {"unit": "px", "size": 17},
                            "padding": {"unit": "px", "top": 16, "right": 35, "bottom": 16, "left": 35}
                        }

        # Also, let's fix the section background and overlay properly in settings
        main_section = data[0]
        main_section["settings"].update({
            "background_background": "classic",
            "background_image": {"url": "https://rehace.es/wp-content/uploads/2026/04/hero_neuro_rehab_center.jpg"},
            "background_position": "center 30%",
            "background_size": "cover",
            "background_overlay_background": "gradient",
            "background_overlay_color": "#00223EED",
            "background_overlay_color_b": "rgba(1,164,190,0.20)",
            "background_overlay_gradient_angle": {"unit": "deg", "size": 110},
            "height": "min-height",
            "custom_height": {"unit": "vh", "size": 92}
        })

    except Exception as e:
        print(f"❌ Error logic in restructuring: {e}")
        return

    # 3. Inject back
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {
        "meta": {
            "_elementor_data": json.dumps(data)
        }
    }
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    
    if response.status_code == 200:
        print(f"✅ Hero Section armonizada con botones nativos (Page ID: {PAGE_ID})")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_hero_with_user_widgets()
