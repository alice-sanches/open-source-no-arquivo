import requests
import json

termos_pesquisa = ["código aberto", "open source", "software livre", "acesso aberto", "linux"]

i = 0
while i < len(termos_pesquisa):
    response = requests.get(f"https://arquivo.pt/textsearch?q={termos_pesquisa[i]}&maxItems=50&prettyPrint=true")
    with open('text_search_results.json', '+a') as f:   
        json.dump(response.json(), f)
    i += 1
