from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsRecent
import asyncio

#вводимо свої дані
API_ID = ********
API_HASH = '*******************************'
PHONE_NUMBER = '************'

TARGET_GROUP = 'ictnurebot'

TARGET_CONTACT = 'me'

client = TelegramClient('session_name', API_ID, API_HASH)


async def run_telethon_task():
    print("Запуск Telethon клієнта")
    await client.start(phone=PHONE_NUMBER)

    # 1. ОТРИМАННЯ ПЕРЕЛІКУ КОРИСТУВАЧІВ (Учасників)
    print(f"\n 1. Отримання перших 10 учасників з @{TARGET_GROUP}...")
    try:
        participants = await client.get_participants(TARGET_GROUP, limit=10)

        if participants:
            for user in participants:
                print(f"ID: {user.id} | Username: @{user.username} | Name: {user.first_name}")
        else:
            print("Не знайдено учасників або немає прав доступу.")

    except Exception as e:
        print(f"Помилка при отриманні учасників: {e}")

    print(f"\n2. Відправлення повідомлення у {TARGET_CONTACT}...")
    message_text = "Тест Telethon: успішне виконання завдання для звіту."
    await client.send_message(TARGET_CONTACT, message_text)
    print("Повідомлення успішно відправлено.")

    await client.disconnect()


if __name__ == '__main__':
    client.loop.run_until_complete(run_telethon_task())