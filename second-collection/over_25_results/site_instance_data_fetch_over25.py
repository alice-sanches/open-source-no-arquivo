import json
import pandas as pd
import csv

original_urls = []
timestamps = []
collections = []
titles = []
content_lengths = []

with open('D:\Projetos\Programming\open-source-no-arquivo\second-collection\over_25_results\over_25_metadata.json', 'r') as f:
    json_data = json.load(f)
    for seed in json_data:
        for site_instance in seed["response_items"]:
            original_urls.append(site_instance["originalURL"])
            timestamps.append(site_instance["tstamp"])
            collections.append(site_instance["collection"])
            titles.append(site_instance["title"])
            content_lengths.append(site_instance["contentLength"])
        
site_instance_data = pd.DataFrame(
    {
       "seed_url": original_urls,
       "timestamp": timestamps,
       "collection": collections,
       "title": titles,
       "contentLength" : content_lengths
     }
)

site_instance_data.to_csv(r'D:\Projetos\Programming\open-source-no-arquivo\second-collection\over_25_results\over25_site_instance_data.csv')