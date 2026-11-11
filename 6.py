import os
import requests

with open('test_links.txt', 'r') as file:
    pdf_links = file.readlines()


download_directory = 'pdfs'
os.makedirs(download_directory, exist_ok=True)

for link in pdf_links:
    link = link.strip()  # quitar caracteres vacíos
    response = requests.get(link)

    if response.status_code == 200:
        pdf_name = link.split('/')[-1]  # sacar el nombre del pdf del url
        pdf_path = os.path.join(download_directory, pdf_name)

        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

        print(f"Downloaded: {pdf_name}")
    else:
        print(f"Failed to download: {link}")
