# ambientCG Downloader

Download all the CC0 textures from the official ambientcg.com website easily.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0efce479-5cbe-4ed1-9805-818c18b6a151" />
</p>

## Download the entire ambientCG texture library
This repository was created to simplify a repetitive process: downloading textures from ambientCG, extracting them, and manually removing unused images.

With this automation, all textures are pre-downloaded to your computer. Once you find the texture you need on the ambientCG website, you can quickly locate it locally without additional steps.

Here’s the translation and an explanation of how to use the configuration file:  

---

## Setting Up the Script  

To configure the script, use the `config.yaml` file. Here's an example configuration:  

```yaml
resolution: "1K"                  # (1K, 2K, 4K, 8K)
file_type: "JPG"                  # (JPG/PNG)
downloads_folder: "downloads"
unzip: 
  enabled: true                   # (true/false)
  folder: "unzipped"
keep_files:                       # Files marked as false will be deleted
  color: true
  roughness: true
  normal_gl: true
  normal_dx: true
  metalness: true
  opacity: true
  ambient_occlusion: true
  displacement: false
  cover: false
```

### How to Use It  

1. **Adjust the Settings**  
   - Open the `config.yaml` file in a text editor.  
   - Set the `resolution` to the desired quality (e.g., "1K", "2K").  
   - Choose the `file_type` (either "JPG" or "PNG").  
   - Specify the folder for downloaded textures under `downloads_folder`.  

2. **Configure Unzipping**  
   - If you want the textures to be automatically extracted, set `enabled` to `true`.  
   - Define the folder for unzipped files under `folder`.  

3. **Manage File Types**  
   - In the `keep_files` section, mark the file types you want to keep as `true`.  
   - Any file type set to `false` will be deleted after extraction.  

4. **Run the Script**  
   - Save your changes to the `config.yaml` file.  
   - Execute the script, and it will follow the configuration to download, unzip, and manage the textures automatically.

## Installation  

You can set up the project in two ways: using **Poetry** or a traditional setup with `requirements.txt`. Choose the method that best suits your workflow.  

### Option 1: Using Poetry  
1. Ensure you have [Poetry](https://python-poetry.org/) installed.  
   ```bash
   pip install poetry
   ```
2. Clone the repository:  
   ```bash
   git clone https://github.com/alvarognnzz/ambientcg-downloader
   cd ambientcg-downloader
   ```
3. Install dependencies:  
   ```bash
   poetry install
   ```
   ```
4. Run the script:  
   ```bash
   poetry run python main.py
   ```

### Option 2: Without Poetry (using `requirements.txt`)  
1. Clone the repository:  
   ```bash
   git clone https://github.com/alvarognnzz/ambientcg-downloader
   cd ambientcg-downloader
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:  
   ```bash
   python script.py
   ```
---

Both methods will set up the environment for running the project. If you're new to dependency management, the second option (`requirements.txt`) is more straightforward.
