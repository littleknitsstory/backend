#from decouple import config

BASE_CURRENCY = "EUR"
CURRENCIES = ("USD", "EUR", "RUB")
CURRENCY_CHOICES = [("USD", "USD $"), ("EUR", "EUR €"), ("RUB", "RUB ₽")]
EXCHANGE_BACKEND = "djmoney.contrib.exchange.backends.FixerBackend"
OPEN_EXCHANGE_RATES_APP_ID = "" #config("OPEN_EXCHANGE_RATES_APP_ID", "")
FIXER_ACCESS_KEY = "" #config("FIXER_ACCESS_KEY", "")
FIXER_URL = "http://data.fixer.io/api/latest?symbols=EUR,USD,RUB"
LANG_EXCHANGE = {"ru": "RUB", "en": "EUR"}
