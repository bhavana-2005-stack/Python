class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(amount,"deposited")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("less balance")
        else:
            self.__balance-=amount
            print(amount,"withdrawn")

    def get_balance(self):
        print("balance:",self.__balance)
b1=BankAccount(0)
b1.deposit(5000)
b1.withdraw(2000)
b1.get_balance()


