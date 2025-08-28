def process_text_file():
    """
    This function reads a text file, processes its content, and writes results to a new file.
    """
    try:
        # Step 1: Read the contents of input.txt
        with open('input.txt', 'r') as input_file:
            content = input_file.read()
        
        # Step 2: Process the content
        # Count the number of words
        word_count = len(content.split())
        
        # Convert all text to uppercase
        uppercase_content = content.upper()
        
        # Step 3: Write processed text and word count to output.txt
        with open('output.txt', 'w') as output_file:
            output_file.write("PROCESSED TEXT:\n")
            output_file.write("=" * 50 + "\n")
            output_file.write(uppercase_content)
            output_file.write("\n" + "=" * 50 + "\n")
            output_file.write(f"WORD COUNT: {word_count}\n")
        
        # Step 4: Print success message
        print("✅ Success! The file has been processed and saved as output.txt")
        print(f"📊 Total words counted: {word_count}")
        
    except FileNotFoundError:
        print("❌ Error: input.txt file not found. Please create the file first.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def create_sample_input_file():
    """
    Optional function to create a sample input.txt file with some text
    """
    sample_text = """Hello world! This is a sample text file.
It contains multiple lines of text for processing.
Python is a powerful programming language for data processing.
File handling is an essential skill for programmers.
This is the fifth and final line of our sample text."""
    
    with open('input.txt', 'w') as file:
        file.write(sample_text)
    print("📝 Sample input.txt file has been created!")

# Main program execution
if __name__ == "__main__":
    # Check if input.txt exists, if not create a sample one
    try:
        with open('input.txt', 'r'):
            pass
    except FileNotFoundError:
        print("input.txt not found. Creating a sample file...")
        create_sample_input_file()
        print()  # Empty line for better formatting
    
    # Process the file
    process_text_file()
