class Bank_Account: 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
    def bankFees(self):
        self.balance = (95/100)*self.balance        
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")    
newAccount = BankAccount(2178514584, "Albert" , 2700)   
   
s = Bank_Account() 

 
s.deposit() 
s.withdraw() 
s.display() 
newAccount.display()