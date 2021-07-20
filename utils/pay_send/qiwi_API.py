import requests

from utils.get_currency import split_amount
from data.config import QIWI_API_KEY


class qiwiAPI:
    url = 'https://qiwi.com/payment/form/99?'

    def __init__(self, api_access_token, qiwi_login):
        self.api_access_token = api_access_token
        self.qiwi_login = qiwi_login

    def create_qiwi_invoice(self, amount):
        s = requests.Session()
        s.headers = {'content-type': 'application/json'}
        s.headers['authorization'] = 'Bearer' + self.api_access_token
        s.headers['User-Agent'] = 'Android v3.2.0 MKT'
        s.headers['Accept'] = 'application/json'
        if amount > 99999:
            raise ValueError('amount не может превышать 99999 из-за ограничений на один платеж внутри QIWI')
        amount_dict = split_amount(amount)
        parameters = {}
        parameters['amountInteger'] = amount_dict['amountInteger']
        parameters['amountFraction'] = amount_dict['amountFraction']
        parameters['currency'] = '643'
        parameters['extra[\'comment\']'] = 'MoneyTransfer'
        parameters['extra[\'account\']'] = self.qiwi_login
        parameters['blocked'] = ['sum', 'account', 'comment']
        h = s.get('https://qiwi.com/payment/form/99?', params=parameters)
        return h.url

