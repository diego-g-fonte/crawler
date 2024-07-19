from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Path to Chromium executable
chrome_path = '/usr/bin/chromium'

# Path to the Chrome driver
chrome_driver_path = '/data/Diego/UNAM/Titulacion/codigo/selenium_chrome_driver/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the Service object
driver = webdriver.Chrome(service=service)

# Load the initial URL
url = "https://tesiunam.dgb.unam.mx:443/F/E7NPU2GQEGS3HB39JV67P6BQGEY24LCQ5QKKAP5Y12IXBFFYIN-13342?func=service&doc_library=TES01&doc_number=000834775&line_number=0001&func_code=WEB-BRIEF&service_type=MEDIA"
driver.get(url)

# Get the current URL after the redirect
redirected_url = driver.current_url

# Close the browser
driver.quit()

# Print the redirected URL
print(redirected_url)
