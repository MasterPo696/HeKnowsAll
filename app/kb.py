from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder  


agree = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я понял!", callback_data='start')]])

correct = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data='yes'), InlineKeyboardButton(text="Нет", callback_data='no')]])

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❔ Еще вопрос!", callback_data='start')]])


answer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🫵🏻 Точный ответ", callback_data='answer_short')],
    [InlineKeyboardButton(text="🤔 Расскажи подробнее", callback_data='answer_medium')],
    [InlineKeyboardButton(text="🌏 Я хочу знать все", callback_data='answer_long')]])
