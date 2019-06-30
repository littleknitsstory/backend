import requests

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


POST_API_RU_URL = 'http://post-api.ru/api/v2/ibc.php?c={}&s={}&apikey={}'
POST_API_RU_APIKEY = 'ocxk6kh56340ouy5'

POSTPRICE_RU_URL = 'https://postprice.ru/engine/russia/api.php?from={}&to={}&mass={}&valuation={}&vat={}'
POSTPRICE_RU_MASS = 100  # Масса отправления, в граммах
POSTPRICE_RU_VALUATION = 500  # Объявленная ценность, в рублях
POSTPRICE_RU_VAT = 1  #  НДС 20% (1 — с НДС, 0 — без НДС)


class StreetToPostalIndex:
    def _send_request(self, city, street):
        return requests.get(POST_API_RU_URL.format(city, street, POST_API_RU_APIKEY))

    def _parse_response(self, response):
        response = response.json()
        if not response['content']:
            return
        elif response['content'][0]['indexes'][0]:
            return response['content'][0]['indexes'][0]
        else:
            return response['content'][0]['indexes'][1]

    @staticmethod
    def get_index(city, street):
        request = StreetToPostalIndex()._send_request(city, street)
        response = StreetToPostalIndex()._parse_response(request)
        return response if response else 'not found'


class CostCalculation:
    def _send_request(self, index_from, index_to):
        return requests.get(POSTPRICE_RU_URL.format(index_from, index_to, POSTPRICE_RU_MASS, POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT))

    def _parse_response(self, response):
        response = response.json()
        if response:
            return response['pkg']
        return

    @staticmethod
    def get_price(index_from, index_to):
        request = CostCalculation()._send_request(index_from, index_to)
        response = CostCalculation()._parse_response(request)
        return Response(response) if response else Response('not found')


class DeliveryView(APIView):
    queryset = None
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        index_from = StreetToPostalIndex.get_index(request.GET['from_city'], request.GET['from_street'])
        index_to = StreetToPostalIndex.get_index(request.GET['to_city'], request.GET['to_street'])
        response = CostCalculation.get_price(index_from, index_to)
        return response
