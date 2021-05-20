

#Obtaining a calculator
#user defined functions
#this function adds the values    
def add(command1,command3):
    result1= command1+command3
    return round(result1,2)
#this function subtracts the values
def subtract(command1,command3):
    result2= command1-command3
    return result2
#this function multiply the values
def multiply(command1,command3):
    result3= command1*command3
    return round(result3,2)
#this function divide the values
def devision(command1,command3):
    result4= command1/command3
    return round(result4,2)
#this function find modulus of values
def modulus(command1,command3):
    result5= command1%command3
    return round(result5,2)
#this function find exponential
def exponential(command1,command3):
    result6= command1**command3
    return round(result6,2)
#an empty list
resultList =[]

#taking inputs from users

#using loops
try:
  i= 1
  while i<10:
        command1= float(input("Enter first number:"))
        if type(command1) != float:
            raise ValueError
        op= input("Choose operator:")
        if op.isalpha() or op.isnumeric(): 
            raise TypeError
        command3= float(input("Enter second number:"))
        if type(command3)!= float:
            raise ValueError
        if command3 == 0 and op=="/":
            raise ZeroDivisionError
        
        
#printing result according user's choice of operator
 
    
        if op=="+":
           result=add(command1, command3)
           print(result)
           resultList.append(result)
        elif op=="-":
            result= subtract(command1, command3)
            print(result)
            resultList.append(result)
        elif op=="*":
             result=multiply(command1, command3)
             print(result)
             resultList.append(result)
        elif op=="/":
             result=devision(command1, command3) 
             print(result)
             resultList.append(result)
        elif op=="%":
            result=modulus(command1, command3)
            print(result)
            resultList.append(result)
        elif op=="**":
            result=exponential(command1, command3)
            print(result)
            resultList.append(result)
        else:
            result="something went wrong"
            print(result)
            resultList.append(result)
        i+=1
        
except  ValueError:
        print("please enter only numeric value")
except TypeError:
        print("please enter operator only!!")
except ZeroDivisionError:
        print("the number divide by 0 is infinte")
        
except Exception as e:
        print("error")
        
#getting output in list form  
finally:  
     print(resultList)
    


    



    
    
    



    
