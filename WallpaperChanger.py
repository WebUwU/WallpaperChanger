import os
import requests
import ctypes
from urllib.parse import urlparse



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

def get_valid_image_url():
        if not (url.startswith("http://") or url.startswith("https://")):
            print("Invalid URL. Please include 'http://' or 'https://' in the URL.")
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            print("Invalid URL. Please enter a valid image URL.")
        return url

image_url = get_valid_image_url()



response = requests.get(url)
with open(f"{temp_dir}/myImage.png", 'wb') as f:
    f.write(response.content)

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, f"{temp_dir}/myImage.png" , 0)
