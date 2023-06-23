import time
import csv
from cryptography.fernet import Fernet
import pandas as pd
from termcolor import colored

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


def StoreData(userEmail, userPass, websiteURL=None, userName=None):
    # field names
    ColumnName = ['Username', 'Password', 'Email', 'Website']
    Data = [[str(userName), str(userPass), str(userEmail), str(websiteURL)]]

    # name of csv file
    filename = "passwords.csv"

    # writing to csv file in append mode
    with open(filename, 'a+', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # check if the file is empty
        csvfile.seek(0)
        first_char = csvfile.read(1)
        is_empty = not first_char

        # write the fields only if the file is empty
        if is_empty:
            csvwriter.writerow(ColumnName)

        # writing the data row
        csvwriter.writerows(Data)

    # close the file
    csvfile.close()

def encrypt(masterkey=None, already_key_generated=False):

    if already_key_generated==False:
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

def websiteStringValidator(websiteURL):
    if (websiteURL.startswith('https://www.')==True and websiteURL.endswith('.com/') == True):
        pass
    elif(websiteURL.startswith('https://www.')==True and websiteURL.endswith('.com/') == False):
        websiteURL = websiteURL + '.com'
    elif(websiteURL.startswith('https://www.') == False and websiteURL.endswith('.com/') == True):
        websiteURL = 'https://www.'+websiteURL
    else:
        websiteURL = 'https://www.'+websiteURL+'.com/'
    return websiteURL

def PasswordDataFrame():
    df = pd.read_csv('passwords.csv')
    DataFrame = pd.DataFrame(df)
    return DataFrame

def password_finder():
    df = pd.read_csv('passwords.csv')
    password_table = pd.DataFrame(df)

    searchBy = str(
        input("\nDo you want to search by username or website? (u/w): "))
    if (searchBy == 'w'):
        choiceWeb = str(input("\nEnter the website name: "))
        choiceWeb = websiteStringValidator(choiceWeb)
        PostdataFrame = password_table.loc[password_table['website'] == choiceWeb]
        if (len(PostdataFrame.index) > 1):
            print(
                f"\n{len(PostdataFrame.index)} passwords found for {choiceWeb[12:-1]}")
            choice = int(input(
                "\nYour choice : \n1.)See Table form of all usernames and password\n2.)List all usernames and print password for your choice\n3.)Exit\nYour Choice : "))
            if (choice == 1):
                print(PostdataFrame.loc[:, ['username', 'pass']])
            elif choice == 2:
                newFrame = PostdataFrame.loc[:, ['username']].copy()
                newFrame = newFrame.rename(
                    columns={'username': 'Usernames found'})
                newFrame = newFrame.reset_index(drop=True)
                username = str(input("Enter your username: "))
                password = PostdataFrame.loc[PostdataFrame['username']
                                             == username, 'pass'].values[0]
                website = PostdataFrame.loc[PostdataFrame['username']
                                            == username, 'website'].values[0]
                print(f"The password for username {username} is: {password}")
                print(f"The associated website is: {website}")
            else:
                exit()
        else:
            username = PostdataFrame.loc[PostdataFrame['website']
                                         == choiceWeb, 'username'].values[0]
            password = PostdataFrame.loc[PostdataFrame['website']
                                         == choiceWeb, 'pass'].values[0]
            print("One password found for the website\n")
            print(f"The password for username {username} is: -> ", end="")
            print(colored(password, 'red'), end="")
            print(" <-")
            print(f"The associated website is: ", end="")
            print(colored(choiceWeb, 'blue'))
    elif searchBy == 'u':
        username = str(input("\nEnter the username: "))
        matching_passwords = password_table.loc[password_table['Username'] == username]
        password_count = len(matching_passwords)
        print(f"{password_count} passwords found for {username}")
        if len(matching_passwords) == 0:
            print("No password found for the given username.")
        else:
            for index, row in matching_passwords.iterrows():
                password = row['Password']
                website = row['Website']
                
                print(f"The password for username {username} is: -> ", end="")
                print(colored(password, 'red'), end="")
                print(" <-")
                print(f"The associated website is: ", end="")
                print(colored(website, 'blue'))
                print("")
    else:
        exit()
        
        
        
        

if __name__ == "__main__":
    print("Wrong file!")
