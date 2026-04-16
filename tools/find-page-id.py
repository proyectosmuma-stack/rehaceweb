import requests
SITE = "https://rehace.es/nueva-home-propuesta-diseno/"
r = requests.get(SITE)
import re
match = re.search(r'post-(\d+)', r.text)
if match:
    print(f"Page ID found: {match.group(1)}")
else:
    print("Page ID not found in post-XXX class.")
