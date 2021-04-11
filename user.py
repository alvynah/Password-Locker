class User:
    """
    Class that generates new instances of users
    """
    User_List =[]; # Empty User list
    def __init__(self, full_name, password):
        self.full_name=full_name
        self.password=password
