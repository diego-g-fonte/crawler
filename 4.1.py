import requests
import re
from bs4 import BeautifulSoup









# Make a GET request to the page and get the HTML content
response = requests.get("https://tesiunam.dgb.unam.mx:443/F/68J2MIK3ILB7CNYRYNJ8IJS4DSVRUAERQHEFXVIIRFXFGM8PFB-37893?func=service&doc_library=TES01&doc_number=000834775&line_number=0001&func_code=WEB-BRIEF&service_type=MEDIA", allow_redirects=True)

# Get the URL of the redirected page
redirected_url = response.url
print(redirected_url)

# Make a GET request to the redirected page
response = requests.get(redirected_url)

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
