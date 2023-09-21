import telebot
from telebot import types
import time
from Pstgresql import result_code


print('[INFO] START TIOR-BOT')


bot = telebot.TeleBot('6410920387:AAF1gPJTdtsU-d3TyCdysXEpFkkuht-JHPU')


# START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Привет, <b>{message.from_user.first_name}!</b>\n Добро пожаловать в нашу сиситему бронирования отелей '
            f'TIOR. Основались мы  совсем недавно, и в честь этого, всем нашим клиентам на протяжении осени будет '
            f'предоставлена <b>скидка 10%</b>✨ на бронирование любых отелей в нашем сервисе!.')

    # choice
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🌴 Продолжить 🌴')
    btn2 = types.KeyboardButton("⛔️ Пока остановимся ⛔️")
    markup.add(btn1, btn2)

    mess_2 = 'Желаешь продолжить?'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, mess_2, reply_markup=markup)


# CONTINUATION OR END
@bot.message_handler(content_types=['text'])
def continuation_or_end(message):
    markup_site = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton('TIOR', url='www.tior.space')
    markup_site.add(btn_site)
    if (message.text == "🌴 Продолжить 🌴"):
        bot.send_message(message.chat.id, "Отлично, продолжим!")

        # CHOICE CITY
        markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_city1 = types.KeyboardButton("Нижний Новгород")
        btn_city2 = types.KeyboardButton("Москва")
        btn_city3 = types.KeyboardButton("Санкт-Петербург")
        btn_city4 = types.KeyboardButton("Сочи")
        btn_city5 = types.KeyboardButton("Города крыма")
        btn_city6 = types.KeyboardButton("Туапсе")
        btn_city7 = types.KeyboardButton("Геленджик")
        btn_city8 = types.KeyboardButton("Калининград")
        btn_city_9 = types.KeyboardButton("Казань")
        btn_city_10 = types.KeyboardButton("Выбрать свой вариант 😎")
        btn_city_11 = types.KeyboardButton("Назад🔙")
        markup_2.add(btn_city1, btn_city2, btn_city3, btn_city4, btn_city5, btn_city6, btn_city7, btn_city8, btn_city_9, btn_city_10, btn_city_11)
        bot.send_message(message.chat.id, "В каком городе вы бы хотели отдохнуть?", reply_markup=markup_2)

    # BACK
    elif (message.text == "Назад🔙"):
        bot.send_message(message.chat.id, "🔙🔙🔙")
        start(message)


    elif (message.text == "Нижний Новгород"):
        bot.send_message(message.chat.id, "Отлично, чтобы забронировать номер в отеле, вы можете воспользовться нашим сайтом!", reply_markup=markup_site)
        time.sleep(2.5)
        bot.send_message(message.chat.id, 'Если хотите продолжить на сайте - тыкните на кнопку чуть выше). Ну а я сейчас загружу список отелей - наших партнёров, Нижнего Новгорода!')

        # CONCLUSION LIST_HOTELS
        def get_clean_code(result_code):
            list_hotels = result_code
            str_hotel = str(list_hotels)

            completed_text = str_hotel.translate({ord(i): None for i in "()'[]'"})
            new = completed_text.replace(',,','\n',100)
            bot.send_message(message.chat.id, new)
        get_clean_code(result_code)






    elif (message.text == "Москва"):
        bot.send_message(message.chat.id, "Москва")


    elif (message.text == "Санкт-Петербург"):
        bot.send_message(message.chat.id, "Санкт-Петербург")


    elif (message.text == "Сочи"):
        bot.send_message(message.chat.id, "Сочи")


    elif (message.text == "Геленджик"):
        bot.send_message(message.chat.id, "Геленджик")


    elif (message.text == "Города крыма"):
        bot.send_message(message.chat.id, "Города крыма")


    elif (message.text == "Туапсе"):
        bot.send_message(message.chat.id, "Туапсе")


    elif (message.text == "Калининград"):
        bot.send_message(message.chat.id, "Калининград")


    elif (message.text == "Казань"):
        bot.send_message(message.chat.id, "Казань")





    elif (message.text == "Выбрать свой вариант 😎"):
        bot.send_message(message.chat.id, "Пожалуйста введите название города вручную")


    elif (message.text == "⛔️ Пока остановимся ⛔️"):
        bot.send_message(message.chat.id, "Ок, пишите как только будет время!")






bot.polling(none_stop=True)
