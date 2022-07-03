from datetime import datetime


class Account:
    def __init__(self,account_name,account_number):
        self.account_number=account_number
        self.account_name = account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=100
        self.loan_balance=0
        
    
    def withdraw (self,amount):
        self.amount=amount
        date=datetime.now()

        if amount>self.balance:
            return f"Dear {self.account_name}, you have insuffient funds for this withdraw"
        elif amount<=0:
            return f"Dear {self.account_name}, you can't withdraw zero amount "            
        else:
             self.balance -=amount
             newdct={
                "date":date.strftime("%d/%m/%Y"),
                "amount":amount,
                "narration":'withdraw'}
             self.withdrawals.append(newdct)
             withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
             return "insufficient balance"
        self.balance-=amount+self.transaction
        return f"You have withdrawn Kshs.{self.withdrawals} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')}"

      
    def deposit(self,amount):
        date=datetime.now()
        
        self.amount=amount 
        if amount<=0:
            return f"deposit amount must be greater than zero(0)"
        else:
             self.balance+=amount
             dct={
                "date":date.strftime("%d/%m/%Y"),
                "amount":amount,
                "narration":'deposit'}
             self.deposits.append(dct)
             
        return f"You have deposited Kshs.{amount} and your new balance is {self.balance}"
    
         
    def deposit_statement(self):
        for depo in self.deposits:
            print (depo)
    def withdraw_statement(self):
        for withdro in self.withdrawals: 
            print(withdro)
         
    def current_balance(self):
        return f" Your current balance is  {self.balance}" 
    
    def full_statement(self):
        statement=self.deposits+self.withdrawals
        for state in statement:
           date = state['date']
           amount = state['amount']
           narration = state['narration']   

           print( f"{date}---{amount}----{narration}")

    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
            
        if len(self.deposits) <10:
            return f"you are not eligible to borrow.make {10-len(self.deposits)} more deposits to borrow "
        if amount<100:
            return f"hello,you can borrow atleast above 100"  
        if amount>sum/3:
            return f"you can borrow upto {sum/3}" 
        if self.balance!=0:
            return f"you have Kshs.{self.balance} you can't borrow yet you still have balance on your account"
        if self.loan_balance!=0:
            return f"you have a debt of {self.loan_balance} you have to pay first for you to borrow."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"you have borrowed {amount} your loan is now at {self.loan_balance}"
    
    def loan_repayment(self,amount):
        
         if amount<=self.loan_balance:
             self.loan_balance-=amount
             
             return f" thank you for paying the loan of {amount} your account balance is {self.loan_balance}"
               
         else:
            overpay = amount - self.loan_balance
            self.loan_balance+=overpay
            self.loan_balance=0
            return f"thank you and your loan balance is {self.loan_balance}"
            
         
    def transfer(self,amount,new_account):
        if amount<=self.balance:
            self.balance-=amount
            new_account.deposit(amount)
            return f"you have sent {amount} to {new_account.account_name} with the name your new balance is {self.balance}"        

        else:
            amount>self.balance
            return f"You have inssufficient funds to transfer {amount} to {new_account} "
