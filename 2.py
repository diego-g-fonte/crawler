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

# vaciar "links.txt"
with open("links.txt", "w") as file:
    file.write("")

# leer los urls de "urls.txt"
with open('urls.txt', 'r') as f:
    urls = f.readlines()

# bucle por cada url
for url in urls:
    # hacer una solicitud GET y conseguir el HTML
    response = requests.get(url.strip())
    html_content = response.content

    # leer el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # encontrar la tabla de resultados
    table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})
    print("TABLE", table)

    # encontrar todas las filas en la tabla, excepto la fila header
    rows = table.find_all("tr")[1:]

    # extraer los links de la sexta columna de cada fila
    links = []
    for row in rows:
        cells = row.find_all("td")
        link = cells[5].find("a")["href"]
        links.append(link)

    # guardar los links a un .txt
    with open("links.txt", "a") as file:
        file.write("\n".join(links) + "\n")
