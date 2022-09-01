
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Celal/Documents/pythonProject/Seleniums/chromedriver.exe')
url="https://btkakademi.gov.tr"
driver.get(url)