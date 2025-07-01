import telebot
import re

# Замените на ваш токен бота
TOKEN = '7408981942:AAFVgmREMTF-Q0nU27UeiFQ8ost9ybnpxe0'

# Список запрещенных слов (добавьте свои)
BAD_WORDS = ['сука', 'блять', 'ебать']

bot = telebot.TeleBot(TOKEN)

# Обработчик новых сообщений
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.chat.type in ('group', 'supergroup'):  # Обрабатываем только групповые чаты
        for word in BAD_WORDS:
            if re.search(r'\b' + re.escape(word) + r'\b', message.text.lower()):
                try:
                    bot.delete_message(message.chat.id, message.message_id)
                    # Можно также отправить уведомление об удалении:
                    # bot.send_message(message.chat.id, f"Сообщение пользователя {message.from_user.first_name} удалено за использование нецензурной лексики.")
                    print(f"Сообщение от {message.from_user.username} удалено: {message.text}")
                except Exception as e:
                    print(f"Ошибка при удалении сообщения: {e}")
                break  # Прекращаем проверку после первого совпадения


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling()
