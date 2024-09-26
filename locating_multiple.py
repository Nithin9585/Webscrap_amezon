from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "pants"
for q in range(1,5):
 driver.get(f"https://www.amazon.in/s?k={query}&page={q}&crid=21ZBQMMJBJEV8&sprefix=pants%2Caps%2C814&ref=nb_sb_noss_1")
 elems = driver.find_elements(By.CLASS_NAME , "puis-card-container")
 print(f"{len(elems)} items found ............... ")
 for elem in elems:
     print(elem.text)
 driver.close()