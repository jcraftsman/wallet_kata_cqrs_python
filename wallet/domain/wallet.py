from domain.amount import Amount
from domain.stock import Stock


class Wallet(object):
    def __init__(self, stocks: [Stock]) -> None:
        super().__init__()
        self.stocks = stocks

    def value(self, stock_type, rate_provider) -> Amount:
        price = 0
        for stock in self.stocks:
            rate = rate_provider.rate(stock.stock_type, stock_type)
            price += stock.volume * rate
        return Amount(price, stock_type)
