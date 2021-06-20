#ATM display

#taking inputs
print("Hello!! Welcome to Bank ATM")
closeList = ["n","N","no","NO","No","nO"]
restart = "y"
chances = 3
Balance = 1000

while  chances>=0:
    pin = int(input("Please enter your 4-digit pin: "))
    if pin==1234:
        while restart not in closeList:
            print("Please Enter 1 for your Balance")
            print("Please Enter 2 to make a Withdrawl")
            print("Please enter 3 to pay in ")
            print("Please enter 4 to return card")
            
         
            option = int(input("what would you like you choose? "))
            if option == 1:
                print("Your Balance is:{}".format(Balance))
                    
                restart = input("would you like to continue? \n (y/n)")
                if restart in closeList:
                    print("THANK YOU")
                    break
            elif option == 2:
                withdrawl = float(input("How much do you like to withdraw?\n 10,20,50,100\n for other enter: "))
                if withdrawl in [10,20,50,100]:
                    Balance = Balance - withdrawl
                    print("Your balance is now: {}".format(Balance))
                    restart = input("would you like to continue? \n")
                    if restart in closeList:
                        print("THANK YOU")
                        break
                if withdrawl not in [10,20,50,100]:
                    withdrawl = float(input("Confirm enter Desired amount: "))
                    Balance = Balance - withdrawl
                    print("Your balance is now: {}".format(Balance))
                    restart = input("would you like to continue? \n")
                    if restart in closeList:
                        print("THANK YOU")
                        break
            elif option== 3:
                Pay_in = float(input("How much would you like to pay in : "))
                Balance = Balance + Pay_in
                print("Your Balance is now:{}".format(Balance))
                restart = input("would you like to continue? \n")
                if restart in closeList:
                    print("THANK YOU")
                    break
            elif option == 4:
                print("Your card is returned....Please wait!!")
                print("Thank you for your service")
                restart = input("would you like to continue? \n (y/n)")
                if restart in closeList:
                    print("THANK YOU")
                    break
                    
            else:
                print("please enter a correct number:\n")
    elif pin != 1234:
        print("Incorrect Pin")
        chances-=1
        if chances ==0:
            print("No more Tries")
            break

