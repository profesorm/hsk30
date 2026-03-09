import requests

url = "https://www.chinesetest.cn/api/hsk/outline/hanziPage?current=1&size=4290"

response = requests.post(url)

with open("hsk_hanzi_raw.json", "wb") as f:
    f.write(response.content)

print("Downloaded raw JSON")