import json, requests, re
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 782 # The new page ID
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🧠 Updating Fresh Page with Correct Selectors...")
    
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    source_data = r.json()
    el_data_str = source_data.get("meta", {}).get("_elementor_data", "[]")
    el_data = json.loads(el_data_str)
    
    script = """
<script id="neuron-final-v11">
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
        // Find Hero by class elementor-element-rh-v2-hero OR elementor-section:first-of-type
        const h = document.querySelector('.rh-hero-h1')?.closest('.elementor-container') || document.querySelector('.elementor-element-rh-v2-hero') || document.querySelector('.elementor-section:first-of-type') || document.querySelector('.e-con:first-of-type');
        if(h && !h.querySelector('.n-canv')){
            let c=document.createElement('canvas'); c.className='n-canv';
            c.style.cssText='position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:0.35;';
            h.style.position='relative'; h.prepend(c); initN(c,'rgba(255,255,255,0.5)',0.7);
        }
    }
    setInterval(go, 1000); go();
})();
</script>
    """
    
    found = False
    def process_elements(elements):
        nonlocal found
        for el in elements:
            if el.get("id") == "rh-v2-global-css":
                html = el["settings"].get("html", "")
                html = re.sub(r'<script id="neuron-final-v10">.*?</script>', '', html, flags=re.DOTALL)
                el["settings"]["html"] = html + script
                found = True
            if "elements" in el: process_elements(el["elements"])
            
    process_elements(el_data)
    
    if found:
        r = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
            "meta": {
                "_elementor_data": json.dumps(el_data)
            }
        })
        print(f"Update Result: {r.status_code}")
    else:
        print("Widget rh-v2-global-css not found")

if __name__ == "__main__":
    main()
