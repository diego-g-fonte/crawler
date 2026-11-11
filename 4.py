# 4.0.py, 4.1.py, y 4.2.py son versiones que no funcionan. Esta es la buena

# Este codigo agarra los links generados en 3.py, en el archivo "clean_links.txt"
# y genera oootro archivo de texto con oootra lista de links, pero ahora con los links
# estáticos a las páginas de tesiunam que muestran los pdfs que empiezan con 132.248.9.195.
# Los saca a 'static_urls.txt'. Luego yo copio los urls estáticos de las tres páginas de
# resultados en las que están los trabajos de titulación que no están en tesiunam.

# Todavía falta hacer otro que descargue los pdfs.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# dirección de chromium
chrome_path = '/usr/bin/chromium'

# dirección de chromedriver
chrome_driver_path = '/data/Documents/UNAM/titulacion/codigo/crawler/chrome_driver/chromedriver'

# hacer un objeto tipo service
service = Service(executable_path=chrome_driver_path)

# inicializar chromium con el objeto Service
driver = webdriver.Chrome(service=service)

# Leer los urls de "clean_links.txt"
with open('clean_links.txt', 'r') as f:
    urls = f.readlines()

# vaciar "static_urls.txt"
with open("static_urls.txt", "w") as file:
    file.write("")

# bucle por cada línea en "clean_links.txt"
for url in urls:
    # cargar el url inicial
    original_url = url
    driver.get(original_url)

    # conseguir el url actual después de la redirección
    redirected_url = driver.current_url

    with open("static_urls.txt", "a") as f_out:
        f_out.write(redirected_url + "\n")

# cerrar el buscador
driver.quit()
