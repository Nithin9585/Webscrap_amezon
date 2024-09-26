from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "pants"
driver.get(f"https://www.amazon.in/s?k={query}&crid=21ZBQMMJBJEV8&sprefix=pants%2Caps%2C814&ref=nb_sb_noss_1")
elem = driver.find_element(By.CLASS_NAME , "sg-col-inner")
print(elem.get_attribute("outerHTML"))
driver.close()