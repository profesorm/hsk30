import json

input_file = "hsk_hanzi_raw.json"
output_file = "hsk_hanzi_compact.json"

# Read the raw JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Prepare one-line JSON strings for each record
records = data["data"]["records"]
one_line_records = [json.dumps(rec, ensure_ascii=False) for rec in records]

# Replace 'records' temporarily with string placeholders
data["data"]["records"] = one_line_records

# Dump the whole JSON with indentation
json_text = json.dumps(data, ensure_ascii=False, indent=2)

# Remove quotes around each record to restore proper JSON objects
for rec in one_line_records:
    json_text = json_text.replace(json.dumps(rec, ensure_ascii=False), rec)

# Save the compact file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(json_text)

print(f"Saved compact one-line records JSON: {output_file}")