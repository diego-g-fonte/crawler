# Necesita no existir "pdf_links.txt"
# Define the function to transform a URL to a PDF link
def transform_url_to_pdf(url):
    # Extract relevant parts of the URL
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

# Input and output file paths
input_file_path = 'static_urls2.txt'
output_file_path = 'pdf_links.txt'

# Read the input URLs from the file
with open(input_file_path, 'r') as input_file:
    input_urls = input_file.read().splitlines()

# Transform the URLs and store them in a list
pdf_links = [transform_url_to_pdf(url) for url in input_urls]

print(pdf_links)

# Write the transformed PDF links to the output file
with open(output_file_path, 'w') as output_file:
    for pdf_link in pdf_links:
        output_file.write(pdf_link + '\n')

print(f"Transformed URLs saved to {output_file_path}")
