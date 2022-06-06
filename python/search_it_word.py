from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

cservice = service.Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=cservice, options=options)

driver.get('https://www.google.com/')

input = driver.find_element(by=By.XPATH, value='//input[@class="gLFyf gsfi"]')
input.send_keys('selenium', 'とは IT用語')
input.send_keys(Keys.ENTER)

headers = driver.find_elements(by=By.XPATH, value='//div[@id="res"]//a')

for header in headers:
    href = header.get_attribute('href')
    
