from utils.pay_send import cryptonator_API
from decimal import Decimal

api = cryptonator_API.cryptonatorAPI(merchant_id='e9d0f828c9b8b52f00631e4b6789b0fb', secret='a4533e9799acd0e92a9800c20a10d556', language='ru')
amount = Decimal('40')

invoice_id = api.create_invoice(item_name='test_tovar', invoice_amount=amount, invoice_currency='usd')
print(invoice_id)
status = api.check_invoice(invoice_id)
print(status)