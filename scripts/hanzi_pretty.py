import requests
import json

url = "https://www.chinesetest.cn/api/hsk/outline/hanziPage?current=1&size=5000"

response = requests.post(url)
data = response.json()  # raw API JSON

# save pretty-printed JSON
with open("hsk_hanzi_pretty.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # indent=2 makes it readable

print("Downloaded hsk_hanzi_pretty.json (human-readable)")

