class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, x, y):
        self.dollars = x
        self.cents = y

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents

        if self.cents > 99:
            self.dollars = self.dollars + (self.cents // 100)
            self.cents = self.cents % 100


# money = PiggyBank(1, 1)

# money.add_money(0, 99)
# money.add_money(0, 88)
# money.add_money(500, 500)
# print(money.dollars, money.cents)
