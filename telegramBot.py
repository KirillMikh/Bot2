import threading
import telebot
import schedule
import time
import random
import os

token = str(os.environ.get('BOT_TOKEN'))
bot1 = telebot.TeleBot(token)
user_set = set()

list1=['CAACAgQAAxkBAAIGxV5ZgbTShDZJ8N5DBF-I_rk6xhU7AAK4AwACKz2QAALWsempncZ0GAQ',
       'CAACAgQAAxkBAAIGw15ZgawVcsVYujTOzHsrfnvlgS52AAI5AwACKz2QAAFA5Qu3dLM56xgE',
       'CAACAgQAAxkBAAIG015ZgeiOLLH-DAXhTkDsGsK90pucAAJRAAMv3_gJfJDF2jryWzcYBA',
       'CAACAgQAAxkBAAIG0V5ZgejR0CG03NrwUdDHQZFt7sgjAAJNAAMv3_gJyS__UyL6ynsYBA',
       'CAACAgQAAxkBAAIGzV5ZgeONz2ZF2Mt80eADFWPnTvxUAAJMAAMv3_gJThtbfK5wFm0YBA',
       'CAACAgQAAxkBAAIGy15ZgeJG0zZqWU33XceQaV6u_cgsAAJIAAMv3_gJl7IsvCjAtjgYBA',
       'CAACAgQAAxkBAAIGyV5ZgeGN2GBpfFsuVZIJ56XwFJ9CAAJBAAMv3_gJVhXYD3WvXeEYBA']
def job():
    for id in user_set:
        bot1.send_message(id, 'Не забудь,пожалуйста, зарядить свой телефон!')
        bot1.send_sticker(id, random.choice(list1))
    print('Не забудь,пожалуйста зарядить свой телефон!')

@bot1.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.from_user.id not in user_set:
        user_set.add(message.from_user.id)
    if message.text == "Привет":
        bot1.send_message(message.from_user.id, "И тебе привет), надеюсь у тебя все хорошо, солнышко")
        print(user_set)

    elif message.text == "/help":
        bot1.send_message(message.from_user.id, "Доступные команды:\n"
                                                "Привет\n"
                                                "Расскажи шутку\n"
                                                "Что ты можешь"
                          )
    elif message.text == "Расскажи шутку":
        bot1.send_message(message.from_user.id, "Колобок повесился ыыыыыыыы")
    elif message.text == "Что ты можешь":
        bot1.send_message(message.from_user.id, "Я напоминаю тебе забываке, что нужно каждый день ставить телефон на зарядку в 9 часов")
    else:
        bot1.send_message(message.from_user.id, "Я тебя не понимаю. Но и не сильно то и хотелось))))(шуточка)")



def runBot():
    bot1.polling()
def runSchedulers():
    schedule.every().day.at("21:30").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

