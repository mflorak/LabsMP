import telebot
from telebot import types

# Ставимо свій токен
BOT_TOKEN = '**********************************'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/scream ATTENTION")
    btn2 = types.KeyboardButton("/whisper secret")
    markup.add(btn1, btn2)

    bot.reply_to(message, "Вітаю! Оберіть дію або введіть команду:", reply_markup=markup)


@bot.message_handler(commands=['scream'])
def scream_command(message):
    text_to_process = message.text[len('/scream'):].strip()

    if not text_to_process:
        bot.reply_to(message, "Що кричати?")
        return

    response_text = f"📢 {text_to_process.upper()} !!!"
    bot.reply_to(message, response_text)


@bot.message_handler(commands=['whisper'])
def whisper_command(message):
    text_to_process = message.text[len('/whisper'):].strip()

    if not text_to_process:
        bot.reply_to(message, "Що шепотіти?")
        return

    safe_text = telebot.formatting.escape_markdown(text_to_process.lower())

    response_text = f"🤫 _{safe_text}_"

    bot.send_message(message.chat.id, response_text, parse_mode='MarkdownV2')


print("Бот запущено. Очікування команд...")
# Запуск бота на постоянный опрос API
bot.infinity_polling()