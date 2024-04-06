import json
import requests
from bs4 import BeautifulSoup

page_links = []

with open('page_data.json', 'r') as f:
    json_data = json.load(f)
    for search_term_data in json_data:
        for item in search_term_data['response_items']:
            link = item['linkToArchive']
            page_links.append(link)

print(page_links)
   
html_text = []
for link in page_links:
    html_text.append(requests.get(link).text)

print(html_text)

souped_text = []
for page_html in html_text:
    souped_text.append(BeautifulSoup(page_html, 'html.parser'))

with open('page_content.txt', 'w') as content_file:
    for soup in souped_text:
        print(f"__PAGE START__\n{soup}\n__PAGE END__", file=content_file)