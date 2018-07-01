from unittest import TestCase
from unittest.mock import Mock, call

from domain.amount import Amount
from domain.stock import Stock
from domain.stock_type import PETROLEUM, EUR, USD, BITCOIN
from domain.wallet import Wallet


class TestWallet(TestCase):

    def test_value_should_return_the_stock_amount(self):
        # Given
        rate_provider = Mock()
        rate_provider.rate.return_value = 80

        # When
        wallet_value = Wallet([Stock(1, PETROLEUM)]).value(EUR, rate_provider)

        # Then
        self.assertEqual(wallet_value, Amount(80, EUR))

    def test_value_should_return_the_stock_amount_using_the_rate_provider(self):
        # Given
        rate_provider = Mock()
        rate_provider.rate.return_value = 78

        # When
        wallet_value = Wallet([Stock(1, PETROLEUM)]).value(USD, rate_provider)

        # Then
        self.assertEqual(wallet_value, Amount(78, USD))
        rate_provider.rate.assert_called_once_with(PETROLEUM, USD)

    def test_value_should_return_the_weighted_stock_amount_using_the_rate_and_stock_volume(self):
        # Given
        rate_provider = Mock()
        rate_provider.rate.return_value = 7500

        # When
        wallet_value = Wallet([Stock(2, BITCOIN)]).value(USD, rate_provider)

        # Then
        self.assertEqual(wallet_value, Amount(15000, USD))
        rate_provider.rate.assert_called_once_with(BITCOIN, USD)

    def test_value_should_return_the_weighted_stock_amount_for_all_stocks_in_the_wallet(self):
        # Given
        rate_provider = Mock()
        rate_provider.rate.side_effect = [89, 7000]

        # When
        wallet_value = Wallet([Stock(10, PETROLEUM), Stock(2, BITCOIN)]).value(EUR, rate_provider)

        # Then
        self.assertEqual(wallet_value, Amount(14890, EUR))
        rate_provider.rate.assert_has_calls(
            [
                call(PETROLEUM, EUR),
                call(BITCOIN, EUR)
            ])
