# 📋 Rehace Homepage — Plan de Migración a WordPress + Elementor

> **Documento de referencia para agente.** Sigue cada fase en orden. No avances a la siguiente fase sin completar la anterior. El diseño de referencia está en `index.html` del mismo directorio.

---

## 🎯 Objetivo

Replicar fielmente el diseño de la maqueta `index.html` del proyecto Rehace en una instalación de WordPress usando **Elementor Pro** como constructor de páginas, respetando paleta, tipografía, animaciones y estructura de secciones.

---

## ⚙️ FASE 0 — Prerequisitos del Entorno

Antes de comenzar, verificar que el entorno cumple **todos** los puntos:

### 0.1 WordPress & Plugins
- [ ] WordPress >= 6.4 instalado y accesible (local o remoto)
- [ ] **Elementor Pro** >= 3.18 activo (se necesita Pro para Theme Builder)
- [ ] Plugin **Hello Elementor** o **GeneratePress** como tema base (lightweight)
- [ ] WP-CLI disponible (verificar con `wp --info`) **O** acceso a wp-admin
- [ ] REST API activada y accesible (`/wp-json/wp/v2/`)

### 0.2 Credenciales necesarias
```
WP_URL=https://rehace.es
WP_USER=admin
WP_PASSWORD=xxxx   (Settings > Application Passwords)
```

### 0.3 Archivos de assets a tener disponibles
- `hero_neuro_rehab_center_1775658330763.png`
- `treatment_stroke.png`
- `treatment_parkinson.png`
- `treatment_cognitive.png`
- `treatment_child_neuro_1775657348721.png`
- `therapy_session_physio_1775656527885.png`
- `therapy_home_visit_1775659496678.png`
- `rehab_center_modern_1775656504951.png`

---

## 📁 FASE 1 — Configuración del Tema Hijo

### 1.1 Crear Tema Hijo

```bash
wp scaffold child-theme rehace-child --parent_theme=hello-elementor \
  --theme_name="Rehace Child" --author="Rehace" --activate
```

**`style.css`** (encabezado obligatorio):
```css
/*
 Theme Name: Rehace Child
 Template: hello-elementor
 Version: 1.0
*/
```

### 1.2 Activar
```bash
wp theme activate rehace-child
```

---

## 🎨 FASE 2 — CSS Global (Variables y Estilos Base)

Añadir en **Apariencia > Personalizar > CSS Adicional** o en `rehace-child/style.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700;800;900&family=Figtree:wght@400;500;600;700&display=swap');

:root {
  --navy:       #003366;
  --navy-dark:  #001F3F;
  --navy-mid:   #00203D;
  --cyan:       #01A4BE;
  --cyan-light: #4ECDE4;
  --cyan-pale:  rgba(1,164,190,0.10);
  --off-white:  #F4F7FB;
  --light-gray: #E8EEF5;
  --text-body:  #2D3D52;
  --text-muted: #6B7E96;
  --radius:     12px;
  --radius-lg:  20px;
}

body { font-family: 'Figtree', sans-serif; color: var(--text-body); }
h1,h2,h3,h4,h5,h6 { font-family: 'Outfit', sans-serif; }

/* Botones globales */
.btn-rehace-primary {
  background: var(--cyan); color: white;
  padding: 1rem 2.4rem; border-radius: 50px;
  font-family: 'Outfit', sans-serif; font-weight: 700;
  display: inline-block; text-decoration: none;
  transition: all .3s ease;
}
.btn-rehace-primary:hover {
  background: #018FAA; transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(1,164,190,.35); color: white;
}
.btn-rehace-outline {
  background: transparent; color: white;
  padding: 1rem 2.4rem; border-radius: 50px;
  border: 2px solid rgba(255,255,255,.6);
  font-family: 'Outfit', sans-serif; font-weight: 700;
  display: inline-block; text-decoration: none;
  transition: all .3s ease;
}
.btn-rehace-outline:hover { border-color: white; background: rgba(255,255,255,.1); }

/* Scroll reveal */
.reveal { opacity: 0; transform: translateY(30px); transition: opacity .7s ease, transform .7s ease; }
.reveal.visible { opacity: 1; transform: none; }
```

### Configurar tipografías en Elementor > Kit de Sitio
- **H1/H2**: Outfit, Weight 900/800
- **Cuerpo**: Figtree, Weight 400

---

## 🖼️ FASE 3 — Subir imágenes a Media Library

```bash
# Ejecutar desde el directorio /ollama-local/
wp media import hero_neuro_rehab_center_1775658330763.png --title="Rehace Hero"
wp media import treatment_stroke.png              --title="Ictus y Daño Cerebral"
wp media import treatment_parkinson.png           --title="Parkinson"
wp media import treatment_cognitive.png           --title="Alzheimer y Demencias"
wp media import treatment_child_neuro_1775657348721.png --title="Neuropediatría"
wp media import therapy_session_physio_1775656527885.png --title="Fisioterapia"
wp media import therapy_home_visit_1775659496678.png --title="Terapia a Domicilio"
wp media import rehab_center_modern_1775656504951.png --title="Centro REHACE"
```

> Anotar los IDs devueltos para configurar los widgets de imagen de Elementor.

---

## 🔝 FASE 4 — Header con Theme Builder

**Elementor > Theme Builder > Header > Añadir Nuevo**

### 4.1 Topbar (barra teal)

```
Seccion: topbar | bg: #01A4BE | padding: 8px 0 | font: Figtree 13px

  Columna izquierda (flex-row, gap: 1.5rem):
    "Majadahonda, Madrid"
    "info@rehace.es" (mailto link)
    "Valoracion inicial GRATUITA"

  Columna derecha (text-right):
    "L-V 9:00-20:00"
    Boton pastilla blanca: "915 481 732" (tel: link)
```

CSS:
```css
.topbar-phone-pill {
  background: white; color: #01A4BE; padding: 4px 14px;
  border-radius: 50px; font-weight: 700; font-size: 13px;
}
```

### 4.2 Nav principal (sticky)

```
Seccion: bg white | min-height: 72px | sticky | z-index: 1000

  Col 1 (20%): Logo REHACE (height: 52px)
    src: https://rehace.es/wp-content/uploads/elementor/thumbs/logo-rehace-color-...png

  Col 2 (55%): Nav Menu Widget
    Items: "Que tratamos?" | "Como lo hacemos?" | "Quienes somos?" | "A domicilio"
    Font: Outfit 500 | Hover: #01A4BE

  Col 3 (25%): Telefono + Boton CTA
    Texto: "915 481 732" (color: #01A4BE, Outfit 700)
    Boton: "Pide cita" (bg: #01A4BE, color: white, border-radius: 50px)
```

CSS + JS para efecto scroll (anadir en functions.php):
```css
.site-header-rehace { transition: box-shadow .3s ease; }
.site-header-rehace.scrolled { box-shadow: 0 4px 24px rgba(0,51,102,.10); }
```
```php
add_action('wp_footer', function() { ?>
<script>
window.addEventListener('scroll', function() {
  document.querySelector('.site-header-rehace')
    ?.classList.toggle('scrolled', window.scrollY > 60);
});
</script>
<?php });
```

> Condicion de visualizacion: **Todo el Sitio**

---

## 🦸 FASE 5 — Hero Section

**Seccion principal en pagina de inicio:**

```
Fondo: imagen hero_neuro_rehab_center | center 30% | cover
Overlay degradado: rgba(0,34,62,0.88) → rgba(1,164,190,0.20) | angulo: 110deg
Min-height: 92vh | Alineacion vertical: centro
Padding: 7rem 0 9rem
```

**Contenido (anadir en una columna al 55% de anchura):**

```
[HTML Widget] Eyebrow con lineas decorativas:
  <div class="hero-eyebrow-line">
    <span class="hero-eyebrow-text">Rehabilitacion Neurologica · Majadahonda</span>
  </div>

[Titulo H1] (Outfit 900, blanco, mayusculas, 3.8rem):
  "Recupera tu <em style='color:#4ECDE4;font-style:normal;'>AUTONOMIA</em>
   con el equipo que te entiende"

[Parrafo] (Figtree, rgba(255,255,255,.82), 1.1rem):
  "Tratamos a ninos y adultos con lesiones neurologicas..."

[2 Botones]:
  "Solicitar Valoracion Gratuita" → clase: btn-rehace-primary | padding: 1.1rem 2.5rem
  "Ver especialidades →" → clase: btn-rehace-outline

[HTML Widget] Stats bar:
  <div class="hero-stats-bar">
    <div class="stat"><span class="stat-num">+500</span><span class="stat-lbl">Pacientes tratados</span></div>
    <div class="stat"><span class="stat-num">4</span><span class="stat-lbl">Especialidades</span></div>
    <div class="stat"><span class="stat-num">10+</span><span class="stat-lbl">Anos de experiencia</span></div>
  </div>
```

CSS para la seccion hero (anadir en CSS personalizado de la seccion):
```css
.hero-eyebrow-line {
  display: flex; align-items: center; gap: 1rem; margin-bottom: 1.8rem;
}
.hero-eyebrow-line::before, .hero-eyebrow-line::after {
  content: ''; flex: 0 0 40px; height: 1.5px; background: #01A4BE;
}
.hero-eyebrow-text {
  font-family: 'Outfit', sans-serif; font-weight: 700; font-size: .78rem;
  letter-spacing: .18em; text-transform: uppercase; color: #4ECDE4;
}
.hero-stats-bar {
  display: flex; gap: 2.5rem; flex-wrap: wrap;
  padding-top: 2rem; border-top: 1px solid rgba(255,255,255,.15); margin-top: 2rem;
}
.hero-stats-bar .stat-num {
  font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 2rem;
  color: #4ECDE4; display: block;
}
.hero-stats-bar .stat-lbl { font-size: .8rem; color: rgba(255,255,255,.6); }
```

---

## 🃏 FASE 6 — Trust Cards (bajo el Hero)

```
Seccion: bg white | padding: 0 0 4rem
4 Columnas iguales con separadores verticales

  Col 1: Icono circulo cian + "Neuropatia" (Outfit 700) + subtexto muted
  Col 2: "En centro y a domicilio"
  Col 3: "Valoracion gratuita"
  Col 4: "Apoyo integral"
```

CSS:
```css
.trust-col {
  display: flex; flex-direction: column; align-items: center; text-align: center;
  gap: .6rem; padding: 2.2rem 1.5rem;
  border-right: 1px solid #E8EEF5; transition: background .3s;
}
.trust-col:last-child { border-right: none; }
.trust-col:hover { background: #F4F7FB; }
.trust-icon-wrap {
  width: 52px; height: 52px; border-radius: 50%;
  background: rgba(1,164,190,.10);
  display: flex; align-items: center; justify-content: center; font-size: 1.5rem;
}
```

---

## 🧠 FASE 7 — "Que Tratamos en REHACE" (Tabs)

```
Eyebrow: "Especialidades"
H2: "Que tratamos en REHACE?"
Parrafo intro
[Elementor Tabs Widget]
```

**Tab 1 — Adultos y Mayores** (grid 4 cols):

| Imagen | Tag | Titulo |
|---|---|---|
| treatment_stroke.png | Neurologia | Ictus y Dano Cerebral |
| treatment_parkinson.png | Neurologia | Parkinson |
| treatment_cognitive.png | Neuropsicologia | Alzheimer y Demencias |
| therapy_session_physio.png | Fisioterapia | Esclerosis Multiple |

**Tab 2 — Ninos** (grid 3 cols):

| Imagen | Tag | Titulo |
|---|---|---|
| treatment_child_neuro.png | Neuropediatria | TEA – Espectro Autista |
| treatment_child_neuro.png | Neuropsicologia | TDAH y Trastornos del Lenguaje |
| treatment_cognitive.png | T. Ocupacional | Retraso Madurativo |

CSS cards:
```css
.prog-card-rehace {
  background: white; border-radius: 12px; overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,51,102,.08); border: 1px solid #E8EEF5;
  transition: transform .35s ease, box-shadow .35s ease;
}
.prog-card-rehace:hover { transform: translateY(-8px); box-shadow: 0 24px 56px rgba(0,51,102,.14); }
.prog-card-tag {
  font-family: 'Outfit', sans-serif; font-size: .72rem; font-weight: 700;
  color: #01A4BE; text-transform: uppercase; letter-spacing: .1em;
}
```

---

## ✅ FASE 8 — "Por que elegir REHACE?" (Split 50/50)

```
Seccion: bg #F4F7FB | padding: 8rem 0
2 Columnas 50/50

  Col izquierda (imagen compuesta):
    Imagen principal: rehab_center_modern.png (border-radius: 20px)
    Imagen flotante accent: therapy_session_physio.png (posicion: bottom-right, border: 6px white)
    Badge flotante: "+500 / Pacientes tratados" (bg: navy, numero en cyan)

  Col derecha:
    Eyebrow: "Mas que una clinica"
    H2: "Por que elegir REHACE?"
    Lista features (4 items, borde izq cian):
      - Equipo Multidisciplinar
      - Tratamiento Personalizado
      - Reevaluacion Continua
      - Tambien a Domicilio
    Boton: "Conoce a nuestro equipo"
```

---

## 4️⃣ FASE 9 — "Tu Recuperacion en 4 Pasos"

```
Seccion: bg #F4F7FB con patron puntillado | padding: 7rem 0 8rem
Eyebrow, H2, parrafo (centrados)

[HTML Widget]: tarjeta blanca con 4 columnas + fila CTA
```

```html
<div class="steps-card-rehace">
  <div class="steps-grid-rehace">
    <div class="step-col">
      <span class="step-n">01</span>
      <h3>Valoracion Inicial Gratuita</h3>
      <p>Evaluamos tu situacion sin compromiso. Conocemos al paciente, su historia y entorno para disenar la propuesta mas adecuada.</p>
    </div>
    <div class="step-col">
      <span class="step-n">02</span>
      <h3>Elaboracion de Objetivos</h3>
      <p>Establecemos conjuntamente con el paciente y la familia las metas a alcanzar, con plazos realistas y medibles.</p>
    </div>
    <div class="step-col">
      <span class="step-n">03</span>
      <h3>Terapia Personalizada</h3>
      <p>Nuestro equipo multidisciplinar trabaja de forma coordinada para conseguir la maxima recuperacion funcional posible.</p>
    </div>
    <div class="step-col">
      <span class="step-n">04</span>
      <h3>Reevaluacion Continua</h3>
      <p>Hacemos valoraciones periodicas para medir el progreso y reajustar el plan. El camino no termina hasta alcanzar los objetivos.</p>
    </div>
  </div>
  <div class="steps-cta-rehace">
    <p>La valoracion inicial es <strong>completamente gratuita</strong> y sin ningun compromiso.</p>
    <a href="#cita" class="btn-rehace-primary">Pedir mi Valoracion Gratuita</a>
  </div>
</div>
```

CSS:
```css
.steps-card-rehace {
  background: white; border-radius: 20px;
  box-shadow: 0 20px 70px rgba(0,51,102,.10);
  overflow: hidden; margin-top: 3.5rem;
}
.steps-grid-rehace { display: grid; grid-template-columns: repeat(4, 1fr); }
.step-col {
  padding: 3rem 2.5rem; border-right: 1px solid #E8EEF5;
  position: relative; transition: background .3s ease;
}
.step-col:last-child { border-right: none; }
.step-col:hover { background: #F4F7FB; }
.step-col::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 3px; background: #01A4BE;
  transform: scaleX(0); transition: transform .35s ease; transform-origin: left;
}
.step-col:hover::before { transform: scaleX(1); }
.step-n {
  font-family: 'Outfit', sans-serif; font-weight: 900;
  font-size: 4.5rem; line-height: 1; margin-bottom: 1rem;
  color: #003366; opacity: 0.12; display: block;
}
.step-col h3 { font-size: 1.1rem; font-weight: 800; margin-bottom: .7rem; color: #003366; }
.step-col p { font-size: .88rem; line-height: 1.7; color: #6B7E96; }
.steps-cta-rehace {
  border-top: 1px solid #E8EEF5; padding: 1.8rem 2.5rem;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 1rem; background: #F9FBFD;
}
.steps-cta-rehace p { font-size: .92rem; color: #6B7E96; font-style: italic; }
```

---

## 🏠 FASE 10 — Terapia a Domicilio (Strip Image)

```
Seccion: full-width, sin padding | 2 columnas 50/50

  Col izquierda:
    Imagen: therapy_home_visit.png | height: 460px | object-fit: cover

  Col derecha: bg: #01A4BE | padding: 5rem 4rem
    Eyebrow blanco translucido: "A tu lado, en tu hogar"
    H2 blanco: "Tambien realizamos terapia en tu domicilio"
    Parrafo rgba(255,255,255,.9): "Si el desplazamiento al centro es un obstaculo..."
    Boton outline blanco: "Solicitar terapia a domicilio"
```

---

## 🩺 FASE 11 — Disciplinas / Areas del Equipo

```
Seccion: bg #F4F7FB | padding: 7rem 0
Eyebrow + H2: "Nuestras Areas de Trabajo"
4 Columnas (Disc Cards):
  Fisioterapia Neurologica | Logopedia | Terapia Ocupacional | Neuropsicologia
```

CSS disc cards:
```css
.disc-card-rehace {
  background: white; border-radius: 12px; padding: 2.5rem 1.8rem;
  text-align: center; transition: all .35s ease;
  border-bottom: 3px solid transparent;
  box-shadow: 0 2px 16px rgba(0,51,102,.05);
}
.disc-card-rehace:hover {
  transform: translateY(-6px); border-bottom-color: #01A4BE;
  box-shadow: 0 20px 50px rgba(0,51,102,.1);
}
```

---

## 💬 FASE 12 — Testimonios

```
Seccion: bg white | padding: 7rem 0
H2: "Lo que dicen nuestros pacientes"
3 Columnas (Testimonial Cards):
  Cada card: Estrellas + texto italic + nombre + badge Google
```

---

## 📢 FASE 13 — CTA Banner Pre-Footer

```
Seccion: bg #003366 (navy) | padding: 6rem 0 | position: relative
Canvas de neuronas (HTML Widget): <canvas id="neuron-cta" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>

H2 (centro, blanco, Outfit 900): "Da el primer paso hacia tu recuperacion"
Parrafo (rgba(255,255,255,.75)): "La valoracion inicial es completamente gratuita..."

2 Botones centrados:
  "Pedir Valoracion Gratuita" → btn-rehace-primary grande
  "Llamanos: 915 481 732" → btn-rehace-outline
```

---

## 🦶 FASE 14 — Footer con Theme Builder

**Elementor > Theme Builder > Footer > Anadir Nuevo**

```
Seccion principal: bg #00203D | padding: 5rem 0
4 Columnas

  Col 1 (Branding):
    Logo REHACE (max-height: 48px)
    Texto descriptivo: "Centro de neurorrehabilitacion en Majadahonda..."
    Social Links: Facebook | Instagram | LinkedIn | YouTube
    (iconos color cyan, hover cyan-light)

  Col 2 (Especialidades):
    Titulo "Especialidades" (Outfit 700, blanco, border-bottom: 2px solid #01A4BE)
    Links gris claro hover cyan: Ictus | Parkinson | Alzheimer | Esclerosis | Neuropediatria

  Col 3 (Empresa):
    Titulo "Empresa"
    Links: Quienes Somos | Nuestro Equipo | Blog | Trabaja con Nosotros | Contacto

  Col 4 (Tarjeta Contacto):
    Div con bg rgba(1,164,190,.15) | border: 1px solid rgba(1,164,190,.25) | border-radius: 12px | padding: 1.8rem
    "Tienes alguna duda?" (Outfit 700, blanco)
    Tel: 915 481 732 (cian)
    Email: info@rehace.es
    Dir: Majadahonda, Madrid
    Boton: "Pedir Cita Gratuita" (btn-rehace-primary)

Barra inferior: bg rgba(0,0,0,.3) | padding: 1.2rem 0
  "2024 REHACE — Todos los derechos reservados"
  Links derecha: Privacidad | Aviso Legal | Cookies
```

CSS footer:
```css
.footer-col-title {
  font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1rem;
  color: white; margin-bottom: 1.4rem; padding-bottom: .8rem;
  border-bottom: 2px solid #01A4BE; display: block;
}
.footer-link {
  color: rgba(255,255,255,.6); text-decoration: none; display: block;
  margin-bottom: .5rem; font-size: .9rem; transition: all .2s ease;
}
.footer-link:hover { color: #4ECDE4; padding-left: 4px; }
```

> Condicion de visualizacion: **Todo el Sitio**

---

## ✨ FASE 15 — Canvas Animacion Neuronal

Anadir en `functions.php`:

```php
add_action('wp_footer', function() {
    if (!is_front_page()) return;
    ?>
    <script>
    function initNeuronCanvas(canvasId, opts) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const cfg = { nodeCount: opts?.nodeCount || 50, color: opts?.color || 'rgba(1,164,190,', maxDist: 130, speed: 0.4 };
        canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight;
        const nodes = Array.from({length: cfg.nodeCount}, () => ({
            x: Math.random()*canvas.width, y: Math.random()*canvas.height,
            vx: (Math.random()-.5)*cfg.speed, vy: (Math.random()-.5)*cfg.speed,
            r: Math.random()*2.5+1
        }));
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            nodes.forEach(n => {
                n.x += n.vx; n.y += n.vy;
                if (n.x < 0 || n.x > canvas.width) n.vx *= -1;
                if (n.y < 0 || n.y > canvas.height) n.vy *= -1;
                ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI*2);
                ctx.fillStyle = cfg.color+'0.5)'; ctx.fill();
            });
            nodes.forEach((a, i) => {
                for (let j = i+1; j < nodes.length; j++) {
                    const b = nodes[j], d = Math.hypot(a.x-b.x, a.y-b.y);
                    if (d < cfg.maxDist) {
                        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
                        ctx.strokeStyle = cfg.color+(1-d/cfg.maxDist)*.4+')';
                        ctx.lineWidth = 1; ctx.stroke();
                    }
                }
            });
            requestAnimationFrame(draw);
        }
        draw();
    }
    document.addEventListener('DOMContentLoaded', () => {
        initNeuronCanvas('neuron-cta', { nodeCount: 45 });
    });
    </script>
    <?php
});
```

---

## 🔁 FASE 16 — Scroll Reveal

Anadir en `functions.php`:

```php
add_action('wp_footer', function() { ?>
<script>
const revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); revealObs.unobserve(e.target); }});
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));
</script>
<?php });
```

> Anadir clase `reveal` a los widgets via **Avanzado > Clase CSS** en Elementor.

---

## ✅ FASE 17 — QA Final

### Checklist Visual
- [ ] Header sticky con sombra al hacer scroll
- [ ] Topbar cian con telefono en pastilla blanca
- [ ] Hero: overlay oscuro, texto blanco, eyebrow con lineas decorativas cian
- [ ] Hero: estadisticas en cian claro y legibles
- [ ] Trust cards: 4 columnas con separadores y hover
- [ ] Tabs Especialidades: funcionales Adultos/Ninos con imagen en cada card
- [ ] Split "Por que Rehace": imagen compuesta con badge flotante
- [ ] 4 Pasos: tarjeta blanca con grid 4 columnas y numeros 12% opacidad
- [ ] 4 Pasos: fila CTA en base de la tarjeta
- [ ] Domicilio: imagen izq + panel cian derecha
- [ ] Footer 4 columnas sobre #00203D con tarjeta de contacto

### Checklist Tecnico
- [ ] Google Fonts (Outfit + Figtree) funcionando
- [ ] Cero errores JS en consola
- [ ] Canvas neuronal animandose en CTA banner
- [ ] Reveal animations activas al hacer scroll
- [ ] Responsive verificado en: 375px / 768px / 1024px / 1440px
- [ ] Alt text en todas las imagenes
- [ ] Links de nav apuntan a anchors correctos
- [ ] Botones CTA apuntan a formulario de contacto o #cita

### Breakpoints Responsive (Elementor)
- **Mobile (<768px)**: Columnas unicas, hero 70vh, trust cards 2x2, steps 1 col
- **Tablet (768-1024px)**: Footer 2x2, steps 2x2, trust cards 2x2
- **Desktop (>1024px)**: Layout completo segun diseno

---

> **NOTA FINAL:** Todos los textos deben copiarse literalmente del archivo `index.html` de referencia. El token de color principal es siempre `#01A4BE` (cian) y `#003366` (navy). No usar variaciones no documentadas en este plan.
