#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth

SITE = "https://rehace.es"
USER = "MumaWpx_2025"
PASS = "sgJp rAHd o25S tiom izG8 sPlD"
PAGE_ID = 665

def get_elementor_data():
    # Attempt to fetch with context=edit to see meta
    url = f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit"
    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS))
    if response.status_code == 200:
        data = response.json()
        # In many setups, _elementor_data is directly in a 'meta' object if registered
        # otherwise we might need to check if Elementor has its own endpoint
        with open("raw_elementor_page.json", "w") as f:
            json.dump(data, f, indent=2)
        print("✅ Raw page data saved to raw_elementor_page.json")
        
        # Check if _elementor_data exists in meta
        meta = data.get("meta", {})
        if "_elementor_data" in meta:
            try:
                # elementor_data is often stored as stringified JSON
                el_json = json.loads(meta["_elementor_data"])
                with open("current_elementor_data.json", "w") as f:
                    json.dump(el_json, f, indent=2)
                print("✅ current_elementor_data.json extracted.")
            except:
                print("⚠️ Found _elementor_data but failed to parse as JSON.")
        else:
            print("❌ _elementor_data not found in meta.")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_elementor_data()
