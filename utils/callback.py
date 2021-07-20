from aiogram.utils.callback_data import CallbackData

currency_cb = CallbackData('order', 'action', 'currency')
country_cb = CallbackData('order', 'action', 'country')
pay_cb = CallbackData('deposit', 'type', 'url')
