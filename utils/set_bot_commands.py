from aiogram import types


async def set_deafult_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommsnd("start", "Запустить бота"),
        types.BotCommsnd("help", "Помощь")
    ])