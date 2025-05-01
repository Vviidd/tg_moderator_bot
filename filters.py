from aiogram import types, Dispatcher

BAD_WORDS = {лох, красава}
LINK_TRIGGERS = ("http://", "https://", "t.me/")

async def filter_messages(message: types.Message):
    text = message.text.lower()
    
    if any(bad in text for bad in BAD_WORDS):
        await message.delete()
        await message.answer("Айайай. Запретка!")
    elif any(link in text for link in LINK_TRIGGERS):
        await message.delete()
        await message.answer("Ссылки неззя.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(filter_messages)