import re

def parse_logs(info):
    match = re.match(r"([A-Z]+)\s+(\d{4}-\d{2}-\d{2})\s+(.+)", info)
    return [{
        "level": match.group(1),
        "date": match.group(2),
        "message": match.group(3)
    }]

def test_logs():
    logs = "INFO 2024-01-01 User logged in"
    result = parse_logs(logs)
    assert result[0]["level"] == "INFO"
