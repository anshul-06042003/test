import os

output_dir = r"D:\Metering_data\smart_meter_data_GMR\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_10\Agra_Blockload_Oct_5_6_split"
for file in os.listdir(output_dir):
    if file.endswith(".csv"):
        size = os.path.getsize(os.path.join(output_dir, file)) / (1024*1024)
        print(f"{file}: {size:.2f} MB")
