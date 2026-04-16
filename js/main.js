/* ── Tab switching ── */
function switchTab(tab, btn) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    document.getElementById('tab-' + tab).classList.add('active');
    btn.classList.add('active');
}

/* ── Sticky header shadow on scroll ── */
window.addEventListener('scroll', () => {
    const h = document.getElementById('site-header');
    if (h) h.classList.toggle('scrolled', window.scrollY > 60);
});

/* ── Neuron Canvas ── */
function initNeuronCanvas(canvasId, dotColor = 'rgba(1,164,190,0.6)', lineOpacity = 0.45) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let pts = [];

    function resize() {
        const p = canvas.parentElement;
        canvas.width = p.offsetWidth;
        canvas.height = p.offsetHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    class Pt {
        constructor() { this.reset(); }
        reset() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - .5) * .4;
            this.vy = (Math.random() - .5) * .4;
            this.r = Math.random() * 1.8 + .8;
        }
        update() {
            this.x += this.vx; this.y += this.vy;
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = dotColor;
            ctx.fill();
        }
    }

    for (let i = 0; i < 50; i++) pts.push(new Pt());

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < pts.length; i++) {
            pts[i].update();
            pts[i].draw();
            for (let j = i + 1; j < pts.length; j++) {
                const dx = pts[i].x - pts[j].x;
                const dy = pts[i].y - pts[j].y;
                const d = Math.sqrt(dx * dx + dy * dy);
                if (d < 130) {
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(1,164,190,${lineOpacity * (1 - d / 130)})`;
                    ctx.lineWidth = .6;
                    ctx.moveTo(pts[i].x, pts[i].y);
                    ctx.lineTo(pts[j].x, pts[j].y);
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(animate);
    }
    animate();
}

document.addEventListener('DOMContentLoaded', () => {
    initNeuronCanvas('neuron-canvas-hero', 'rgba(255,255,255,0.4)', 0.5);
    initNeuronCanvas('neuron-canvas-specialties', 'rgba(1,164,190,0.6)', 0.4);
    
    /* Check if neuron-canvas-steps exists in HTML */
    if (document.getElementById('neuron-canvas-steps')) {
        initNeuronCanvas('neuron-canvas-steps', 'rgba(1,164,190,0.7)', 0.5);
    }

    /* ── Scroll reveal ── */
    const observer = new IntersectionObserver(
        entries => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
        { threshold: 0.1 }
    );
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
});
