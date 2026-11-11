# Necesita no existir "pdf_links.txt"
# definir la función que transforma un url a un link de pdf
def transform_url_to_pdf(url):
    # extraer las partes relevantes del url
    parts = url.split('/')
    month = parts[-3]
    code = parts[-2]
    year = parts[-4]

    if len(parts) == 7:
        pdf_link = f"http://132.248.9.195/pdfviewer?file=/{year}/{month}/{code}/{code}.pdf"
    elif len(parts) == 8:    
        code = parts[-2]
        year = parts[-5]
        pdf_link = f"http://132.248.9.195/pdfviewer?file=/{year}/anteriores/filosofia/{code}/{code}.pdf"
    elif len(parts) == 6:
        code = parts[-2]
        year = parts[-3]
        pdf_link = f"http://132.248.9.195/pdfviewer?file=/{year}/{code}/{code}.pdf"    

    return pdf_link

# Input y output de links
input_file_path = 'static_urls2.txt'
output_file_path = 'pdf_links.txt'

# leer los urls input
with open(input_file_path, 'r') as input_file:
    input_urls = input_file.read().splitlines()

# transformar los urls y guardarlos en una lista
pdf_links = [transform_url_to_pdf(url) for url in input_urls]

print(pdf_links)

# escribir los urls transformados en "pdf_links.txt"
with open(output_file_path, 'w') as output_file:
    for pdf_link in pdf_links:
        output_file.write(pdf_link + '\n')

print(f"Transformed URLs saved to {output_file_path}")
