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

# URLs mapping including the ones we just uploaded
URLS = {
    "rehab_center_modern.png": "https://rehace.es/wp-content/uploads/2026/04/rehab_center_modern_1775656504951-1.jpg",
    "therapy_session_physio.png": "https://rehace.es/wp-content/uploads/2026/04/therapy_session_physio_1775656527885-1.jpg",
    "treatment_stroke.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_stroke-1.jpg",
    "treatment_parkinson.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_parkinson-1.jpg",
    "treatment_cognitive.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_cognitive-1.jpg",
    "treatment_child_neuro.png": "https://rehace.es/wp-content/uploads/2026/04/treatment_child_neuro_1775657348721-1.jpg"
}

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def process_content(content):
    if isinstance(content, str):
        for k, v in URLS.items():
            content = content.replace(f"https://rehace.es/wp-content/uploads/2026/04/{k}", v)
            content = content.replace(k, v)
        return content
    elif isinstance(content, list):
        return [process_content(i) for i in content]
    elif isinstance(content, dict):
        return {k: process_content(v) for k, v in content.items()}
    return content

def process_section(section):
    section['id'] = gen_id()
    for col in section.get('elements', []):
        col['id'] = gen_id()
        for widget in col.get('elements', []):
            widget['id'] = gen_id()
            if widget.get('elType') == 'section':
                process_section(widget)
            elif widget.get('settings'):
                widget['settings'] = process_content(widget['settings'])
    return section

def get_hero_data():
    return {
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
                    "settings": {"_column_size": 100},
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;align-items:center;gap:1rem;margin-bottom:1.8rem;'><div style='width:40px;height:2px;background:#4ECDE4;'></div><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:700;font-size:14px;letter-spacing:2px;text-transform:uppercase;'>Rehabilitación Neurológica · Majadahonda</span></div>"}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Recupera tu <em style='color:#4ECDE4;font-style:normal;'>AUTONOMÍA</em><br>con el equipo que te entiende", "header_size": "h1", "typography_typography": "custom", "typography_font_family": "Outfit", "typography_font_weight": "900", "typography_font_size": {"unit": "rem", "size": 3.8}, "typography_line_height": {"unit": "em", "size": 1.1}, "title_color": "#ffffff", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 24, "left": 0}}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p>Tratamos a niños y adultos con lesiones neurológicas. Un enfoque médico, cercano y 100% personalizado para cada paciente y su familia.</p>", "typography_typography": "custom", "typography_font_family": "Figtree", "typography_font_size": {"unit": "rem", "size": 1.1}, "text_color": "rgba(255,255,255,0.82)", "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 40, "left": 0}}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap;'><a href='#' class='btn-rehace-primary'>Solicitar Valoración Gratuita</a><a href='#' class='btn-rehace-outline'>Ver especialidades →</a></div>"}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:3rem;margin-top:4rem;border-top:1px solid rgba(255,255,255,0.2);padding-top:2rem;'><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>+500</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Pacientes tratados</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>4</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Especialidades clínicas</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>10+</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Años de experiencia</span></div></div>"}}
                    ]
                }]
            }]
        }]
    }

def deploy():
    print("🚀 Iniciando despliegue consolidado Ph 5-9...")
    
    sections_final = [process_section(get_hero_data())]
    
    templates = [
        "templates/fase_6_trust_cards.json",
        "templates/fase_7_especialidades.json",
        "templates/fase_8_por_que_elegir.json",
        "templates/fase_9_cuatro_pasos.json"
    ]
    
    for t_path in templates:
        with open(t_path, "r") as f:
            t_list = json.load(f)
            sections_final.extend([process_section(s) for s in t_list])
            
    final_payload = process_content(sections_final)
    
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    auth = HTTPBasicAuth(USER, PASS)
    
    resp = requests.post(url, auth=auth, json={
        "meta": {
            "_elementor_data": json.dumps(final_payload),
            "_elementor_edit_mode": "builder"
        }
    })
    
    if resp.status_code == 200:
        print("✅ Despliegue Ph 5-9 completado con éxito.")
        requests.post(url, auth=auth, json={"title": "Nueva Home - V9 Final Build"})
        requests.post(url, auth=auth, json={"title": "Nueva Home - Propuesta Diseño"})
    else:
        print(f"❌ Error: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    deploy()
