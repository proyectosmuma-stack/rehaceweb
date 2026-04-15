import json, requests, random, string
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

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
                        {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap;'><a href='#cita' class='btn-rehace-primary' style='background:#01A4BE;color:#fff;padding:1.1rem 2.5rem;border-radius:4px;font-family:\"Figtree\",sans-serif;font-weight:600;text-decoration:none;'>Solicitar Valoración Gratuita</a><a href='#tratamos' class='btn-rehace-outline' style='border:1px solid rgba(255,255,255,0.3);color:#fff;padding:1.1rem 2.5rem;border-radius:4px;font-family:\"Figtree\",sans-serif;font-weight:600;text-decoration:none;'>Ver especialidades →</a></div>"}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "html", "settings": {"html": "<div style='display:flex;gap:3rem;margin-top:4rem;border-top:1px solid rgba(255,255,255,0.2);padding-top:2rem;'><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>+500</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Pacientes tratados</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>4</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Especialidades clínicas</span></div><div style='display:flex;flex-direction:column;'><span style='color:#fff;font-family:\"Outfit\",sans-serif;font-weight:900;font-size:2rem;'>10+</span><span style='color:rgba(255,255,255,0.7);font-family:\"Figtree\",sans-serif;font-size:14px;'>Años de experiencia</span></div></div>"}}
                    ]
                }]
            }]
        }]
    }

def main():
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    current_data = r.json().get("meta", {}).get("_elementor_data", "[]")
    if isinstance(current_data, str):
        current_data = json.loads(current_data)
        
    print(f"Total sections loaded from live: {len(current_data)}")
    
    # We find the Hero section index
    # In my v2 generated script, the sections were generated in order.
    # 0=CSS, 1=Topbar, 2=Header, 3=Hero. Let's look for the one with the text "Recupera tu"
    
    hero_index = -1
    for i, section in enumerate(current_data):
        s_str = json.dumps(section)
        if "Recupera tu" in s_str or "AUTONOM" in s_str:
            hero_index = i
            break
            
    if hero_index == -1:
        # Fallback to index 3 (the 4th element usually if full v2 applied)
        print("Warning: Hero text not found to replace exactly. Trying index 3.")
        hero_index = 3

    print(f"Reverting section at index {hero_index} with 16:00 Hero...")
    current_data[hero_index] = get_hero_data()
    
    # Push back
    resp = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "meta": {
            "_elementor_data": json.dumps(current_data),
            "_elementor_edit_mode": "builder"
        }
    })
    
    if resp.status_code == 200:
        print("✅ Restored Hero to 16:00 version successfully.")
    else:
        print(f"❌ Error {resp.status_code}: {resp.text}")

if __name__ == "__main__":
    main()
