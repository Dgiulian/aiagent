import os


def write_file(working_directory, file_path, content):
    wd_abs = os.path.abspath(working_directory)
    f_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not f_abs.startswith(wd_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        dirname = os.path.dirname(f_abs)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(f_abs, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: An exception occurred: {e}"
