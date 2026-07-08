import re

def extract_dates(dateString):
    dates = re.findall(r"\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}", dateString)

    def func(date):
        if "/" in date:
            day, month, year = date.split("/")
            return f"{year}-{month}-{day}"
        return date

    return list(map(func, dates))

def test_dates():
    text = "Dates: 12/05/2023 and 2024-01-15"
    assert extract_dates(text) == ["2023-05-12", "2024-01-15"]