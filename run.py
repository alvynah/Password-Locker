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


