
"""
Task#3:

Create a BankAccount class with attributes for account holder name, account number, and balance. 
Include methods to deposit money (increasing balance), withdraw money (decreasing balance with sufficient funds 
check), and display account details. Ensure withdrawals do not cause negative balance and deposits are 
positive amounts only.
"""
class BankAccount:
    def __init__ (self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def Deposit(self):
        self.amount=int(input("Enter deposit amount :"))
        if self.amount >0:
            self.balance+=self.amount
            print("Deposited successfully")
        else:
            print("Invalid Deposit amount")
    def withdraw(self):
        self.amount=int(input("Enter withdrawal amount :"))
        if self.amount>0:
            self.temp=self.balance-self.amount
            if self.temp<0:
                print("Not enough balance")
            else:
                self.balance-=self.amount
                print("Withdrawal successful")
        else:
            print("Enter a valid withdrawal amount")
    def display(self):
        print("Account Holder Name :",self.name)
        print("Account Number :",self.number)
        print("Current Balance :",self.balance)

e1=BankAccount("Saad",18726,41000)
while True:
    print("Press 1 for deposit")
    print("Press 2 for withdrawal")
    print("Press 3 for Account Details")
    print("Press 4 or exit to quit")
    choice=input("Enter your choice :")
    if choice=="1":
        e1.Deposit()
    elif choice=="2":
        e1.withdraw()
    elif choice=="3":
        e1.display()
    elif choice=="4" or choice=="exit":
        print("Exiting")
        break
    else:
        print("Invalid Choice")



