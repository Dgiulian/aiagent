import os


def get_files_info(working_directory, directory):
    wd_abs = os.path.abspath(working_directory)
    d_abs = os.path.abspath(os.path.join(working_directory, directory))

    if not d_abs.startswith(wd_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(d_abs):
        return f'Error: "{directory}" is not a directory'
    try:
        contents = ""
        for i in os.listdir(d_abs):
            size = os.path.getsize(os.path.join(d_abs, i))
            name = i.split("/")[-1]
            is_dir = os.path.isdir(os.path.join(d_abs, i))
            contents = contents + f"- {name}: file_size:{size} bytes, is_dir={is_dir}\n"
    except:
        return f"Error: An exception occurred"
    return contents
