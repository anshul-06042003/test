import pandas as pd
import os

# INPUT CSV PATH
input_file = r"C:\Users\HP\Desktop\chunk_div\Agra_DailyLoad_Oct_01_10.csv"

# OUTPUT FOLDER
output_folder = r"C:\Users\HP\Desktop\chunk_div\output_chunks"
os.makedirs(output_folder, exist_ok=True)

# ROWS PER CHUNK
chunk_size = 100000

# Read and split CSV in chunks
chunk_number = 100000
for chunk in pd.read_csv(input_file, chunksize=chunk_size, low_memory=False):
    output_file = os.path.join(output_folder, f"chunk_{chunk_number}.csv")
    chunk.to_csv(output_file, index=False)
    print(f"✔ Saved: {output_file}")
    chunk_number += 1
    
print("🎉 All chunks created successfully!")
