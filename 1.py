# Este código es obsoleto.

import requests
from bs4 import BeautifulSoup

# Define the URL of the search results page
url = "https://tesiunam.dgb.unam.mx/F/TVE8ACS32EQKSTSQAKK2BCSN3RH9196Q7XYUT28983KPJHRHVM-34908?func=short-jump&jump=000001"

# Make a GET request to the page and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the results table on the page
table = soup.find("table", {"class": "table table-bordered table-hover table-sm"})
print("TABLE", table)

# Find all rows in the table (excluding the header row)
rows = table.find_all("tr")[1:]

# Extract the links from the sixth column of each row
links = []
for row in rows:
    cells = row.find_all("td")
    link = cells[5].find("a")["href"]
    links.append(link)

# Save the links to a text file
with open("links.txt", "w") as file:
    file.write("\n".join(links))
