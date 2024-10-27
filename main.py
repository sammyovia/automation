from selenium import webdriver

driver = webdriver.Chrome()  # No need to specify path if added to PATH
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
