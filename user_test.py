import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase:Testcase class that help in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user= User("Alvynah Wabwoba","Secho")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to see if the object is initialized properly
        '''
        self.assertEqual(self.new_user.full_name,"Alvynah Wabwoba")
        self.assertEqual(self.new_user.password,"Secho")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test User", "user")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test User", "user")
        test_user.save_user()

        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.user_list),1)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.user_list)

if __name__ == '__main__':
    unittest.main()
    
