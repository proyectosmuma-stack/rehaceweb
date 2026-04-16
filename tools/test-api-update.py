import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("Testing API Update on Title...")
    r = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "title": "Nueva Home - Propuesta Diseño - TEST"
    })
    if r.status_code == 200:
        print("✅ Title updated to TEST. Please check live page title.")
    else:
        print(f"❌ Update failed: {r.status_code}")
        print(r.text)

if __name__ == "__main__":
    main()
