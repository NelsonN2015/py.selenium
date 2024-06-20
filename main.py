from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# A classe Service é usada para iniciar uma instância do Chrome WebDriver
service = Service()

# webdriver.ChromeOptions é usado para definir a preferência para o browser do Chrome
options = webdriver.ChromeOptions()

# Inicia-se a instância do Chrome WebDriver com as definidas 'options' e 'service'
driver = webdriver.Chrome(service=service, options=options)

url = 'https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090'
driver.get (url)

driver.find_elements(By.TAG_NAME, 'a')

