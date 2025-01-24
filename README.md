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
- `IMAGE_COMPRESSOR_FOLDER_PATH`: The path to the folder you want to monitor for new images. This should be set to the directory where images will be automatically compressed and converted to WEBP format.

## Configuration

Before running the image compressor script, ensure you have set the necessary environment variables:

- `TINIFY_API_KEY`: Your API key for the Tinify service.
- `IMAGE_COMPRESSOR_FOLDER_PATH`: The path to the folder you want to monitor for new images. This should be set to the directory where images will be automatically compressed and converted to WEBP format.

You can set these environment variables in your shell or in a `.env` file if you are using a tool like `dotenv`.

## Usage

### 1. Set Up Environment Variables
Set the environment variables `TINIFY_API_KEY` and `IMAGE_COMPRESSOR_FOLDER_PATH`. You can do this by adding the following lines to your shell profile (`.bashrc`, `.zshrc`, etc.) or setting them directly in your terminal:

```bash
export TINIFY_API_KEY="your_tinify_api_key"
export IMAGE_COMPRESSOR_FOLDER_PATH="/absolute/path/to/your/folder"
```