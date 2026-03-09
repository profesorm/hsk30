import json

files = [
    "hsk_grammar_raw.json",
    "hsk_hanzi_raw.json",
    "hsk_task_raw.json",
    "hsk_topic_raw.json",
    "hsk_vocabulary_raw.json",
]

for input_file in files:
    # Read raw JSON
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Build one-line JSON strings for each record
    records = data["data"]["records"]
    one_line_records = [json.dumps(rec, ensure_ascii=False) for rec in records]

    # Replace only the 'records' array in the data dict
    data["data"]["records"] = one_line_records  # temporarily store strings

    # Convert the whole data back to JSON string, but keep records as one line
    json_text = json.dumps(data, ensure_ascii=False, indent=2)

    # Fix records array formatting: remove quotes around each record
    for rec in one_line_records:
        json_text = json_text.replace(json.dumps(rec, ensure_ascii=False), rec)

    # Save compact file
    output_file = input_file.replace("_raw.json", "_compact.json")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(json_text)

    print("written:", output_file)