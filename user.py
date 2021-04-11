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
   