from aiogram import executor

from aiogram.dispatcher.webhook import configure_app
from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.database import create_db
from aiohttp import web


async def api_handler(request):
    return web.json_response({"status": "OK"}, status=200)


async def on_startup(dispatcher):
    webhook = await bot.get_webhook_info()
    print(webhook)
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_webhook(dp, webhook_path='/user_bot', on_startup=on_startup, host='127.0.0.1', port=8080)
