from datetime import datetime
class Account:
        
    def __init__(self, phone_number, first_name, last_name):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.loan = 0
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_repayments = []
        

    def getCurrentTime(self):
        now = datetime.now()
        time_formatted = now.strftime("%b %d %Y, %H;%M:%S")  
        return time_formatted  
    
        
    def account_name(self):
        time = self.getCurrentTime()
        name = "Account for  {} {} at ".format(self.first_name,self.last_name, time)

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
            
            print("You have deposited {} to {} {} on {} ".format(amount, self.account_name(),time)) 

      
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
            repayment= {"time": time, "amount": amount}
            self.loan_repayments.append(repayment)
            print("Dear Customer, you have repaid your loan with {} , your loan balance is {} on {}".format(amount,self.loan,time))

    def loan_repayment_statement(self,repayment):
        for repayment in self.loan_repayments:
            time = repayment["time"]
            amount = repayment ["amount"]
            time = self.getCurrentTime()
            statement =("You have repaid {} on {}".format(amount, time) )
            print(statement)    
                  


class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number) 

class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider ):
        self.service_provider = service_provider
        self.airtime = []
        self.paybills = []
        super().__init__(first_name, last_name, phone_number)

    def buy_airtime(self,amount):
        try:
            amount +10 
        except TypeError:
            print("Enter the amount in figures.")   
            return

        if amount > self.balance:
            print("You dont have enough money. Your balance is {}".format(self.balance)) 
        else: 
            self.balance -= amount 
            time = self.getCurrentTime()
            airtime = amount
            self.airtime.append(airtime)
            print("You have bought airtime worth KSHs{} on {} ".format(amount, time))

            
    def paybill(self,amount):
        try:
            amount +10
        except:
            print("Dear Customer please enter the amount in figures.")    
        if amount <= 0:
            print ("Dear Customer kindly top up your balance to enjoy the service.")    
        elif amount > self.balance:
            print("Dear customer your balance is KSHs{} kindly enter an amount that is less than your balance .".format(self.balance))
        else:
            self.balance -= amount
            time = getCurrentTime.now()
            paybills = amount
            self.paybills.append(paybills)
            print("You transferred this amount KSHs {} on {}.".format(amount,time))
    def receive_money(self, amount):
        time = self.getCurrentTime()
        self.balance += amount
        print("You have received this amount KHSs {}, Your account balance is KSHs{} at {}".format(amount, self.balance, time))


    def send_money(self,amount):
        time = self.getCurrentTime()
        try:
            amount +10
        except:
            print("Dear customer please enter the amount in figures.")    
        if amount <= 0:
            print ("Dear Customer kindly top up your balance to enjoy the service.") 
        elif amount > self.balance:
            print("Dear customer your balance is KSHs {}  at {} kindly an amount that is less than your balance.".format( self.balance, time))  
        else:
            self.balance -= amount
            print("You have send this KSHs {}, Your account balance is KSHs{} at {}".format(amount, self.balance, time))
