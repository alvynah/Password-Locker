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
def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()
def copy_password():
    '''
    Function that copies the password to the clipboard
    '''
    return Credentials.copy_password()
def generate_password():
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
    print("*" * 70)
    print(f"Olaa {full_name}. Type in the action you would like to perform ")
    print("*" *70)

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

            print("Enter Full Name :")
            fname=input()

            print("Enter Password :")
            passwordUser=input()

            save_user(create_user(fname,passwordUser))

            print('\n')
            print("*" * 80)
            print(f"Welcome {fname}.Enjoy your experience with Password Locker!")
            print("Log in by typing lu to get started")
            print("_" * 80)
            print('\n')
        elif short_code == 'du':
            '''
            Display the user accounts
            '''
            if display_users():
                print('\n')
                print("Below is the list of users}")
                print("*"*50)

                for user in display_users():

                    print(f"Username: {user.full_name} --> password: {user.password}")
                    print("-"*50)
                    print('\n')
            else:
                print('\n')
                print('There is no existing user in Password Locker')
                print('\n')

        elif short_code == "lu":
            '''
            Log in the user into their account
            '''
            print("Log into your account")
            print("_" * 50)

            print("Enter the full name :")
            fname=input()

            print("Enter the password :")
            passwordUser= input()

            if user_login(fname,passwordUser) == None:
                  print('\n')
                  print("Please check your credentials(especially the case) or create a new account")
                  print('\n')
            else:
                user_login(fname,passwordUser)
                print('\n')
                print("*" * 100)
                print("-" * 100)
                print(f'''
                Welcome to creating credentials {fname}
                Use these short codes to get around
                ''')
                print("*" *50)
                print("_" *50)
                print('\n')

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
                        account=input().lower()
                        print("Enter your account username")
                        flname=input().lower()
                        print("Enter password")
                        while True:
                            print(''' 
                            Type short code :
                            cp -to type your own customized password
                            gp- get generated password
                            ''')
                            choice=input().lower()
                            if choice == 'cp':
                                passwordCred=input("Enter Your Own Password \n")
                                break
                            
                            elif choice == 'gp':
                                passwordCred=generate_password()
                                print("_" * 70)
                                print('\n')
                                print(f"password for acount username: {flname} is {passwordCred}")
                                print("*" * 70)                
                                break
                            else:
                                print("Kindly type a valid password option using availed short codes")
                        save_credentials(create_credentials(account,flname,passwordCred))
                        print(f"\nCredentials for {account}, account username: {flname} is created successfully \n")
                        print("_" * 90)

                   
                    #Displaying credentials
                    elif short_code == 'dc':
                        if display_credentials():
                            print("Below is a list of account credentials you have : ")
                            
                            for credential in display_credentials():
                                print("*"*30)
                                print("_"*30)
                                print(f"\nAccount name: {credential.account_name} \nUser Name:{credential.full_name}\nPassword:{credential.password}")
                                print('_' * 30)
                                print('*'*30)
                        else:
                            print("\nThere are no existing account credentials, Kindly create new ones\n")
                    #Finding credentials
                    elif short_code == "fc":
                        print("Enter the Account Name for credential you are looking for : ")
                        account_name = input().lower()
                        if find_credential(account_name):
                            search_credential = find_credential(account_name)
                            print(f"\n Account Name : {search_credential.account_name}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.full_name} \nPassword :{search_credential.password}")
                            print('-' * 50)
                            print('\n')
                        else:
                            print("\nSorry, This account does not exist. Enter correct account name")
                            print('\n')
                    #Deleting Credential account
                    elif short_code == "del":
                        print("Enter the account name to delete :")

                        account_name = input().lower()
                        if find_credential(account_name):
                            search_credential = find_credential(account_name)
                            print("_"*40)
                            search_credential.delete_credentials()
                            print('\n')
                            print("*"*80)
                            print(f"Your account credentials for : {search_credential.account_name} {search_credential.full_name}  is successfully deleted!!!")
                            print('\n')
                            print("*"*80)
                            print("_"*80)

                        else:
                            print('\n')
                            print("_"*80)
                            print("Sorry,this account credentials does not exist in your store yet\n")
                            print("_"*80)
                            print('\n')

                    
                    elif short_code == 'ex':
                        print("*"*80)
                        print("_"*80)

                        print(f"Thanks for interacting with credentials {full_name}. See you again soon")
                        print("*"*80)
                        print("_"*80)

                        print('\n')
                        break
                    else:
                        print('\n')
                        print("Invalid short_code entered, choose one of the below")
                        print('\n')

        elif short_code == 'ex':
            print('\n')
            print("Bye.Thanks for using Password Locker......")
            break
        else:
            print("\n")
            print(f"Invalid command.Type in the correct short code to interact more")
            print("\n")  

if __name__ == '__main__':
    main()               







