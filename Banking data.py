#banking data manipulation
listofUsers = []

class BankUsers():
    def __init__(self):
        self.name = ""
        self.accountno = 0
        self.principalamount = 0
        self.time = 0
        self.rate = 0
        
    def calulateSI(self):
        self.SI = (self.principalamount * self.rate * self.time)/100
        
    def calculateAmount(self):
        self.Amount = self.principalamount + self.SI
i=0
while i<5:
      user = BankUsers()
      user.name = input("Enter user name: ")
      listofUsers.append(user.name)
      user.accountno = int(input("Enter your account number: "))
      user.principalamount = float(input("Enter the principal amount: "))
      user.rate =float(input("Enter rate per month: "))
      user.time = float(input("Enter time in months: "))
      user.calulateSI()
      user.calculateAmount()
      print(user.SI)
      i+=1
print(listofUsers)
for user in listofUsers:
    print(" {} have to pay {} simple interst and the total amount is {}".format(user.name, user.SI, user.amount))
          
      
     
        
          

