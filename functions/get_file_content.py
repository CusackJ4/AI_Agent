import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    normalized_path = os.path.normpath(full_path) # get full normalised working_directory + directory path

    #  Check if the normalised path is a valid path within the working directory
    common_prefix = os.path.commonprefix([normalized_path, working_directory]) # find the common prefix between both paths
    if (common_prefix != working_directory): # ensure that the common prefix is the same as the working directory prefix
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(normalized_path): # check if path exists
        return f'Error:  File not found or is not a regular file: "{file_path}"'
    print(normalized_path)
    with open(normalized_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    return file_content_string


# Read the file and return its contents as a string.
# I'll list some useful standard library functions in the tips section below.
# If the file is longer than 10000 characters, truncate it to 10000 characters and append this message to the end [...File "{file_path}" truncated at 10000 characters].
# Instead of hard-coding the 10000 character limit, I stored it in a config.py file.