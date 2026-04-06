class Portfolio:
    def __init__(self, starting_cash=100000):
        self.cash     = starting_cash
        self.holdings = {}

    def buy(self, ticker, quantity, price):
        cost = quantity * price
        if cost <= self.cash:
            self.holdings[ticker] = \
                self.holdings.get(ticker, 0) + quantity
            self.cash -= cost
            return True
        return False

    def sell(self, ticker, quantity, price):
        if self.holdings.get(ticker, 0) >= quantity:
            self.holdings[ticker] -= quantity
            self.cash += quantity * price
            return True
        return False

    def get_state(self):
        return {
            "cash":     round(self.cash, 2),
            "holdings": self.holdings
        }