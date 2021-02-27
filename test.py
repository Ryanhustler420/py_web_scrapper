from selenium import webdriver

driver = webdriver.Chrome(executable_path= r'C:\chromedriver.exe') # This fires a browser
# driver = webdriver.PhantomJS(executable_path= r'C:\phantomjs-1.9.2-windows\phantomjs.exe') # This helps us to prevent chrome window in the middle of the operation
# webdriver.firefox() # also an option

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)
