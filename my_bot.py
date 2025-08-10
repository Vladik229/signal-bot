from telethon import TelegramClient, events
from datetime import datetime
import asyncio

# Дані Telegram API (отримані на my.telegram.org)
api_id = 22324300
api_hash = "cf6c90f7c5140c6494e37f00dcb6dbd6"

# Твій ID акаунта (йому будуть надсилатися повідомлення)
your_user_id = 1574352010

# Ім'я сесії — створиться файл my_desktop_session.session
session_path = "my_desktop_session"

# ID каналів, які слухаємо
channel_ids = [-1838832012, -1732065792, -2488924018, -1861059770]

# Ініціалізація клієнта
client = TelegramClient(session_path, api_id, api_hash)

@client.on(events.NewMessage(chats=channel_ids))
async def handler(event):
    try:
        message = event.message.message
        sender = await event.get_chat()
        channel_name = sender.title if sender else "Unknown"
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

        print(f"\n📡 Сигнал із: {channel_name}")
        print(f"🕒 {timestamp}")
        print(f"📨 {message}\n")

        await client.send_message(
            your_user_id,
            f"📡 {channel_name} | {timestamp}\n\n{message}"
        )
    except Exception as e:
        print(f"Помилка в обробнику: {e}")

async def main():
    print("✅ Підключення до Telegram...")
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Клієнт не авторизований. Будь ласка, запусти скрипт локально і введи код, щоб створити сесію.")
        return

    print("🚀 Бот запущений! Слухаємо повідомлення...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())