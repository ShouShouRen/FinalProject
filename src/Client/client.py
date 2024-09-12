# import grpc
# from proto.recommendations_pb2 import BookCategory, RecommendationRequest
# from proto.recommendations_pb2_grpc import RecommendationsStub
# import sys
# from grpc import FutureTimeoutError


# class RecommendationClient:
#     def __init__(self, server_address):
#         """
#         初始化客戶端類，設定 gRPC 服務端位址並建立連線。
#         """
#         self.server_address = server_address
#         self.channel = None
#         self.client = None

#     def connect(self, timeout=5):
#         """
#         建立與 gRPC 伺服器的連接，等待通道準備好後返回。
#         """
#         try:
#             self.channel = grpc.insecure_channel(self.server_address)
#             grpc.channel_ready_future(self.channel).result(timeout=timeout)
#             self.client = RecommendationsStub(self.channel)
#             print(f"Connected to gRPC server at {self.server_address}")
#         except FutureTimeoutError:
#             print(f"Failed to connect to gRPC server at {
#                   self.server_address} (timeout after {timeout} seconds)")
#             sys.exit(1)
#         except grpc.RpcError as e:
#             print(f"Failed to connect to gRPC server: {e.details()}")
#             sys.exit(1)

#     def get_recommendations(self, user_id, category, max_results):
#         """
#         發起推薦請求並傳回結果。

#         :param user_id: 用戶 ID
#         :param category: 圖書類別
#         :param max_results: 最大返回數量
#         :return: 推薦結果
#         """
#         request = RecommendationRequest(
#             user_id=user_id,
#             category=category,
#             max_results=max_results
#         )
#         return self.client.Recommend(request)

#     def close(self):
#         """
#         關閉連接。
#         """
#         if self.channel:
#             self.channel.close()
#             print("Connection closed.")


# # if __name__ == "__main__":
# def client(args: list[str]):
#     host: str = 'localhost'
#     port: str = "50051"
#     if len(args) == 1:
#         import json
#         data: dict[str, str] = json.loads(args[0])
#         if 'host' in data:
#             host = data['host']
#         if 'port' in data:
#             port = data['port']
#     connect_address: str = f"{host}:{port}"
#     client = RecommendationClient(connect_address)
#     client.connect()
#     try:
#         response = client.get_recommendations(
#             user_id=1,
#             category=BookCategory.SCIENCE_FICTION,
#             max_results=3
#         )
#         print(response)
#     finally:
#         client.close()

import os
import grpc
from proto import hello_pb2_grpc, hello_pb2


def read_iterfile(file_path: str, chunk_size: int = 1024):
    split_data = os.path.splitext(file_path.split('/')[-1])
    filename = split_data[0]
    extension = split_data[1]
    metadata = hello_pb2.MetaData(filename=filename, extension=extension)
    print(f'{filename=}, {extension=}')
    yield hello_pb2.UploadFileRequest(metadata=metadata)
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                entry_request = hello_pb2.UploadFileRequest(chunk_data=chunk)
                yield entry_request
            else:  # The chunk was empty, which means we're at the end of the file
                break


def get_filepath(filename, extension):
    return f'{filename}{extension}'


def client(args: list[str]):
    host: str = 'localhost'
    port: str = "50051"
    if len(args) == 1:
        import json
        data: dict[str, str] = json.loads(args[0])
        if 'host' in data:
            host = data['host']
        if 'port' in data:
            port = data['port']
    connect_address: str = f"{host}:{port}"
    with grpc.insecure_channel(connect_address) as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='you', age=18))
        print("Greeter client received: " + response.message)
        src_dir: str = os.path.dirname(os.path.dirname(__file__))
        data_dir: str = os.path.join(src_dir, "Data")
        uploads_dir: str = os.path.join(data_dir, "uploads")
        downloads_dir: str = os.path.join(data_dir, "downloads")
        ret = stub.UploadFile(read_iterfile(
            os.path.join(data_dir, "info.txt")))
        # read_iterfile(
        #     os.path.join(data_dir, "info.txt"))
        print("Greeter client received: " + ret.message)

        filename = 'info'
        extension = '.txt'
        filepath = get_filepath(filename, extension)
        for entry_response in stub.DownloadFile(hello_pb2.MetaData(filename=filename, extension=extension)):
            with open(os.path.join(downloads_dir, filepath), mode="ab") as f:
                f.write(entry_response.chunk_data)
            # print(entry_response)
