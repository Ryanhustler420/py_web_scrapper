from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--profile-directory=Default') 

driver = webdriver.Chrome(options = options, executable_path= r'C:\chromedriver.exe') # This fires a browser

driver.get('http://python.org')

html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup)

driver.quit()