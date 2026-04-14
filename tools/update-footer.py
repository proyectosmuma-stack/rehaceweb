#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

# Configuración
SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
TEMPLATE_ID = 698

# JSON completo del footer para Elementor
footer_data = [
    {
        "id": "main-section",
        "elType": "section",
        "settings": {
            "content_width": {"unit": "px", "size": 1280},
            "background_background": "classic",
            "background_color": "#00203D",
            "padding": {"unit": "px", "top": 80, "right": 32, "bottom": 0, "left": 32},
            "padding_mobile": {"unit": "px", "top": 50, "right": 20, "bottom": 0, "left": 20}
        },
        "elements": [
            {
                "id": "main-row",
                "elType": "row",
                "settings": {},
                "elements": [
                    # Columna 1: Brand
                    {
                        "id": "col-brand",
                        "elType": "column",
                        "settings": {
                            "_column_size": 25,
                            "padding": {"unit": "px", "top": 0, "right": 40, "bottom": 50, "left": 0},
                            "padding_mobile": {"unit": "px", "top": 0, "right": 0, "bottom": 30, "left": 0}
                        },
                        "elements": [
                            {
                                "id": "logo-widget",
                                "elType": "widget",
                                "widgetType": "image",
                                "settings": {
                                    "image": {
                                        "url": "https://rehace.es/wp-content/uploads/elementor/thumbs/logo-rehace-color-rcv0eee8zplo5nag58v86h0465dillryzgmzuhy9z4.png"
                                    },
                                    "image_size": "custom",
                                    "image_custom_dimension": {"width": 150, "height": 50},
                                    "align": "left",
                                    "space": {"unit": "px", "size": 20}
                                }
                            },
                            {
                                "id": "desc-widget",
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": "<p>Centro especializado en rehabilitación neurológica en Majadahonda, Madrid. Nace desde la pasión y la experiencia familiar para devolverte la libertad.</p>",
                                    "align": "left",
                                    "text_color": "rgba(255,255,255,0.5)",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "typography_line_height": {"unit": "em", "size": 1.75}
                                }
                            },
                            {
                                "id": "social-icons",
                                "elType": "widget",
                                "widgetType": "social-icons",
                                "settings": {
                                    "social_icon_list": [
                                        {
                                            "social_icon": {"value": "fab fa-facebook-f", "library": "fa-brands"},
                                            "text": "Facebook"
                                        },
                                        {
                                            "social_icon": {"value": "fab fa-instagram", "library": "fa-brands"},
                                            "text": "Instagram"
                                        },
                                        {
                                            "social_icon": {"value": "fab fa-youtube", "library": "fa-brands"},
                                            "text": "YouTube"
                                        },
                                        {
                                            "social_icon": {"value": "fab fa-linkedin-in", "library": "fa-brands"},
                                            "text": "LinkedIn"
                                        }
                                    ],
                                    "icon_color": "custom",
                                    "icon_primary_color": "rgba(255,255,255,0.55)",
                                    "icon_secondary_color": "transparent",
                                    "icon_size": {"unit": "px", "size": 14},
                                    "icon_spacing": {"unit": "px", "size": 10},
                                    "icon_border_radius": {"unit": "%", "size": 50},
                                    "icon_border_border": "solid",
                                    "icon_border_width": {"unit": "px", "top": 1, "right": 1, "bottom": 1, "left": 1},
                                    "icon_border_color": "rgba(255,255,255,0.18)",
                                    "hover_color": "#01A4BE",
                                    "hover_primary_color": "#01A4BE",
                                    "hover_border_color": "#01A4BE"
                                }
                            }
                        ]
                    },
                    # Columna 2: Especialidades
                    {
                        "id": "col-services",
                        "elType": "column",
                        "settings": {
                            "_column_size": 20,
                            "padding": {"unit": "px", "top": 0, "right": 20, "bottom": 50, "left": 20},
                            "padding_mobile": {"unit": "px", "top": 0, "right": 0, "bottom": 30, "left": 0}
                        },
                        "elements": [
                            {
                                "id": "services-title",
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Especialidades",
                                    "header_size": "h4",
                                    "align": "left",
                                    "title_color": "#FFFFFF",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Outfit",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "typography_font_weight": "700",
                                    "typography_letter_spacing": {"unit": "px", "size": 0.6},
                                    "text_transform": "uppercase"
                                }
                            },
                            {
                                "id": "services-list",
                                "elType": "widget",
                                "widgetType": "icon-list",
                                "settings": {
                                    "icon_list": [
                                        {"text": "Ictus y Daño Cerebral", "link": {"url": "#"}},
                                        {"text": "Parkinson", "link": {"url": "#"}},
                                        {"text": "Alzheimer y Demencias", "link": {"url": "#"}},
                                        {"text": "Esclerosis Múltiple", "link": {"url": "#"}},
                                        {"text": "TEA y TDAH (Niños)", "link": {"url": "#"}}
                                    ],
                                    "space_between": {"unit": "px", "size": 10},
                                    "icon_color": "#01A4BE",
                                    "icon_size": {"unit": "px", "size": 12},
                                    "text_color": "rgba(255,255,255,0.5)",
                                    "text_color_hover": "#02C0DD",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "link_inline": "yes"
                                }
                            }
                        ]
                    },
                    # Columna 3: Empresa
                    {
                        "id": "col-company",
                        "elType": "column",
                        "settings": {
                            "_column_size": 20,
                            "padding": {"unit": "px", "top": 0, "right": 20, "bottom": 50, "left": 20},
                            "padding_mobile": {"unit": "px", "top": 0, "right": 0, "bottom": 30, "left": 0}
                        },
                        "elements": [
                            {
                                "id": "company-title",
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Empresa",
                                    "header_size": "h4",
                                    "align": "left",
                                    "title_color": "#FFFFFF",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Outfit",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "typography_font_weight": "700",
                                    "typography_letter_spacing": {"unit": "px", "size": 0.6},
                                    "text_transform": "uppercase"
                                }
                            },
                            {
                                "id": "company-list",
                                "elType": "widget",
                                "widgetType": "icon-list",
                                "settings": {
                                    "icon_list": [
                                        {"text": "¿Cómo lo hacemos?", "link": {"url": "#"}},
                                        {"text": "¿Quiénes somos?", "link": {"url": "#"}},
                                        {"text": "Nuestro equipo", "link": {"url": "#"}},
                                        {"text": "Terapia a domicilio", "link": {"url": "#"}},
                                        {"text": "Blog", "link": {"url": "#"}}
                                    ],
                                    "space_between": {"unit": "px", "size": 10},
                                    "icon_color": "#01A4BE",
                                    "icon_size": {"unit": "px", "size": 12},
                                    "text_color": "rgba(255,255,255,0.5)",
                                    "text_color_hover": "#02C0DD",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "link_inline": "yes"
                                }
                            }
                        ]
                    },
                    # Columna 4: Contacto
                    {
                        "id": "col-contact",
                        "elType": "column",
                        "settings": {
                            "_column_size": 35,
                            "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 50, "left": 20},
                            "padding_mobile": {"unit": "px", "top": 0, "right": 0, "bottom": 30, "left": 0}
                        },
                        "elements": [
                            {
                                "id": "contact-card",
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": '<div style="background: rgba(1,164,190,0.1); border: 1px solid rgba(1,164,190,0.25); border-radius: 20px; padding: 24px;">'
                                }
                            },
                            {
                                "id": "contact-title",
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Contacto",
                                    "header_size": "h4",
                                    "align": "left",
                                    "title_color": "#FFFFFF",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Outfit",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "typography_font_weight": "700",
                                    "typography_letter_spacing": {"unit": "px", "size": 0.6},
                                    "text_transform": "uppercase",
                                    "_margin": {"unit": "px", "top": 0, "right": 0, "bottom": 16, "left": 0}
                                }
                            },
                            {
                                "id": "contact-items",
                                "elType": "widget",
                                "widgetType": "icon-list",
                                "settings": {
                                    "icon_list": [
                                        {
                                            "text": "C/ Ejemplo 12, 28220 Majadahonda, Madrid",
                                            "selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"}
                                        },
                                        {
                                            "text": "915 481 732",
                                            "link": {"url": "tel:+34915481732"},
                                            "selected_icon": {"value": "fas fa-phone", "library": "fa-solid"}
                                        },
                                        {
                                            "text": "info@rehace.es",
                                            "link": {"url": "mailto:info@rehace.es"},
                                            "selected_icon": {"value": "fas fa-envelope", "library": "fa-solid"}
                                        },
                                        {
                                            "text": "L–V: 9:00 – 20:00",
                                            "selected_icon": {"value": "fas fa-clock", "library": "fa-solid"}
                                        }
                                    ],
                                    "space_between": {"unit": "px", "size": 14},
                                    "icon_color": "#01A4BE",
                                    "icon_size": {"unit": "px", "size": 14},
                                    "text_color": "rgba(255,255,255,0.65)",
                                    "text_color_hover": "#02C0DD",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "link_inline": "yes"
                                }
                            },
                            {
                                "id": "contact-btn",
                                "elType": "widget",
                                "widgetType": "button",
                                "settings": {
                                    "text": "Pedir Cita →",
                                    "align": "left",
                                    "size": "sm",
                                    "link": {"url": "#"},
                                    "background_color": "#01A4BE",
                                    "button_text_color": "#FFFFFF",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Outfit",
                                    "typography_font_size": {"unit": "px", "size": 14},
                                    "typography_font_weight": "700",
                                    "border_radius": {"unit": "px", "size": 50},
                                    "button_padding": {"unit": "px", "top": 12, "right": 24, "bottom": 12, "left": 24},
                                    "hover_color": "#FFFFFF",
                                    "button_background_hover_color": "#02C0DD",
                                    "hover_animation": "grow",
                                    "_margin": {"unit": "px", "top": 20, "right": 0, "bottom": 0, "left": 0}
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "bottom-section",
        "elType": "section",
        "settings": {
            "content_width": {"unit": "px", "size": 1280},
            "background_background": "classic",
            "background_color": "#00203D",
            "padding": {"unit": "px", "top": 0, "right": 32, "bottom": 24, "left": 32},
            "margin": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0}
        },
        "elements": [
            {
                "id": "bottom-row",
                "elType": "row",
                "settings": {},
                "elements": [
                    {
                        "id": "col-copyright",
                        "elType": "column",
                        "settings": {
                            "_column_size": 50,
                            "padding": {"unit": "px", "top": 0, "right": 20, "bottom": 0, "left": 0}
                        },
                        "elements": [
                            {
                                "id": "copyright-text",
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": "<p>© 2026 REHACE Centro de Neurorehabilitación · Majadahonda, Madrid</p>",
                                    "align": "left",
                                    "text_color": "rgba(255,255,255,0.28)",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 13}
                                }
                            }
                        ]
                    },
                    {
                        "id": "col-legal",
                        "elType": "column",
                        "settings": {
                            "_column_size": 50,
                            "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 20}
                        },
                        "elements": [
                            {
                                "id": "legal-links",
                                "elType": "widget",
                                "widgetType": "icon-list",
                                "settings": {
                                    "icon_list": [
                                        {"text": "Política de privacidad", "link": {"url": "/politica-privacidad"}},
                                        {"text": "Aviso legal", "link": {"url": "/aviso-legal"}},
                                        {"text": "Cookies", "link": {"url": "/politica-de-cookies-ue"}}
                                    ],
                                    "space_between": {"unit": "px", "size": 24},
                                    "layout": "inline",
                                    "icon_color": "rgba(255,255,255,0.28)",
                                    "icon_size": {"unit": "px", "size": 12},
                                    "text_color": "rgba(255,255,255,0.28)",
                                    "text_color_hover": "#02C0DD",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Figtree",
                                    "typography_font_size": {"unit": "px", "size": 13},
                                    "align": "right",
                                    "link_inline": "yes"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

    # Actualizar template
def update_footer():
    url = f"{SITE}/wp-json/wp/v2/elementor_library/{TEMPLATE_ID}"
    
    # Enviar como string JSON
    data = json.dumps({
        "meta": {
            "_elementor_data": json.dumps(footer_data)
        }
    })
    
    response = requests.post(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers={"Content-Type": "application/json"},
        data=data
    )
    
    if response.status_code == 200:
        print(f"✅ Footer actualizado exitosamente (ID: {TEMPLATE_ID})")
        print(f"   Fecha: {response.json().get('modified')}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_footer()
