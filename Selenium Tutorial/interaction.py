from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=option)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Pratik")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Gaikwad")

lname = driver.find_element(By.NAME, "email")
lname.send_keys("gaikwadpratik8105@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()