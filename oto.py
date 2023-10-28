import os
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneNumberInvalidError
from colorama import Fore, Style, init
import time
import traceback  # Hataları kaydetmek için

os.system("clear")
init(autoreset=True)

async def start_bot(api_id, api_hash, source_group, message_id, interval, target_groups):
    os.system("clear")
    try:
        client = TelegramClient("session", api_id, api_hash)
        await client.start()
    except SessionPasswordNeededError:
        print(Fore.RED + "🔐 | İki Adımlı Doğrulama Şifreniz - ")
        password = input("Şifre: ")
        client = TelegramClient("session", api_id, api_hash)
        await client.start(password=password)
        print(Fore.GREEN + "✔️ | Bot Başlatıldı.")
    except PhoneNumberInvalidError:
        print(Fore.RED + "❌ | Hatalı Numara")
        return

    while True:
        try:
            message = await client.get_messages(source_group, ids=message_id)
            for group in target_groups:
                try:
                    await client.send_message(group, message)
                    print(Fore.GREEN + f"Mesaj, {group}'a Başarıyla Gönderildi.")
                except Exception as send_error:
                    pass  # Hataları log dosyasına yazabilirsiniz

            if interval > 0:
                print("Spam Koruması İçin Bekleniyor.")
                time.sleep(interval)

                # Count total messages sent
                total_messages_sent = len(target_groups)
                total_messages = total_messages_sent * message_id
                print(f"Toplam {total_messages_sent} grupa mesaj gönderildi.")

                # Send total messages to LagonOtoMesajBot
                lagon_bot_username = "@LagonOtoMesajBot"  # Bot'un kullanıcı adını güncelleyin
                await client.send_message(lagon_bot_username, f"Toplam {total_messages_sent} gruba mesaj gönderildi.")

        except Exception as e:
            traceback.print_exc()  # Hataları log dosyasına yazabilirsiniz

async def main():
    try:
        with open("lagonotomessage.txt", "r") as f:
            config = f.read().splitlines()
        api_id, api_hash = config[0].split(",")
        source_group = int(config[1])
        message_id = int(config[2])
        interval = int(config[3])
        target_groups = config[4:]
    except FileNotFoundError:
        api_id = int(input("API_ID  : "))
        api_hash = input("API_HASH : ")
        source_group = int(input("Grup ID : "))
        message_id = int(input("Mesaj ID : "))
        interval = int(input("Kaç Saniye Ara Verilsin : "))
        target_groups = []
        for i in range(n):
            target_groups.append(group_name)
        with open("lagonotomessage.txt", "w") as f:
            f.write(f"{api_id},{api_hash}\n{source_group}\n{message_id}\n{interval}\n")
            f.write("\n".join(target_groups))
        print(Fore.GREEN + "Bilgiler Kaydedildi.")

    await start_bot(api_id, api_hash, source_group, message_id, interval, target_groups)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
