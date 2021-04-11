#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

# Users
def create_user(flname,password):
    '''
    Function to create a new user
    '''
    new_user= User(flname,password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def check_existing_users(full_name):
    '''
    Function that checks if a user account name already exists

    Args:
        name: the user account name
    '''
    return User.user_exist(full_name)
def user_login(full_name,password):
    '''
    Function that allows a user to log into their  account

    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(full_name, password)
    if log_in != False:
        return User.log_in(full_name, password)


# Credentials
def create_credentials(account_name,full_name,password):
    '''
    Function to create new credentials
    '''
    new_credential=Credentials(account_name,full_name,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save a credential
    '''
    credential.save_credentials()
def del_credentials(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credentials()
def find_credential(account_name):
    '''
    Function that finds a credential by account name and returns the credential
    '''
    return Credentials.get_credential_by_account(account_name)
def check_existing_credentials(account_name):
    '''
    Function that check if a credential exists with that account name and return a Boolean
    '''
    return Credentials.credential_exist(account_name)
def display_credentials:
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()
def copy_password:
    '''
    Function that copies the password to the clipboard
    '''
    return Credentials.copy_password()
def generate_password:
    '''
    Function that generates arandom password for credentials.
    '''
    random_password = Credentials.generate_password()
    return random_password
def main():
    print("Hello, Welcome to Password Locker. An app that helps you store and manage your passwords")
    print('\n')
    print("What's your full name")
    full_name =input()
    print('\n')
    print(f"Olaa {full_name}. Type in the action you would like to perform ")
    print('\n')

    while True:
        print('''Use these short codes interact with Password Locker :
        1.cu - create a new user account \n
        2.du - display user accounts \n
        3.lu -log into your existing account \n
        4.ex-exit application ''')

        short_code=input().lower()

        if short_code == 'cu':
            '''
            create a new password locker account
            '''
            print("Create a new account")
            print("*" *50)

            print("Enter Full Name")
            full_name=input()

            print("Enter Password")
            password=input()

            save_user(create_user(full_name,password))

            print('\n')
            print(f" Welcome {full_name}.Enjoy your experience with Password Locker")
            print('\n')
            print('\n')
        elif short_code == 'du':
            '''
            Display the user accounts
            '''
            if display_users():
                print('\n')
                print(f"{user.full_name}")
                print("*"*50)

            else:
                print('\n')
                print('There is no existing user in Password Locker')
                print('\n')

        elif short_code == "lg":
            '''
            Log in the user into their account
            '''
            print('\n')
            print("Log into your account")

            print("Enter the full name")
            full_name=input()

            print("Enter the password"
            password= input()

            if user_login(full_name,password) == None:
                  print('\n')
                  print("Please check your credentials(especially the case) or create a new account")
                  print('\n')
            else:
                user_login(full_name,password)
                print('\n')
                print(f'''{full_name}\n
                Welcome to creating credentials\n
                Use these short codes to get around
                ''')
                while True:
                    print('''Use these short codes to :
                    1.cc - add a credential\n
                    2.dc - display credentials \n
                    3.fc - find a credential \n
                    4.del - Delete credential \n
                    5.ex - exit credentials
                     ''')

                    short_code=input().lower()
                    #Create credentials
                    if short_code == 'cc':
                        '''
                        Creating a credentials
                        '''

                        print('\n')
                        print("new Credentials")
                        print("*" *50)
                        print("Enter account name")
                        account_name=input().lower()
                        print("Enter your account username")
                        full_name=input().lower()
                        while True:
                            print(''' Type:
                            cp -to type your own customized password \n
                            gp- get generated password
                            ''')
                            choice=input().lower()
                            if choice == 'cp':
                                password=input("Enter Your Own Password \n")
                                break
                            
                            elif choice == 'gp':
                                password=generate_password()
                                break
                            else:
                                print("Kindly choose a password option using availed short codes")
                        save_credentials(create_credentials(account_name,full_name,password))
                        print(f"\n Credentials for {account_name} account Username: {full_name} is created successfully \n")
                   
                    #Displaying credentials
                    elif short_code == 'dc':
                        if display_credentials():
                            print("Below is a list of account credentials you have : ")
                            print("*"*30)
                            print("_"*30)
                            for credential in display_credentials():
                                print(f''' Account name: {credential.account_name} \n 
                                User Name:{full_name}\n 
                                Password:{password}
                                ''')
                                print('_' * 30)")
                            print("*"*30)
                        else:
                            print("There are no existing account credentials, Kindly create new ones")
                    #Finding credentials
                    elif short_code == "fc":
                        print("Enter the Account Name for credential you are looking for")
                        account_name = input().lower()
                        if find_credential(account_name):
                            search_credential = find_credential(account_name)
                            print(f"Account Name : {search_credential.account_name}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.full_name} \n  Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("This account does not exist")
                            print('\n')
                    #Deleting Credential account
                    elif short_code == "del":
                        print("Enter the account name of the account credentials you want to delete")
                        account_name = input().lower()
                        if find_credential(account_name):
                            search_credential = find_credential(account_name)
                            print("_"*50)
                            search_credential.del_credentials()
                            print('\n')
                            print(f"Your account credentials for : {search_credential.account_name} {search-credentials.full_name}  is successfully deleted!!!")
                            print('\n')
                        else:
                            print("This account credentials does not exist in your store yet")
                    
                    elif short_code == 'ex':
                        print(f"Thanks for interacting with credentials {full_name}. See you soon")
                        print('\n')
                        break
                    else:
                        print('\n')
                        print("Invalid short_code entered, choose one of the below")
                        print('\n')

        elif short_code == 'ex':
            print('\n')
            print("Bye ......")
            break
        else:
            print("\n")
            print(f"Thank you for using Password Locker. Interact with app again using the short code")
            print("\n")   
if __name__ == '__main__':
    main()               





                    








     break
                    else:
                            print("I really didn't get that. Please use the short codes") 





