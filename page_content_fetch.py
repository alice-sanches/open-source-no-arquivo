'''import json
import requests
from bs4 import BeautifulSoup

page_extracted_html = [] #html completo de cada página
souped_html = [] #html parsed pelo BeautifulSoup



print("links fetched")
print(page_links)

#recolher o html completo de cada página num array   
for link in page_links:
    page_extracted_html.append(requests.get(link).text)

print("html fetched")

#aplicar o BeautifulSoup para tornar html legível
for page_html in page_extracted_html:
    souped_html.append(BeautifulSoup(page_html, 'html.parser'))

print("html souped")

#next steps: writing important info to json file (links in each page, text - use json custom object encoder)'''