from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

driver.get("http://gmail.com")

user = driver.find_element(By.ID,"identifierId")
user.send_keys("djbartovcp@gmail.com")
user.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element(By.NAME,"password")
password.send_keys("123456")
password.send_keys(Keys.ENTER)
driver.close()
