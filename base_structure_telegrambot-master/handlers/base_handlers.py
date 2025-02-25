import math
from aiogram import Router , types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.handlers import CallbackQueryHandler,callback_query
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
import datetime
import aiohttp
import asyncio


from config_data.config import Config, load_config

from key_boards.main_menu import inline1
from key_boards.start_keyboard import start_inline
from lexicon.lexicon import LEXICON_MESSAGE

config: Config = load_config()

router: Router = Router()

KEY = "3ae2871f54498debb79415e049e63cf4"


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply("Привет!",reply_markup=inline1())
    
    
class Reg(StatesGroup):
    city = State()
    
    
@router.callback_query(F.data== 'weather')
async def data(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.city)
    await callback.answer("Введите ваш город")


@router.message(Reg.city)
async def get_weather(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    city_data = await state.get_data()
    city = city_data['city']
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={KEY}") as response:
                data = await response.json()
                city = data["name"]
                cur_temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        # продолжительность дня
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        
        await message.reply(f"⏲{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            f"🌧Погода в городе: {city}\n\n🌡Температура: {cur_temp}°C \n\n"
            f"💧Влажность: {humidity}%\n\n🌬Давление: {math.ceil(pressure/1.333)} мм.рт.ст\n\n💨Ветер: {wind} м/с \n\n"
            f"☀️Восход солнца: {sunrise_timestamp}\n\n🌅Закат солнца: {sunset_timestamp}\n\n⏳Продолжительность дня: {length_of_the_day}\n\n"
            f"⭐️Хорошего дня!⭐️"
        )
        await state.clear()
    except(KeyError):
        await message.reply("Проверьте название города!")
        await state.clear()
        
        
@router.message(F.text.lower() == ("москва"))
async def get_weather1(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid={KEY}") as response:
            data = await response.json()
            city = data["name"]
            cur_temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]

    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

    # продолжительность дня
    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        
    await message.reply(f"⏲{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        f"🌧Погода в городе: {city}\n\n🌡Температура: {cur_temp}°C \n\n"
        f"💧Влажность: {humidity}%\n\n🌬Давление: {math.ceil(pressure/1.333)} мм.рт.ст\n\n💨Ветер: {wind} м/с \n\n"
        f"☀️Восход солнца: {sunrise_timestamp}\n\n🌅Закат солнца: {sunset_timestamp}\n\n⏳Продолжительность дня: {length_of_the_day}\n\n"
        f"⭐️Хорошего дня!⭐️"
    )
        

@router.message(F.text.lower() == ("екатеринбург"))
async def get_weather2(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q=екатеринбург&lang=ru&units=metric&appid={KEY}") as response:
            data = await response.json()
            city = data["name"]
            cur_temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]

    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        # продолжительность дня
    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        
    await message.reply(f"⏲{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        f"🌧Погода в городе: {city}\n\n🌡Температура: {cur_temp}°C \n\n"
        f"💧Влажность: {humidity}%\n\n🌬Давление: {math.ceil(pressure/1.333)} мм.рт.ст\n\n💨Ветер: {wind} м/с \n\n"
        f"☀️Восход солнца: {sunrise_timestamp}\n\n🌅Закат солнца: {sunset_timestamp}\n\n⏳Продолжительность дня: {length_of_the_day}\n\n"
        f"⭐️Хорошего дня!⭐️"
    )
