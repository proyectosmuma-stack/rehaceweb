#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def restore_and_build_3_sections():
    print("🔄 Restaurando y construyendo las 3 secciones principales...")

    # 1. Definir Hero (Basado en el diseño harmonizado)
    hero_section = {
        "id": "hero-section-final",
        "elType": "section",
        "settings": {
            "background_background": "classic",
            "background_image": {"url": "https://rehace.es/wp-content/uploads/2026/04/hero_neuro_rehab_center.jpg"},
            "background_position": "center center",
            "background_size": "cover",
            "background_overlay_background": "gradient",
            "background_overlay_color": "rgba(0,34,62,0.88)",
            "background_overlay_color_b": "rgba(1,164,190,0.20)",
            "background_overlay_gradient_angle": {"unit": "deg", "size": 110},
            "height": "min-height",
            "custom_height": {"unit": "vh", "size": 92},
            "content_position": "middle",
            "padding": {"unit": "rem", "top": 7, "right": 0, "bottom": 9, "left": 0}
        },
        "elements": [{
            "id": "hero-column",
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [{
                "id": "hero-inner",
                "elType": "section",
                "isInner": True,
                "settings": {"content_width": {"unit": "px", "size": 1280}},
                "elements": [{
                    "id": "hero-content-col",
                    "elType": "column",
                    "settings": {"_column_size": 55},
                    "elements": [
                        {"id": "h-e", "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.8rem;'><div style='width:40px;height:2px;background:#4ECDE4;'></div><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:700;font-size:14px;letter-spacing:2px;text-transform:uppercase;'>Rehabilitación Neurológica · Majadahonda</span></div>"}},
                        {"id": "h-t", "elType": "widget", "widgetType": "heading", "settings": {"title": "Recupera tu <em style='color:#4ECDE4;font-style:normal;'>AUTONOMÍA</em><br>con el equipo que te entiende", "header_size": "h1", "typography_typography": "custom", "typography_font_family": "Outfit", "typography_font_weight": "900", "typography_font_size": {"unit": "rem", "size": 3.8}, "typography_line_height": {"unit": "em", "size": 1.1}, "title_color": "#ffffff", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 24, "left": 0}}},
                        {"id": "h-d", "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p>Tratamos a niños y adultos con lesiones neurológicas. Un enfoque médico, cercano y 100% personalizado para cada paciente y su familia.</p>", "typography_typography": "custom", "typography_font_family": "Figtree", "typography_font_size": {"unit": "rem", "size": 1.1}, "text_color": "rgba(255,255,255,0.82)", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 40, "left": 0}}},
                        {"id": "h-b", "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap;'><a href='#' class='btn-rehace-primary' style='background:#01A4BE;color:#fff;padding:1.1rem 2.5rem;border-radius:50px;font-family:\"Outfit\",sans-serif;font-weight:700;text-decoration:none;'>Solicitar Valoración Gratuita</a><a href='#' class='btn-rehace-outline' style='background:transparent;color:#fff;border:2px solid #fff;padding:1.1rem 2.5rem;border-radius:50px;font-family:\"Outfit\",sans-serif;font-weight:700;text-decoration:none;'>Ver especialidades →</a></div>"}},
                        {"id": "h-s", "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:3rem;margin-top:4rem;border-top:1px solid rgba(255,255,255,0.2);padding-top:2rem;'><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>+500</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Pacientes tratados</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>4</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Especialidades clínicas</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>10+</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Años de experiencia</span></div></div>"}}
                    ]
                }]
            }]
        }]
    }

    # 2. Load Fase 6
    with open("templates/fase_6_trust_cards.json", "r") as f:
        f6 = json.load(f)
    
    # 3. Load Fase 7
    with open("templates/fase_7_especialidades.json", "r") as f:
        f7 = json.load(f)

    # Combine all
    full_data = [hero_section] + f6 + f7

    # 4. Inyectar
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {
        "meta": {
            "_elementor_data": json.dumps(full_data)
        }
    }
    
    resp = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    
    if resp.status_code == 200:
        print(f"✅ Full Stack (Hero + F6 + F7) inyectado con éxito.")
    else:
        print(f"❌ Error: {resp.status_code}")
        print(resp.text)

if __name__ == "__main__":
    restore_and_build_3_sections()
