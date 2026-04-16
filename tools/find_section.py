import requests
from bs4 import BeautifulSoup

def find_section():
    url = "https://rehace.es/nueva-home-propuesta-diseno/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # We look for text that contains 'elegir'
    elements = soup.find_all(string=lambda t: t and 'elegir' in t.lower())
    
    for el in elements:
        print(f"Found text: {el.strip()}")
        # Find closest parent section or e-con
        parent = el.find_parent('section') or el.find_parent(class_='e-con')
        if parent:
            print(f"Parent Element Tag: {parent.name}")
            print(f"Parent ID: {parent.get('id')}")
            print(f"Parent Classes: {parent.get('class')}")
            print("---")

if __name__ == "__main__":
    find_section()
