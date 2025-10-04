from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os 
from dotenv import load_dotenv

load_dotenv()

test_key = os.getenv("TEST")
test_key_2 = os.getenv("TEST_2")

print(test_key)
print(test_key_2)

# With Selenium i can use a webdriver to read a webpage in different navigator

# Here i can make option and use the driver in different way. I disable the GPU because the script 
# do not support the use of the graphic cards
options = Options()
# the option headless mean we not gonna see our bot act 
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

driver.get("https://meteofrance.com/previsions-meteo-france/montpellier/34000")

# I  make two arrays  to store the wind direction and is speed 

wind_dict ={ "N": {"name": "Nord" , "description" : " Froid, sec en hiver. "},"NE": {"name": "Nord-Est" , "description" : " Froid et sec (continental). "},"E": {"name": " Est " , "description" : " Sec, parfois froid (continental). "},"SE": {"name": " Sud-Est " , "description" : " Chaud, humide (méditerranéen). "},"S": {"name": " Sud " , "description" : " Chaud, humide. "},"SO": {"name": " Sud-Ouest " , "description" : " Doux, humide (océanique). "},"O": {"name": " Ouest " , "description" : " Humide, perturbé (océanique). "},"NO": {"name": " Nord-Ouest " , "description" : " Frais, humide (océanique). "},  
"NNE": {"name": " Nord-Nord-Est " , "description" : " Froid, sec. "},"ENE": {"name": " Est-Nord-Est " , "description" : " Sec, frais. "},"ESE": {"name": " Est-Sud-Est " , "description" : "Doux, sec/humide selon saison. "},"SSE": {"name": " Sud-Sud-Est " , "description" : " Chaud, humide. "},"SSO": {"name": " Sud-Sud-Ouest " , "description" : "  Doux, humide. "},"OSO": {"name": " Ouest-Sud-Ouest " , "description" : " Doux, humide, perturbé. "},"ONO": {"name": " Ouest-Nord-Ouest " , "description" : " Frais, humide. "},"NNO": {"name": " Nord-Nord-Ouest " , "description" : " Frais, humide, souvent instable. "}}


def compass(the_wind_direction):
    for x in wind_dict:
        if x == the_wind_direction:
            print("Vent" , wind_dict[x]["name"], "/", wind_dict[x]["description"]) 

beaufort_dict = {
    0: {"name": "Calme", "speed": (0, 0), "effect": "La fumée monte verticalement, pas de vent."},
    1: {"name": "Brise légère", "speed": (1, 19), "effect": "Les feuilles bougent, drapeaux se lèvent légèrement."},
    4: {"name": "Jolie brise / Bonne brise", "speed": (20, 38), "effect": "Branches bougent, vagues légères."},
    6: {"name": "Vent frais / Grand frais", "speed": (39, 61), "effect": "Arbres bougent, marche contre le vent perceptible."},
    8: {"name": "Coup de vent / Fort coup de vent", "speed": (62, 88), "effect": "Arbres secoués, vagues importantes, difficile de marcher."},
    11: {"name": "Tempête / Forte tempête", "speed": (89, 117), "effect": "Gros arbres bougent, dommages possibles, mer agitée."},
    12: {"name": "Ouragan", "speed": (118), "effect": "Dégâts généralisés, vents très violents."},
}

# I need to make a function who take the speed of the wind and output the name and the effect
def beaufort_from_speed(the_speed):
    if the_speed >= 1 or the_speed <= 19 : 
        print(beaufort_dict[1]["name"] , ".", beaufort_dict[1]["effect"])

    elif the_speed >= 20 or the_speed  <= 38: 
        print(beaufort_dict[4]["name"] ,".", beaufort_dict[4]["effect"])

    elif the_speed >= 39 or the_speed <= 61:  
        print(beaufort_dict[6]["name"] ,".", beaufort_dict[6]["effect"])

    elif the_speed >= 62 or the_speed <= 88 : 
        print(beaufort_dict[8]["name"] ,".", beaufort_dict[8]["effect"])

    elif the_speed >= 89 or the_speed <= 117: 
        print(beaufort_dict[11]["name"] ,".", beaufort_dict[11]["effect"])

    elif the_speed >= 118: 
        print(beaufort_dict[12]["name"] ,".", beaufort_dict[12]["effect"])

    else: 
        print(beaufort_dict[0]["name"] ,".", beaufort_dict[10]["effect"])

    


# | Force | Nom court                        | Vitesse (km/h) | Effet observé                                             |
# | ----- | -------------------------------- | -------------- | --------------------------------------------------------- |
# | 0     | Calme                            | < 1            | La fumée monte verticalement, pas de vent.                |
# | 1–3   | Brise légère                     | 1–19           | Les feuilles bougent, drapeaux se lèvent légèrement.      |
# | 4–5   | Jolie brise / Bonne brise        | 20–38          | Branches bougent, vagues légères.                         |
# | 6–7   | Vent frais / Grand frais         | 39–61          | Arbres bougent, marche contre le vent perceptible.        |
# | 8–9   | Coup de vent / Fort coup de vent | 62–88          | Arbres secoués, vagues importantes, difficile de marcher. |
# | 10–11 | Tempête / Forte tempête          | 89–117         | Gros arbres bougent, dommages possibles, mer agitée.      |
# | 12    | Ouragan                          | ≥ 118          | Dégâts généralisés, vents très violents.                  |


element = driver.find_element(By.CSS_SELECTOR,".weather_temp")
temperature = element.find_element(By.TAG_NAME, "p").text

# I  take the time 
# To Have the "soirée" part i can make a if time_element variable by tag_name p = "Soirée" then tell me (temp , weather)
time_element = driver.find_element(By.CSS_SELECTOR, ".period").text

# I  take the title or the alt of the img in .weather_temp
temp_img = element.find_element(By.TAG_NAME, "img").get_attribute("title")

# I  understand how wind information works and take the information
wind = driver.find_element(By.CSS_SELECTOR,".wind")
wind_arrow = wind.find_element(By.TAG_NAME, "img").get_attribute("title")
wind_speed = wind.find_element(By.TAG_NAME, "strong").text 
# I split the wind to only have the wind direction 
wind_arrow_split = wind_arrow.split()




print(temperature)
print(time_element)
print(temp_img)
print(wind_arrow)
print(wind_speed, "Km/h")
beaufort_from_speed(int(wind_speed))
compass(wind_arrow_split[1])


# I need to find how i can send data to my mail

driver.quit()

#           N
#       NO     NE
#    O             E
#       SO     SE
#           S









