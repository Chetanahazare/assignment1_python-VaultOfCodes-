#code3

def read_and_write_file(filename):
    try:
        # Read the content of the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Open the file in 'w' mode, which truncates the file, and write the uppercase content
        with open(filename, 'w') as file:
            file.write(content.upper())
        
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()


#Issues And Solutions 
#1.The code reads the content of the file and immediately opens the file in write mode, which truncates the file before writing. It results in the loss of the original content.
#solution: Read the content first, close the file, and then open the file in write mode to avoid overwriting.
#2.The code doesn't handle potential issues with file reading or writing, such as file not found or permissions issues.
#Solution: Use a try-except block to catch exceptions and handle errors gracefully