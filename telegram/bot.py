import telebot
from address import address
from telebot import types
from database.db import *
urls = ['https://www.scalemates.com/colors/italeri-acrylic-paint--678',
        'https://www.scalemates.com/colors/ak-3rd-generation-afv--976',
        'https://www.scalemates.com/colors/revell-aqua-color--654']

bot = telebot.TeleBot(address)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Ссылки на исходники")
	btn2 = types.KeyboardButton("Посмотреть цвета")
	markup.add(btn1, btn2)
	bot.send_message(message.chat.id,
					 text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
						 message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
	if (message.text == "Ссылки на исходники"):
		markup = types.InlineKeyboardMarkup()
		button1 = types.InlineKeyboardButton("Iteleri", url='https://www.scalemates.com/colors/italeri-acrylic-paint--678')
		button2 = types.InlineKeyboardButton("AFV",
											 url='https://www.scalemates.com/colors/ak-3rd-generation-afv--976')
		button3 = types.InlineKeyboardButton("Revell Aqua",
											 url='https://www.scalemates.com/colors/revell-aqua-color--654')
		markup.add(button1)
		markup.add(button2)
		markup.add(button3)
		bot.send_message(message.chat.id,
						 "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
						 reply_markup=markup)
	elif (message.text == "Посмотреть цвета"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		for x in allProducers:
			button = types.KeyboardButton(f"{x.name}")
			markup.add(button)
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(back)
		bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
	elif (message.text in list(map(lambda x: x.name, allProducers))):
		print('sassaassa')
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(back)
		bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
	elif (message.text == "Вернуться в главное меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button1 = types.KeyboardButton("Ссылки на исходники")
		button2 = types.KeyboardButton("Посмотреть цвета")
		markup.add(button1, button2)
		bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

allProducers = getAllProducers()
bot.polling(none_stop=True)