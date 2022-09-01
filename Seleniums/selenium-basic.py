from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/Users/Celal/Documents/pythonProject/Seleniums/chromedriver.exe')
url= ("https://github.com")
driver.get(url)
time.sleep(2)
driver.maximize_window()
# driver.save_screenshot("github.com_home_page.png")
url= ("https://github.com/k-celal")
driver.get(url)
print(driver.title)
if "k-celal" in driver.title:
    driver.save_screenshot("github-kcelal.png")
driver.back
time.sleep(2)
driver.close()