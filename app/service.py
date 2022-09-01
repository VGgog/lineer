import os
from typing import Iterator


def get_number_of_lines_in_file(file_path: str) -> int:
    """get the number of lines in a file"""
    with open(file_path) as file:
        return len(file.readlines())


def get_file_path() -> Iterator[str]:
    """iterates the path to all files in a directory"""
    for address, dirs, files in os.walk('.'):
        if 'venv' in dirs:
            dirs.remove('venv')

        for file_name in files:
            if file_name.endswith('.py'):
                yield os.path.join(address, file_name)
