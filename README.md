# Desktop Cleaner

A Python-based application that automatically organizes your desktop files into categorized folders, making it clutter-free and easy to navigate. The app includes automation to run daily at a specific time and supports custom rules for organizing files, including screenshots.

## Features

- Categorizes files into predefined folders such as:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.psd`
  - **Documents**: `.pdf`, `.docx`, `.xlsx`, `.csv`, `.txt`
  - **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`
  - **Screenshots**: Captures macOS screenshots
  - **Others**: Any file types not explicitly listed
- Creates folders dynamically if they do not exist.
- Moves files to the corresponding folder based on their extension or filename.
- Automatically runs daily at 8:00 AM using the `schedule` library.

## Prerequisites

- Python 3.12 or later
- Required Python packages: `schedule`

### Install the required dependencies:

```bash
pip install schedule
```

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/jorge-allende/DesktopCleaner.git
    cd DesktopCleaner
    ```

2. Run the script:

    ```bash
    python3 desktop_cleaner.py
    ```

## Automation

The application uses the `schedule` library to run automatically every day at **8:00 AM**. You can modify the time by editing the following line in the script:

```python
schedule.every().day.at("08:00").do(organize_desktop)
```

## Customization

To add or modify file categories, update the `FILE_TYPES` dictionary in the script:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".xlsx", ".csv", ".txt"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Screenshots": [],  # For screenshots specifically
    "Others": []
}
```

## How It Works

1. The script scans the files on your desktop.
2. It categorizes the files based on their extensions or filenames.
3. It creates the required folders (if not already present) and moves files accordingly.
4. Logs actions to the terminal (e.g., `Moved example.jpg to Images`).
