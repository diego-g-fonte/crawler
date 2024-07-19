from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.Chrome('/data/Diego/UNAM/Titulacion/codigo/selenium_chrome_driver/')

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/app/chromium'
driver = webdriver.Chrome(options=chrome_options)

url = 'https://tesiunam.dgb.unam.mx:443/F/XC5E5BQTJ8S67CC11UAV4HNQPKDCJ8F2NE97D7C242B1AGC8LN-11464?func=service&doc_library=TES01&doc_number=000834775&line_number=0001&func_code=WEB-BRIEF&service_type=MEDIA'

# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
browser = webdriver.Chrome(options=options)

# Load the initial URL
browser.get(url)

# Extract the final URL after the redirection
redirect_url = browser.current_url

# Load the final URL
browser.get(redirect_url)

# Extract the PDF path from the HTML content
soup = BeautifulSoup(browser.page_source, 'html.parser')
pdf_path = soup.find_all('frame')[1]['src']

# Print the PDF path
print(pdf_path)

# Quit the browser
browser.quit()
