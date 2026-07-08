import re

def mask_card(cardNo):
    return "*"*(len(cardNo)-4)+cardNo[-4:]

def test_mask_card():
    assert mask_card("1234567812345678") == "************5678"
