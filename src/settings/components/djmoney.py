from decouple import config

BASE_CURRENCY = "RUB"
CURRENCIES = ('USD', 'EUR', 'RUB')
CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €'), ('RUB', 'RUB ₽')]

EXCHANGE_BACKEND = 'djmoney.contrib.exchange.backends.FixerBackend'
OPEN_EXCHANGE_RATES_APP_ID = config('OPEN_EXCHANGE_RATES_APP_ID', '')
FIXER_ACCESS_KEY = config('FIXER_ACCESS_KEY', '')

# OPEN_EXCHANGE_RATES_URL = 'https://openexchangerates.org/api/historical/2017-01-01.json?symbols=EUR,NOK,SEK,CZK'
FIXER_URL = 'http://data.fixer.io/api/latest?symbols=EUR,USD,RUB'

LANG_EXCHANGE = {
	"ru": "RUB",
	"en": "EUR"
}
