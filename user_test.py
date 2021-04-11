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
    def test_init(self):
        '''
        test_init test case to see if the object is initialized properly
        '''
        self.assertEqual(self.new_user.full_name,"Alvynah Wabwoba")
        self.assertEqual(self.new_user.password,"Secho")

if __name__ == '__main__':
    unittest.main()
    