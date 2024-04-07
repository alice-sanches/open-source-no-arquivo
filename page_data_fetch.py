#import requests
#import json

#termos_pesquisa = ["código aberto", "open source", "software livre", "acesso aberto", "linux", "unix"]
#urls = []

#def make_urls():
#    for termo in termos_pesquisa:
#        urls.append(f"https://arquivo.pt/textsearch?q=\"{termo}\"&maxItems=50&prettyPrint=true")
#    return(urls)

#make_urls()
#print(urls)

#with open('page_data.json', 'w') as f:
#    for url in urls:
#        print(url)
#        response = requests.get(url)
#        print(response) 
#        json.dump(response.json(), f)
#        f.write('\n')
    
 
