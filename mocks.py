import unittest
from unittest.mock import patch, Mock
import requests

#function under test
def get_user_data(user_id):
    #sends an api request to an endpoint to grab user data
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

class TestGetUserData(unittest.TestCase):
    #'patch' replaces 'requests.get' with a mock during the test
    mock_response = Mock()
    
    #Define what .json() should return when called on the mock response
    response_dict = {'name': 'John Doe', 'email': 'john.doe@example.com'}
