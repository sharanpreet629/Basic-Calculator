
#checking Email validation
class Error(Exception):
    pass
class MissingValueError(Error):
    pass
class MissingDomainError(Error):
    pass
class AddressError(Error):
    pass
class passwordtooshortError(Error):
    pass

#email pattern : [alphanumeric characters]@[alphanumeric characters].[alphabet characters(domain name)]

while True:
     try:   
          email = input("Enter your Email address: ")
          listofdomains = ["com","org","co.in","net","ac.in"]
          password = input("enter your passwords: ")
          #missing @
          if "@" not in email:
              raise MissingValueError
          else:
              userdomain = email.split(".",1)[-1]
              if userdomain not in listofdomains:
                   raise MissingDomainError
          
          if len(password)<6:
              raise passwordtooshortError
         
         #cheking the charcters before @
     
          splitemail = email.split("@")
    
          if not splitemail[0].isalnum():
            raise AddressError
        
        #checking the characters before .
          emailstr = ".".join(splitemail)
          splitemail2 = emailstr.split(".")
          
          if not splitemail2[1].isalnum():
             raise AddressError
          else:
               print("your Email is VALID which is {}".format(email.lower()))
               break
         
     except MissingValueError:
           print("invalid Email Address.It must contain @")
     except MissingDomainError:
       print("You missed the domain name")
     except AddressError:
        print("Address will contain only alphabets and numbers. try again!!")
    
     except passwordtooshortError:
         print("password is too short")
        
        
        

