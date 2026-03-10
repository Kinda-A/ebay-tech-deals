from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
import os

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/globaldeals/tech")

time.sleep(5)

for i in range(12):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


    products = driver.find_elements(By.CSS_SELECTOR, ".dne-itemtile")
    print("Products found:", len(products))


    data = []

for product in products:

    try:
        title = product.find_element(By.CSS_SELECTOR, ".dne-itemtile-title").text
    except:
        title = "N/A"

    try:
        price = product.find_element(By.CSS_SELECTOR, ".dne-itemtile-price").text
    except:
        price = "N/A"

    try:
        original_price = product.find_element(By.CSS_SELECTOR, ".dne-itemtile-original-price").text
    except:
        original_price = "N/A"

    try:
        shipping = product.find_element(By.CSS_SELECTOR, ".dne-itemtile-delivery").text
    except:
        shipping = "N/A"

    try:
        item_url = product.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        item_url = "N/A"

    timestamp = datetime.now()

    data.append([
        timestamp,
        title,
        price,
        original_price,
        shipping,
        item_url
    ])


    



df = pd.DataFrame(data, columns=[
    "timestamp",
    "title",
    "price",
    "original_price",
    "shipping",
    "item_url"
])

print("Rows collected:", len(data))

file = "ebay_tech_deals.csv"

if os.path.exists(file):
    df.to_csv(file, mode="a", header=False, index=False)
else:
    df.to_csv(file, index=False)

print("CSV file saved!")

driver.quit()