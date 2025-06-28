import os


def get_file_content(working_directory, file_path):
    wd_abs = os.path.abspath(working_directory)
    f_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not f_abs.startswith(wd_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(f_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(f_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(f_abs) > 10000:
                return f"{file_content_string} [...File '{file_path}' truncated at 10000 characters]"

            return file_content_string
    except Exception as e:
        return f"Error: An exception occurred: {e}"
