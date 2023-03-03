import os
import requests
import ctypes



print("""

 █     █░ ██▓███   ▄████▄   ██░ ██  ▄▄▄       ███▄    █   ▄████ ▓█████  ██▀███  
▓█░ █ ░█░▓██░  ██▒▒██▀ ▀█  ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▓██░ ██▓▒▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓ ▒██▒ ░  ░▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒  ▒▓▒░ ░  ░░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░  ░▒ ░       ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
  ░   ░  ░░       ░         ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
    ░             ░ ░       ░  ░  ░      ░  ░         ░       ░    ░  ░   ░     
                  ░                                                             """)


temp_dir = os.environ['TEMP']

url = input("Please enter the URL of the image: ")

response = requests.get(url)
if response.status_code != 200:
    print("Error: Invalid URL or unable to download image.")
    exit()

with open(f"{temp_dir}/myImage.png", 'wb') as f:
    f.write(response.content)

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, f"{temp_dir}/myImage.png", 0)
