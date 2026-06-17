class Account:
    def __init__(self, owner, balance):
        """
        owner: str, balance: initial balance (int or float)
        balance must be stored through the property/setter rules below.
        """
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        """
        - If value is neither int nor float, raise TypeError
        - If value is negative, raise ValueError
        - Otherwise, store it normally
        """
        if value < 0:
            raise ValueError
        elif not isinstance(value, (int or float)):
            raise TypeError
        self.__balance = value

    def __repr__(self):
        """ e.g. Account('Ana', 100) """
        return f"Account({self.owner}, {self.balance})"

    def __eq__(self, other):
        """ True if the two Accounts have equal balance (ignore owner) """
        return self.balance == other.balance

    def __add__(self, other):
        """
        - Account + Account  -> return a NEW Account with the summed balance
                                (use self.owner as the owner)
        - Account + number    -> return a NEW Account with number added to balance
        - any other type      -> return NotImplemented
        Never mutate the existing object (always build and return a new one).
        """
        if isinstance(other, Account):
            return Account(self.owner, self.balance + other.balance)
        elif isinstance(other, int or float):
            return Account(self.owner, self.balance + other)
        else:
            return NotImplemented