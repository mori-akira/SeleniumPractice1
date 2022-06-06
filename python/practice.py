from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

cservice = service.Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=cservice, options=options)

driver.get('http://localhost:8888/')

h1 = driver.find_element(by=By.TAG_NAME, value='h1')
print(h1.text)
