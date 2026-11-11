# Este hace un JSON con el autor, titulo y año de todas las tesis de 'urls_results_pages.txt'
# FALTA: que el JSON tenga un formato en el que no esten agrupadas las cosas

import requests
from bs4 import BeautifulSoup
import json

with open('urls_results_pages.txt', 'r') as f:
    urls = f.readlines()

with open('results.json', 'w') as f:
    f.write('')

for url in urls:
    # hacer un pedido GET y conseguir el HTML
    response = requests.get(url.strip())
    html_content = response.content

    # Leer el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontrar la tabla de resultados
    table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})

    # Encontrar todas las filas y extraer las columnas 3, 4 y 5 de cada fila
    results = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 5:
            col3 = cols[2].get_text(strip=True)
            col4 = cols[3].get_text(strip=True)
            col5 = cols[4].get_text(strip=True)

            start_index = col4.find("'") + 1  # índice de la primera comilla después de "title = "
            end_index = col4.find("'", start_index)  # índice de la siguiente comilla
            title = col4[start_index:end_index].replace("&nbsp;", " ")
            title = title.replace(' /', '')
            title = title.replace('&rsquo;', '\'')

            results.append({'name': col3, 'title': title, 'date': col5})

    # guardar resultados a un .JSON
    with open('results.json', 'a') as f:
        json.dump(results, f)
        f.write('\n')
