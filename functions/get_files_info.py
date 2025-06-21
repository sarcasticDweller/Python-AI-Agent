import os

def get_files_info(working_directory, directory=None):
    working_directory_contents = os.listdir(working_directory)

    directory = "." if directory is None else directory # clean input

    if directory not in working_directory_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(os.path.join(working_directory, directory)):
        return f'Error: "{directory}" is not a directory'
    return "hoo-rah"