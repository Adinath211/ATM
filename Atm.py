class ATM:
    def __init__(self):
        self.balance=1000
    def Deposit(self):
        amount=int(input("Enter the Amount to be Deposited:"))
        self.balance+=amount
        print("Amount Deposited in Bank Account:",amount)
        print("\n Net Available Balance =", self.balance) 
    def Withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
            print("\n Net Available Balance =", self.balance) 
        else:
            print("\nInsufficient balance")
    def Inquiry(self):
        print("\n Net Available Balance =", self.balance)     
self=ATM()        
action=int(input("Please enter 1 to Deposit 2 to Withdraw 3 to Check your bank Balance "))            
if action==1:
    self.Deposit()  
if action==2:
    self.Withdraw()                    
if action==3:
    self.Inquiry()                                              
