from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URL

import asyncio

db = Gino()

from sqlalchemy import (Column, Integer, String, Sequence, DateTime, Float, ForeignKey, Boolean)
from sqlalchemy import sql
import datetime


class Users(db.Model):
    __tablename__ = 'users'
    query: sql.Select

    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    id_telegram = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(50))
    balance = db.Column(db.Float)
    time_registered = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)


class Transactions(db.Model):
    __tablename__ = 'transactions'
    query: sql.Select

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id_telegram'))
    amount = db.Column(db.Float)
    type_transaction = db.Column(db.String(20))
    status = db.Column(db.String(20))
    pay_url = db.Column(db.String(1000))
    time_payed = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)


class Orders(db.Model):
    __tablename__ = 'orders'
    query: sql.Select

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id_telegram'))
    amount_get = db.Column(db.Float)
    currency_get = db.Column(db.String(20))
    country_get = db.Column(db.String(20))
    card_number = db.Column(db.String(20))
    FIO = db.Column(db.String(50))
    amount_spend = db.Column(db.Float)
    accepted = db.Column(db.Boolean)
    status = db.Column(db.String(60))
    time_ordered = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)


async def create_db():
    await db.set_bind(POSTGRES_URL)
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
