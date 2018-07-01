from domain.rate_provider import RateProvider
from domain.stock_type import PETROLEUM, EUR, USD


class FixedRateProvider(RateProvider):

    def rate(self, from_stock_type, to_stock_type):
        return RATES[from_stock_type][to_stock_type]


RATES = {
    PETROLEUM: {
        EUR: 63.4938,
        USD: 74.31
    }
}
