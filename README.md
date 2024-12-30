# Desktop Cleaner

A Python-based application that organizes your desktop files into categorized folders, making it clutter-free and easy to navigate. This tool supports manual execution for immediate cleanup and can be automated using system-level tools for convenience.

## Features

- Categorizes files into predefined folders such as:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.psd`
  - **Documents**: `.pdf`, `.docx`, `.xlsx`, `.csv`, `.txt`
  - **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`
  - **Screenshots**: Captures macOS screenshots
  - **Others**: Any file types not explicitly listed
- Creates folders dynamically if they do not exist.
- Moves files to the corresponding folder based on their extension or filename.
- Logs all actions to desktop_cleaner.log.
- Can be automated to run daily at a specific time using system-level schedulers (e.g., Cron, Task Scheduler).

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

2. Run the script for manual cleanup:

   ```bash
   python3 desktop_cleaner.py
   ```

   This mode:

   - Scans your desktop.
   - Files are categorized into folders based on their extensions or filenames.
   - Actions are logged in the desktop_cleaner.log file.

3. Check the desktop_cleaner.log file for details of the cleanup process.

## Automate the Script (Optional)

### **For Linux/macOS (Using Cron):**

1. Open the crontab editor:

   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script to run daily at **8:00 AM**:

   ```bash
   0 8 * * * python3 /path/to/DesktopCleaner/desktop_cleaner.py
   ```

   Replace `/path/to/DesktopCleaner/desktop_cleaner.py` with the full path to the script.

3. Save and exit. The script will now run automatically every day at **8:00 AM**.

### **For Windows (Using Task Scheduler):**

1. Open **Task Scheduler**:

   - Press `Win + S`, type "Task Scheduler," and open it.

2. Create a new task:

   - Click on `Create Basic Task`.
   - Name the task (e.g., "DesktopCleaner Daily").
   - Select `Daily` and set the time (e.g., **8:00 AM**).

3. Set the action:

   - Choose `Start a Program`.
   - Enter the path to your Python executable (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\python.exe`).
   - Add the script as an argument (e.g., `"C:\path\to\DesktopCleaner\desktop_cleaner.py"`).

4. Save and test:
   - Save the task.
   - Right-click the task and select `Run` to test it.

## Customization

To add or modify file categories, update the `FILE_TYPES` dictionary in the script:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".psd"],
    "Documents": [".pdf", ".docx", ".xlsx", ".csv", ".txt"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Screenshots": [],  # For screenshots specifically
    "Others": []  # Default category for uncategorized files
}
```

## How It Works

### One-Time Cleanup:

- The script scans your desktop for files.
- It categorizes the files based on their extensions or filenames.
- It creates folders if they don’t already exist.
- It moves files into the appropriate folders and logs actions to the desktop_cleaner.log for review.

### Scheduled Automation:

- You can automate the script using:
  - **Cron** (Linux/macOS): Schedule it to run daily at a specific time.
  - **Task Scheduler** (Windows): Set it up to run daily at a specific time.

## Logs

Logs are saved in `desktop_cleaner.log` in the project directory.

### Example Log Entry:

```yaml
2024-12-29 14:23:45,678 - INFO - Moved photo1.jpg to Images
2024-12-29 14:23:46,123 - INFO - Created folder: Images
```
