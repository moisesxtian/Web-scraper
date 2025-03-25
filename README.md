# Bing Image Downloader

This project allows users to efficiently download images from Bing using specific search queries while avoiding duplicate images. The script ensures a clean dataset by filtering out duplicate images based on their hash values.

## Features
- Downloads images from Bing based on predefined search queries.
- Stores images in a structured folder system for easy access.
- Prevents duplicate downloads by checking image hashes.
- Ensures the total number of images downloaded does not exceed a specified limit.
- Cleans up temporary files after execution.

## Requirements
Before running the script, make sure you have the following dependencies installed:

```sh
pip install bing-image-downloader pillow
```

## How to Start

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Script
```sh
python download_images.py
```

## How It Works
1. **Define Search Queries**: The script contains a predefined list of search terms related to "Chery cars".
2. **Set Image Limit**: The total number of images is controlled by `total_images`.
3. **Create Required Folders**: The script ensures necessary directories exist before downloading.
4. **Check Existing Images**: Before downloading, the script scans previously saved images to avoid duplicates.
5. **Download New Images**: It downloads the remaining required images and stores them temporarily.
6. **Filter Unique Images**: The script checks the hash of each image and moves unique ones to the dataset folder.
7. **Cleanup**: Any temporary files and duplicate images are removed at the end.

## File Structure
```
.
├── datasets/
│   ├── Chery/  # Stores unique images
├── temp_bing_downloads/  # Temporary storage during download
├── download_images.py  # The main script
├── requirements.txt  # Required dependencies
└── README.md  # Documentation
```

## Customization
- Modify the `search_queries` list to download images of different objects.
- Adjust `total_images` to change the dataset size.
- Change `output_directory` to store images in a different location.

## Notes
- Running the script multiple times will not redownload images that already exist.
- Duplicate images are removed using hash-based checking.
- If Bing blocks requests due to excessive downloads, consider adding delays or using proxies.

## License
This project is open-source and free to use under the MIT License.

---
For any issues or contributions, feel free to open a pull request or contact the repository owner.

