import json, requests, re
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665 # Main Page
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🧠 Updating Main Page (665) with 3 Sections...")
    
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    source_data = r.json()
    el_data_str = source_data.get("meta", {}).get("_elementor_data", "[]")
    el_data = json.loads(el_data_str)
    
    script = """
<script id="neuron-final-v13">
(function() {
    console.log("Neuron Init v13 - Tracking 3 Sections");
    function initN(c, d, l) {
        if (!c || c.dataset.init) return;
        const ctx = c.getContext('2d'); let pts = [];
        function rz() { c.width = c.parentElement.offsetWidth; c.height = c.parentElement.offsetHeight; }
        window.addEventListener('resize', rz); rz();
        class P {
            constructor() { this.rs(); }
            rs() { this.x=Math.random()*c.width; this.y=Math.random()*c.height; this.vx=(Math.random()-.5)*.4; this.vy=(Math.random()-.5)*.4; this.r=Math.random()*1.8+.8; }
            up() { this.x+=this.vx; this.y+=this.vy; if(this.x<0||this.x>c.width)this.vx*=-1; if(this.y<0||this.y>c.height)this.vy*=-1; }
            dr() { ctx.beginPath(); ctx.arc(this.x,this.y,this.r,0,Math.PI*2); ctx.fillStyle=d; ctx.fill(); }
        }
        for(let i=0;i<60;i++) pts.push(new P());
        function anim() {
            ctx.clearRect(0,0,c.width,c.height);
            for(let i=0;i<pts.length;i++){
                pts[i].up(); pts[i].dr();
                for(let j=i+1;j<pts.length;j++){
                    let dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y, d=Math.sqrt(dx*dx+dy*dy);
                    if(d<140){ ctx.beginPath(); ctx.strokeStyle=`rgba(1,164,190,${l*(1-d/140)})`; ctx.lineWidth=.6; ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y); ctx.stroke(); }
                }
            }
            requestAnimationFrame(anim);
        }
        c.dataset.init='1'; anim();
    }
    
    function attachCanvas(target, cClass, particleColor, opacity, zCanvas, zInner) {
        if (!target || target.querySelector('.' + cClass)) return;
        
        let c = document.createElement('canvas'); c.className = cClass;
        c.style.cssText = `position:absolute;top:0;left:0;width:100%;height:100%;z-index:${zCanvas};pointer-events:none;opacity:0.6;`;
        
        if(window.getComputedStyle(target).position === 'static') {
            target.style.position = 'relative';
        }
        target.appendChild(c);
        initN(c, particleColor, opacity);
        
        // Z-Index fix for children
        Array.from(target.children).forEach(child => {
            if(child !== c && !child.classList.contains('elementor-background-overlay') && !child.classList.contains('elementor-shape')) {
                if(window.getComputedStyle(child).position === 'static') {
                    child.style.position = 'relative';
                }
                child.style.zIndex = zInner;
            }
        });
    }

    function go() {
        // 1. Hero
        const title = document.querySelector('.rh-hero-h1');
        const h = title?.closest('.e-con') || title?.closest('section');
        if(h) attachCanvas(h, 'n-canv-hero', 'rgba(255,255,255,1)', 0.9, 9, 10);
        
        // 2. Specialties
        const spec = document.querySelector('#tratamos')?.closest('.e-con') || document.querySelector('#tratamos')?.closest('section');
        if(spec) attachCanvas(spec, 'n-canv-spec', 'rgba(1,164,190,0.8)', 0.7, 9, 10);
        
        // 3. Why Choose Us (Por que elegir Rehace)
        const why = document.querySelector('.elementor-element-rh-v2-why') || document.querySelector('#nosotros')?.closest('.e-con');
        if(why) attachCanvas(why, 'n-canv-why', 'rgba(1,164,190,0.6)', 0.5, 0, 2); // For this section, we might just need it at the very bottom since it has a light background, no overlay issues likely
    }
    setTimeout(() => { setInterval(go, 1000); go(); }, 500);
})();
</script>
    """
    
    found = False
    def process_elements(elements):
        nonlocal found
        for el in elements:
            if el.get("id") == "rh-v2-global-css":
                html = el["settings"].get("html", "")
                
                # Strip ALL previous iterations of neuron scripts to keep it clean
                html = re.sub(r'<script id="neuron-.*?">.*?</script>', '', html, flags=re.DOTALL)
                
                el["settings"]["html"] = script + html
                found = True
            if "elements" in el: process_elements(el["elements"])
            
    process_elements(el_data)
    
    if found:
        r = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
            "meta": {
                "_elementor_data": json.dumps(el_data)
            }
        })
        if r.status_code == 200:
            print("✅ Main Page Updated Successfully")
        else:
            print(f"❌ Failed to update. Status code: {r.status_code}")
            print(r.text)
    else:
        print("Widget rh-v2-global-css not found on main page")

if __name__ == "__main__":
    main()
