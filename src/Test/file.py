from io import BufferedReader
from os.path import dirname, join
from os import listdir
from typing import Literal, Self


class File:
    def __init__(self: Self):
        self.src_dir: str = dirname(dirname(__file__))
        self.data_dir: str = join(self.src_dir, "Data")
        self.uploads_dir: str = join(self.data_dir, "uploads")
        ignored: set[str] = {"uploads"}
        self.files = [x for x in listdir(self.data_dir) if x not in ignored]
        self.run()

    def run(self: Self) -> None:
        # with open(join(self.data_dir, "info.txt"), "rb") as f:
        #     print(f.read())
        self.list_files()
        content: bytes = self.read_file("info.txt")
        self.write_file("test.txt", content)

    def list_files(self: Self) -> None:
        print("\nList Files\n")
        for file in self.files:
            print(file)
        print("\n")

    def read_file(self: Self, file: str, buffer: Literal[-1, 1] = -1) -> bytes:
        file: BufferedReader = open(join(self.data_dir, file,buffer), "rb")
        return file.read()

    def write_file(self: Self, file: str, data: bytes) -> None:
        with open(join(self.uploads_dir, file), "wb") as f:
            f.write(data)
        print("\n")
