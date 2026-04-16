import requests
import re

def find_section():
    url = "https://rehace.es/nueva-home-propuesta-diseno/"
    r = requests.get(url)
    
    html = r.text
    # We want to find an element like `<section ... id="...">... por qué elegir...`
    # Or `<div class="...e-con..." id="...">... por qué elegir ...`
    
    # Split the HTML into chunks around "elegir"
    chunks = html.lower().split("elegir")
    if len(chunks) > 1:
        # The section element should be before the text
        before_text = chunks[0]
        # Find the last occurence of 'e-con' or 'section' before the text
        econ_idx = before_text.rfind('e-con')
        section_idx = before_text.rfind('<section')
        
        last_block = max(econ_idx, section_idx)
        if last_block != -1:
            # Get the substring from that block to the end of before_text
            snippet = before_text[last_block-50:]
            print("Snippet surrounding the element:")
            print(snippet)
        else:
            print("Could not find a section or e-con container before the word 'elegir'.")
            print("Surrounding text instead:")
            print(before_text[-200:])
            
    else:
        print("Could not find the word 'elegir' in the page text.")

if __name__ == "__main__":
    find_section()
