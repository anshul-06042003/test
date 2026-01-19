import os
import csv

INPUT_FILE = r"D:\split\billing_load_profile_data_AGRA_066 (3)-1 3.csv"
DEVICE_ID_COL = "METER_NUMBER"                           # "METER_NUMBER"      # "deviceId"
CHUNK_SIZE_MB = 100

TARGET_BYTES = CHUNK_SIZE_MB * 1024 * 1024


def split_fast_csv(input_file):

    print(f"\n📂 Reading file: {input_file}")

    # Extract base file name WITHOUT extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # ADD _GMR in output folder & filenames
    base_name_gmr = f"{base_name}_GMR"

    # Create output folder using file name + _GMR_split
    output_dir = os.path.join(os.path.dirname(input_file), f"{base_name_gmr}_split")
    os.makedirs(output_dir, exist_ok=True)

    print(f"📁 Output folder created: {output_dir}")

    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        headers = reader.fieldnames

        if DEVICE_ID_COL not in headers:
            raise Exception(f"Column {DEVICE_ID_COL} not found!")

        part = 1
        current_size = 0
        last_device = None

        # Output file name format
        out_file = os.path.join(output_dir, f"{base_name_gmr}_part{part}.csv")

        outfile = open(out_file, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()

        print(f"✔ Writing: {out_file}")

        for row in reader:
            device_value = row[DEVICE_ID_COL]
            row_bytes = sum(len(str(v)) for v in row.values())

            # If next device group exceeds 100MB → start new file
            if last_device is not None and device_value != last_device and (current_size + row_bytes > TARGET_BYTES):
                outfile.close()
                print(f"✔ Saved: {out_file}")

                part += 1
                current_size = 0

                # New output file with _GMR
                out_file = os.path.join(output_dir, f"{base_name_gmr}_part{part}.csv")
                outfile = open(out_file, "w", newline="", encoding="utf-8")
                writer = csv.DictWriter(outfile, fieldnames=headers)
                writer.writeheader()

                print(f"✔ Writing: {out_file}")

            writer.writerow(row)
            current_size += row_bytes
            last_device = device_value

        outfile.close()
        print(f"✔ Saved Final Part: {out_file}")

    print("\n🎉 SPLIT COMPLETED SUCCESSFULLY!")


split_fast_csv(INPUT_FILE)
