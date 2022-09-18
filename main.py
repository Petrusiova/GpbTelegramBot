from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot('5658251229:AAGoAE5S6udqEHHouIFinjzwQcTm8I4e0BM')
dp = Dispatcher(bot)
ids = []
texts = {}
forms = {}


@dp.message_handler(content_types=["new_chat_members"])
async def new_member(message: types.Message):
    id = message.new_chat_members[0].id
    try:
        name = message.new_chat_members[0].first_name

        ids.append(id)

        mes_ = await bot.send_message(message.chat.id, f"Добро пожаловать, @{name}!"
                                                       f"\nЧтобы все участники знали кто есть кто, мы ввели правило: прежде чем войти, необходимо рассказать о себе")

        texts[id] = []
        texts[id].append(mes_["message_id"])
        mes_ = await bot.send_message(message.chat.id,
                                      "Как тебя зовут? \nИз какого ты подразделения? \nКакая у тебя роль в банке? \nРасскажи о своих хобби?"
                                      "Пожалуйста, напиши ответ в одном сообщении (не менее 15 символов). Мы будем ждать твой ответ (целых 240 секунд!)")

        texts[id].append(mes_["message_id"])
        forms[id] = datetime.now()

    except Exception as e:
        print(e)
        await check_time(message)


@dp.message_handler(content_types=['text'])
async def start(message):
    id = message.from_user.id
    if id in ids:
        await check_time(message)
        try:
            if (datetime.now() - forms[id]).total_seconds() <= 240:
                if len(message.text) >= 15:
                    await delete_previous(id, message)
                else:
                    await bot.kick_chat_member(message.chat.id, id)
        except Exception as e:
            print(e)


async def check_time(message):
    id = message.from_user.id
    if id in ids:
        try:
            for id, start in forms.items():
                if (datetime.now() - forms[id]).total_seconds() > 240:
                    await bot.kick_chat_member(message.chat.id, id)
                    await delete_previous(id, message)
                    await bot.delete_message(message.chat.id, message["message_id"])
                    await bot.send_message(message.chat.id,
                                           f" @{message.from_user.first_name} не поздоровался и его пришлось удалить")
        except Exception as e:
            print(e)
            pass

# @dp.message_handler(content_types=['text'])
# async def next_method(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             mes_ = await message.answer(message.chat.id, "Кем ты работаешь?")
#             texts[id].append(mes_.id)
#         bot.register_next_step_handler(message=message, callback=next_method_2)
#     except:
#         delete_previous(id, message)
#
#
# @dp.message_handler(content_types=['text'])
# async def next_method_2(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             mes_ = await message.answer(message.chat.id, "Чем ты увлекаешься?")
#             texts[id].append(mes_.id)
#         bot.register_next_step_handler(message=message, callback=next_method_3)
#     except:
#         delete_previous(id, message)
#
#
# @dp.message_handler(content_types=['text'])
# async def next_method_3(message):
#     id = message.from_user.id
#     try:
#         if message.from_user.id in ids:
#             forms[id].append(message.text)
#             texts[id].append(message.id)
#             await message.answer(message.chat.id,
#                              "К нам присоединился(ась) " + str(forms[id][0]) + " из " + str(
#                                  forms[id][1]) + ", он(а) работает " + str(forms[id][2]) + " и увлекается " + (
#                              forms[id][3]))
#     finally:
#         delete_previous(id, message)


async def delete_previous(id, message):
    try:
        if texts[id] is not None:
            for i in texts[id]:
                await bot.delete_message(message.chat.id, i)
        if ids is not None:
            async with ids:
                ids.remove(id)
        if forms is not None:
            async with forms:
                forms.__delitem__(id)
        if texts is not None:
            async with texts:
                texts.__delitem__(id)
    # bot.register_next_step_handler(message=message, callback=start)
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=print("Бот запущен " + str(datetime.now())))
