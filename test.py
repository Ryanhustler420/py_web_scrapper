from selenium import webdriver

driver = webdriver.Chrome(executable_path= r'C:\chromedriver.exe') # This fires a browser
# webdriver.PhantomJS() # This helps us to prevent chrome window in the middle of the operation
# webdriver.firefox() # also an option

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)
