import csv
import requests
import os
import sys
import zipfile

resolution = "1K"
file_type = "JPG"
unzip = True

if len(sys.argv) >= 2:
    resolution = sys.argv[1].upper()
if len(sys.argv) == 3:
    file_type = sys.argv[2].upper()

if resolution not in ["1K", "2K", "4K", "8K"] or file_type not in ["PNG", "JPG"]:
    print("Invalid format or type. Valid formats: 1k, 2k, 4k, 8k. Valid types: png, jpg.")
    sys.exit(1)

os.makedirs("downloads", exist_ok=True)
os.makedirs("unzipped", exist_ok=True)

csv_url = "https://ambientCG.com/api/v2/downloads_csv"
response = requests.get(csv_url)
csv_file = "downloads.csv"

with open(csv_file, "wb") as file:
    file.write(response.content)

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if resolution in row["downloadAttribute"] and file_type in row["downloadAttribute"]:
            download_url = row["downloadLink"]
            file_name = os.path.join("downloads", download_url.split("file=")[1])
            if os.path.exists(file_name):
                print(f"File {file_name} already exists. Skipping...")
                continue
            print(f"Downloading {file_name}...")
            zip_response = requests.get(download_url)
            with open(file_name, "wb") as zip_file:
                zip_file.write(zip_response.content)
            print(f"File {file_name} downloaded.")

if unzip:
    for file in os.listdir("downloads"):
        with zipfile.ZipFile("downloads/" + file, 'r') as zip_ref:
            print(file + " extracted.")
            zip_ref.extractall("unzipped/" + file[:-4])