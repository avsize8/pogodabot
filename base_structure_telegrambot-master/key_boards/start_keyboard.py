from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_KEYBOARD


def creat_start_keyboard(*buttons: str) -> ReplyKeyboardMarkup:
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb_builder.row(
        *[KeyboardButton(text=LEXICON_KEYBOARD[button] if button in LEXICON_KEYBOARD else button)
          for button in buttons], 
    )
    return kb_builder.as_markup(resize_keyboard=True)


def start_inline(*buttons: str) -> ReplyKeyboardMarkup:
    start_inline = [
        [InlineKeyboardButton(text="💁FAQ", url='https://t.me/avsPr09RaM1n9')],
        [InlineKeyboardButton(text="🏰Гарантии", url='https://t.me/avsPr09RaM1n9')],
        [InlineKeyboardButton(text="👏Отзывы", url="https://t.me/+Bog8x1i7ESA5ZmIy")],
        [InlineKeyboardButton(text="🦸Поддержка", url="https://t.me/avsPr09RaM1n9")],
        [InlineKeyboardButton(text="👥Staff", url="https://t.me/avsPr09RaM1n9")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=start_inline,resize_keyboard=True)

