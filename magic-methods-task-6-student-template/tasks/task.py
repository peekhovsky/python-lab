import os
import time


class Cd:
    def __init__(self, new_dir):
        self.folder_name = ''
        self.base_dir = ''
        self.new_dir = new_dir

    def __enter__(self):
        self.base_dir = os.getcwd()
        print("Current working directory: ", self.base_dir)

        if not os.path.isdir(self.new_dir):
            raise ValueError("Invalid directory")

        os.chdir(self.new_dir)
        print("New current working directory: ", os.getcwd())

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.base_dir)


if __name__ == '__main__':
    with Cd('temp_dir') as cd:
        file = open('filename', 'w')
        file.write("First Line\n")
        file.write("Second Line")
        file.close()
        time.sleep(2)

    print('exit ctx')
    print("Current working directory: ", os.getcwd())