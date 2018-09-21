class bank_account:

    def __init__ (self):
        self.balance = 0
        self.status = True

    def open(self):
        pass

    def balance(self):
        if self.status == False:
            raise "Error"
        return self.balance

    def deposit(self, money):
        if self.status == False:
            raise "Error"
        if money < 0:
            raise "Error"
        self.balance += money

    def withdraw(self,money):
        if self.status == False:
            raise "Error"
        if money > self.balance:
            raise "Error"
        if money < 0:
            raise "Error"
        self.balance -= money
    
    def close(self):
        self.status = False