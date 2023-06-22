import pandas as pd

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

def password_finder():
    df = pd.read_csv('pass.csv')
    password_table = pd.DataFrame(df)
    
    searchBy = str(input("Do you want to search by username or website? (u/w): "))
    if (searchBy=='w'):
        choiceWeb = str(input("Enter your website name: "))
        choiceWeb = websiteStringValidator(choiceWeb)
        PostdataFrame = password_table.loc[password_table['website'] == choiceWeb]
        if (len(PostdataFrame.index)>1):
            print(f"Total of {len(PostdataFrame.index)} passwords found for {choiceWeb[12:-1]}")
            choice = int(input("Your choice : \n1.) See Table form of all usernames and password\n2.)List all usernames and print password for your choice\n3.)Exit\nYour Choice : "))
            if (choice == 1 ):
                print(PostdataFrame.loc[:,['username','pass']])
            elif choice == 2:
                newFrame = PostdataFrame.loc[:, ['username']].copy()
                newFrame = newFrame.rename(columns={'username': 'Usernames found'})
                newFrame = newFrame.reset_index(drop=True)
                
                userName_userInput = int(input("Enter your username: "))
                print("")
                print(f"The password for username {newFrame.iloc[choice].to_string(index=False, header=False)} is /n/n/t{PostdataFrame.loc[PostdataFrame['username'] == userName_userInput, 'pass'].values[0]}/n/n")
                
                


# def password_finder():
    # df = pd.read_csv('pass.csv')
    # password_table = pd.DataFrame(df)
    # searchBy = input("Do you want to search by username or website? (u/w): ")
    # if searchBy == 'w':
    #     choiceWeb = input("Enter your website name: ")
    #     PostdataFrame = df.loc[df['website'] == choiceWeb]
    #     if len(PostdataFrame.index) > 1:
    #         print(f"Total of {len(PostdataFrame.index)} passwords found for {choiceWeb}")
    #         choice = int(input("Your choice:\n1.) See Table form of all usernames and passwords\n2.) List all usernames and print password for your choice\n3.) Exit\nYour Choice: "))
    #         if choice == 1:
    #             print(PostdataFrame.loc[:, ['username', 'pass']])
    #         elif choice == 2:
    #             newFrame = PostdataFrame.loc[:, ['username']].copy()
    #             newFrame = newFrame.rename(columns={'username': 'Usernames found'})
    #             newFrame = newFrame.reset_index(drop=True)
                
    #             userName_userInput = input("Enter your username: ")
    #             print(f"The password for username {userName_userInput} is:\n\t{PostdataFrame.loc[PostdataFrame['username'] == userName_userInput, 'pass'].values[0]}\n")
      

password_finder()
# print(newFrame.iloc[1].to_string(index=False, header=False))