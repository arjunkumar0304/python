class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance for {self.owner}: ₹{self.__balance}")

acc = BankAccount("Karan", 5000)
acc.deposit(2000)
acc.show_balance()

# Output
# Balance for Karan: ₹7000
##### You can’t access acc.__balance directly — it’s private
