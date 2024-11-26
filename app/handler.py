import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from database import Database
from app.config import TOKEN
PAYMENT_TIMEOUT = 10 #15 * 60  # 15 минут в секунда
import app.kb as kb
from aiogram import Bot, Dispatcher, types, F
# Configure logging
from datetime import datetime, timedelta
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ai21.chat_models import ChatAI21
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
API_KEY = 'Wma8L9fiyWGvEI48rP2QSPfOXNl8FBsc'

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

router = Router()




# ############    MiddleWare    ############    ############    ############
# isbot = message.from_user.is_bot
#     if isbot == True: return
# ############  ############    ############    ############    ############


from texts import sticker_pack



answer_text = """

Ты помощник-мудрец для решения задач по школьной программе. Ты должен отвечать как мастер-учитель. Ты получаешь вопрос и кодовое слово.

short - ответ должен быть коротким и содержательным. Мне нужен только ответ без пояснений.
medium - ответ должен быть средним и чтобы были рассказана дополнительная полезная информация. используй научные факты и термины. 
long - ответ должен быть раскарытым и полезным и без лишней информации. 


"""
import random

# Инициализация модели и парсера
parser = StrOutputParser()
model = ChatAI21(model="jamba-instruct", api_key=API_KEY, streaming=True)

class test(StatesGroup):
    text = State()
    vars = State()

async def get_sticker():
    result = random.randrange(0, len(sticker_pack))
    return sticker_pack[result]

@router.message(Command("start"))
async def start(message: Message):
    name = message.from_user.full_name
    isbot = message.from_user.is_bot
    if isbot == True: return
    sticker = await get_sticker()
    await bot.send_sticker(message.from_user.id, sticker) 
    # user_id = message.from_user.id
    await message.answer(
        f"Привет, <b>{name}</b>! Я тут для того, чтобы помочь тебе с твоими заданиями!"
        "<b>Для того, чтобы получить правильный ответ, нужно задать правильный вопрос!</b>",  parse_mode="HTML")
    await message.answer(f"Я знаю столько всего, но я лишь всего лишь <b>помощник</b> и могу ошибаться. Доверяй, но проверяй!", parse_mode="HTML", reply_markup=kb.agree)
    
@router.callback_query(F.data == "start")
async def handle_start(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    
    await callback.message.answer(
        f"<b>Слушаю твой вопрос, мой дорогой друг! Помни, один вопрос - один ответ.\n</b>", parse_mode="HTML")
    await state.set_state(test.text)

@router.message(test.text)
async def handle_meal_name(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(f"<b>Отличный вопрос! Теперь выбери тут.</b>", parse_mode="HTML", reply_markup=kb.answer)
    
@router.callback_query(lambda c: c.data.startswith("answer_"))
async def handle_answer_type(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    answer_type = callback.data.split("_")[1]  # Extract the file_id
    # system_message = get_system_message(answer_type)
    sticker = await get_sticker()
    await bot.send_sticker(callback.from_user.id, "CAACAgIAAxkBAAEJ8kpnMggSSecbipiEYnkeCYxiiJZYNgACSwADv2adGAT4R80tEyacNgQ") 
    await callback.message.answer(f"<b>Дай мне подумать...</b>", parse_mode="HTML")
    
    answer = get_response(text, answer_type)
    await callback.message.answer(f"<b>Я подумал, подумал и вот мой ответ.\n\n</b> {answer}", parse_mode="HTML", reply_markup=kb.start)
    await state.clear()

# Функция для взаимодействия с моделью AI21
def get_response(question, options):
    user_message = f"Вопрос: {question}, ключевое слово: {options}."
    messages = [
        SystemMessage(content=answer_text),
        HumanMessage(content=user_message)
    ]
    response = model.invoke(messages)
    return parser.invoke(response)
