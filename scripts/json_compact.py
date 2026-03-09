import json

# Input and output file
input_file = "hsk_hanzi_raw.json"
output_file = "hsk_hanzi_compact.json"

# Read raw JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Rebuild the 'records' array as one-line objects
records = data["data"]["records"]
data["data"]["records"] = [json.loads(json.dumps(rec, ensure_ascii=False)) for rec in records]

# Save JSON with standard indent, but one-line records
with open(output_file, "w", encoding="utf-8") as f:
    f.write('{\n')
    f.write(f'  "code": {data["code"]},\n')
    f.write('  "data": {\n')
    f.write('    "records": [\n')
    for i, rec in enumerate(data["data"]["records"]):
        line = json.dumps(rec, ensure_ascii=False)
        if i < len(data["data"]["records"]) - 1:
            line += ','
        f.write(f'      {line}\n')
    f.write('    ]\n')
    f.write('  }\n')
    f.write('}\n')

print(f"Saved one-line objects JSON: {output_file}")