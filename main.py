from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://img05.rl0.ru/afisha/e1200x800i/daily.afisha.ru/uploads/images/6/9f/69f86e59a86e8162aea80769f971435a.jpg', caption= 'Вот тебе кот!!')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkT5HDfBWfgP-XAqCJGbvI3Cn0v7YSuCGbEWHp6CxoPA&s', caption= 'Вот тебе собака!!')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)
