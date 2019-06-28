import requests

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


class StreetToPostalIndex:
    def _send_request(self, city, street):
        return requests.get(f"http://post-api.ru/api/v2/ibc.php?c={city}&s={street}&apikey=ocxk6kh56340ouy5")

    def _parse_response(self, response):
        response = response.json()
        if not response['content']:
            return None
        elif response['content'][0]['indexes'][0]:
            return response['content'][0]['indexes'][0]
        else:
            return response['content'][0]['indexes'][1]

    def get_index(self, city, street):
        request = self._send_request(city, street)
        response = self._parse_response(request)
        if response:
            return response
        else:
            return 'not found'


class CostCalculation:
    def _send_request(self, index_from, index_to):
        return requests.get(f"https://postprice.ru/engine/russia/api.php?from={index_from}&to={index_to}&mass=100&valuation=500&vat=1")

    def _parse_response(self, response):
        response = response.json()
        if response:
            return response['pkg']
        else:
            return None

    def get_index(self, index_from, index_to):
        request = self._send_request(index_from, index_to)
        response = self._parse_response(request)
        if response:
            return response
        else:
            return 'not found'


class DeliveryView(APIView):
    queryset = None
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        index_from = StreetToPostalIndex().get_index(request.GET['from_city'], request.GET['from_street'])
        index_to = StreetToPostalIndex().get_index(request.GET['to_city'], request.GET['to_street'])
        response = CostCalculation().get_index(index_from, index_to)
        return Response(response)
