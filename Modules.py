import time
import csv
from cryptography.fernet import Fernet

def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
        
def fileCreationComplete():
    text = "A new file has been created for you!\nDeleting that file will delete all your passwords!\nBut it's encrypted so you don't have to worry about it!"
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
        
def blinking_cursor():
    while True:
        print('_', end='', flush=True)
        time.sleep(0.5)
        print('\b', end='', flush=True)
        time.sleep(0.5)

def greet(NewUser):
    if NewUser==False:
        from termcolor import colored
        print(colored('\n\nWhat do you want to do today?', 'green', attrs=['bold']))   
        print("")
    else:
        welcome_message1 = "Seems like you are a new user!"
        welcome_message2 = "\nLet's get you started!"
        typewriter_effect(welcome_message1)
        typewriter_effect(welcome_message2)
        

def options(NewUser):
    if NewUser:
        print("\n1. Create an account")
        print("2. Exit")
        choice = input("Enter your choice: ")
        return choice

def StoreData(userName, userEmail, userPass):
    # field names
    ColumnName = ['Name', 'Email', 'MasterPassword']
    Data = [[str(userName), str(userEmail), str(userPass)]]

    # name of csv file
    filename = "passwords.csv"

    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(ColumnName)

        # writing the data row
        csvwriter.writerows(Data)
    csvfile.close()


def encrypt():
    key = Fernet.generate_key()
    print(key)

    with open('name.csv', 'rb') as file:
        original = file.read()
    
    fernet = Fernet(key)
    
    encrypted = fernet.encrypt(data = original)

    with open('name.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        
    return key




def decrypt(key):
    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('name.csv', 'rb') as enc_file:
	    encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('name.csv', 'wb') as dec_file:
	    dec_file.write(decrypted)



if __name__ == "__main__":
    print("Wrong file!")
    
