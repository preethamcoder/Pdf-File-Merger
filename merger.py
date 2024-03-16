import os
import sys
import PyPDF2

def extract_files(dir_name):
    # Extract all the files in the directory
    res = os.listdir(dir_name)
    # Filter out all the pdf files
    res = [dir_name+"/"+each for each in res if each[-3:] == "pdf"]
    # Sort all the files in order
    res.sort()
    # Declare stack for push and pop operations
    stck = []
    # Put number files at the end
    for file in res:
        # Get the file names that start with the numbers
        words = file.split("/")
        # Check for the common prefix, was "ORG" in my case
        if words[-1][:3] != 'ORG':
            stck.append(file)
    # Remove the files
    res = [each for each in res if each not in stck]
    # Add file at the end
    for file in stck:
        res.append(file)
    # Return sorted list
    return res

def merge_files(file_list):
    # Get a writer to combine the texts
    merger = PyPDF2.PdfWriter()
    # Append each file to the writer
    for pdf in file_list:
        merger.append(pdf)
    # Declare end path
    res_name = "resultant.pdf"
    # Write the file to the path
    merger.write(res_name)
    # Close file and send success message
    merger.close()
    return f"File has been saved to {res_name}"

if __name__ == '__main__':
    # Get files
    files = extract_files(sys.argv[1])
    # End the process
    print(merge_files(files))
