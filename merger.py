import os
import sys
import PyPDF2

def extract_files(dir_name):
    # Extract all the files in the directory
    res = os.listdir(dir_name)
    # Filter out all the pdf files
    res = [dir_name+"/"+each for each in res if each[-3:] == "pdf"]
    # Declare stack for push and pop operations
    stck = []
    # Put number files at the end
    for file in res:
        # Get the file names that start with the numbers
        words = file.split("/")
        if words[-1][:3].lower() == 'org':
            stck.append(file)
    # Filter out the numeric files
    res = [each for each in res if each not in stck]
    # Sort the files that start with ORG based on their number
    stck.sort(key= lambda x: int(x.split("/")[-1].split("-")[0][3:]))
    # Sort the files that dont have ORG
    res.sort()
    # Combine both the files lists together
    res = stck + res
    # Return sorted list
    return res

def merge_files(file_list):
    # Get a writer to combine the texts
    merger = PyPDF2.PdfWriter()
    # Append each file to the writer
    cter = 0
    for pdf in file_list:
        cter += 1
        with open(pdf, 'rb') as file:
            print(pdf)
            merger.append(file)
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
