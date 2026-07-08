import re

def extract_tags(element):
    ans=re.findall(r"<([a-z]+)>",element)
    return ans

def test_tags():
    html = "<div><p>Hello</p></div>"
    assert extract_tags(html) == ["div", "p"]
