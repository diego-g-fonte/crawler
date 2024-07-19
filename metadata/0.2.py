# Este hace un JSON con el autor, titulo y año de todas las tesis de 'urls_results_pages.txt'
# FALTA: que el JSON tenga un formato en el que no esten agrupada lasa cosas

import requests
from bs4 import BeautifulSoup
import json

with open('urls_results_pages.txt', 'r') as f:
    urls = f.readlines()

with open('results.json', 'w') as f:
    f.write('')

for url in urls:
    # Make a GET request to the page and get the HTML content
    response = requests.get(url.strip())
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the results table on the page
    table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})

    # Find all rows of the table and extract columns 3, 4, and 5 for each row
    results = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 5:
            col3 = cols[2].get_text(strip=True)
            col4 = cols[3].get_text(strip=True)
            col5 = cols[4].get_text(strip=True)

            start_index = col4.find("'") + 1  # index of the first quote after "title = "
            end_index = col4.find("'", start_index)  # index of the next quote
            title = col4[start_index:end_index].replace("&nbsp;", " ")
            title = title.replace(' /', '')
            title = title.replace('&rsquo;', '\'')

            results.append({'name': col3, 'title': title, 'date': col5})

    # Save the results to a JSON file
    with open('results.json', 'a') as f:
        json.dump(results, f)
        f.write('\n')
