import re

def is_strong_password(password):
        pattren=r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])[^\s]{8,}"
        ans=bool(re.fullmatch(pattren,password))
        return ans

def test_password():
    assert is_strong_password("Str0ng@Pass")
    assert not is_strong_password("weakpass")
    assert not is_strong_password("NoSpecial123")
