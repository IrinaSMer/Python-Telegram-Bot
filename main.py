import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton(text="Да!", callback_data="asq:yes")
    button_2 = types.InlineKeyboardButton(text="Не сейчас.", callback_data="asq:no")
    markup_inline.add(button_1, button_2)
    mess = f'Привет, <b>{message.from_user.first_name}</b>! Готовы сыграть?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('asq'))
def rules(call):
    if call.data == "asq:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        button_yes = types.InlineKeyboardButton(text="Да!", callback_data="qwe:yes")
        markup_inline.add(button_yes)
        mess1 = 'Правила Правила Правила. Готовы?'
        bot.send_message(call.message.chat.id, mess1, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "asq:no":
        mess2 = 'Хорошего дня.'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data.startswith('qwe'))
def question1(call):
    if call.data == "qwe:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Тепло", callback_data="wer:no")
        button_2 = types.InlineKeyboardButton(text="Б: Сытно", callback_data="wer:no")
        button_3 = types.InlineKeyboardButton(text="С: Хорошо", callback_data="wer:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Весело", callback_data="wer:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Как же, согласно поговорке, все-таки там, где нас нет?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('wer'))
def question2(call):
    if call.data == "wer:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Соль", callback_data="ert:no")
        button_2 = types.InlineKeyboardButton(text="Б: Колбаса", callback_data="ert:no")
        button_3 = types.InlineKeyboardButton(text="С: Хлеб", callback_data="ert:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Зрелища", callback_data="ert:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 500 рублей Ваши! Следующий вопрос: \nЧто, согласно пословице, является всему головой?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "wer:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный! Хотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('ert'))
def question3(call):
    if call.data == "ert:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Парус", callback_data="rty:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Яхта", callback_data="rty:no")
        button_3 = types.InlineKeyboardButton(text="С: Теплоход", callback_data="rty:no")
        button_4 = types.InlineKeyboardButton(text="Д: Айсберг", callback_data="rty:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 1 000 рублей Ваши! Следующий вопрос на 2000 рублей: \nЧто одиноко белело «в тумане моря» в известном стихотворении Лермонтова?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "ert:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный! Хотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('rty'))
def question4(call):
    if call.data == "rty:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Десантники", callback_data="tyu:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Моряки", callback_data="tyu:no")
        button_3 = types.InlineKeyboardButton(text="С: Летчики", callback_data="tyu:no")
        button_4 = types.InlineKeyboardButton(text="Д: Танкисты", callback_data="tyu:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 2 000 рублей Ваши! Следующий вопрос: \nВоеннослужащие каких войск называют себя «голубыми беретами»?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "rty:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный! Хотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('tyu'))
def question5(call):
    if call.data == "tyu:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Теннис", callback_data="yui:no")
        button_2 = types.InlineKeyboardButton(text="Б: Волейбол", callback_data="yui:no")
        button_3 = types.InlineKeyboardButton(text="С: Баскетбол", callback_data="yui:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Бадминтон", callback_data="yui:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 3 000 рублей Ваши! До первой несгораемой суммы в 5000 рублей остался один вопрос! Следующий вопрос: \nКакую спортивную игру начинают не с подачи?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "tyu:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный! Хотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('yui'))
def question6(call):
    if call.data == "yui:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Скалы", callback_data="uio:no")
        button_2 = types.InlineKeyboardButton(text="Б: Пещеры", callback_data="uio:yes")
        button_3 = types.InlineKeyboardButton(text="С: Вулканы", callback_data="uio:no")
        button_4 = types.InlineKeyboardButton(text="Д: Сопки", callback_data="uio:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 5 000 рублей Ваши! Следующий вопрос: \nКакие формы земной поверхности изучает спелеолог?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "yui:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('uio'))
def question7(call):
    if call.data == "uio:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Металлургом", callback_data="iop:no")
        button_2 = types.InlineKeyboardButton(text="Б: Нефтяником", callback_data="iop:no")
        button_3 = types.InlineKeyboardButton(text="С: Шахтёром", callback_data="iop:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Строителем", callback_data="iop:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 10 000 рублей Ваши! \nКем по профессии был зачинатель рабочего движения за производительность труда Стаханов?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "uio:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('iop'))
def question8(call):
    if call.data == "iop:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Измайлово", callback_data="opa:no")
        button_2 = types.InlineKeyboardButton(text="Б: Сокольники", callback_data="opa:no")
        button_3 = types.InlineKeyboardButton(text="С: Фили", callback_data="opa:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Замоскворечье", callback_data="opa:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 15 000 рублей Ваши! Следующий вопрос: \nНа совете в каком подмосковном селе в 1812 году Кутузов решил сдать Москву французам? На кону 25 000 рублей!'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "iop:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('opa'))
def question9(call):
    if call.data == "opa:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Рондо", callback_data="pas:no")
        button_2 = types.InlineKeyboardButton(text="Б: Триолет", callback_data="pas:no")
        button_3 = types.InlineKeyboardButton(text="С: Рубаи", callback_data="pas:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Сонет", callback_data="pas:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 25 000 рублей Ваши! Следующий вопрос: \nВ каком жанре творил Омар Хайям?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "opa:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('pas'))
def question10(call):
    if call.data == "pas:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Добронравов", callback_data="asd:no")
        button_2 = types.InlineKeyboardButton(text="Б: Матусовский", callback_data="asd:no")
        button_3 = types.InlineKeyboardButton(text="С: Харитонов", callback_data="asd:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Ошанин", callback_data="asd:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 50 000 рублей Ваши! Следующий вопрос: \nНа чьи стихи написана песня «День победы?»'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "pas:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('asd'))
def question11(call):
    if call.data == "asd:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Белое", callback_data="sdf:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Балтийское", callback_data="sdf:no")
        button_3 = types.InlineKeyboardButton(text="С: Баренцево", callback_data="sdf:no")
        button_4 = types.InlineKeyboardButton(text="Д: Карское", callback_data="sdf:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 100 000 рублей Ваши! Следующий вопрос: \nВ каком море находятся Соловецкие острова?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "asd:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 5 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('sdf'))
def question12(call):
    if call.data == "sdf:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Ляпидевский", callback_data="dfg:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Чкалов", callback_data="dfg:no")
        button_3 = types.InlineKeyboardButton(text="С: Водопьянов", callback_data="dfg:no")
        button_4 = types.InlineKeyboardButton(text="Д: Шмидт", callback_data="dfg:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 200 000 рублей Ваши! Следующий вопрос: \nКто из наших соотечественников был первым удостоен звания Героя Советского Союза?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "sdf:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 100 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('dfg'))
def question13(call):
    if call.data == "dfg:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Нефтегорск", callback_data="fgh:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Нефтекамск", callback_data="fgh:no")
        button_3 = types.InlineKeyboardButton(text="С: Нефтекумск", callback_data="fgh:no")
        button_4 = types.InlineKeyboardButton(text="Д: Нефтеюганск", callback_data="fgh:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 400 000 рублей Ваши! Следующий вопрос: \nНазвание какого из этих городов связано не с добычей, а с переработкой нефти?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "dfg:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 100 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('fgh'))
def question14(call):
    if call.data == "fgh:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Олег Вещий", callback_data="ghj:yes")
        button_2 = types.InlineKeyboardButton(text="Б: Ярослав Мудрый", callback_data="ghj:no")
        button_3 = types.InlineKeyboardButton(text="С: Игорь", callback_data="ghj:no")
        button_4 = types.InlineKeyboardButton(text="Д: Владимир Мономах", callback_data="ghj:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 800 000 рублей Ваши! Следующий вопрос: \nКакой русский князь осадил столицу Византийской империи и наложил на империю контрибуцию?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "fgh:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 100 000 рублей!! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data.startswith('ghj'))
def question15(call):
    if call.data == "ghj:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="A: Юнг", callback_data="hjk:no")
        button_2 = types.InlineKeyboardButton(text="Б: Гегель", callback_data="hjk:no")
        button_3 = types.InlineKeyboardButton(text="С: Ницше", callback_data="hjk:yes")
        button_4 = types.InlineKeyboardButton(text="Д: Шопенгауэр", callback_data="hjk:no")
        markup_inline.add(button_1, button_2, button_3, button_4)
        mess = 'Поздравляю, 1 000 000 рублей Ваши! Следующий вопрос: \nКто из этих философов в 1864 году написал музыку на стихи А. С. Пушкина «Заклинание» и «Зимний вечер»?'
        bot.send_message(call.message.chat.id, mess, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "ghj:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="asq:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'К сожалению, ответ неверный, но не расстраивайтесь, Вы выиграли 100 000 рублей!! Хотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: call.data.startswith('hjk'))
def question16(call):
    if call.data == "hjk:yes":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="qwe:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'Поздравляю, Вы выиграли 3 000 000 рублей, теперь Вы - Миллионер! \nХотите сыграть еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)
    elif call.data == "hjk:no":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        button_1 = types.InlineKeyboardButton(text="Да", callback_data="qwe:yes")
        button_2 = types.InlineKeyboardButton(text="Нет", callback_data="qwe:no")
        markup_inline.add(button_1, button_2)
        mess2 = 'Очень жаль, но Вы ошиблись! Но не расстраивайтесь, несгораемая сумма в 100 000 рублей достается Вам! \nХотите попробовать еще раз?'
        bot.send_message(call.message.chat.id, mess2, parse_mode='html', reply_markup=markup_inline)


bot.polling(none_stop=True)
