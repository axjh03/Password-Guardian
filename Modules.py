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
    if not NewUser:
        print(colored('\n\nWhat do you want to do today?',
              'white', attrs=['bold']))
        print("")
        print(colored("1. Create a new password", 'blue'))
        print(colored("2. View your passwords", 'green'))
        print(colored("3. Delete a password", 'red'))
        print(colored("4. View table form of all saved password", 'green'))
        print(colored("5. Exit", 'yellow'))


def options(NewUser):
    if NewUser:
        print("\n1. Create an account")
        print("2. Exit")
        choice = input("Enter your choice: ")
        return choice


def StoreData(userEmail, userPass, websiteURL=None, userName=None):
    ColumnName = ['Username', 'Password', 'Email', 'Website']
    Data = [[str(userName), str(userPass), str(userEmail), str(websiteURL)]]
    filename = "passwords.csv"

    with open(filename, 'a+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvfile.seek(0)
        first_char = csvfile.read(1)
        is_empty = not first_char

        if is_empty:
            csvwriter.writerow(ColumnName)

        csvwriter.writerows(Data)

    csvfile.close()


def encrypt(masterkey=None, already_key_generated=False):
    if not already_key_generated:
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
    fernet = Fernet(key)

    with open('passwords.csv', 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('passwords.csv', 'wb') as dec_file:
        dec_file.write(decrypted)


def websiteStringValidator(websiteURL):
    if websiteURL.startswith('https://www.') and websiteURL.endswith('.com/'):
        pass
    elif websiteURL.startswith('https://www.') and not websiteURL.endswith('.com/'):
        websiteURL = websiteURL + '.com'
    elif not websiteURL.startswith('https://www.') and websiteURL.endswith('.com/'):
        websiteURL = 'https://www.' + websiteURL
    else:
        websiteURL = 'https://www.' + websiteURL + '.com/'

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

    if searchBy == 'w':
        choiceWeb = str(input("\nEnter the website name: "))
        choiceWeb = websiteStringValidator(choiceWeb)
        PostdataFrame = password_table.loc[password_table['Website'] == choiceWeb]

        if len(PostdataFrame.index) > 1:
            print(
                f"\n{len(PostdataFrame.index)} passwords found for website : {choiceWeb[12:-1]}")
            choice = int(input(
                "\nYour choice:\n1.) See Table form of all usernames and password\n2.) By specific username\n3.) Exit\nYour Choice: "))

            if choice == 1:
                print(PostdataFrame.loc[:, ['Username', 'Password', 'Email']])
            elif choice == 2:
                newFrame = PostdataFrame.loc[:, ['Username']].copy()
                newFrame = newFrame.rename(
                    columns={'Username': 'Usernames found'})
                newFrame = newFrame.reset_index(drop=True)
                username = str(input("Enter your username: "))
                password = PostdataFrame.loc[PostdataFrame['Username']
                                             == username, 'Password'].values[0]
                website = PostdataFrame.loc[PostdataFrame['Username']
                                            == username, 'Website'].values[0]
                email = PostdataFrame.loc[PostdataFrame['Username']
                                          == username, 'Email'].values[0]
                print(f"The password for username {username} is: -> ", end="")
                print(colored(password, 'red'), end="")
                print(" <-")
                print(f"The associated email is: ", end="")
                print(colored(email, 'green'))
                print(f"The associated website is: ", end="")
                print(colored(choiceWeb, 'blue'))
            else:
                exit()

        else:
            username = PostdataFrame.loc[PostdataFrame['Website']
                                         == choiceWeb, 'Username'].values[0]
            password = PostdataFrame.loc[PostdataFrame['Website']
                                         == choiceWeb, 'Password'].values[0]
            email = PostdataFrame.loc[PostdataFrame['Website']
                                      == choiceWeb, 'Email'].values[0]
            print("One password found for the website\n")
            print(f"The password for username {username} is: -> ", end="")
            print(colored(password, 'red'), end="")
            print(" <-")
            print(f"The associated email is: ", end="")
            print(colored(email, 'green'))
            print(f"The associated website is: ", end="")
            print(colored(choiceWeb, 'blue'))

    elif searchBy == 'u':
        username = str(input("\nEnter the username: "))
        matching_passwords = password_table.loc[password_table['Username'] == username]
        password_count = len(matching_passwords)
        print(f"\n{password_count} passwords found for {username}\n")

        if len(matching_passwords) == 0:
            # print("No password found for the given username.")
            pass
        else:
            for index, row in matching_passwords.iterrows():
                password = row['Password']
                website = row['Website']
                email = row['Email']

                print(f"The password for username {username} is: -> ", end="")
                print(colored(password, 'red'), end="")
                print(" <-")
                print(f"The associated email is: ", end="")
                print(colored(email, 'green'))
                print(f"The associated website is: ", end="")
                print(colored(website, 'blue'))
                print("")
    else:
        exit()


def deletePassword():
    df = pd.read_csv('passwords.csv')
    password_table = pd.DataFrame(df)

    choice = str(
        input("\nDo you want to delete by username, email, or website? (u/e/w): "))

    if choice == 'u':
        username = str(input("\nEnter the username: "))
        matching_passwords = password_table.loc[password_table['Username'] == username]
    elif choice == 'e':
        email = str(input("\nEnter the email: "))
        matching_passwords = password_table.loc[password_table['Email'] == email]
    elif choice == 'w':
        website = str(input("\nEnter the website: "))
        website = websiteStringValidator(website)
        matching_passwords = password_table.loc[password_table['Website'] == website]
    else:
        print("Invalid choice.")
        return

    if len(matching_passwords) == 0:
        print("No password found for the given input.")
        return

    if len(matching_passwords) > 1:
        print(f"\n{len(matching_passwords)} passwords found:")
        print(matching_passwords.to_string(index=False))

        # Future fix : Create a copy of dataframe and then display that with index from 1. so that original dataframe is not affected
        print(colored("Choose the number from table to delete", 'red'))
        index_choice = int(
            input("\nEnter the index of the password you want to delete: "))

        if index_choice < 0 or index_choice >= len(matching_passwords):
            print("Invalid index choice.")
            return
        index_choice = index_choice-1
        password_row = matching_passwords.iloc[index_choice]
    else:
        password_row = matching_passwords.iloc[0]
    # print(colored(password_row, 'red')))
    print(f"\nPassword to delete:\n{password_row}\n")

    confirm = str(
        input("Are you sure you want to delete this password? (y/n): "))

    if confirm.lower() == 'y':
        password_table = password_table.drop(password_row.name)
        password_table.to_csv('passwords.csv', index=False)
        print("Password deleted successfully.")
    else:
        print("\nDeletion canceled.")


if __name__ == "__main__":
    print("Wrong file!")
