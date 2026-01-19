import csv
import os
import re

output_dir = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6_split"

sci_pattern = re.compile(r"^\d+\.\d+e\+\d+$", re.IGNORECASE)

found = False

for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        with open(os.path.join(output_dir, file), "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            
            for row in reader:
                for value in row:
                    if sci_pattern.match(value.strip()):
                        print("❌ Found scientific notation:", value, "in file:", file)
                        found = True

if not found:
    print("✔ PASS — No scientific notation conversion found.")
