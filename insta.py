import random
import requests
import pyfiglet
import time
import webbrowser
open.webbrowser('https://t.me/lagontech')
from colorama import Fore, Style, init
Z1 = '\x1b[2;31m'
B = '\x1b[2;36m'

text = "4L Bulucu"

# ASCII art oluştur
ascii_banner = pyfiglet.figlet_format(text)

# ASCII art'ı küçült
ascii_banner_lower = ascii_banner.lower()

# Renklendirilmiş olarak ekrana yazdır
print(Fore.RED + ascii_banner_lower)
print(Z1+ 'Lagon 4L Bulma Aracı🔎 v1.1          \n\n')
time.sleep(3)

try:
    with open('4lbilgi.txt', 'r') as file:
        lines = file.readlines()
        ID = lines[0].strip()
        token = lines[1].strip()
except FileNotFoundError:
    print(Z1 + "Dosya bulunamadı. '4lbilgi.txt' dosyası oluşturulacak.")
    ID = input(Z1 + 'ID: ')
    token = input(Z1 + 'BOT TOKEN: ')
    with open('4lbilgi.txt', 'w') as file:
        file.write(f"{ID}\n{token}")
    print("Bilgiler '4lbilgi.txt' dosyasına kaydedildi.")

uus = 'qwertyuiopasdfghjklzxcvbnm._1234567890'
while True:
    ks = str(''.join((random.choice(uus) for i in range(4))))
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    headers_kai = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        # diğer header bilgileri...
        'x-requested-with': 'XMLHttpRequest'
    }
    datas_kai = {
        'email': 'a@gmail.com',
        'username': f"{ks}",
        'first_name': 'AA',
        'opt_into_one_tap': 'false'
    }
    kd = requests.post(url, headers=headers_kai, data=datas_kai).text
    if 'kd' in kd:
        print(B + 'Başarılı : ' + ks)
    else:
        print(Z1 + 'Hatalı :        ' + ks)
