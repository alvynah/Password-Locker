class User:
    """
    Class that generates new instances of users
    """
    user_list =[]; # Empty User list

    def save_user(self):
        '''
        save_user method saves contact objects into user_list
        '''
        User.user_list.append(self)
    def __init__(self, full_name, password):
        self.full_name=full_name
        self.password=password
    def delete_user(self):
        '''
        delete_user method to delete a user from the user_list
        '''
        User.user_list.remove(self)
