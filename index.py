from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# With Selenium i can use a webdriver to read a webpage in different navigator

# Here i can make option and use the driver in different way. I disable the GPU because the script 
# do not support the use of the graphic cards
options = Options()
# the option headless mean we not gonna see our bot act 
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

driver.get("https://meteofrance.com/previsions-meteo-france/montpellier/34000")

element = driver.find_element(By.CSS_SELECTOR,".weather_temp")
temperature = element.find_element(By.TAG_NAME, "p").text

# I need to take the time in .period
# To Have the "soirée" part i can make a if time_element variable by tag_name p = "Soirée" then tell me (temp , weather)
time_element = driver.find_element(By.CSS_SELECTOR, ".period").text

print(temperature)
print(time_element)

# I need to take the title or the alt of the img in .weather_temp
# I need to understand how wind information wroks and take the information


# I need to find how i can send data to my phone by is number 


driver.quit()