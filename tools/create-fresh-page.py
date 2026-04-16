import json, requests, re
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
SOURCE_PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("🧠 Creating Fresh Page to bypass Cache...")
    
    # 1. Get Source Data
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{SOURCE_PAGE_ID}?context=edit", auth=auth)
    source_data = r.json()
    el_data_str = source_data.get("meta", {}).get("_elementor_data", "[]")
    el_data = json.loads(el_data_str)
    
    # 2. Inject Animation Script into the global widget of the new data
    script = """
<script id="neuron-final-v10">
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
        const h = document.querySelector('.rh-hero-h1')?.closest('section') || document.querySelector('.elementor-section:first-of-type');
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
                el["settings"]["html"] = script + el["settings"].get("html", "")
                found = True
            if "elements" in el: process_elements(el["elements"])
    process_elements(el_data)
    
    # 3. Create NEW Page
    new_page = {
        "title": "NUEVA HOME ANIMADA",
        "status": "publish",
        "slug": "home-animada-test",
        "meta": {
            "_elementor_data": json.dumps(el_data),
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page"
        }
    }
    
    r = requests.post(f"{SITE}/wp-json/wp/v2/pages", auth=auth, json=new_page)
    if r.status_code == 201:
        data = r.json()
        print(f"✅ Success! Page Created ID: {data['id']}")
        print(f"🔗 URL: {data['link']}")
    else:
        print(f"❌ Error: {r.status_code}")
        print(r.text)

if __name__ == "__main__":
    main()
