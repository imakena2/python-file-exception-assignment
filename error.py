def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (e.g., converts to uppercase), and writes to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = line.upper()  # Example modification: convert to uppercase
                outfile.write(modified_line)
        print(f"File '{input_filename}' successfully modified and written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_filename_and_handle_errors():
    """
    Prompts the user for a filename and handles potential errors during file reading.
    """
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                contents = file.read() # read the file to test its existence and read permissions.
                print(f"File '{filename}' successfully read. Contents:\n{contents}")
                break # break the loop if successful.
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read file '{filename}'. Please check permissions.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
if __name__ == "__main__":
    # File Read & Write Challenge
    input_file = "input.txt"  # Create a dummy input.txt file for testing.
    with open(input_file, "w") as f:
        f.write("This is a test file.\nAnother line for testing.\n")

    output_file = "output.txt"
    modify_and_write_file(input_file, output_file)

    # Error Handling Lab
    get_filename_and_handle_errors()