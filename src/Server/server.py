# from concurrent import futures
# import random
# import grpc
# from proto.recommendations_pb2 import BookCategory, BookRecommendation, RecommendationResponse
# from proto.recommendations_pb2_grpc import RecommendationsServicer, add_RecommendationsServicer_to_server


# class RecommendationService(RecommendationsServicer):
#     def Recommend(self, request, context):
#         if request.category not in books_by_category:
#             context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

#         books_for_category = books_by_category[request.category]
#         num_results = min(request.max_results, len(books_for_category))
#         books_to_recommend = random.sample(
#             books_for_category, num_results
#         )

#         return RecommendationResponse(recommendations=books_to_recommend)


# books_by_category = {
#     BookCategory.MYSTERY: [
#         BookRecommendation(id=1, title="The Maltese Falcon"),
#         BookRecommendation(id=2, title="Murder on the Orient Express"),
#         BookRecommendation(id=3, title="The Hound of the Baskervilles"),
#     ],
#     BookCategory.SCIENCE_FICTION: [
#         BookRecommendation(
#             id=4, title="The Hitchhiker's Guide to the Galaxy"
#         ),
#         BookRecommendation(id=5, title="Ender's Game"),
#         BookRecommendation(id=6, title="The Dune Chronicles"),
#     ],
#     BookCategory.SELF_HELP: [
#         BookRecommendation(
#             id=7, title="The 7 Habits of Highly Effective People"
#         ),
#         BookRecommendation(
#             id=8, title="How to Win Friends and Influence People"
#         ),
#         BookRecommendation(id=9, title="Man's Search for Meaning"),
#     ],
# }

# # 將剛剛實作完的service架起來


# def server(args: list[str]):
#     host: str = '[::]'
#     port: str = "50051"
#     if len(args) == 1:
#         import json
#         data: dict[str, str] = json.loads(args[0])
#         if 'host' in data:
#             host = data['host']
#         if 'port' in data:
#             port = data['port']
#     connect_address: str = f"{host}:{port}"

#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     add_RecommendationsServicer_to_server(
#         RecommendationService(), server
#     )
#     print(f"Server start at {connect_address}")
#     server.add_insecure_port(connect_address)
#     server.start()
#     server.wait_for_termination()

from concurrent import futures
import os
import grpc
from proto import hello_pb2, hello_pb2_grpc


def get_filepath(filename: str, extension: str) -> str:
    return f"{filename}{extension}"


class Greeter(hello_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.src_dir: str = os.path.dirname(os.path.dirname(__file__))
        self.data_dir: str = os.path.join(self.src_dir, "Data")
        self.uploads_dir: str = os.path.join(self.data_dir, "uploads")
        self.chunk_size: int = 1024

    def SayHello(self, request, context):
        return hello_pb2.StringResponse(message=f'Hello, {request.name}! Your age is {request.age}')

    def UploadFile(self, request_iterator, context):
        data: bytearray = bytearray()
        for request in request_iterator:
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(
                    request.metadata.filename, request.metadata.extension)
                continue
            data.extend(request.chunk_data)
        with open(os.path.join(self.uploads_dir, filepath), 'wb') as file:
            file.write(data)
        return hello_pb2.StringResponse(message=f'File {filepath} uploaded.')

    def DownloadFile(self, request, context):

        filepath = get_filepath(request.filename, request.extension)
        if os.path.exists(os.path.join(self.uploads_dir, filepath)):
            with open(os.path.join(self.uploads_dir, filepath), 'rb') as file:
                while True:
                    chunk = file.read(self.chunk_size)
                    if chunk:
                        yield hello_pb2.FileResponse(chunk_data=chunk)
                    else:
                        return


def server(args: list[str]):
    host: str = '[::]'
    port: str = "50051"
    if len(args) == 1:
        import json
        data: dict[str, str] = json.loads(args[0])
        if 'host' in data:
            host = data['host']
        if 'port' in data:
            port = data['port']
    connect_address: str = f"{host}:{port}"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    print(f"Server start at {connect_address}")
    server.add_insecure_port(connect_address)
    server.start()
    server.wait_for_termination()
