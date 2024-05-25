import requests
import json
import csv

urls_over_25 = []
query_strings = []

with open ('D:\Projetos\Programming\open-source-no-arquivo\second-collection\over_25_results\over25.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
            urls_over_25.append(row[0])


def make_queries():
    for url in urls_over_25:
        query_strings.append("https://arquivo.pt/textsearch?prettyPrint=true&versionHistory={}&maxItems=1600".format(url))
    return query_strings

make_queries()

with open('D:\Projetos\Programming\open-source-no-arquivo\second-collection\over_25_results\over_25_metadata.json', 'w') as f:
    for query in query_strings:
        response = requests.get(query)
        json.dump(response.json(), f)
        f.write('\n')

print("URLs successfully written to json document")