import os
from telegram import Bot
import asyncio
import random
import schedule
import time
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = 476103207

bot = Bot(token=TOKEN)

phrases = {
    "Daily Conversation": [
        ("How's it going?", "Как дела?"),
        ("What's up?", "Что нового?"),
        ("No worries.", "Не переживай."),
        ("Sounds good.", "Звучит хорошо."),
        ("I'm good.", "У меня всё хорошо."),
        ("You got it.", "Конечно / без проблем."),
        ("My bad.", "Моя ошибка."),
        ("Hang on a second.", "Подожди секунду."),
        ("I'm just kidding.", "Я просто шучу."),
        ("That makes sense.", "Это имеет смысл.")
    ],

    "Work": [
        ("I'll take care of it.", "Я этим займусь."),
        ("Let me check.", "Дай мне проверить."),
        ("I'm on my way.", "Я уже еду."),
        ("I'll get back to you.", "Я позже отвечу."),
        ("I'm running late.", "Я опаздываю."),
    ],

    "Shopping": [
        ("I'm just looking around.", "Я просто смотрю."),
        ("How much is this?", "Сколько это стоит?"),
        ("I'll take it.", "Беру."),
        ("Can I pay by card?", "Можно оплатить картой?"),
        ("Do you have this in another size?", "Есть другой размер?")
    ],

    "Car": [
        ("I need an oil change.", "Мне нужна замена масла."),
        ("Can you check the brakes?", "Можете проверить тормоза?"),
        ("My car is making a strange noise.", "Машина издает странный звук."),
        ("How long will it take?", "Сколько это займет времени?"),
        ("Is it covered under warranty?", "Это покрывается гарантией?")
    ],

    "Restaurant": [
        ("Can I get the check, please?", "Можно счет, пожалуйста?"),
        ("I'd like a refill.", "Можно добавку напитка?"),
        ("What do you recommend?", "Что вы рекомендуете?"),
        ("Can I get this to go?", "Можно завернуть с собой?"),
        ("I'm ready to order.", "Я готов заказать.")
    ]
}

sent_phrases = []

async def send_lesson():

    topic = random.choice(list(phrases.keys()))
    lesson = random.sample(phrases[topic], min(5, len(phrases[topic])))

    text = f"🇺🇸 English for Today\n\n"
    text += f"📌 Topic: {topic}\n\n"

    for i, (eng, rus) in enumerate(lesson, start=1):
        text += f"{i}. {eng}\n{rus}\n\n"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

    print("Lesson sent:", datetime.now())

def run_send():
    asyncio.run(send_lesson())
run_send()
schedule.every().day.at("19:00").do(run_send)

print("Bot started. Waiting for 19:00...")

while True:
    schedule.run_pending()
    time.sleep(30)