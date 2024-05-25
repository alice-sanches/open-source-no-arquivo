import json
import pandas as pd
import csv

capture_count = []
selected_urls = []

with open('D:\Projetos\Programming\open-source-no-arquivo\second-collection\selected_urls_metadata.json', 'r') as f:
    json_data = json.load(f)
    for link in json_data:
        capture_count.append(link['estimated_nr_results'])

print(capture_count)

with open ('D:\Projetos\Programming\open-source-no-arquivo\second-collection\selected_urls.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
            selected_urls.append(row[0])

seed_data = pd.DataFrame(
    {
       "seed_url": selected_urls,
       "number_of_results": capture_count
     }
)

seed_data.to_csv(r'D:\Projetos\Programming\open-source-no-arquivo\second-collection\seed_data.csv')

