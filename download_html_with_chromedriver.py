from selenium import webdriver

driver = webdriver.Chrome(executable_path= r'C:\chromedriver.exe') # This fires a browser

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)
