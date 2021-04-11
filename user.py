class User:
    """
    Class that generates new instances of users
    """
    user_list =[]; # Empty User list


    def __init__(self, full_name, password):
        self.full_name = full_name
        self.password = password
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    
    def delete_user(self):
        '''
        delete_user method to delete a user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def get_user_by_name(cls, full_name):
        """
        get_credentials_by_name method which takes in a user's full_name and returns the respective account
        
        Args:
            full_name: full name to search for
        Returns :
            respective account details
        """
        for user in cls.user_list:
            if user.full_name == full_name:
                return user

    @classmethod
    def user_exist(cls, full_name):
        '''
        Method that checks if a user exists from the users list.
        Args:
            full_name: Full name to search if user exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.full_name == full_name:
                return True

        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def log_in(cls, full_name, password):
        '''
        Method that allows a user to log into their account

        Args:
            name : name of the user
            password : password for the user

        Returns:
            User list for the user that matches the name and password
            False: if the name or password is incorrect
        '''

        # Search for the user in the user list
        for user in cls.user_list:
            if user.full_name == full_name and user.password == password:
                return User.user_list

        return False
