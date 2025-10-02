class Bank:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

#        @staticmethod
    def debit(self, amount):
            self.balance -= amount
            print("Rs.", amount, "was debited")
            print("Your balance amount is: ", self.get_balance())

    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("Your balance amount is: ", self.get_balance())

    def get_balance(self):
          return self.balance
             
acc1 = Bank(2223, 7535)
acc1.debit(11)
acc1.credit(99)
