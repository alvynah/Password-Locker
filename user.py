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
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
