from utils.db_api.models import Users


async def add_user(**kwargs):
    new_user = await Users(**kwargs).create()
    return new_user


async def get_user(telegram_id) -> Users:
    users = await Users.query.where(Users.id_telegram == telegram_id).gino.first()
    return users


async def update_balance(telegram_id, balance):
    transaction = await Users.update.values(balance=balance).where(Users.id_telegram == telegram_id).gino.status()
    return transaction




