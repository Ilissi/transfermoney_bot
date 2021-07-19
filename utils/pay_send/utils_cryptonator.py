from data.config import MERCHANT_ID, ITEM_NAME, SECRET
from utils.pay_send import cryptonator_API

def create_invoice(amount):
    api = cryptonator_API.cryptonatorAPI(merchant_id=MERCHANT_ID, secret=SECRET,  language='ru')
    invoice_id = api.create_invoice(item_name=ITEM_NAME, invoice_amount=amount, invoice_currency='usd')
    return invoice_id