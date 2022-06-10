# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.


class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []


    def deposit(self,amount):
        self.deposits.append(amount)
        if amount<=0:
            return f"Deposit ,ust be positive amount"
        else:

            self.balance+=amount
            print(self.deposits)
            return f"Hi {self.account_name} you have deposited {amount} and your balance is {self.balance} and this are your statements {self.deposits}"


    def withdraw(self,amount):
        self.transaction = 100
        self.withdrawals.append(amount)
        if amount<=0:
            return f"withdraw must be positive"
        elif amount>self.balance:
            return f"your balance is {self.balance}, you cant withdraw {amount}"
        else:
            self.balance-=amount+self.transaction
            return f"Hi {self.account_name} you have withdrawn {amount} and your balance is {self.balance} your withdrawal statements are {self.withdrawals}"


    def deposit_statement(self):
        for depo in self.deposits:
            print(depo, end="\n")

    def withdrawals_statements(self):
        for withdro in self.withdrawals:
            print(withdro,end="\n")
    
    def current_balance(self):
        return self.balance













































