import selenium
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# Start up headless webdriver
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options = op)

# Navigate to website
driver.get("https://mangapark.net/title/10953-one-piece")

# Locate target element
count = driver.find_element(By.XPATH, './/body/div/div/main/div/div[5]/div[2]/div/div/div/div/div/div/a').text

# Check text on element
chapter = count.split()[-1]

print(chapter)