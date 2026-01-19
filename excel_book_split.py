import pandas as pd
import os

# =========================
# CONFIG
# =========================
INPUT_EXCEL_FILE = r"D:\Metering_data\Load_Survey November month (2).xlsx"  # 👈 your Excel file path
OUTPUT_FOLDER_NAME = "excel_split_books"        # 👈 fixed output folder name
# =========================


def split_excel_by_sheets(input_file):

    print(f"\n Reading Excel file: {input_file}")

    # Output folder (same directory as input file)
    output_dir = os.path.join(os.path.dirname(input_file), OUTPUT_FOLDER_NAME)
    os.makedirs(output_dir, exist_ok=True)

    # Load Excel file metadata
    xls = pd.ExcelFile(input_file)

    print(f"📄 Total sheets found: {len(xls.sheet_names)}")

    for sheet_name in xls.sheet_names:
        print(f"➡ Processing sheet: {sheet_name}")

        # Read sheet exactly as-is
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Safe file name for sheet
        safe_sheet_name = sheet_name.replace("/", "_").replace("\\", "_")

        # Output file path
        output_file = os.path.join(output_dir, f"{safe_sheet_name}.xlsx")

        # Write to Excel (no index to avoid extra column)
        df.to_excel(output_file, index=False)

        print(f"✔ Saved: {output_file}")

    print("\n🎉 DONE — All sheets split successfully into 'excel_split_books'!")


split_excel_by_sheets(INPUT_EXCEL_FILE)
