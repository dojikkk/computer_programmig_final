class Won:
    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self.__account

    @amount.setter
    def amount(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError
        self.__account = value
        pass


    def __add__(self, other):
        if isinstance(other, Won):
            return Won(self.amount + other.amount)
        elif isinstance(other, int):
            return Won(self.amount + other)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Won):
            return Won(self.amount - other.amount)
        elif isinstance(other, int):
            return Won(self.amount - other)
        else:
            raise TypeError

    def __lt__(self, other):
        # Compare amounts between two Won objects. 🔴 If other is not a Won -> raise TypeError
        # TODO
        if not isinstance(other, Won):
            raise TypeError
        return self.amount < other.amount

    def __str__(self):
        # Format: "1000원"
        # TODO
        return f"{self.amount}원"