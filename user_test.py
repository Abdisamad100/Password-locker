import unittest # Importing the unittest module
from user import User #importing user class




class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User('Abdi', '123456')
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Abdi")
        self.assertEqual(self.new_user.password,"123456")
    
    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []  


if __name__ == '__main__':
    unittest.main()        
