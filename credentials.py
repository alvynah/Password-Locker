import pyperclip
import random
import string


class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    def __init__(self, account_name, full_name, password):
        """
        method that initializes user credentials to be stored
        """
        self.account_name = account_name
        self.full_name = full_name
        self.password = password

    def save_credentials(self):
        """
        save_credentials method saves credentials objects into user_list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method to delete credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def get_credential_by_account(cls, account_name):
        """
        get_credentials method which takes in an account_name and returns credentials with that account-name.
        
        Args:
            account_name: Account name to search for
        Returns :
            credentials of account that matches the account name.
        """
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            account_name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_password(cls, account_name):
        credential_found = Credentials.get_credential_by_account(account_name)
        pyperclip.copy(credential_found.password)

    def generate_password(stringLength=12):
        """
        Generate a random password made of letters ,symbols and numbers
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength)) 
