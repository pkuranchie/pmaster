from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/papa/repo/pmaster/chromedriver")

driver.get(' https://www.amazon.com/gp/help/customer/display.html ')

driver.find_element(By.ID, 'helpsearch').send_keys(' Cancel order' + Keys.RETURN)

actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
print(actual_result)
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result} '

driver.quit()
