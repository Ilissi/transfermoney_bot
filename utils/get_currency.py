import requests


def get_currency(post_currency, get_currency):
    req_values = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    append_dict = {}
    for values in req_values.json():
        if values['cc'] == post_currency:
            append_dict.update(post_currency=float(values['rate']))
        elif values['cc'] == get_currency:
            append_dict.update(get_currency=float(values['rate']))
        elif post_currency == "USD":
            append_dict.update(post_currency=float(values['rate']))
            append_dict.update(get_currency=float(values['rate']))
        elif post_currency == 'UAH':
            append_dict.update(get_currency=float(1))
        elif get_currency == 'UAH':
            append_dict.update(get_currency=float(1))
    return append_dict


def calculate_sum(dict_object):
    currency_dict = get_currency(dict_object['get_currency'], 'USD')
    print(currency_dict)
    get_value = (currency_dict['post_currency']/currency_dict['get_currency'])*1.157*dict_object['amount_order']
    return round(get_value, 1)


def split_amount(amount):
    list_elements = str(amount).split('.')
    qiwi_dict = {}
    if len(list_elements) == 1:
        qiwi_dict.update(amountInteger=list_elements[0])
        qiwi_dict.update(amountFraction='00')
    elif len(list_elements) == 2:
        qiwi_dict.update(amountInteger=list_elements[0])
        qiwi_dict.update(amountFraction=list_elements[1])
    return qiwi_dict





