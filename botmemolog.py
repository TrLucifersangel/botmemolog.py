import telebot
import random
import requests
from telebot import types
from bs4 import BeautifulSoup


def urlrandomvibor():
    url = 'https://vk.com/album-214765737_284342576'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    vklinka = 'https://vk.com/'

    for link in soup.find_all('a'):
        h = (link.get('href'))
        urls.append(vklinka + h)
    mempic = random.choice(urls)
    return mempic


vidosi = ['1.mp4',
          '2.mp4', '3.mp4']

bot = telebot.TeleBot('5540934047:AAF0PjWfM0ONqyPEu-NcgSsDOgyFCj4_Dls')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b> {message.from_user.first_name} </b>. Для рофл картинки пиши мем,для видоса-видос.Могу кинуть музыку командой: Музыку урони.Задолбал мир?Команда-Взорвать мир'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMJYuGFLL_l41pCT4hpW4QsqU4dWl4AAhMAA8A2TxOqs4f3fzjKpSkE")


@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "мем":
        h = urlrandomvibor()
        bot.send_photo(message.chat.id, h)
    elif message.text.lower() == 'видос':
        memvid = random.choice(vidosi)
        vidos = open(memvid, 'rb')
        bot.send_video(message.chat.id, vidos)
    elif message.text.lower() == 'музыку урони':
        musika = open('Неизвестен - Без названия.mp3', 'rb')
        bot.send_audio(message.chat.id, musika)
    elif message.text.lower() == 'взорвать мир':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        da = markup.add(types.KeyboardButton('Да'))
        net = markup.add(types.KeyboardButton('Нет'))
        bot.send_message(message.chat.id, 'А ты уверен?', reply_markup=markup)
    elif message.text == 'Да':
        bot.send_photo(message.chat.id, open('10.jpg', 'rb'))
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Ну и не надо!')
    else:
        bot.send_message(message.chat.id, 'Я тоби не вразумил', parse_mode='html')


bot.polling(none_stop=True)
