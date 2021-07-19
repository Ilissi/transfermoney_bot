from typing import List

from utils.db_api.models import Transactions


async def create_transaction(**kwargs):
    new_transaction = await Transactions(**kwargs).create()
    return new_transaction


async def get_transaction(telegram_id):
    transaction = await Transactions.query.where(Transactions.user_id == telegram_id).gino.first()
    return transaction


async def update_transaction(telegram_id, amount):
    transaction = await Transactions.update.values(amount=amount).where(Transactions.user_id == telegram_id).gino.status()
    return transaction

