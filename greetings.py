import time

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
        
            
if __name__ == "__main__":
    print("Wrong file Daddy!")