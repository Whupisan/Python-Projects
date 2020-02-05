class BankAccount():
    def __init__(self, balance, interest_rate):
        self.acct_holder = ""
        self.balance = 0
        self.interest_rate = 0.01
        self.interest_yield = 0
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
        else:
            print("Please enter a non-imaginary amount please.")
        return self
    def withdrawal(self, amount):
        if(amount > self.balance):
            print("I'm sorry {}, but you don't have enough funds, you're short ${}.".format(self.acct_holder, amount-self.balance))
        else:
            self.balance -= amount
            print("You have successfully withdrew ${}.".format(amount))
        return self
    def yield_interest(self):
        interest_yield = self.balance*(self.interest_rate)
        print("You have gained ${} in interest yield so far!".format(interest_yield))
        return self
    def display_account_info(self):
        print("Your balance is ${}.".format(self.balance + self.interest_yield))
        return self

checking_acct = BankAccount(100, 0.04)
savings_acct = BankAccount(1500, 0.001)

# checking_acct.deposit(30).deposit(500).deposit(25).withdrawal(45).yield_interest().display_account_info()
# savings_acct.deposit(200).deposit(20).withdrawal(4).withdrawal(20).withdrawal(8).withdrawal(90).yield_interest().display_account_info()