from globals import *
import os

def process_file_list() -> None:
    res = ""
    if len(my_files) == 0:
        return info("No file added")
    res += "[{}{}{}] file added :\n".format(c.lgrn, len(my_files), c.r)
    for i in range(len(my_files)):
        res += f"{c.unde}{i + 1}{c.r}. " + my_files[i] + "\n"
    return nprint(res)


def process_file(command: str) -> None:
    if (len(command) == 3 and command[2] == '?'):
        return process_file_list()
    command = command[2:]
    if not os.path.exists(command):
        return warn(f"The file '{command}' do not exist.")
    if not os.path.isfile(command):
        return warn(f"The instance needs to be a file.")
    if command in my_files:
        info("{} Removed".format(command))
        my_files.remove(command)
    else:
        info("{} Added".format(command))
        my_files.append(command)