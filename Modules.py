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
    if NewUser == False:
        from termcolor import colored
        print(colored('\n\nWhat do you want to do today?',
              'white', attrs=['bold']))
        print("")
        print(colored("1. Create a new password", 'blue'))
        print(colored("2. View your passwords", 'green'))
        print(colored("3. Delete a password", 'red'))
        print(colored("4. View table form of all saved password", 'green'))
        print(colored("5. Exit", 'yellow'))
        
        
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


def encrypt(masterkey, already_encrypted=False):

    if already_encrypted==False:
        key = Fernet.generate_key()
    else:
        key = masterkey.encode('utf-8')

    with open('passwords.csv', 'rb') as file:
        original = file.read()

    fernet = Fernet(key)

    encrypted = fernet.encrypt(data=original)

    with open('passwords.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return key


def decrypt(key):
    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('passwords.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)

    # Write the decrypted data to a new file
    with open('passwords.csv', 'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == "__main__":
    print("Wrong file!")
