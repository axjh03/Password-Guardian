# Importing modules
import pandas as pd
import os
import csv
from greetings import greet, options

if 'passwords.csv' not in os.listdir():
    greet(NewUser=True)
    choice = options(NewUser=True)
    if choice == '1':
        file = open('passwords.csv', 'a+')
        file.seek(0) # get to the start of the file
               