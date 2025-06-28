import os
import subprocess


def run_python_file(working_directory, file_path):
    wd_abs = os.path.abspath(working_directory)
    f_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not f_abs.startswith(wd_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(f_abs):
        return f'Error: File "{file_path}" not found.'

    if not f_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", f_abs], cwd=wd_abs, capture_output=True, text=True, timeout=30
        )

        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode

        output = ""
        if stdout:
            output += f"STDOUT: {stdout}\n"
        if stderr:
            output += f"STDERR: {stderr}\n"
        if return_code != 0:
            output += f"Process exited with code {return_code}\n"

        if not output:
            return "No output produced."
        else:
            return output

    except subprocess.TimeoutExpired:
        return "Error: Process timed out after 30 seconds."
    except Exception as e:
        return f"Error: An exception occurred: {e}"
