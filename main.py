# Importing modules
import pandas as pd
import os
import csv
from Modules import greet, options, fileCreationComplete, StoreData, encrypt, decrypt, typewriter_effect, websiteStringValidator, PasswordDataFrame, password_finder

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
        
        # userPass = str(input("Enter your master password: "))
        # userPass = userPass.encode('utf-8')
        key = encrypt(already_key_generated=False)
        f = open("MasterPassword.txt", "x")
        key = key.decode('utf-8')
        f.write(str(key))
        
        typewriter_effect("For your security, we have encrypted your password.\nBut the file containing your password is not encrypted.\nFor your ease we extracted the key and stored it in a text file. named 'MasterPassword.txt'\nPlease keep it safe.\n")

        print(f"Your key is \n\n{key}\n\nWe are trying to make a feature of using user's password as masterpassword.\nBut for now, we are using a random key.\n")
        

else:
    ## Greet before asking for master key [feature]
    key_input = input("Enter your master key: ")
    key = key_input.encode('utf-8')
    try:
        decrypt(key_input)
        
    except ValueError:
        print("Wrong Password\nTryAgain\n")
        typewriter_effect("Exiting..............")
        exit()
    
    greet(NewUser=False)
    
    
    userChoice = int(input("Enter your choice: "))
    while userChoice != 5:
        if userChoice not in [1, 2, 3, 4, 5]:
            print("Try again!")
        else:
            if userChoice == 5:
                break
            
            
            
            elif userChoice == 4:
                print(f"\n\n{PasswordDataFrame()}\n\n")
                
                
                
            elif userChoice == 2:
                password_finder()
            
            
            
            elif userChoice == 1:
                userName = input("Enter your username for the account: ")
                userPassword = input("Enter the password for the account: ")
                choice = input("Do you want to enter the website URL? (y/n): ")
                if choice == 'y':
                    websiteURL = input("Enter the website URL: ")
                    websiteURL = websiteStringValidator(websiteURL)
                else:
                    websiteURL = None
            
                choice = input("Do you want to enter the email? (y/n): ")
                if choice == 'y':
                    userEmail = input("Enter the email: ")
                else:
                    userEmail = None
                
                StoreData(userEmail, userPassword, websiteURL, userName)
                typewriter_effect("Your data has been stored successfully!")
        print("")
        greet(NewUser=False)
        userChoice = int(input("\nEnter your choice: "))

    encrypt(masterkey=str(key_input), already_key_generated=True) 
    typewriter_effect("Exiting..............")
    