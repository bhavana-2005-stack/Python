class Payment:
    def __init__(self,amount):
        self.amount=amount
class CashPayment(Payment):
    def pay(self):
        print(self.amount,"is paid in cash")
class CardPayment(Payment):
    def pay(self):
        print(self.amount,"paid through card:")
class UPIPayment(Payment):
    def pay(self):
        print(self.amount," paid through upi:")
c1=CashPayment(500)
c2=CardPayment(100000)
c3=UPIPayment(6268)
c1.pay()
c2.pay()
c3.pay()


