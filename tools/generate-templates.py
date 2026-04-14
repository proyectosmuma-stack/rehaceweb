#!/usr/bin/env python3
import json
import os

TEMPLATES_DIR = "templates"

def save_template(name, data):
    filename = os.path.join(TEMPLATES_DIR, f"{name}.json")
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Template guardado: {filename}")

# --- FASE 6: TRUST CARDS ---
fase_6_data = [
    {
        "id": "trust-cards-section",
        "elType": "section",
        "settings": {
            "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 64, "left": 0},
            "background_background": "classic",
            "background_color": "#FFFFFF"
        },
        "elements": [
            {
                "id": "trust-cards-column",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "trust-cards-html",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": """
<style>
.trust-grid-rehace {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    max-width: 1280px;
    margin: -50px auto 0; /* Solapamiento negativo para que se vea premium */
    background: white;
    border-radius: 12px;
    box-shadow: 0 12px 48px rgba(0,51,102,0.12);
    overflow: hidden;
    position: relative;
    z-index: 10;
}
.trust-col-rehace {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 1rem;
    padding: 3rem 1.5rem;
    border-right: 1px solid #E8EEF5;
    transition: background 0.3s ease;
}
.trust-col-rehace:last-child { border-right: none; }
.trust-col-rehace:hover { background: #F4F7FB; }
.trust-icon-wrap {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: rgba(1,164,190,0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #01A4BE;
    font-size: 1.5rem;
}
.trust-col-rehace h3 {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: #003366;
    margin: 0;
}
.trust-col-rehace p {
    font-family: 'Figtree', sans-serif;
    font-size: 0.9rem;
    color: #6B7E96;
    margin: 0;
    line-height: 1.5;
}
@media (max-width: 1024px) {
    .trust-grid-rehace { grid-template-columns: repeat(2, 1fr); margin-top: 2rem; }
    .trust-col-rehace:nth-child(2) { border-right: none; }
    .trust-col-rehace { border-bottom: 1px solid #E8EEF5; }
}
@media (max-width: 600px) {
    .trust-grid-rehace { grid-template-columns: 1fr; }
    .trust-col-rehace { border-right: none; }
}
</style>
<div class="trust-grid-rehace">
    <div class="trust-col-rehace">
        <div class="trust-icon-wrap"><i class="fas fa-brain"></i></div>
        <h3>Especialidad Neuro</h3>
        <p>Expertos en daño cerebral, ictus y parkinson.</p>
    </div>
    <div class="trust-col-rehace">
        <div class="trust-icon-wrap"><i class="fas fa-house-user"></i></div>
        <h3>Centro y Domicilio</h3>
        <p>Nos adaptamos a tu comodidad y necesidad real.</p>
    </div>
    <div class="trust-col-rehace">
        <div class="trust-icon-wrap"><i class="fas fa-hand-holding-medical"></i></div>
        <h3>Valoración Gratuita</h3>
        <p>Ven a conocernos y evaluaremos tu caso sin compromiso.</p>
    </div>
    <div class="trust-col-rehace">
        <div class="trust-icon-wrap"><i class="fas fa-users"></i></div>
        <h3>Apoyo Integral</h3>
        <p>Acompañamos al paciente y a toda su familia.</p>
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

# --- FASE 7: ESPECIALIDADES ---
fase_7_data = [
    {
        "id": "specialties-section",
        "elType": "section",
        "settings": {
            "padding": {"unit": "px", "top": 100, "right": 0, "bottom": 100, "left": 0},
            "background_background": "classic",
            "background_color": "#F4F7FB"
        },
        "elements": [
            {
                "id": "specialties-col",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "specialties-header-html",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": """
<div style="text-align:center; max-width: 800px; margin: 0 auto 4rem;">
    <span class="hero-eyebrow-text">Especialidades</span>
    <h2 style="font-family:'Outfit', sans-serif; font-weight:900; font-size:3rem; color:#003366; margin-top:1rem; text-transform:uppercase;">¿Qué tratamos en REHACE?</h2>
    <p style="font-family:'Figtree', sans-serif; font-size:1.1rem; color:#6B7E96; line-height:1.7;">Disponemos de equipos especializados para el tratamiento del daño cerebral y patologías neurodegenerativas en todas las etapas de la vida.</p>
</div>
                            """
                        }
                    },
                    {
                        "id": "specialties-grid-html",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": """
<style>
.specialties-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    max-width: 1280px;
    margin: 0 auto;
}
.spec-card {
    background: white; border-radius: 12px; overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,51,102,0.06); border: 1px solid #E8EEF5;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}
.spec-card:hover { transform: translateY(-8px); box-shadow: 0 20px 48px rgba(0,51,102,0.12); }
.spec-img { width: 100%; height: 200px; background: #eee; background-size: cover; background-position: center; }
.spec-content { padding: 1.5rem; }
.spec-tag { font-family:'Outfit', sans-serif; font-size:0.7rem; font-weight:700; color:#01A4BE; text-transform:uppercase; letter-spacing:0.1em; display:block; margin-bottom:0.5rem; }
.spec-content h3 { font-family:'Outfit', sans-serif; font-weight:800; font-size:1.2rem; color:#003366; margin:0; line-height:1.3; }
</style>
<div class="specialties-grid">
    <div class="spec-card">
        <div class="spec-img" style="background-image:url('https://rehace.es/wp-content/uploads/2026/04/treatment_stroke.png')"></div>
        <div class="spec-content">
            <span class="spec-tag">Neurología</span>
            <h3>Ictus y Daño Cerebral Adquirido</h3>
        </div>
    </div>
    <div class="spec-card">
        <div class="spec-img" style="background-image:url('https://rehace.es/wp-content/uploads/2026/04/treatment_parkinson.png')"></div>
        <div class="spec-content">
            <span class="spec-tag">Neurología</span>
            <h3>Parkinson y Trastornos de Movimiento</h3>
        </div>
    </div>
    <div class="spec-card">
        <div class="spec-img" style="background-image:url('https://rehace.es/wp-content/uploads/2026/04/treatment_cognitive.png')"></div>
        <div class="spec-content">
            <span class="spec-tag">Neuropsicología</span>
            <h3>Alzheimer y Demencias</h3>
        </div>
    </div>
    <div class="spec-card">
        <div class="spec-img" style="background-image:url('https://rehace.es/wp-content/uploads/2026/04/therapy_session_physio.png')"></div>
        <div class="spec-content">
            <span class="spec-tag">Fisioterapia</span>
            <h3>Esclerosis Múltiple</h3>
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

if __name__ == "__main__":
    save_template("fase_6_trust_cards", fase_6_data)
    save_template("fase_7_especialidades", fase_7_data)
