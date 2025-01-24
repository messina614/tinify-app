import tinify
import os
from PIL import Image
import io
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Prompt the user for the Tinify API key and folder path
tinify.key = input("Enter your Tinify API key: ")
folder_path = input("Enter the path to the folder you want to monitor: ")

# Supported image extensions
image_extensions = ['.png', '.jpg', '.jpeg']

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Event detected: {event.src_path}")
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            name, ext = os.path.splitext(filename)
            if ext.lower() in image_extensions:
                file_path = event.src_path
                print(f"Processing {filename}...")
                
                # Compress the image using Tinify API
                try:
                    source = tinify.from_file(file_path)
                    # Get the compressed image as a byte buffer
                    compressed_bytes = source.to_buffer()
                    print(f"Successfully compressed {filename}.")
                except tinify.Error as e:
                    print(f"Error compressing {filename}: {e}")
                    return

                # Open the compressed image with PIL from the byte buffer
                try:
                    image = Image.open(io.BytesIO(compressed_bytes))
                    # Convert to WEBP and save
                    webp_path = os.path.join(os.path.dirname(file_path), name + ".webp")
                    image.save(webp_path, 'WEBP')
                    print(f"Converted {filename} to WEBP format and saved.")
                except Exception as e:
                    print(f"Error converting {filename} to WEBP: {e}")
                    return

                # Remove the original file
                try:
                    os.remove(file_path)
                    print(f"Removed original file {filename}.")
                except Exception as e:
                    print(f"Error removing original file {filename}: {e}")

if __name__ == "__main__":
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    print(f"Monitoring folder: {folder_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()