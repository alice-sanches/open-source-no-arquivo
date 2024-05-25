import requests
import json
import csv

selected_urls = []
query_strings = []

with open ('D:\Projetos\Programming\open-source-no-arquivo\Selected URLs\selected_urls.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
            selected_urls.append(row[0])


def make_queries():
    for url in selected_urls:
        query_strings.append("https://arquivo.pt/textsearch?prettyPrint=true&versionHistory={}&maxItems=25".format(url))
    return query_strings

make_queries()

with open('D:\Projetos\Programming\open-source-no-arquivo\Selected URLs\selected_urls_metadata.json', 'w') as f:
    for query in query_strings:
        print(query)
        response = requests.get(query)
        print(response)
        json.dump(response.json(), f)
        f.write('\n')

print("URLs successfully written to json document")