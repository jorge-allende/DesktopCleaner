import os
import shutil
import schedule
import time

# Define file types for organizing
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".csv", ".txt"],
    "Videos": [".mp4", ".mkv", ".flv", "avi"],
    "Others": []
}

def organize_desktop():
    # Confirm the script is running
    print("Organizing desktop...")
    # Find desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # For loop through files on desktop
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Find file extension
        _, ext = os.path.splitext(filename)

        # Match file extension to a category
        folder_name = "Others"
        for category, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                folder_name = category
                break

        # Create the category folder if it doesn't exist
        category_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Move the file into the folder
        shutil.move(file_path, os.path.join(category_path, filename))
        print(f"Moved {filename} to {folder_name}") # File moved confirmation

if __name__ == "__main__":
    organize_desktop()

# Automation to run daily at 8 AM
schedule.every().day.at("08:00").do(organize_desktop)
print("Daily cleanup was ran! I'll be back tomorrow :)")

while True:
    schedule.run_pending()
    time.sleep(1)