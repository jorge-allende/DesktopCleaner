import os
import shutil
import schedule
import time
import argparse

# Define file types for organizing
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".csv", ".txt"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Screenshots": [],
    "Others": []
}

def organize_desktop():
    print("Organizing desktop...")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        if os.path.isdir(file_path):
            continue

        if filename.lower().startswith("screenshot"):
            folder_name = "Screenshots"
        else:
            _, ext = os.path.splitext(filename)
            folder_name = "Others"
            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    folder_name = category
                    break

        category_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        shutil.move(file_path, os.path.join(category_path, filename))
        print(f"Moved {filename} to {folder_name}")

def run_scheduler():
    print("Scheduling daily cleanup at 8:00 AM...")
    schedule.every().day.at("08:00").do(organize_desktop)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Desktop Cleaner")
    parser.add_argument("--schedule", action="store_true", help="Run daily at 8 AM")
    args = parser.parse_args()

    if args.schedule:
        run_scheduler()
    else:
        print("Cleaning your desktop now...")
        organize_desktop()
        print("Done! Your desktop is now organized.")
