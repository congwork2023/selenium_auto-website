from selenium import webdriver
from time import sleep

chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_option) #không cần thêm path của chromedriver.exe như phiên bản cữ

driver.get("https://www.google.com")
sleep(6)
driver.get("https://www.python.org")
sleep(2)
driver.back()
sleep(2)