import csv
import requests
import os
import sys
import zipfile
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

resolution = config['resolution']
file_type = config['file_type']
unzip = config['unzip']
unzipping_directory = config['unzip']['folder']

if resolution not in ["1K", "2K", "4K", "8K"] or file_type not in ["PNG", "JPG"]:
    print("Invalid format or type. Valid formats: 1k, 2k, 4k, 8k. Valid types: png, jpg.")
    sys.exit(1)

os.makedirs("downloads", exist_ok=True)
os.makedirs(unzipping_directory, exist_ok=True)

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
        with zipfile.ZipFile(f"downloads/{file}", 'r') as zip_ref:
            if not os.path.exists(f"{unzipping_directory}/{file[:-4]}"):
                print(file + " extracted.")
                zip_ref.extractall(unzipping_directory + "/" + file[:-4])
            else:
                print(f"{file} already extracted. Skipping...")

def delete_files(file_type):
    for directory in os.listdir(unzipping_directory):
        for file in os.listdir(os.path.join(unzipping_directory, directory)):
            if file_type in file:
                print(f'Found {file_type} at {unzipping_directory}/{directory}. Deleting...')
                os.remove(os.path.join(unzipping_directory, directory, file))

for file_type in config['keep_files']:
    match file_type:
        case "color":
            if not config['keep_files']['color']:
                delete_files("Color")
        
        case "roughness":
            if not config['keep_files']['roughness']:
                delete_files("Roughness")

        case "normal_gl":
            if not config['keep_files']['normal_gl']:
                delete_files("NormalGL")
        
        case "normal_dx":
            if not config['keep_files']['normal_dx']:
                delete_files("NormalDX")

        case "metalness":
            if not config['keep_files']['metalness']:
                delete_files("Metalness")

        case "opacity":
            if not config['keep_files']['opacity']:
                delete_files("Opacity")

        case "ambient_occlusion":
            if not config['keep_files']['ambient_occlusion']:
                delete_files("AmbientOcclusion")
        
        case "displacement":
                    if not config['keep_files']['displacement']:
                        delete_files("Displacement")

        case "cover":
            if not config['keep_files']['ambient_occlusion']:
                for directory in os.listdir(unzipping_directory):
                    for file in os.listdir(os.path.join(unzipping_directory, directory)):
                        if not any(keyword in file for keyword in ["Color", "Roughness", "NormalGL", "NormalDX","Metalness", "AmbientOcclusion", "Opacity", "Displacement"]):
                            print(f'Found {file_type} at {unzipping_directory}/{directory}. Deleting...')
                            os.remove(os.path.join(unzipping_directory, directory, file))