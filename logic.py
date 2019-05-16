from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# Collect user input for zip code

# Automation Section
driver = webdriver.Chrome()
driver.get("https://weather.com/")

# Scraping Section
url = "https://weather.com/"
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser') #this may need be changed to lxml, depending on site
print(soup.prettify())

# Request zip code