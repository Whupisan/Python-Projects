# importing the Bank Account python file for solidarity
from Bank_Account import*

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.02, balance = 200)
    def deposit(self, amount):
        self.account.balance += amount
        return self
    def withdrawal(self, amount):
        if(self.account.balance <=0):
            print("I'm sorry {}, but you don't have enough funds to withdrawal ${}.".format(self.name, amount))
        else:
            self.account.balance -= amount
        return self
    def xfersMoneyTo(self, tranferee, amount):
        if(self.account.balance < amount):
            print("Please tell me how you are going to transfer ${}, when you only have ${} in your account?".format(amount, self.account.balance))
        elif(amount < 0.01):
            print("I'm sorry {}, but you have to transfer at least a penny! Or else it seems like {} owes you ${}!".format(self.name, tranferee.name, amount*-1))
        else:
            self.account.balance -= amount
            tranferee.account.balance += amount
        return self
    def check_balance(self):
        print("Greetings {}. Your balance is ${}.".format(self.name, self.account.balance))
        return self
    def openAcct(self):
        pass

Mike = User("Mickie", "madman@yahoo.com")
Tommy = User("Theodore", "madmonkeyIam@euphoria.com")
Alex = User("Alexis", "mirrorChild@bluemonkey.southside")

Mike.deposit(10)
Tommy.withdrawal(200)  

Mike.check_balance()

Tommy.deposit(3999)
Tommy.xfersMoneyTo(Mike, 500)

Mike.check_balance()
Tommy.check_balance()

Mike.xfersMoneyTo(Tommy, 418)
Mike.xfersMoneyTo(Alex, 56)
Tommy.xfersMoneyTo(Alex, -45)

Mike.check_balance()
Tommy.check_balance()
Alex.check_balance()

Alex.account.display_account_info()


# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
# Create a file with the User class, including the __init__ and make_deposit methods Add a make_withdrawal method to the User class Add a display_user_balance method to the User class Create 3 instances of the User class Have the first user make 3 deposits and 1 withdrawal and then display their balance Have the second user make 2 deposits and 2 withdrawals and then display their balance Have the third user make 1 deposits and 3 withdrawals and then display their balance BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances