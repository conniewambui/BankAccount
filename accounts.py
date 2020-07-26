from datetime import datetime
class BankAccount:
        
    def __init__(self, bank, phone_number, first_name, last_name):
        self.bank = bank
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        loan = {}
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        

    def getCurrentTime(self):
        now = datetime.now()
        time_formatted = now.strftime("%b %d %Y, %H;%M:%S")  
        return time_formatted  
    
        
    def account_name(self):
        time = self.getCurrentTime()
        name = "{} account for  {} {} at ".format(self.bank, self.first_name,self.last_name, time)

        return name
        
   
    def deposit(self, amount):
        


        amount = input("Enter the amount you want to deposit : ")
        try:
            amount = int(amount)
        except:
            print("Invalid input, only numbers are allowed.") 
            return
        if amount <= 0:
            print("You can not deposit zero or a negative amount")
        else:
            self.balance += amount
            self.deposits.append(amount) 
            time = self.getCurrentTime()
            
            print("You have deposited {} to {} on {} ".format(amount, self.account_name(),time)) 

      
    def withdraw(self, amount):
        amount = input("Enter the amount you want to withdraw : ")
        try:
            amount = int(amount)
        except:
            print("Invalid input, only numbers are allowed.") 
            return   
          
        if amount <= 0:
              print("You cannot withdraw a zero or a negative amount")

        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            time = self.getCurrentTime()
            print("You have withdrawn {} from {} at {}".format(amount, self.account_name(),time))

 
    def  get_balance(self):
        time = self.getCurrentTime()
        return "The balance for {} is {} at {}".format(self.account_name(),self.balance, time)
     
    def show_deposit_statement(self):
        for deposit in self.deposits:
            time = self.getCurrentTime()

            print("Dear customer your deposit statement is {} as at {}.".format(deposit,time))
       

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            time = self.getCurrentTime()
            print("Dear customer your withdrawal statement is {} as at {}.".format(withdrawal,time))



    def request_loan(self,amount): 
        amount = input("Enter the amount of loan you want : ")
        try:
            amount = int(amount)
        except:
            print("!!!Invalid input, only numbers are allowed.") 
            return
        if amount <= 0:
            print("Dear customer, you cannot request a loan of zero or negative amount.")

        else: 
            self.loan = amount 
            time = self.getCurrentTime() 
            print("Dear customer, your account has been debited with a loan of {} on {}".format(amount,time))   

    def repay_loan(self,amount):
        amount = input("Enter the amount of loan you want to REPAY : ")
        try:
            amount = int(amount)
        except:
            print("!!!Invalid input, only numbers are allowed.") 
            return
        if amount <= 0:
            print("Dear Customer you cannot repay you loan with a zero or a negative amount.")
        elif self.loan == 0:
            print("Dear Customer you do not have a loan at the moment.")

        elif amount > self.loan :
            time = self.getCurrentTime()
            print("Dear Customer, Your loan is {} , please enter an amount that is less or equal to your loan {}." .format(self.loan,time))

        else:
            time = self.getCurrentTime()
            self.loan -= amount
            print("Dear Customer, you have repaid your loan with {} , your loan balance is {} on {}".format(amount,self.loan,time))

            
                  







    



