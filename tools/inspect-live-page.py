import json, requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 86
auth = HTTPBasicAuth(USER, PASS)

def main():
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    data = r.json()
    meta = data.get("meta", {})
    el_data_str = meta.get("_elementor_data", "[]")
    
    with open("tools/live_page_inspect.json", "w") as f:
        json.dump(json.loads(el_data_str), f, indent=2)
    
    print(f"Inspected page {PAGE_ID}. Data saved to tools/live_page_inspect.json")

if __name__ == "__main__":
    main()
