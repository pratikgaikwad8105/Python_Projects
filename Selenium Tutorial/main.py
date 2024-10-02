from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)


driver = webdriver.Edge(options=edge_option)
driver.get("https://www.python.org/")

time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


driver.quit()
