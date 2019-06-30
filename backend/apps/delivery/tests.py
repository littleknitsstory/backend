from .viewsets import StreetToPostalIndex, CostCalculation

from rest_framework.test import APITestCase


def test_service_street_to_index():
    index = StreetToPostalIndex.get_index('москва', 'алтуфьевское')
    assert index == '127273'


# def test_service_index_to_pay():
#     cost = CostCalculation.get_price('127273', '450022')
#     assert cost.data == 259.34


class AccountTests(APITestCase):
    def test_api_delivery(self):
        response = self.client.get(
            '/delivery-management/mail-delivery?from_city=москва&from_street=алтуфьевское&to_city=уфа&to_street=парковая')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 259.34)
