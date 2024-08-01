# python proram to arrange all file in a folder accordng to extension
import os
import shutil

# get current working directory
current_folder = os.getcwd()
# Name of the current script file
script_name = os.path.basename(__file__)
# folder for file for no extension files
no_extension = 'undefined'
# if undefined folder doesnt exist make one
if not os.path.exists(no_extension):
    os.mkdir(no_extension)

# get all files in the folder
files = os.listdir(current_folder)

# Check if there are no files
if not files:
    print("No files here.")
    exit()

# for each file, move it to a folder with the same name as the file extension
for file in files:
    try:
        #skip for directory
        if os.path.isdir(file):
            continue
        #skip for this script
        if file == script_name:
            continue

        # get the file extension
        filename, file_extension = os.path.splitext(file)
        # Remove the  dot from the file extension
        file_extension = file_extension.lstrip('.')

        #destination folder determining
        if not file_extension:
            dstn_folder = no_extension
        else:
            dstn_folder = file_extension
    
        # Create the destination folder if it doesn't exist
        if not os.path.exists(dstn_folder):
            os.makedirs(dstn_folder)
    
        # Move the file to the destination folder
        shutil.move(os.path.join(current_folder, file), os.path.join(current_folder, dstn_folder, file))

        print(f"Sucessfully Moved File {file} to folder {dstn_folder}")

    except Exception as e:
        print(f"Error Moving File {file}: {e}")

print("File organization completed..")