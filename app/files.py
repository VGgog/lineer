import os


class FilesInDirectory:

    @staticmethod
    def get_all_files() -> list:
        all_files = []
        for address, dirs, files in os.walk('.'):
            if 'venv' in dirs:
                dirs.remove('venv')
            for name in files:
                all_files.append(os.path.join(address, name))
                if name.endswith('.py'):
                    yield os.path.join(address, name)
    
    @staticmethod 
    def get_dirs_in_current_dir():
        return os.listdir()

    def get_files() -> list:
        dirs = os.listdir()
        if not dirs:
            ...

        return files 
