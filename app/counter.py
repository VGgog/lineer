class LineCounter:

    @staticmethod
    def get_number_of_lines_in_file(file_path: str) -> int:
        with open(file_path) as file:
            return len(file.readlines())
