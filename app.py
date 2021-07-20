from aiogram import executor

from aiogram.dispatcher.webhook import configure_app
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.database import create_db
from aiohttp import web


async def api_handler(request):
    return web.json_response({"status": "OK"}, status=200)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    res = await create_db()
    app = web.Application()

    app.add_routes([web.post('/api', api_handler)])
    configure_app(dp, app, "/bot")
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_webhook(dp, on_startup=on_startup)
