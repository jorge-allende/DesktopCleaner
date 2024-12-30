import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename="desktop_cleaner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define file types for organizing. The keys are folder names, and the values are lists of file extensions.
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".xlsx", ".csv", ".txt"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Screenshots": [],
    "Others": []
}

def organize_desktop():
    logging.info("Organizing desktop...")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Iterate through all files in the desktop directory.
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Skip directories as we're only organizing files.
        if os.path.isdir(file_path):
            logging.debug(f"Skipping directory: {filename}")
            continue

        # Determine the folder name based on file type or name pattern.    
        if filename.lower().startswith("screenshot"):
            folder_name = "Screenshots"
        else:
            _, ext = os.path.splitext(filename)
            folder_name = "Others"
            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    folder_name = category
                    break

        # Create the category folder if it doesn't exist.
        category_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            logging.info(f"Created folder: {folder_name}")

        # Move the file to the appropriate category folder.
        try:
            shutil.move(file_path, os.path.join(category_path, filename))
            logging.info(f"Moved {filename} to {folder_name}")
        except Exception as e:
            logging.error(f"Failed to move {filename}: {e}")

if __name__ == "__main__":
    try:
        organize_desktop()
        logging.info("Done! Your desktop is now organized.")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
