class BankAccount:
    def __init__(self, bank, phone_number, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number
        self.loan_balance = 0
    
        
    def account_name(self):
        name = "{} account for  {} {}".format(self.bank, self.first_name, 
        self.last_name, self.deposit)
        
        return name
        
    def deposit(self, amount):

        self.balance += amount 
        print("You have deposited {} into your account ".format(amount))
    
    
    def withdraw(self, amount): 

        if self.balance>=amount: 
            self.balance-=amount
            print("\n You Withdrew:", amount) 
        else:
            print("\n Insufficient balance  ") 

    
    def  get_balance(self):

        return "The balance for {} is {}".format(self.account_name(),self.loan)

    def loan_balance(self,amount):
        if loan_balance < 0: 
            self.loan_balance += amount

        else:
          print("Sorry you already have a loan balance.")




    def repay(self,amount):
        if self.loan_balance == 0:
            print("You have no loan balance")
        elif amount>self.loan_balance:
            self.loan_balance=0

        elif amount<=self.loan_balance:
            self.loan_balance-=amount
        return

            
                  







    



