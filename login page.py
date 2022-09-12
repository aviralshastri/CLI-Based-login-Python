import smtplib
import random

def otpgenrator(x):
    otp=''.join([str(random.randint(0,9))for i in range (0,4)])
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your gmail address with "@gmail.com"','your gmail app password')
    server.sendmail('your gmail address without "@gmail.com"',x,otp)
    
  # To create gmail app password just turn on two step verification. 
  # Then go to security you will find app password option create one and choose others in select app & name it.
  # Paste the password that you created.
  # Also paste the gmail id you used to create this password.
  # Lastly paste app password and gmail id in the respective fields above.

    return otp

def login():
     l=input("username:")
     m=input("password:")
     elementn = l+':'+m+'\n'
     element = l+':'+m
     file = open("idpassword.txt", "r+")
     y = file.readlines()
     g=0
     while True:
         if elementn in y:
             print("Username and password checked")
             otp = otpgenrator(l)
             while True:
                 k = str(input("otp: "))
                 if k == otp:
                     print("Login succesfull!!")
                     break
                 elif k !=otp:
                     print("Wrong otp")
                     print("Re-enter the otp")
             break
         elif element in y:
             print("Username and password checked")
             otp = otpgenrator(l)
             while True:
                 k = str(input("otp: "))
                 if k == otp:
                     print("Login succesfull!!")
                     break
                 else:
                     print("Wrong otp")
                     print("Re-enter the otp")
             break

         else:
             g=g+1
             print("invalid username or password")
             break
     file.close()
     return l

q=input("Do you have your account registered (yes/no): ")
q=q.lower()

if q=='yes':
    login()

elif q=='no':
    while True:
        p=input("Wanna create the account (yes/no): ")
        p=p.lower()
        if p == 'yes':
            l = input("Enter your gmail: ")
            n = input("Create password: ")
            file = open("idpassword.txt", 'r+')
            p = l + ":" + n + "\n"
            if p in file:
                print("This account is already registered")
            else:
                file.writelines(p)
                file.close()
                print("(: Account created successfully. Now you can Login to the account :)")
            login()
            break
        elif p == 'no':
            login()
            break
        else:
            print("Invalid input")
