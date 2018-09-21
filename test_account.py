import unittest
from account import bank_account

class TestAccount (unittest.TestCase):
    def open(self):
        self.account = bank_account()
    
    def balance(self):
        self.open()
        self.assertEqual(self.balance(), 0)
    def deposit(self):
        self.open()
        self.deposit(100)
        self.assert_Equal(self.balance(), 100)
    def withdraw(self):
        self.open()
        self.balance(100)
        self.withdraw(20)
        self.assertEqual(self.balance(), 80)
    def close(self):
        self.open()
        self.close()

if __name__ == "__main__":
    unittest.main()      