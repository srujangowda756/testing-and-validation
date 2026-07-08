import re

def extract_indian_numbers(string):
    ans=re.findall(r"[6-9][0-9]{9}|\+91-[6-9][0-9]{9}|91 [6-9][0-9]{9}",string)
    return ans

def test_indian_numbers():
    text = "Call +91-9876543210 or 9123456789 or 1234567890"
    assert extract_indian_numbers(text) == ["+91-9876543210", "9123456789"]
