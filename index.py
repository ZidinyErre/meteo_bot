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

# I  take the title or the alt of the img in .weather_temp
temp_img = element.find_element(By.TAG_NAME, "img").get_attribute("title")

# I need to understand how wind information works and take the information
wind = driver.find_element(By.CSS_SELECTOR,".wind")
wind_arrow = wind.find_element(By.TAG_NAME, "img").get_attribute("title")
wind_speed = wind.find_element(By.TAG_NAME, "strong").text 




print(temperature)
print(time_element)
print(temp_img)
print(wind_arrow)
print(wind_speed, "Km/h")

# I need to make two arrays (or another way to keep data) to store the wind direction and is speed 

# I need to find how i can send data to my phone by is number 


driver.quit()

#           N
#       NO     NE
#    O             E
#       SO     SE
#           S


# Vents principaux (8) :

# N (Nord) → Froid, sec en hiver.

# NE (Nord-Est) → Froid et sec (continental).

# E (Est) → Sec, parfois froid (continental).

# SE (Sud-Est) → Chaud, humide (méditerranéen).

# S (Sud) → Chaud, humide.

# SO (Sud-Ouest) → Doux, humide (océanique).

# O (Ouest) → Humide, perturbé (océanique).

# NO (Nord-Ouest) → Frais, humide (océanique).



# Intermédiaires (16-vents) :

# NNE (Nord-Nord-Est) → Froid, sec.

# ENE (Est-Nord-Est) → Sec, frais.

# ESE (Est-Sud-Est) → Doux, sec/humide selon saison.

# SSE (Sud-Sud-Est) → Chaud, humide.

# SSO (Sud-Sud-Ouest) → Doux, humide.

# OSO (Ouest-Sud-Ouest) → Doux, humide, perturbé.

# ONO (Ouest-Nord-Ouest) → Frais, humide.

# NNO (Nord-Nord-Ouest) → Frais, humide, souvent instable.


# | Force | Nom court                        | Vitesse (km/h) | Effet observé                                             |
# | ----- | -------------------------------- | -------------- | --------------------------------------------------------- |
# | 0     | Calme                            | < 1            | La fumée monte verticalement, pas de vent.                |
# | 1–3   | Brise légère                     | 1–19           | Les feuilles bougent, drapeaux se lèvent légèrement.      |
# | 4–5   | Jolie brise / Bonne brise        | 20–38          | Branches bougent, vagues légères.                         |
# | 6–7   | Vent frais / Grand frais         | 39–61          | Arbres bougent, marche contre le vent perceptible.        |
# | 8–9   | Coup de vent / Fort coup de vent | 62–88          | Arbres secoués, vagues importantes, difficile de marcher. |
# | 10–11 | Tempête / Forte tempête          | 89–117         | Gros arbres bougent, dommages possibles, mer agitée.      |
# | 12    | Ouragan                          | ≥ 118          | Dégâts généralisés, vents très violents.                  |
