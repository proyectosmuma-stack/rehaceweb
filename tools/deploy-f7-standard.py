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

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) # Elementor usually 7-8 chars

def process_section(section):
    section['id'] = gen_id()
    for col in section.get('elements', []):
        col['id'] = gen_id()
        for widget in col.get('elements', []):
            widget['id'] = gen_id()
            # If inner section
            if widget.get('elType') == 'section':
                process_section(widget)
    return section

def deploy_phase_7_full():
    print("🎨 Generando IDs estándar para Hero + F6 + F7...")
    
    # 1. Hero
    with open("update-hero.py", "r") as f:
        # I'll just hardcode the hero here to be safe and clean
        hero_raw = {
            "id": gen_id(),
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
                "id": gen_id(),
                "elType": "column",
                "elements": [{
                    "id": gen_id(),
                    "elType": "section",
                    "isInner": True,
                    "settings": {"content_width": {"unit": "px", "size": 1280}},
                    "elements": [{
                        "id": gen_id(),
                        "elType": "column",
                        "settings": {"_column_size": 55},
                        "elements": [
                            {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.8rem;'><div style='width:40px;height:2px;background:#4ECDE4;'></div><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:700;font-size:14px;letter-spacing:2px;text-transform:uppercase;'>Rehabilitación Neurológica · Majadahonda</span></div>"}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Recupera tu <em style='color:#4ECDE4;font-style:normal;'>AUTONOMÍA</em><br>con el equipo que te entiende", "header_size": "h1", "typography_typography": "custom", "typography_font_family": "Outfit", "typography_font_weight": "900", "typography_font_size": {"unit": "rem", "size": 3.8}, "typography_line_height": {"unit": "em", "size": 1.1}, "title_color": "#ffffff", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 24, "left": 0}}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p>Tratamos a niños y adultos con lesiones neurológicas. Un enfoque médico, cercano y 100% personalizado para cada paciente y su familia.</p>", "typography_typography": "custom", "typography_font_family": "Figtree", "typography_font_size": {"unit": "rem", "size": 1.1}, "text_color": "rgba(255,255,255,0.82)", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 40, "left": 0}}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap;'><a href='#' class='btn-rehace-primary' style='background:#01A4BE;color:#fff;padding:1.1rem 2.5rem;border-radius:50px;font-family:\"Outfit\",sans-serif;font-weight:700;text-decoration:none;'>Solicitar Valoración Gratuita</a><a href='#' class='btn-rehace-outline' style='background:transparent;color:#fff;border:2px solid #fff;padding:1.1rem 2.5rem;border-radius:50px;font-family:\"Outfit\",sans-serif;font-weight:700;text-decoration:none;'>Ver especialidades →</a></div>"}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:3rem;margin-top:4rem;border-top:1px solid rgba(255,255,255,0.2);padding-top:2rem;'><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>+500</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Pacientes tratados</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>4</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Especialidades clínicas</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>10+</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Años de experiencia</span></div></div>"}}
                        ]
                    }]
                }]
            }]
        }

    # 2. Load F6 & F7 templates and randomize IDs
    with open("templates/fase_6_trust_cards.json", "r") as f:
        f6_list = json.load(f)
        f6 = [process_section(s) for s in f6_list]

    with open("templates/fase_7_especialidades.json", "r") as f:
        f7_list = json.load(f)
        f7 = [process_section(s) for s in f7_list]

    full_data = [hero_raw] + f6 + f7

    # 3. Inject
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    payload = {"meta": {"_elementor_data": json.dumps(full_data)}}
    
    resp = requests.post(url, auth=HTTPBasicAuth(USER, PASS), json=payload)
    
    if resp.status_code == 200:
        print(f"✅ Full Stack (Hero + F6 + F7) desplegado con IDs estándar.")
    else:
        print(f"❌ Error {resp.status_code}: {resp.text}")

if __name__ == "__main__":
    deploy_phase_7_full()
