from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

query = "pants"
file = 0

# Ensure the 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

try:
    # Loop through pages (Amazon typically supports up to a certain number of pages)
    for q in range(1, 10):
        driver.get(f"https://www.amazon.in/s?k={query}&page={q}")
        
        # Adding a sleep to allow the page to load (could also use explicit waits)
        time.sleep(3)

        # Use a more reliable selector such as XPATH or CSS selector if CLASS_NAME is dynamic
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")  # Adjust if needed
        
        print(f"{len(elems)} items found on page {q} ............... ")

        # Save each element's HTML
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1

finally:
    # Ensure the driver is closed after the script finishes or if an error occurs
    driver.quit()
