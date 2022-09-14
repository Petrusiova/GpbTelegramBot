# import schedule
import telebot
from datetime import datetime

bot = telebot.TeleBot('5658251229:AAGoAE5S6udqEHHouIFinjzwQcTm8I4e0BM')
ids = []
texts = {}
forms = {}


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    id = message.new_chat_members[0].id


    try:
        name = message.new_chat_members[0].first_name

        ids.append(id)

        mes_ = bot.send_message(message.chat.id, f"Добро пожаловать, @{name}!"
                                                 f"\nУ нас здесь круто, но есть правило: прежде чем войти, необходимо рассказать о себе"
                                                 f"\n(У тебя 240 секунд и минимум 15 символов)")
        texts[id] = []
        texts[id].append(mes_.id)
        mes_ = bot.send_message(message.chat.id, "Как тебя зовут? \nИз какого ты подразделения? \nКакая у тебя роль в банке? \nРасскажи о своих хобби?")

        texts[id].append(mes_.id)
        forms[id] = datetime.now()

    except:
        check_time(message)


@bot.message_handler(content_types=['text'])
def start(message):
    check_time(message)

    id = message.from_user.id
    if id in ids:
        try:
            if (datetime.now() - forms[id]).total_seconds() <= 240:
                if len(message.text) >= 15:
                    delete_previous(id, message)
                else:
                    bot.kick_chat_member(message.chat.id, id)

        except:
            pass


def check_time(message):
    for id, start in forms.items():
        if (datetime.now() - forms[id]).total_seconds() > 240:
            delete_previous(id, message)
            bot.kick_chat_member(message.chat.id, id)


# @bot.message_handler(content_types=['text'])
# def next_method(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             mes_ = bot.send_message(message.chat.id, "Кем ты работаешь?")
#             texts[id].append(mes_.id)
#         bot.register_next_step_handler(message=message, callback=next_method_2)
#     except:
#         delete_previous(id, message)
#
#
# @bot.message_handler(content_types=['text'])
# def next_method_2(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             mes_ = bot.send_message(message.chat.id, "Чем ты увлекаешься?")
#             texts[id].append(mes_.id)
#         bot.register_next_step_handler(message=message, callback=next_method_3)
#     except:
#         delete_previous(id, message)
#
#
# @bot.message_handler(content_types=['text'])
# def next_method_3(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             bot.send_message(message.chat.id,
#                              "К нам присоединился(ась) " + str(forms[id][0]) + " из " + str(
#                                  forms[id][1]) + ", он(а) работает " + str(forms[id][2]) + " и увлекается " + (
#                              forms[id][3]))
#     finally:
#         delete_previous(id, message)


def delete_previous(id, message):
    for i in texts[id]:
        bot.delete_message(message.chat.id, i)
    ids.remove(id)
    forms.__delitem__(id)
    texts.__delitem__(id)
    bot.register_next_step_handler(message=message, callback=start)


bot.polling(none_stop=True)
