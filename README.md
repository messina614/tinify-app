# Hot Folder Image Compressor and Converter

This Python script monitors a designated "hot folder," compresses supported image files (PNG, JPG, JPEG) using the [Tinify API](https://tinypng.com/), converts them to WEBP format, and replaces the original files.

## Features
- **Folder Monitoring**: Watches a user-defined folder for newly created image files.
- **Image Compression**: Compresses PNG, JPG, and JPEG images using the Tinify API.
- **Format Conversion**: Converts compressed images to WEBP format using Pillow.
- **Automatic Cleanup**: Removes the original image files after processing.

## Requirements
### Python Version
- Python 3.6 or higher

### Install Required Packages
Install the necessary dependencies listed in `requirements.txt`:
```bash
pip3 install -r requirements.txt
```

### `requirements.txt`
```
tinify
pillow
watchdog
```

## Usage

### 1. Set Up the Script
Clone or copy the script to your desired location.

### 2. Run the Script
Execute the script from the terminal:
```bash
python3 image_compressor.py
```
When prompted:
- Enter your Tinify API key.
- Enter the absolute path to the folder you want to monitor (e.g., `/Users/username/images`).

### 3. Add Images to the Folder
Add PNG, JPG, or JPEG files to the monitored folder. The script will:
1. Compress the image using the Tinify API.
2. Convert the compressed image to WEBP format.
3. Replace the original image by deleting it.

### 4. Stop the Script
To stop monitoring the folder, press `Ctrl+C` in the terminal.

## Supported File Formats
The script supports the following image file extensions:
- `.png`
- `.jpg`
- `.jpeg`

## Notes
- Ensure your Tinify API key is valid and has enough credits for image compression.
- The monitored folder must exist and be writable.
- The WEBP files will be saved in the same directory as the original images.

## Error Handling
- **Compression Errors**: If an image cannot be compressed using the Tinify API, an error will be logged and the image will remain unchanged.
- **Conversion Errors**: If an image cannot be converted to WEBP, an error will be logged and the original file will remain.
- **File Removal Errors**: If the script fails to remove the original file, an error will be logged but the converted file will still be saved.

## Acknowledgments
- [Tinify API](https://tinypng.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Watchdog](https://pypi.org/project/watchdog/)
