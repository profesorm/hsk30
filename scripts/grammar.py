import requests
import json

# API URL
url = "https://www.chinesetest.cn/api/hsk/outline/languagePage?current=1&size=600"

# Send POST request
response = requests.post(url)
data = response.json()  # raw API JSON

# Save directly as JSON
with open("hsk_grammar_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

print("Downloaded hsk_grammar_raw.json")
