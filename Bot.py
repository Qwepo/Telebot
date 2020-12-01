from aiogram import Dispatcher, Bot, executor, types
from DataBase import SQL
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import Config
from Parser import parser

bot = Bot(Config.Token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Connect to the database
db = SQL('Data.db')


# Create a state class
class From(StatesGroup):
    add_links = State()


# The command handler "/start"
@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
    await bot.send_message(message.from_user.id, text=Config.message_start)


# The command handler "/help"
@dp.message_handler(commands=['help'])
async def help_commands(message: types.Message):
    await bot.send_message(message.from_user.id, text=Config.message_help)


# The command handler "/add"
@dp.message_handler(state='*', commands=['add'])
async def add_commands(message: types.Message):
    await bot.send_message(message.from_user.id, 'Enter link')
    await From.add_links.set()  # Passing the response to add_url_links


# Add a link to the database
@dp.message_handler(state=From.add_links)
async def add_url_links(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.find(Config.coinmarketcap) == -1:  # Checking the link for correctness
        await bot.send_message(message.from_user.id, text='Invalid link!')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, text='Link added!')
        db.add(message.from_user.id, answer)
        await state.finish()


# Display information about the cryptocurrency and check if the user and his links are in the database
@dp.message_handler(commands=['info'])
async def crypt_info(message: types.Message):
    if not db.chek_user_for_data_base(message.from_user.id):
        await bot.send_message(message.from_user.id, text='''You haven't added any links!''')
    else:
        await bot.send_message(message.from_user.id, parser(message.from_user.id))


# Removing links from the database
@dp.message_handler(commands=['dell'])
async def dell_commands(message: types.Message):
    db.dell_user_and_links(message.from_user.id)
    await bot.send_message(message.from_user.id, text='Links removed!')


if __name__ == "__main__":
    print('The bot is running!')
    executor.start_polling(dp)
