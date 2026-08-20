import os
import shutil
from pathlib import Path

# Map extensions to corresponding category folders
EXTENSION_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json"]
}

# Determine category folder name based on file extension
def get_category(file_path):
    ext = file_path.suffix.lower()
    for category, extensions in EXTENSION_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

# Generate a unique path to prevent accidental overwriting
def get_unique_destination(destination_folder, file_path):
    base_name = file_path.stem
    extension = file_path.suffix
    destination_file = destination_folder / file_path.name

    counter = 1
    while destination_file.exists():
        new_name = f"{base_name}_{counter}{extension}"
        destination_file = destination_folder / new_name
        counter += 1

    return destination_file

# Inspect directory and organize files into category subfolders
def organize_directory(target_dir):
    target_path = Path(target_dir).resolve()

    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: Directory '{target_dir}' does not exist or is not valid.")
        return

    category_counts = {}
    total_moved = 0

    # Inspect all items in the target directory
    for item in target_path.iterdir():
        if item.is_file():
            category = get_category(item)
            dest_dir = target_path / category
            dest_dir.mkdir(exist_ok=True)

            # Prevent overwriting
            dest_file = get_unique_destination(dest_dir, item)

            shutil.move(str(item), str(dest_file))
            category_counts[category] = category_counts.get(category, 0) + 1
            total_moved += 1

            if dest_file.name != item.name:
                print(f"[RENAMED & MOVED] '{item.name}' -> {category}/{dest_file.name}")
            else:
                print(f"[MOVED] '{item.name}' -> {category}/{dest_file.name}")

    # Print operation summary
    print("\n" + "=" * 40)
    print("           OPERATION SUMMARY            ")
    print("=" * 40)
    if total_moved == 0:
        print("No files found to organize.")
    else:
        for category, count in category_counts.items():
            print(f"{category:<20}: {count} file(s)")
        print("-" * 40)
        print(f"Total Files Moved   : {total_moved}")
    print("=" * 40 + "\n")

# Main interactive entry point
def main():
    print("=== FILE ORGANISER ===")
    print("Note: Test this on a temporary or practice directory first.\n")

    dir_input = input("Enter the path of the directory to organise: ").strip()
    if dir_input:
        organize_directory(dir_input)
    else:
        print("No path provided. Exiting.")

if __name__ == "__main__":
    main()
