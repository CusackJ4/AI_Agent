import os

def get_files_info(working_directory, directory=None):
    
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, directory)
    normalized_path = os.path.normpath(full_path) # get full normalised working_directory + directory path

    #  Check if the normalised path is a valid path within the working directory
    common_prefix = os.path.commonprefix([normalized_path, working_directory]) # find the common prefix between both paths
    if (common_prefix != working_directory): # ensure that the common prefix is the same as the working directory prefix
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.exists(normalized_path): # check if path exists
        return f'Error: "{directory}" is not a directory'
    

    dir_contents = os.listdir(normalized_path) # contents of directory
    # print(dir_contents)
    # print(f"Check: {os.path.getsize(os.path.join(normalized_path, dir_contents[2]))}")

    var_dict = {}
    for dir in dir_contents:
        try:
            file_size = os.path.getsize(os.path.join(normalized_path, dir))
        except Exception as e:
            return f"Error: file_size operation failed. {str(e)}"
            # print("file_size operation failed")

        try:
            is_dir = os.path.isdir(os.path.join(normalized_path, dir))
        except Exception as e:
            return f"Error: is_dir operation failed. {str(e)}"
            # print("is_dir operation failed")
        
        var_dict[dir] = {
                'file_size=':file_size,
                'is_dir=':is_dir}

    dir_files_info = ''
    for key in var_dict:
        file_info = f"- {key}: file_size={var_dict[key]['file_size=']} bytes, is_dir={var_dict[key]['is_dir=']}\n"
        dir_files_info = dir_files_info + file_info

    return dir_files_info


    







    
