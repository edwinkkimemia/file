def process_file():
    # Get filename from user
    input_filename = input("Please enter the input filename: ")
    
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (example: convert to uppercase and add line numbers)
        lines = content.split('\n')
        modified_content = ''
        for i, line in enumerate(lines, 1):
            if line:  # Only process non-empty lines
                modified_content += f"Line {i}: {line.upper()}\n"
                
        # Create output filename by appending '_modified' to original name
        output_filename = input_filename.rsplit('.', 1)[0] + '_modified.txt'
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully processed file! Output saved as: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write output file.")
    except IOError:
        print(f"Error: An I/O error occurred while processing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    print("File Processing Program")
    print("=====================")
    process_file()