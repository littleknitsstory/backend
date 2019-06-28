from .viewsets import StreetToPostalIndex, CostCalculation


def test_service_street_to_index():
    index = StreetToPostalIndex().get_index('москва', 'алтуфьевское')
    assert index == '127273'


def test_service_index_to_pay():
    cost = CostCalculation().get_index('127273', '450022')
    assert cost == 259.34
