import random
from termcolor import colored
import string
import time

#gives the user options
logins = True
user = input("What is your username? ")
database = {}
database[user] = ""#adds new user to the database 
print("*****************")
print("1 - Sign up")
print("2 - Login")
print("*****************")
option = input("\n1 or 2? ")



#generates random Password for you
if option == "1":
 def password():
    print("Making password..")
    time.sleep(2)
    fh = (''.join(random.choices(string.ascii_letters, k=5)))
    sh = (''.join(random.choices(string.ascii_letters, k=5)))
    fin = sh + fh
    database[user] = fin
    print("Finalizing..")
    time.sleep(1)
    print(f"Your new password is {fin}")
 password()


if option == "2" or logins == True:
    username, password = input("What is your username? "), input("What is your password? ")
    if username in database:
       if password == database[user]:
           print(f"Welcome back {username}!")
       else:
            print("That password is incorrect! Please try again!")
    else:
      print("We don't recognize that user please sign up!")
