import zipfile
import os

zip_path = r"D:\Kaiburr\Task5\complaints.csv.zip"
extract_path = r"D:\Kaiburr\Task5"

if os.path.exists(zip_path):
    print("Extracting file...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("✅ Extraction complete! Files extracted to:", extract_path)
else:
    print("❌ Zip file not found at:", zip_path)
