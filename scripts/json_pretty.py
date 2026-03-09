import json

# read the existing JSON file
with open("hsk_hanzi_raw.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # load it into a Python object

# write it back with indentation
with open("hsk_hanzi_pretty.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # indent=2 makes it readable

print("Saved hsk_hanzi_pretty.json (human-readable)")