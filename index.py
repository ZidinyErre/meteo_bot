from selenium import webdriver

# With Selenium i can use a webdriver to read a webpage in different navigator
driver = webdriver.Chrome()
driver.get("https://meteofrance.com/previsions-meteo-france/montpellier/34000")

element = driver.find_element(By.CSS_SELECTOR, ".weather_temp")
scd_element = driver.find_element(By.TAG_NAME, "p")

print(element.scd_element)