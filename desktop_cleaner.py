import os
import shutil

# Define file types for organizing
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".xlsx", ".csv", ".txt"],
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

if __name__ == "__main__":
    organize_desktop()
    print("Done! Your desktop is now organized.")
