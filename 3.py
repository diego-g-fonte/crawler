# Este código solamente limpia los links con javascript que saco de la página de resultados de tesiunam
# Agarra los links del archivo "links.txt" y los saca en uno que se llama "clean_links.txt"

import re

input_file = "links.txt"
output_file = "clean_links.txt"

# Clear the contents of the links.txt file
with open(output_file, "w") as file:
    file.write("")

url_regex = r'"(https?://.*?)"'

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        urls = re.findall(url_regex, line)
        for url in urls:
            f_out.write(url + "\n")
