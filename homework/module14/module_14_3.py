from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher (bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb1.row(button1,button2)
kb1.add(button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button4 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button5 = InlineKeyboardButton(text='Формулы расчёта' , callback_data='formulas')
kb2.row(button4,button5)

kb3 = InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
button6 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product2' , callback_data='product_buying')
button8 = InlineKeyboardButton(text='Product3' , callback_data='product_buying')
button9 = InlineKeyboardButton(text='Product4' , callback_data='product_buying')
kb3.add(button6,button7,button8, button9)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=kb1)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте!')

@dp.message_handler(text='Рассчитать')
async def menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i}| Описание: описание{i}| Цена: {i*100}')
        with open(f'img/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, 'Выберите продукт для покупки:', reply_markup=kb3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    result = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5, 2)
    await message.answer(f'Ваша норма калорий {result}')
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)