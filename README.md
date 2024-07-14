# Directory Organizer Script

This script organizes files in a specified directory based on their extensions. It moves files into folders named after their respective extensions, creating new folders if they do not already exist.

## How It Works

1. **Directory Setup**: 
   - The script defines a regular expression to match file extensions.
   - It initializes sets and lists to keep track of folders and files.
   - The script sets the parent directory and the working directory (`sample` in this case).

2. **File and Folder Identification**:
   - The script iterates through all items in the working directory.
   - It uses a regular expression to extract file extensions and categorize items as files or folders.

3. **File Organization**:
   - For each file, it checks if a folder with the file's extension already exists.
   - If the folder exists, the file is moved into the corresponding folder.
   - If the folder does not exist, the script creates a new folder named after the file's extension and moves the file into it.

## Prerequisites

- Python 3.x installed on your system.
- The `os` and `shutil` modules are part of the Python standard library, so no additional packages are required.

## Usage

1. Clone or download this script to your local machine.
2. Ensure you have a directory named `sample` in the same location as the script. This directory should contain the files you want to organize.
3. Run the script using the command:
   ```bash
   app.py
