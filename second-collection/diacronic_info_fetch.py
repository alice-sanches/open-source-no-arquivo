import json
import pandas as pd
import re
# from selected_urls import selected_urls

capture_count = []

with open('D:\Projetos\Programming\open-source-no-arquivo\second-collection\selected_urls_metadata.json', 'r') as metadata:
    json_data = json.load(metadata)
    for link in metadata:
        capture_count.append('estimated_nr_results')

print(capture_count)

