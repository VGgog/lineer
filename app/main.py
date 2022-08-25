from app.files import FilesInDirectory
from app.counter import LineCounter


def main():
    total_line = 0
    total_files = 0
    print(FilesInDirectory.get_dirs_in_current_dir())
    for file in FilesInDirectory.get_all_files():
        number_of_line = LineCounter.get_number_of_lines_in_file(file)
        print(file, '->', number_of_line)
        total_line += number_of_line
        total_files += 1

    print('=================================================================')
    print('total files: ', total_files)
    print('total line: ', total_line)

