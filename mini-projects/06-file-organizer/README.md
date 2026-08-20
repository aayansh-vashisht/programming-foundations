# 📁 File Organiser

A command-line utility built in Python that automatically scans a target directory, categorizes files by their extensions, moves them into organized folders, prevents filename collisions, and displays an execution summary.

---

## 🚀 Features

- 🔍 **Directory Inspection**: Scans any designated directory for loose files while ignoring existing subdirectories.
- 🗂️ **Extension Classification**: Maps file extensions to predefined categories (Images, Documents, Audio, Video, Archives, Code, and Others).
- 🛡️ **Overwrite Prevention**: Automatically appends incremental counters (e.g., `file_1.txt`) if a file with the same name already exists in the destination folder.
- 📊 **Operation Summary**: Provides a clear post-run report showing the total files moved and a breakdown per category.

---

## 📁 File Structure

```text
├── file_organizer.py   # Main organizer script
└── README.md           # Project documentation
```

---

## 🛠️ Requirements

- **Python 3.6+**
- Standard Python libraries (`os`, `shutil`, `pathlib`) — *no external packages required!*

---

## 📦 How to Run

1. Navigate to the project directory:
   ```bash
   cd mini-projects/06-file-organizer
   ```

2. Run the application:
   ```bash
   python file_organizer.py
   ```

3. When prompted, enter the absolute or relative path of the practice/temporary directory you want to organize.

---

## 🖥️ Example Usage

```text
=== FILE ORGANISER ===
Note: Test this on a temporary or practice directory first.

Enter the path of the directory to organise: ./practice_dir

[MOVED] 'photo.jpg' -> Images/photo.jpg
[MOVED] 'notes.txt' -> Documents/notes.txt
[RENAMED & MOVED] 'notes.txt' -> Documents/notes_1.txt
[MOVED] 'script.py' -> Code/script.py

========================================
           OPERATION SUMMARY            
========================================
Images              : 1 file(s)
Documents           : 2 file(s)
Code                : 1 file(s)
----------------------------------------
Total Files Moved   : 4
========================================
```
