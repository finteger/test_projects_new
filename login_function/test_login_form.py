import pytest
from login_form import LoginForm

#a fresh form for each test
@pytest.fixture
def form():
    return LoginForm()

#setup the paramtrized test data for the email validation
@pytest.mark.parametrize("email", [
    "user@example.com",
    "23425Sharo@example.com",
    "user@crypto.co",
    "user@domain.ai",
    "user@test.org",
    "john.doe@example.com",
    "jane_doe12@example.com",
    "first.last@company.io",
    "user123@sub.domain.com",
    "alpha.beta@education.edu",
    "test-user@service.net",
    "user_tag@gmail.com",
    "simple@example.co.uk",
    "customer.support@example.com",
    "dev_team@startup.tech"
])

#positive test case
def test_valid_email(form, email):
    assert LoginForm.validate_email(form, email) is True
    
    
    
@pytest.mark.parametrize("invalid_email", [
    "asjfjsalkfjkasjf.com",
    "#################",
    "-__-_-",
    "233-45"
])
    
  
#negative test case    
def test_invalid_email(form, invalid_email):
    assert LoginForm.validate_email(form, invalid_email) is  False
    
    
    
#setup the tests for password validation
@pytest.mark.parametrize("password", [
    "Password123",
    "SecurePass456",
    "MyStrongPass789",
    "ValidPass1",
    "AnotherPass2",
    "UpperCase3"
])

#test the validation

def test_valid_password(form, password):
    assert LoginForm.validate_password(form, password) is True
    

