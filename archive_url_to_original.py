import json
import pandas as pd
import re

page_links = [] #links para as cópias das páginas arquivadas

#recolher os links para as cópias arquivadas de cada página num array
with open('page_data.json', 'r') as f:
    json_data = json.load(f)
    for search_term_data in json_data:
        for item in search_term_data['response_items']:
            link = item['linkToNoFrame']
            page_links.append(link)

print("links fetched")

capture_dates_array = []
original_urls_array = []

for link in page_links:
    capture_date_match_object = re.search(r'\b\d{14}\b', link)
    capture_dates_array.append(capture_date_match_object.group())
    original_urls_match_object = re.search(r'/http\S*', link)
    original_urls_array.append(original_urls_match_object.group())

print(capture_dates_array)
print(original_urls_array)

#store url data in a table with one url per row
link_data = pd.DataFrame(
    {
       "full_url": page_links,
       "capture_date": capture_dates_array,
       "original_url": original_urls_array
     }
)

link_data.to_json(r'url_collection.json', 'records')
link_data.to_csv(r'url_collection.csv')