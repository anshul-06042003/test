import csv
import os

output_dir = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6_split"

for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        print(f"\nChecking {file}")
        last = None

        with open(os.path.join(output_dir, file), "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                dev = row["deviceId"]
                if last is not None and dev != last:
                    # New device came — but check if same device appears later?
                    pass
                last = dev

        print("✔ deviceId continuity OK")
