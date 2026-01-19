import csv

INPUT_FILE = r"D:\Metering_data\smart_meter_data_GMR\Agra_Event Profile_Nov\Agra_event_profile_Oct_01_31.csv"
DEVICE_ID_COL = "deviceId"

def count_unique_device_ids(input_file):

    print("\n📂 Reading large CSV file…")

    unique_ids = set()

    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        if DEVICE_ID_COL not in reader.fieldnames:
            raise Exception(f"Column '{DEVICE_ID_COL}' not found!")

        for idx, row in enumerate(reader):
            unique_ids.add(row[DEVICE_ID_COL])

            # progress update every 1 million rows
            if idx % 1_000_000 == 0 and idx > 0:
                print(f"Processed {idx:,} rows…")

    print("\n---------------------------------------")
    print(f"✔ Total DISTINCT deviceId count = {len(unique_ids):,}")
    print("---------------------------------------")

count_unique_device_ids(INPUT_FILE)
