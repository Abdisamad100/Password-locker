from user import User
import random #import random variable generator
import string  #import string constants
import pyperclip


class Credentials:
    '''
    Class to create  account credentials, generate new passwords and save user information
    '''
    
    credential_list = []
    
    def __init__(self,user_name,account_name,password):
        '''
        Method to define the properties for each user object.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password
    
    
    def save_credentials(self):
        '''
        A method that saves new user object
        '''
        Credentials.credential_list.append(self)    
        
    def delete_credentials(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)        
        
    @classmethod
    def check_user(cls,user_name,password):
        '''
        Method that checks if the name and password entered exist in the users_list
        '''
        current_user = ''
        for user in User.user_list:
        	if (user.user_name == user_name and user.password == password):
        		current_user = user.user_name
        return current_user

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.
        Args:
            account_name: Phone account_name to search for
        Returns :
            Credential of person that matches the account_name.
        '''

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account_name:  account_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False


    @classmethod
    def display_credentials(cls):
        '''
        Method to display the list of credentials saved.
        '''
        return cls.credential_list

    @classmethod
    def copy_credentials(cls, account_name):
        credential_found = Credentials.find_by_account_name(account_name)
        pyperclip.copy(credential_found.account_name)
