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

# Path to Chromium executable
chrome_path = '/usr/bin/chromium'

# Path to the Chrome driver
chrome_driver_path = '/data/Documents/UNAM/titulacion/codigo/crawler/chrome_driver/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the Service object
driver = webdriver.Chrome(service=service)

# Read in the URLs from the text file
with open('clean_links.txt', 'r') as f:
    urls = f.readlines()

# Clear the contents of the redirected_urls.txt file
with open("static_urls.txt", "w") as file:
    file.write("")

# Loop for every line in clean_links.txt
for url in urls:
    # Load the initial URL
    original_url = url
    driver.get(original_url)

    # Get the current URL after the redirect
    redirected_url = driver.current_url

    with open("static_urls.txt", "a") as f_out:
        f_out.write(redirected_url + "\n")

# Close the browser
driver.quit()


