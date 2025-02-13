from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_KEYBOARD


from lexicon.lexicon import LEXICON_MENU


async def set_main_menu(bot: Bot):
    main_menu = [
        BotCommand(command=command, description=description)
        for command, description in LEXICON_MENU.items()
    ]
    await bot.set_my_commands(main_menu)

def inline1(*buttons: str) -> ReplyKeyboardMarkup:
    inline1 = [
        [InlineKeyboardButton(text="☀ПОГОДА", callback_data='weather')],
        [InlineKeyboardButton(text="👏Отзывы", url="https://t.me/+Bog8x1i7ESA5ZmIy")],
        [InlineKeyboardButton(text="🦸Поддержка проекта", url="https://t.me/avsPr09RaM1n9")],
        [InlineKeyboardButton(text="👥Staff", url="https://t.me/avsPr09RaM1n9")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline1,resize_keyboard=True)