#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

# Configuración
SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
TEMPLATE_ID = 704

header_data = [
    {
        "id": "topbar-section",
        "elType": "section",
        "settings": {
            "background_background": "classic",
            "background_color": "#01A4BE",
            "padding": {"unit": "px", "top": 8, "right": 0, "bottom": 8, "left": 0}
        },
        "elements": [
            {
                "id": "topbar-row",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "topbar-inner-section",
                        "elType": "section",
                        "isInner": True,
                        "settings": {"content_width": {"unit": "px", "size": 1280}},
                        "elements": [
                            {
                                "id": "col-topbar-left",
                                "elType": "column",
                                "settings": {"_column_size": 50},
                                "elements": [
                                    {
                                        "id": "topbar-html-left",
                                        "elType": "widget",
                                        "widgetType": "html",
                                        "settings": {
                                            "html": "<div style=\"display:flex;gap:1.5rem;color:white;font-family:'Figtree', sans-serif;font-size:13px;align-items:center;\"><span><i class=\"fas fa-map-marker-alt\"></i> Majadahonda, Madrid</span><a href=\"mailto:info@rehace.es\" style=\"color:white;text-decoration:none;\"><i class=\"fas fa-envelope\"></i> info@rehace.es</a><span><i class=\"fas fa-star\"></i> Valoración inicial GRATUITA</span></div>"
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "col-topbar-right",
                                "elType": "column",
                                "settings": {"_column_size": 50},
                                "elements": [
                                    {
                                        "id": "topbar-html-right",
                                        "elType": "widget",
                                        "widgetType": "html",
                                        "settings": {
                                            "html": "<div style=\"display:flex;gap:1.5rem;color:white;font-family:'Figtree', sans-serif;font-size:13px;align-items:center;justify-content:flex-end;\"><span>L-V 9:00-20:00</span><a href=\"tel:915481732\" class=\"topbar-phone-pill\">915 481 732</a></div>"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "main-nav-section",
        "elType": "section",
        "settings": {
            "background_background": "classic",
            "background_color": "#ffffff",
            "sticky": "top",
            "z_index": 1000,
            "padding": {"unit": "px", "top": 10, "right": 32, "bottom": 10, "left": 32},
            "css_classes": "site-header-rehace"
        },
        "elements": [
            {
                "id": "nav-col-wrapper",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "nav-inner-section",
                        "elType": "section",
                        "isInner": True,
                        "settings": {"content_width": {"unit": "px", "size": 1280}},
                        "elements": [
                            {
                                "id": "col-logo",
                                "elType": "column",
                                "settings": {"_column_size": 20},
                                "elements": [
                                    {
                                        "id": "header-logo",
                                        "elType": "widget",
                                        "widgetType": "image",
                                        "settings": {
                                            "image": {
                                                "url": "https://rehace.es/wp-content/uploads/elementor/thumbs/logo-rehace-color-rcv0eee8zplo5nag58v86h0465dillryzgmzuhy9z4.png"
                                            },
                                            "image_custom_dimension": {"width": 150, "height": 52},
                                            "align": "left"
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "col-menu",
                                "elType": "column",
                                "settings": {"_column_size": 55},
                                "elements": [
                                    {
                                        "id": "header-menu",
                                        "elType": "widget",
                                        "widgetType": "nav-menu",
                                        "settings": {
                                            "layout": "horizontal",
                                            "align": "center",
                                            "typography_typography": "custom",
                                            "typography_font_family": "Outfit",
                                            "typography_font_weight": "500",
                                            "text_color_hover": "#01A4BE"
                                        }
                                    }
                                ]
                            },
                            {
                                "id": "col-cta",
                                "elType": "column",
                                "settings": {"_column_size": 25},
                                "elements": [
                                    {
                                        "id": "header-cta",
                                        "elType": "widget",
                                        "widgetType": "html",
                                        "settings": {
                                            "html": "<div style=\"display:flex;align-items:center;justify-content:flex-end;gap:1.5rem;\"><a href=\"tel:915481732\" style=\"color:#01A4BE;font-family:'Outfit', sans-serif;font-weight:700;text-decoration:none;\">915 481 732</a><a href=\"#\" class=\"btn-rehace-primary\" style=\"font-family:'Outfit',sans-serif;font-weight:700;font-size:14px;padding:12px 24px;background:#01A4BE;color:#fff;border-radius:50px;text-decoration:none;\">Pide cita</a></div>"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "scroll-script-section",
        "elType": "section",
        "settings": {},
        "elements": [
            {
                "id": "script-column",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": "header-script",
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": "<script>\nwindow.addEventListener('scroll', function() {\n  const header = document.querySelector('.site-header-rehace');\n  if (header) {\n    if (window.scrollY > 60) { header.classList.add('header-scrolled'); } \n    else { header.classList.remove('header-scrolled'); }\n  }\n});\n</script><style>\n.site-header-rehace { transition: box-shadow 0.3s ease; }\n.site-header-rehace.header-scrolled { box-shadow: 0 4px 24px rgba(0,51,102,.10) !important; }\n.topbar-phone-pill { background: white; color: #01A4BE; padding: 4px 14px; border-radius: 50px; font-weight: 700; font-size: 13px; text-decoration: none; }\n</style>"
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
        print(f"✅ Header actualizado exitosamente (ID: {TEMPLATE_ID})")
        print(f"   Fecha: {response.json().get('modified')}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_header()
