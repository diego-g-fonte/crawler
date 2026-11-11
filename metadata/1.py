# Este código genera los links de las páginas de resultados de tesiunam
# usando un loop que busca y entra los links del botón "Siguiente"

# Antes de usarlo hay que crear un archivo llamado "url_manual.txt"
# con el URL de la primera página de resultados, y uno llamado
# "urls_results_pages.txt"

# Hay que checar manualmente el numero de iteraciones del loop del final

import requests
from bs4 import BeautifulSoup
import re

# Sacar el url de la primera página de resultados
with open('url_manual.txt', 'r') as f:
    url_manual = f.readlines()
    url_manual = url_manual[0]

# añadir el primer url a a la variable "url_list"
url_list = list()
url_list.append(url_manual)

# Vaciar "urls_results_pages.txt"
with open('urls_results_pages.txt', 'w') as f:
    f.write("")

# Hacer una solicitud GET a la página y conseguir el contenido HTML
response = requests.get(url_manual)
html_content = response.content

# Hacer una soup de la primera página de resultados
soup = BeautifulSoup(html_content, "html.parser")

# Encontrar el link de "Siguiente"
next_page_link = soup.find_all('a', title="Next")
next_page_link = str(next_page_link)

# Sacar el url usando regex
match = re.search(r'href="(.*?)"', next_page_link)
url = match.group(1)
url = url.replace('&amp;', '&')

# añadir el segundo url a 'url_list'
url_list.append(url)

# bucle que consigue y le pone enter al link "siguiente" INCOMPLETO
url_loop = url

for i in range(46):     # El numero es 46, porque son 48 páginas de resultados
                        # de hoy al 2006, pero si cambian las cosas hay que cambiar el numero
    # Extrae el url de la pagina siguiente y lo agrega a url_list
    response_loop = requests.get(url_loop)
    html_content_loop = response_loop.content
    soup_loop = BeautifulSoup(html_content_loop, "html.parser")
    next_page_link_loop = soup_loop.find_all('a', title="Next")
    next_page_link_loop = str(next_page_link_loop)
    match_loop = re.search(r'href="(.*?)"', next_page_link_loop)
    url_loop = match_loop.group(1)
    url_loop = url_loop.replace('&amp;', '&')
    url_list.append(url_loop)

# guarda los links a un .txt
with open("urls_results_pages.txt", "a") as file:
    file.write("\n".join(url_list) + "\n")
