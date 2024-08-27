import os
import shutil
import random
import string
import time


def get_folder_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


class TempDir:
    def __init__(self):
        self.folder_name = ''
        self.base_dir = ''

    def __enter__(self):
        self.base_dir = os.getcwd()
        print("Current working directory: ", self.base_dir)

        while True:
            folder_name = get_folder_name()
            if not os.path.exists(folder_name):
                break

        os.mkdir(folder_name)
        self.folder_name = folder_name

        os.chdir(folder_name)

        print("New current working directory: ", os.getcwd())
        return folder_name

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.base_dir)
        shutil.rmtree(self.folder_name)


if __name__ == '__main__':
    with TempDir() as temp_dir:
        file = open('filename', 'w')
        file.write("First Line\n")
        file.write("Second Line")
        file.close()
        time.sleep(2)

    print('exit ctx')
    print("Current working directory: ", os.getcwd())