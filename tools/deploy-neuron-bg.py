import json, requests, re
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🧠 (Z-INDEX FIX DEPLOY) Updating rh-v2-global-css widget...")
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    data = r.json()
    el_data = json.loads(data.get("meta", {}).get("_elementor_data", "[]"))
    
    script = """
<script id="neuron-final-zindex">
(function() {
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
    function go() {
        // Hero
        const title = document.querySelector('.rh-hero-h1');
        const h = title?.closest('.e-con') || title?.closest('section');
        if(h && !h.querySelector('.n-canv-hero')){
            let c=document.createElement('canvas'); c.className='n-canv-hero';
            // Z-INDEX FIX: Push canvas to a high z-index but push the inner content even higher
            c.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;z-index:9;pointer-events:none;opacity:0.6;';
            h.style.position='relative'; 
            h.appendChild(c);
            initN(c,'rgba(255,255,255,1)',0.9);
            
            // Fix children z-index
            Array.from(h.children).forEach(child => {
                if(child !== c && !child.classList.contains('elementor-background-overlay')) {
                    child.style.position = 'relative';
                    child.style.zIndex = '10';
                }
            });
            console.log("Hero injected with Z-Index fix");
        }
        
        // Specialties
        const spec = document.querySelector('#tratamos')?.closest('.e-con') || document.querySelector('#tratamos')?.closest('section');
        if(spec && !spec.querySelector('.n-canv-spec')){
            let c=document.createElement('canvas'); c.className='n-canv-spec';
            c.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;z-index:9;pointer-events:none;opacity:0.5;';
            spec.style.position='relative';
            spec.appendChild(c);
            initN(c,'rgba(1,164,190,0.8)',0.7);
            
            // Fix children z-index
            Array.from(spec.children).forEach(child => {
                if(child !== c && !child.classList.contains('elementor-background-overlay')) {
                    child.style.position = 'relative';
                    child.style.zIndex = '10';
                }
            });
            console.log("Specialties injected with Z-Index fix");
        }
    }
    // Wait for Elementor to finish rendering
    setTimeout(() => { setInterval(go, 1000); go(); }, 1000);
})();
</script>
    """
    
    found = False
    def process_elements(elements):
        nonlocal found
        for el in elements:
            if el.get("id") == "rh-v2-global-css":
                html = el["settings"].get("html", "")
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
        print(f"Update Result MAIN PAGE: {r.status_code}")
    else:
        print("Widget rh-v2-global-css not found on main page")

if __name__ == "__main__":
    main()
