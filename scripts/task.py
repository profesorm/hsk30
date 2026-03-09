import requests
import json

# API URL
url = "https://www.chinesetest.cn/api/hsk/outline/taskPage?current=1&size=680"

# Send POST request
response = requests.post(url)
data = response.json()  # raw API JSON

# Save directly as JSON
with open("hsk_task_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)  # no indent, raw save

print("Downloaded hsk_task_raw.json")
