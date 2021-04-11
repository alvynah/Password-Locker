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
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def get_credential(cls, account):
        """
        get_credentials method which takes in a account_name and returns credentials with that account-name.

        """
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    
