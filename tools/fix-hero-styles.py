#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

# Fase 5: Hero Section JSON Structure but with explicit INLINE CSS since Elementor compiler is bypassed 
hero_data = [
    {
        "id": "hero-section",
        "elType": "section",
        "settings": {},
        "elements": [
            {
                "id": "hero-row",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "hero-inner-section",
                        "elType": "section",
                        "isInner": True,
                        "settings": {},
                        "elements": [
                            {
                                "id": "col-hero-content",
                                "elType": "column",
                                "settings": {"_column_size": 100},
                                "elements": [
                                    {
                                        "id": "hero-raw-html-styles",
                                        "elType": "widget",
                                        "widgetType": "html",
                                        "settings": {
                                            "html": """
<style>
/* Forzando estilos ya que el compilador de Elementor se salta al inyectar por API */
.hero-rehace-container {
    background-image: linear-gradient(110deg, rgba(0,34,62,0.88) 0%, rgba(1,164,190,0.20) 100%), url('https://rehace.es/wp-content/uploads/2026/04/hero_neuro_rehab_center.jpg');
    background-size: cover;
    background-position: center 30%;
    min-height: 92vh;
    display: flex;
    align-items: center;
    padding: 7rem 20px 9rem;
    width: 100%;
}
.hero-rehace-wrapper {
    max-width: 1280px;
    width: 100%;
    margin: 0 auto;
}
.hero-rehace-col {
    width: 55%;
}
@media (max-width: 1024px) {
    .hero-rehace-col { width: 80%; }
}
@media (max-width: 768px) {
    .hero-rehace-col { width: 100%; }
    .hero-rehace-container { min-height: 70vh; padding: 5rem 20px; }
    .hero-stats-bar { justify-content: space-between; }
}

.hero-eyebrow-line { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.8rem; }
.hero-eyebrow-line::before { content: ''; flex: 0 0 40px; height: 1.5px; background: #01A4BE; }
.hero-eyebrow-text { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: .78rem; letter-spacing: .18em; text-transform: uppercase; color: #4ECDE4; }

.hero-title-rehace { color: #ffffff; font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 3.8rem; line-height: 1.1; margin-bottom: 24px; text-transform: uppercase; }
.hero-desc-rehace { color: rgba(255,255,255,0.82); font-family: 'Figtree', sans-serif; font-size: 1.1rem; line-height: 1.6; margin-bottom: 40px; }

.hero-stats-bar { display: flex; gap: 2.5rem; flex-wrap: wrap; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.15); margin-top: 4rem; }
.hero-stats-bar .stat-num { font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 2rem; color: #fff; display: block; }
.hero-stats-bar .stat-lbl { font-size: 14px; color: rgba(255,255,255,0.7); font-family: 'Figtree', sans-serif; }
</style>

<div class="hero-rehace-container">
    <div class="hero-rehace-wrapper">
        <div class="hero-rehace-col">
            <div class="hero-eyebrow-line">
                <span class="hero-eyebrow-text">Rehabilitación Neurológica · Majadahonda</span>
            </div>
            
            <h1 class="hero-title-rehace">Recupera tu <em style='color:#4ECDE4;font-style:normal'>AUTONOMÍA</em><br>con el equipo que te entiende</h1>
            
            <p class="hero-desc-rehace">Tratamos a niños y adultos con lesiones neurológicas. Un enfoque médico, cercano y 100% personalizado para cada paciente y su familia.</p>
            
            <div style="display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap;">
                <a href="#" class="btn-rehace-primary">Solicitar Valoración Gratuita</a>
                <a href="#" class="btn-rehace-outline">Ver especialidades →</a>
            </div>
            
            <div class="hero-stats-bar">
                <div class="stat"><span class="stat-num">+500</span><span class="stat-lbl">Pacientes tratados</span></div>
                <div class="stat"><span class="stat-num">4</span><span class="stat-lbl">Especialidades</span></div>
                <div class="stat"><span class="stat-num">10+</span><span class="stat-lbl">Años de exp.</span></div>
            </div>
        </div>
    </div>
</div>
                                            """
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

def update_hero():
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    
    data = json.dumps({
        "meta": {
            "_elementor_data": json.dumps(hero_data)
        }
    })
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=data
    )
    
    if response.status_code == 200:
        print(f"✅ Hero Section COMPLETAMENTE renderizada con CSS (Page ID: {PAGE_ID})")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_hero()
