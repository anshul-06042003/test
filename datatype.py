import csv
import os
import random

input_file = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6.csv"
output_dir = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6_split"

# Load ALL rows from original (small sample version)
with open(input_file, "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))

header = reader[0]
orig_rows = reader[1:]

# Pick random 100 rows
samples = random.sample(orig_rows, 100)

def find_row_in_output(sample_row):
    for file in os.listdir(output_dir):
        if file.endswith(".csv"):
            with open(os.path.join(output_dir, file), "r", encoding="utf-8") as f:
                for row in csv.reader(f):
                    if row == sample_row:
                        return True
    return False


errors = 0
for row in samples:
    if not find_row_in_output(row):
        print("❌ Row mismatch:", row)
        errors += 1

if errors == 0:
    print("\n✔ PASS — No data corruption or datatype change found!")
else:
    print("\n❌ Some rows are altered!")
