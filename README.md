# Image Compressor and Converter

This Python script monitors a specified folder for newly added image files, compresses them using the [Tinify API](https://tinypng.com/), converts them to the WEBP format, and removes the original files.

## Features
- **Folder Monitoring**: Watches a specified folder for newly created image files.
- **Image Compression**: Compresses PNG, JPG, and JPEG images using the Tinify API.
- **Format Conversion**: Converts compressed images to the WEBP format using the Python Imaging Library (Pillow).
- **Automatic Cleanup**: Deletes the original image files after processing.

## Requirements
### Python Dependencies
- Python 3.6 or higher
- Install the required libraries:
  ```bash
  pip install tinify pillow watchdog
  ```

### Environment Variables
The script uses the following environment variables:
- `TINIFY_API_KEY`: Your API key for the Tinify service.
- `FOLDER_PATH`: The absolute path to the folder you want to monitor (default: `/path/to/your/folder`).

## Usage

### 1. Set Up Environment Variables
Set the environment variables `TINIFY_API_KEY` and `FOLDER_PATH`. You can do this by adding the following lines to your shell profile (`.bashrc`, `.zshrc`, etc.) or setting them directly in your terminal:

```bash
export TINIFY_API_KEY="your_tinify_api_key"
export FOLDER_PATH="/absolute/path/to/your/folder"
```

### 2. Run the Script
Start the script by running:

```bash
python image_compressor.py
```

The script will begin monitoring the specified folder for newly added images.

### 3. Add Images to the Folder
Copy or move PNG, JPG, or JPEG images into the monitored folder. The script will:
1. Compress the image using the Tinify API.
2. Convert the image to the WEBP format.
3. Remove the original image file.

### 4. Stop the Script
To stop monitoring, press `Ctrl+C` in the terminal.

## Supported File Formats
The script currently supports the following image formats:
- `.png`
- `.jpg`
- `.jpeg`

## Error Handling
- **Compression Errors**: If the Tinify API fails to compress an image, the script will log the error and skip further processing of that file.
- **Conversion Errors**: If the image cannot be converted to WEBP, the script will log the error and keep the original file.
- **File Removal Errors**: If the script fails to remove the original file, an error will be logged.

## Notes
- Ensure your Tinify API key is valid and you have enough credits for image compression.
- The folder path must be writable by the script.
- WEBP files will be saved in the same directory as the original images.
