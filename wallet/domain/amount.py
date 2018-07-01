class Amount(object):

    def __init__(self, price, currency) -> None:
        super().__init__()
        self.price = price
        self.currency = currency

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__
