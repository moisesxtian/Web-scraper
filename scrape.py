from bing_image_downloader import downloader
import os
import hashlib
from PIL import Image
import shutil

# Define search queries
search_queries = ["Chery car", "Chery Auto", "Chery sedan", "Chery New Car", "Chery Car Models"]

# Set total image limit
total_images = 500  # Change this to your desired total number

# Base output directory (store all images in "datasets/Chery")
output_directory = 'datasets/Chery'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Temporary folder for downloads
temp_folder = "temp_bing_downloads"
os.makedirs(temp_folder, exist_ok=True)

# Function to calculate the hash of an image
def calculate_hash(image_path):
    try:
        with Image.open(image_path) as img:
            return hashlib.md5(img.tobytes()).hexdigest()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# Load existing hashes to prevent re-downloading
hashes = set()
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    if os.path.isfile(file_path):
        img_hash = calculate_hash(file_path)
        if img_hash:
            hashes.add(img_hash)

# Track number of unique images downloaded
downloaded_count = len(hashes)

# Download images until total_images is reached
for query in search_queries:
    if downloaded_count >= total_images:
        break  # Stop downloading if total limit is reached

    remaining_images = total_images - downloaded_count
    print(f"\nDownloading {remaining_images} more images...")

    downloader.download(
        query,
        limit=remaining_images,  # Only download the remaining needed images
        output_dir=temp_folder,
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True
    )

    # Move unique images to the main directory
    query_folder = os.path.join(temp_folder, query)
    if os.path.exists(query_folder):
        for filename in os.listdir(query_folder):
            if downloaded_count >= total_images:
                break  # Stop moving files if total limit is reached

            src_path = os.path.join(query_folder, filename)
            img_hash = calculate_hash(src_path)

            if img_hash and img_hash not in hashes:
                dst_path = os.path.join(output_directory, filename)
                shutil.move(src_path, dst_path)
                hashes.add(img_hash)
                downloaded_count += 1  # Update count of unique images
            else:
                os.remove(src_path)  # Delete duplicate image

        shutil.rmtree(query_folder)  # Remove empty query folder

# Cleanup: Remove the temp folder
shutil.rmtree(temp_folder, ignore_errors=True)

print(f"\nDownload complete. {downloaded_count} unique images saved in:", output_directory)
