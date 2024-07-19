# Esto saca la tabla del link de 'url_manual.txt'
# Hace falta esto:
#   1. que este codigo limpie los resultados de la tabla para solamente tener
#      el nombre, el titulo y la fecha
#   2. lograr sacar esos tres datos a un archivo JSON
#   3. loopear este codigo para que extraiga la info de cada link en 'urls_results_pages.txt'

import requests
from bs4 import BeautifulSoup
import re
import json

# Get the URL for the first results page
with open('url_manual.txt', 'r') as f:
    url_manual = f.readlines()
    url_manual = url_manual[0]

# Make a GET request to the page and get the HTML content
response = requests.get(url_manual)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the results table on the page
table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})

# Find all rows of the table
rows = table.find_all('tr')

# Loop through rows and extract columns 3, 4, and 5
authors = list()
titles = list()
dates = list()

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 5:
        col3 = cols[2].get_text(strip=True)
        col4 = cols[3].get_text(strip=True)
        col5 = cols[4].get_text(strip=True)

        start_index = col4.find("'") + 1  # index of the first quote after "title = "
        end_index = col4.find("'", start_index)  # index of the next quote
        title = col4[start_index:end_index].replace("&nbsp;", " ")
        title = title.replace(' /', '') # limpiar los finales y corregir los apostrofes
        title = title.replace('&rsquo;', '\'')

        authors.append(col3)
        titles.append(title)
        dates.append(col5)

# Hasta aqui funciona. Lo que hace hasta aui es que 'authors', 'titles', y 'dates' son listas
# con los autores, los titulos y los años de publicacion de las tesis del archivo 'url_manual.txt'

# Create a list of dictionaries with the data
data = []
for i in range(len(authors)):
    row = {
        'author': authors[i],
        'title': titles[i],
        'date': dates[i]
    }
    data.append(row)

# Write the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)
        
