# Esto saca los links de "Texto completo" de los URLs que estén en el archivo "urls.txt"
# 'urls.txt' necesita tener todos los URLs de todas las páginas de resultados de tesiunam
# de las cuales queramos sacar las tesis. 
# Se tiene que hacer justo antes de correr el código
# porque los URLs son únicos a una sesión que expira después de como 15 min.

# Hay tres trabajos de titulación que no están disponibles, pero que aún así aparecen en
# la lista de resultados. Esto hace que el código se detenga, pues la casilla que busca
# está vacía. Yo arreglo esto quitando el link de esos resultados de 'urls.txt' y luego
# copiando manualmente los URLs a 'links.txt'

import requests
from bs4 import BeautifulSoup

# Clear the contents of the links.txt file
with open("links.txt", "w") as file:
    file.write("")

# Read in the URLs from the text file
with open('urls.txt', 'r') as f:
    urls = f.readlines()

# Loop over each URL
for url in urls:
    # Make a GET request to the page and get the HTML content
    response = requests.get(url.strip())
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the results table on the page
    table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})
    print("TABLE", table)

    # Find all rows in the table (excluding the header row)
    rows = table.find_all("tr")[1:]

    # Extract the links from the sixth column of each row
    links = []
    for row in rows:
        cells = row.find_all("td")
        link = cells[5].find("a")["href"]
        links.append(link)

    # Save the links to a text file
    with open("links.txt", "a") as file:
        file.write("\n".join(links) + "\n")
