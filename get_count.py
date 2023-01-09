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
driver.get("https://ww2.readonepiece.com")

# Locate target element
count = driver.find_element(By.XPATH, './/body/div[3]/div/div/div[6]/div/div/a').text

# Check text on element
chapter = count.split()[-1]