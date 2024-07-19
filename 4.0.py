# Este codigo quiere agarrar los links generados en 3.py, en el archivo "clean_links.txt"
# y generar oootro archivo de texto con oootra lista de links, pero ahora con los links
# estáticos a los pdfs

import requests
import re
from bs4 import BeautifulSoup

# Read in the URLs from the text file
with open('clean_links.txt', 'r') as f:
    urls = f.readlines()

# Loop over each URL
for url in urls:
    # Make a GET request to the page and get the HTML content
    response = requests.get(url.strip())
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all frames in the HTML content
    frames = soup.find_all('frame')

    # Access the second frame (index 1)
    second_frame = frames[1]

    # Make it a string
    second_frame_str = str(second_frame)

    # Get the url
    pdf_path = re.search('src="([^"]+)"', second_frame_str).group(1)

    # Print the path to the PDF file
    print(pdf_path)
