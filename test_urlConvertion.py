import re

def extract_urls(text: str) -> list:
    urls = re.findall(r"(?:https?://|www\.)\S+", text)
    return [url.rstrip(".,!?") for url in urls]

def test_urls():
    text = "Visit https://google.com, www.example.org!"
    assert extract_urls(text) == ["https://google.com", "www.example.org"]

text = "Visit https://google.com, www.example.org!"
print(extract_urls(text))