from selenium import webdriver
from selenium.webdriver.common.by import By

# With Selenium i can use a webdriver to read a webpage in different navigator
driver = webdriver.Chrome()
driver.get("https://meteofrance.com/previsions-meteo-france/montpellier/34000")

element = driver.find_element(By.CSS_SELECTOR,".weather_temp")
scd_element = element.find_element(By.TAG_NAME, "p").text

#  Add the .text after scd_element . Same err = GPU state invalid after WaitForGetOffsetInRange
# Reading of the doc in option part to find the solution 

print(scd_element)

driver.quit()