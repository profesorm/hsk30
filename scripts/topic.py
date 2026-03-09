import requests
import json

# API URL
url = "https://www.chinesetest.cn/api/hsk/outline/topicPage?current=1&size=430"

# Send POST request
response = requests.post(url)
data = response.json()  # raw API JSON

# Save directly as JSON
with open("hsk_topic_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

print("Downloaded hsk_topic_raw.json")
