from selenium import webdriver
from bs4 import BeautifulSoup

import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()
# driver.get("http://www.python.org")

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

driver.get("http://localhost:3001/")
print(driver.current_url)
driver.quit()
