import os
os.system('pip install pyfiglet')
os.system('pip install random')
os.system('pip install time')
os.system('pip install requests')
os.system('pip install colorama')
os.system('pip install webbrowser')
import random
import time
import requests
from colorama import Fore, Style, init
import pyfiglet
import webbrowser
os.system('clear')
webbrowser.open('https://t.me/lagontech')
# Colorama'nın başlatılması
init(autoreset=True)

text = "CC Generator"

# ASCII art oluştur
ascii_banner = pyfiglet.figlet_format(text)

# ASCII art'ı küçült
ascii_banner_lower = ascii_banner.lower()

# Renklendirilmiş olarak ekrana yazdır
print(Fore.RED + ascii_banner_lower)

# Kullanıcıdan bot token'ı ve kullanıcı ID'sini al
try:
    with open("bilgiler.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 2:
            tok = lines[0].strip()
            ID = lines[1].strip()
        else:
            raise Exception("Dosya hatalı. Yeniden giriş yapılacak.")
except Exception as e:
    tok = input(Fore.GREEN + "Bot Token : ")
    ID = input(Fore.GREEN + "ID : ")
    with open("bilgiler.txt", "w") as file:
        file.write(f"{tok}\n{ID}")

# Kaç kart üreteceğini kullanıcıdan al
try:
    kart_sayisi = int(input(Fore.CYAN + "Kaç kart üreteceksiniz? "))
except ValueError:
    print(Fore.RED + "Geçerli bir sayı girmelisiniz.")
    exit()

# Bayrak (flag) ekleyin
tlg2_gonderildi = False

# Üretilen kartları kaydetmek için dosyayı aç
with open("kartlar.txt", "w") as kartlar_file:
    while kart_sayisi > 0:
        # 16 haneli random sayı oluştur
        kartno = ''.join(random.choices('0123456789', k=16))

        # 4 haneli random sayı oluştur
        cctarih = f'{random.randint(1, 12):02d}/{random.randint(2024, 2028):02d}'

        cvv = f'{random.randint(1, 999):03d}'

        # Birleştir
        cc = f"{kartno}  |  {cctarih}  |  {cvv}"

        # Üretilen kartı dosyaya kaydet
        kartlar_file.write(cc + "\n")

        # Telegram'a gönder
        tlg = f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={cc}'
        i = requests.post(tlg)

        # tlg2'yi sadece bir kere gönder

        kart_sayisi -= 1
        time.sleep(2)

print(Fore.GREEN + "Başarılı.")
