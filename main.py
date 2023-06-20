# Importing modules
import pandas as pd
import os
import csv
from greetings import greet, options, fileCreationComplete

if 'passwords.csv' not in os.listdir():
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