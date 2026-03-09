import json

files = [
    "hsk_grammar_raw.json",
    "hsk_hanzi_raw.json",
    "hsk_task_raw.json",
    "hsk_topic_raw.json",
    "hsk_vocabulary_raw.json",
]

for input_file in files:

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data["data"]["records"]

    output_file = input_file.replace("_raw.json", "_compact.json")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write('{\n')
        f.write(f'  "code": {data["code"]},\n')
        f.write('  "data": {\n')
        f.write('    "records": [\n')

        for i, rec in enumerate(records):
            line = json.dumps(rec, ensure_ascii=False)
            if i < len(records) - 1:
                line += ","
            f.write(f"      {line}\n")

        f.write('    ]\n')
        f.write('  }\n')
        f.write('}\n')

    print("written:", output_file)