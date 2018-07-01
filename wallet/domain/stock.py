class Stock(object):
    def __init__(self, volume, stock_type) -> None:
        super().__init__()
        self.volume = volume
        self.stock_type = stock_type