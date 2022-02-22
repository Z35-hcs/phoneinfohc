GNU nano 6.2                                  phoneinfohc.py
import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'                                                                                      CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print(RED+"/  |/  /__  _  __(_)________ _____     _________  ____/ /__  __________")
print("   / /|_/ / _ \| |/_/ / ___/ __ `/ __ \   / ___/ __ \/ __  / _ \/ ___/ ___/")
print("  / /  / /  __/>  </ / /__/ /_/ / / / /  / /__/ /_/ / /_/ /  __/ /  (__  )")
print(" /_/  /_/\___/_/|_/_/\___/\__,_/_/ /_/   \___/\____/\__,_/\___/_/  /____/")

print("\033[33m--------------------------------------")
print(YELLOW+"Autor    : Hc alainn")
print("--------------------------------------")
print("INSTAGRAM: 66alainn")
print("--------------------------------------")
print("TIK TOK  : 66alainn")
print("-------------------------------------- \n")
print(GREEN+"escribe el numero de telefono junto\ncon el prefijo, ejemplo: +523313002435\n")

api_key = '31e04799e5b72d22be4bed51565ddadb'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (a>

for key, value in data.json().items():

print("%s: %s" % (key, value))
