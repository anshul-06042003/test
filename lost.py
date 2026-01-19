import pandas as pd
import os

input_file = r"D:\Metering_data\Load_Survey November month (2).xlsx"#"D:\split\billing_load_gmr_data.csv"
output_dir = r"D:\Metering_data\excel_split_books"#"D:\split\billing_load_gmr_data_GMR_split"

orig_count = sum(1 for _ in open(input_file, "r", encoding="utf-8")) - 1

split_count = 0
for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        split_count += sum(1 for _ in open(os.path.join(output_dir, file), "r", encoding="utf-8")) - 1

print("Original rows:", orig_count)
print("Split rows:", split_count)

if orig_count == split_count:
    print("✔ PASS — No row lost or duplicated!")
else:
    print("❌ ERROR — Row mismatch detected!")
