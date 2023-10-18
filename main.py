import telebot
from telebot import types


def atbash(text):
    result = ""
    for char in text:
        if char.isalnum():
            if char.isalpha():
                if char.islower():
                    if 'а' <= char <= 'я':
                        result += chr(ord('а') + ord('я') - ord(char))
                    elif 'a' <= char <= 'z':
                        result += chr(ord('a') + ord('z') - ord(char))
                elif char.isupper():
                    if 'А' <= char <= 'Я':
                        result += chr(ord('А') + ord('Я') - ord(char))
                    elif 'A' <= char <= 'Z':
                        result += chr(ord('A') + ord('Z') - ord(char))
            elif char.isdigit():
                result += str(9 - int(char))
        else:
            result = "Введены символы, которые не пока не реализованы."
            break
    return result


user_previous_section = {}

bot = telebot.TeleBot('6660469951:AAH_HBaN7gACl7W6z42-1HLy1of_4X3BAaU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    welcome_message = "Добро пожаловать! Этот бот позволяет вам шифровать текст методом Атбаш. " \
                      "Выберите раздел, чтобы начать."
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
    item1 = types.KeyboardButton("Раздел 1")
    item2 = types.KeyboardButton("Раздел 2")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Раздел 1")
def handle_section1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Шифр 1")
    item2 = types.KeyboardButton("Шифр 2")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Выбран Раздел 1. Выберите шифр:", reply_markup=markup)
    user_previous_section[message.chat.id] = "Раздел 1"


@bot.message_handler(func=lambda message: message.text == "Раздел 2")
def handle_section2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Шифр 1")
    item2 = types.KeyboardButton("Шифр 2")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Выбран Раздел 2. Выберите шифр:", reply_markup=markup)
    user_previous_section[message.chat.id] = "Раздел 2"


@bot.message_handler(func=lambda message: message.text == "Шифр 1")
def handle_cipher1(message):
    bot.send_message(message.chat.id, "Выбран Шифр 1. Введите текст для шифрования Атбаш:")


@bot.message_handler(func=lambda message: message.text == "Шифр 2")
def handle_cipher2(message):
    bot.send_message(message.chat.id, "Выбран Шифр 2. Введите текст для шифрования Атбаш:")


@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back(message):
    previous_section = user_previous_section.get(message.chat.id)
    if previous_section:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Раздел 1")
        item2 = types.KeyboardButton("Раздел 2")
        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        del user_previous_section[message.chat.id]


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    encrypted_text = atbash(message.text)
    bot.send_message(message.chat.id, f"Зашифрованный текст: {encrypted_text}")


bot.polling(non_stop=True)
