class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,inital_amount,acct_name):
        self.balance = inital_amount
        self.name = acct_name
        print(f"\nAccount {self.name} created. \nBalance = {self.balance:.2f}/= LKR.")

    def get_balance(self):
        print(f"\nBalance : \nAccount '{self.name}' \nBalance = {self.balance:.2f}/= LKR.")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\nDeposit Complted")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount :
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name} only has a balance of {self.balance:.2f}/= LKR.")

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self, amount , account):
        try:
            print('\n********\n\nBeginning Transfer....🚀')
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer completed!!💹\n\n********')
        except BalanceException as error:
             print(f"\transfer interrupted : {error}")

class InterstRewardsAcct(BankAccount):

    def deposit(self,amount):
        self.balance = self.balance + amount * 1.05
        print(f"\nDeposit Complted")
        self.get_balance()
    
class SavingAcct(InterstRewardsAcct):

    def __init__(self, inital_amount, acct_name):
        super().__init__(inital_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount - self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complted.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")
   