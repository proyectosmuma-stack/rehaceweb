import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665
auth = HTTPBasicAuth(USER, PASS)

def main():
    print("Testing HTML Filtering...")
    test_html = "<!-- NEURON COMMENT TEST --><div id='neuron-div-test'>NEURON DIV</div><script>console.log('NEURON SCRIPT TEST');</script>"
    r = requests.post(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}", auth=auth, json={
        "content": test_html
    })
    print(f"Update Result: {r.status_code}")
    
    # Read it back
    r = requests.get(f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit", auth=auth)
    content = r.json().get("content", {}).get("raw", "")
    print("Raw content back:")
    print(content)

if __name__ == "__main__":
    main()
