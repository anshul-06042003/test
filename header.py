import csv
import os

input_file = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6.csv"
output_dir = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6_split"
# Read header from original
with open(input_file, "r", encoding="utf-8") as f:
    orig_header = next(csv.reader(f))

print("Original Header Columns:", orig_header)

# Check all output files
for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        with open(os.path.join(output_dir, file), "r", encoding="utf-8") as f:
            out_header = next(csv.reader(f))

        if orig_header == out_header:
            print(f"✔ {file}: Header matches")
        else:
            print(f"❌ {file}: HEADER MISMATCH")
            print(out_header)
