
from aiogram import types
from bot.handlers.get_api_contents import get_external_data

from dispatcher import dp, bot


@dp.message_handler(is_owner=True, commands="start", commands_prefix="!/")
async def cmd_ping_bot(message: types.Message):
    await message.reply("<b>👊 Up & Running!</b>\n\n")



@dp.message_handler(commands=['getdata'])
async def send_data(message: types.Message):
    external_data = get_external_data()
    if external_data:
        await message.answer(f"Data from the external API: {external_data}")
    else:
        await message.answer("Sorry, there was an error fetching data from the API.")
