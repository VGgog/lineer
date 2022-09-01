from app.service import get_number_of_lines_in_file, get_file_path


def main():
    total_line = 0
    total_files = 0
    for file_path in get_file_path():
        number_of_line = get_number_of_lines_in_file(file_path)
        print(file_path, '->', number_of_line)
        total_line += number_of_line
        total_files += 1

    print('=' * 79)
    print('total files: ', total_files)
    print('total line: ', total_line)
