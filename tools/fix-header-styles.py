#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
TEMPLATE_ID = 704

header_data = [
    {
        "id": "topbar-section",
        "elType": "section",
        "settings": {},
        "elements": [
            {
                "id": "topbar-row",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                         "id": "topbar-html",
                         "elType": "widget",
                         "widgetType": "html",
                         "settings": {
                             "html": """
<style>
.topbar-rehace {
    background: #01A4BE;
    padding: 8px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    font-family: 'Figtree', sans-serif;
    font-size: 13px;
    width: 100%;
}
.topbar-left { display: flex; gap: 1.5rem; align-items: center; }
.topbar-right { display: flex; gap: 1.5rem; align-items: center; justify-content: flex-end; }
.topbar-phone-pill { background: white; color: #01A4BE; padding: 4px 14px; border-radius: 50px; font-weight: 700; text-decoration: none; }
@media (max-width: 768px) { .topbar-rehace { flex-direction: column; gap: 10px; text-align: center; } .topbar-left, .topbar-right { justify-content: center; flex-wrap: wrap; } }
</style>
<div class="topbar-rehace">
    <div class="topbar-left">
        <span><i class="fas fa-map-marker-alt"></i> Majadahonda, Madrid</span>
        <a href="mailto:info@rehace.es" style="color:white;text-decoration:none;"><i class="fas fa-envelope"></i> info@rehace.es</a>
        <span><i class="fas fa-star"></i> Valoración inicial GRATUITA</span>
    </div>
    <div class="topbar-right">
        <span>L-V 9:00-20:00</span>
        <a href="tel:915481732" class="topbar-phone-pill">915 481 732</a>
    </div>
</div>
                             """
                         }
                    }
                ]
            }
        ]
    },
    {
        "id": "main-nav-section",
        "elType": "section",
        "settings": {},
        "elements": [
            {
                "id": "nav-col-wrapper",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "nav-html",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": """
<style>
.site-header-rehace {
    background: #ffffff;
    padding: 10px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-sizing: border-box;
    width: 100%;
    transition: box-shadow 0.3s ease;
}
.site-header-rehace.header-scrolled { box-shadow: 0 4px 24px rgba(0,51,102,.10) !important; }
.header-logo img { height: 52px; width: auto; display: block; }
.header-menu {
    display: flex;
    gap: 2rem;
    list-style: none;
    margin: 0;
    padding: 0;
}
.header-menu li a {
    color: #2D3D52;
    text-decoration: none;
    font-family: 'Outfit', sans-serif;
    font-weight: 500;
    font-size: 16px;
    transition: color 0.3s ease;
}
.header-menu li a:hover { color: #01A4BE; }
.header-cta-wrapper {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
@media (max-width: 1024px) {
    .header-menu { display: none; } /* En móvil se necesita un menú nativo, aquí lo ocultamos por seguridad visual */
    .header-cta-wrapper { display: none; }
}
</style>
<div class="site-header-rehace" id="site-header-custom">
    <div class="header-logo">
        <a href="https://rehace.es"><img src="https://rehace.es/wp-content/uploads/elementor/thumbs/logo-rehace-color-rcv0eee8zplo5nag58v86h0465dillryzgmzuhy9z4.png" alt="Rehace"></a>
    </div>
    <ul class="header-menu">
        <li><a href="#">¿Qué tratamos?</a></li>
        <li><a href="#">¿Cómo lo hacemos?</a></li>
        <li><a href="#">¿Quiénes somos?</a></li>
        <li><a href="#">A domicilio</a></li>
    </ul>
    <div class="header-cta-wrapper">
        <a href="tel:915481732" style="color:#01A4BE;font-family:'Outfit', sans-serif;font-weight:700;text-decoration:none;">915 481 732</a>
        <a href="#" class="btn-rehace-primary">Pide cita</a>
    </div>
</div>
<script>
window.addEventListener('scroll', function() {
  const header = document.getElementById('site-header-custom');
  if (header) {
    if (window.scrollY > 60) { header.classList.add('header-scrolled'); } 
    else { header.classList.remove('header-scrolled'); }
  }
});
</script>
                            """
                        }
                    }
                ]
            }
        ]
    }
]

def update_header():
    url = f"{SITE}/wp-json/wp/v2/elementor_library/{TEMPLATE_ID}"
    
    data = json.dumps({
        "meta": {
            "_elementor_data": json.dumps(header_data)
        }
    })
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=data
    )
    
    if response.status_code == 200:
        print(f"✅ Header COMPLETAMENTE renderizado con CSS (ID: {TEMPLATE_ID})")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_header()
