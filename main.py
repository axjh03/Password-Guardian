# Importing modules
import pandas as pd
import os
import csv
from Modules import greet, options, fileCreationComplete, StoreData, encrypt, decrypt, typewriter_effect

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
        key = encrypt()
        f = open("MasterPassword.txt", "x")
        key = key.decode('utf-8')
        f.write(str(key))
        
        typewriter_effect("For your security, we have encrypted your password.\nBut the file containing your password is not encrypted.\nFor your ease we extracted the key and stored it in a text file. named 'MasterPassword.txt'\nPlease keep it safe.\n")

        print(f"Your key is \n\n{key}\n\nWe are trying to make a feature of using user's password as masterpassword.\nBut for now, we are using a random key.\n")
        

else:
    ## Greet before asking for master key [feature]
    try:
        key_input = input("Enter your master key: ")
        key = key_input.encode('utf-8')
        decrypt(key_input)
        
    except SystemExit:
        print("Wrong Password\nTryAgain\n")
        typewriter_effect("Exiting..............")
        exit()
   
    
    # encrypt(masterkey=str(key_input), already_encrypted=True) 
    