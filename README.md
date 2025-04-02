# File Processing Program

A simple Python script that reads a text file, modifies its content (converts to uppercase and adds line numbers), and writes the result to a new file. Includes robust error handling for file operations.

## Features
- Reads any text file provided by the user.
- Modifies content by converting text to uppercase and numbering lines.
- Creates a new output file with `_modified.txt` appended to the original filename.
- Handles common errors like missing files, permission issues, and I/O problems.

## Requirements
- Python 3.x

## How to Use
1. Save the script as `file_processor.py`.
2. Create a text file (e.g., `test.txt`) with some content.
3. Run the script:
   ```bash
   python file_processor.py