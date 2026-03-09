import json

# List your JSON files here
files = [
    "hsk_grammar_raw.json",
    "hsk_hanzi_raw.json",
    "hsk_task_raw.json",
    "hsk_topic_raw.json",
    "hsk_vocabulary_raw.json",
]

for filename in files:
    # read the raw JSON
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # save it pretty-printed
    pretty_filename = filename.replace("_raw.json", "_pretty.json")
    with open(pretty_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved pretty JSON: {pretty_filename}")