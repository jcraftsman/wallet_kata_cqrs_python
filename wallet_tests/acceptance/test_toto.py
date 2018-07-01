import unittest

from domain.amount import Amount
from domain.stock import Stock
from domain.stock_type import EUR, PETROLEUM
from domain.wallet import Wallet
from infrastructure.fixed_rate_provider import FixedRateProvider


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Given
        rate_provider = FixedRateProvider()

        # When
        value = Wallet([Stock(5, PETROLEUM)]).value(EUR, rate_provider)
        rate = 5 * rate_provider.rate(PETROLEUM, EUR)

        # Then
        self.assertEqual(value, Amount(rate, EUR))
