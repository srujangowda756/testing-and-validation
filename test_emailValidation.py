import re

def is_valid_email(mail):
    pattern= r'^[\w+]+(?:\.[\w+]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,6}$'
    return bool(re.fullmatch(pattern,mail))

def test_email_valid():
    assert is_valid_email("user.name+1@gmail.com")
    assert is_valid_email("test_user@domain.co.in")
def test_email_invalid():
    assert not is_valid_email("user..name@gmail.com")
    assert not is_valid_email("user@domain")
    assert not is_valid_email("@domain.com")