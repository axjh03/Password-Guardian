# Importing modules
import pandas as pd
import os
import csv
from Modules import greet, options, fileCreationComplete, StoreData

if 'passwords.csv' not in os.listdir(): # if there is new user.
    greet(NewUser=True)
    choice = options(NewUser=True)
    while choice not in ['1', '2']:
        print("Invalid choice!")
        print("Please enter a valid choice!")
        choice = options(NewUser=True)
        
    if choice == '1':
        file = open('passwords.csv', 'a+')
        file.seek(0) # get to the start of the file
        fileCreationComplete()
        
        
        userName = str(input("\nEnter your name: "))
        userEmail = str(input("Enter your email: "))
        userPass = str(input("Enter your password: "))
        userPass = userPass.encode('utf-8')
        
        StoreData(userName, userEmail, key)
        print(key)
else:
    pass 