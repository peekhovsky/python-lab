from contextlib import ContextDecorator
import os
import time
import datetime


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.start_time = None

    def __enter__(self):
        self.base_dir = os.getcwd()
        print("Current working directory: ", self.base_dir)

        self.file = open(self.filename, 'a')
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        end_time = datetime.datetime.now()
        run_time = end_time - self.start_time

        msg = f"Start: {self.start_time} | Run: {run_time} | An error occurred: {exc_value}\n"

        self.file.write(msg)
        self.file.close()


@LogFile("log.txt")
def func():
    print('Started')
    file = open('filename', 'w')
    file.write("First Line\n")
    file.write("Second Line")
    file.close()
    time.sleep(2)


if __name__ == '__main__':
    func()
    print('exit ctx')
    print("Current working directory: ", os.getcwd())
