#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def get_page_data():
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}"
    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS))
    if response.status_code == 200:
        with open("post_665_data.json", "w") as f:
            json.dump(response.json(), f, indent=2)
        print("✅ Data saved to post_665_data.json")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_page_data()
