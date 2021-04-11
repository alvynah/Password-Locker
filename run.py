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
def create_credentials(account,flname,password):
    '''
    Function to create new credentials
    '''
    new_credential=Credentials(account,flname,password)
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
        print('''Use these short codes :
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
                    print('''Use these short codes :
                    1.cc - add a credential\n
                    2.dc - display credentials \n
                    3.fc - find a credential \n
                    4.del - Delete credential \n
                    5.ex - exit credentials
                     ''')

                    short_code=input().lower()
                    if short_code == 'cc':
                        '''
                        Creating a credentials
                        '''

                        print('\n')
                        print("new Credentials")
                        print("*" *50)







     break
                    else:
                            print("I really didn't get that. Please use the short codes") 





