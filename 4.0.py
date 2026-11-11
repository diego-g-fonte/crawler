# Este codigo quiere agarrar los links generados en 3.py, en el archivo "clean_links.txt"
# y generar oootro archivo de texto con oootra lista de links, pero ahora con los links
# estáticos a los pdfs

import requests
import re
from bs4 import BeautifulSoup

# leer los urls de "clean_links.txt"
with open('clean_links.txt', 'r') as f:
    urls = f.readlines()

# bucle por cada url
for url in urls:
    # hacer una solicitud GET y conseguir el HTML
    response = requests.get(url.strip())
    html_content = response.content

    # leer el HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # encontrar todos los frames
    frames = soup.find_all('frame')

    # acceder al segundo frame (índice 1)
    second_frame = frames[1]

    # hacerlo un string
    second_frame_str = str(second_frame)

    # conseguir el url
    pdf_path = re.search('src="([^"]+)"', second_frame_str).group(1)

    # imprimir el url
    print(pdf_path)
