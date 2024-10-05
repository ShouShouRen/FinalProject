from concurrent import futures
import grpc
from proto import hello_pb2, hello_pb2_grpc
from Utils.parser import Parser

from os.path import dirname, join, splitext, exists
from os import remove, listdir, makedirs

def get_filepath(filename: str, extension: str) -> str:
    return f"{filename}{extension}"


class Greeter(hello_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.src_dir: str = dirname(dirname(__file__))
        self.data_dir: str = join(self.src_dir, "Data")
        self.uploads_dir: str = join(self.data_dir, "uploads")
        self.chunk_size: int = 1024

        makedirs(self.uploads_dir, exist_ok=True)

    def UploadFile(self, request_iterator, context):
        data: bytearray = bytearray()
        for request in request_iterator:
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(
                    request.metadata.filename, request.metadata.extension)
                continue
            data.extend(request.chunk_data)
        with open(join(self.uploads_dir, filepath), 'wb') as file:
            file.write(data)
        return hello_pb2.StringResponse(message=f'File {filepath} uploaded.')

    def DownloadFile(self, request, context):

        filepath = get_filepath(request.filename, request.extension)
        if exists(join(self.uploads_dir, filepath)):
            with open(join(self.uploads_dir, filepath), 'rb') as file:
                while True:
                    chunk = file.read(self.chunk_size)
                    if chunk:
                        yield hello_pb2.FileResponse(chunk_data=chunk)
                    else:
                        return
    def ListFiles(self, request, context):
        files = listdir(self.uploads_dir)
        return hello_pb2.FileList(files=files)
    def DeleteFile(self, request, context):
        filepath = get_filepath(request.filename, request.extension)
        if exists(join(self.uploads_dir, filepath)):
            remove(join(self.uploads_dir, filepath))
            return hello_pb2.StringResponse(message=f'File {filepath} deleted.')
        return hello_pb2.StringResponse(message=f'File {filepath} not found.')
    def Login(self, request, context):
        if request.username == "admin" and request.password == "admin":
            return hello_pb2.StringResponse(message="Login successful")
        return hello_pb2.StringResponse(message="Login failed. Incorrect username or password")

def server(args: list[str]):
    connect_address = Parser(args).connect_address()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    print(f"Server start at {connect_address}")
    server.add_insecure_port(connect_address)
    server.start()
    server.wait_for_termination()
