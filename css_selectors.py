from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Lesson 3 CSS selector:

# ID
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# Class
driver.find_element(By.CSS_SELECTOR, "a-color-state a-text-bold")

# Portal Attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_em_cs_bestsellers")

# Travelling through nodes
driver.find_element(By.CSS_SELECTOR, "div#nav-xshop-container #nav-xshop a")



