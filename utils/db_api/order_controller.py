from typing import List

from utils.db_api.models import Orders


async def add_order(**kwargs):
    new_order = await Orders(**kwargs).create()
    return new_order


async def get_orders(telegram_id) -> List[Orders]:
    orders = await Orders.query.where(Orders.user_id == telegram_id).gino.all()
    return orders


async def update_order(telegram_id, amount):
    transaction = await Orders.update.values(amount=amount).where(Orders.user_id == telegram_id).gino.status()
    return transaction


