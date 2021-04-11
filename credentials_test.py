import unittest
from credentials import Credentials
import pyperclip


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase:Testcase class that help in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_credential = Credentials("Twitter","Cocoh Vee" ,"Swiss")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to see if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name, "Twitter")
        self.assertEqual(self.new_credential.full_name, "Cocoh Vee")
        self.assertEqual(self.new_credential.password, "Swiss")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credentials list
        '''
        self.new_credential.save_credentials()  # saving the new contact
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential objects to our credentials_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("testAccount", "testUser","testPassword")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("testAccount", "testUser","testPassword")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_get_credentials_by_account(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Instagram", "Taipei Tallin", "justIvy")
        test_credential.save_credentials()

        credential_found = Credentials.get_credential_by_account("Instagram")

        self.assertEqual(credential_found.account_name,test_credential.account_name)

    def credential_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Instagram", "Taipei Tallin", "justIvy")
        test_credential.save_credentials()

        credential_exists = Credentials.credential_exist("Instagram")

        self.assertTrue(credential_exists)

    def test_display_all_credentialss(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found credential
        '''

        self.new_credential.save_credentials()
        Credentials.copy_password("Twitter")

        self.assertEqual(self.new_credential.password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
