import grpc
from proto.recommendations_pb2 import BookCategory, RecommendationRequest
from proto.recommendations_pb2_grpc import RecommendationsStub
import sys
from grpc import FutureTimeoutError


class RecommendationClient:
    def __init__(self, server_address):
        """
        初始化客戶端類，設定 gRPC 服務端位址並建立連線。
        """
        self.server_address = server_address
        self.channel = None
        self.client = None

    def connect(self, timeout=5):
        """
        建立與 gRPC 伺服器的連接，等待通道準備好後返回。
        """
        try:
            self.channel = grpc.insecure_channel(self.server_address)
            grpc.channel_ready_future(self.channel).result(timeout=timeout)
            self.client = RecommendationsStub(self.channel)
            print(f"Connected to gRPC server at {self.server_address}")
        except FutureTimeoutError:
            print(f"Failed to connect to gRPC server at {
                  self.server_address} (timeout after {timeout} seconds)")
            sys.exit(1)
        except grpc.RpcError as e:
            print(f"Failed to connect to gRPC server: {e.details()}")
            sys.exit(1)

    def get_recommendations(self, user_id, category, max_results):
        """
        發起推薦請求並傳回結果。

        :param user_id: 用戶 ID
        :param category: 圖書類別
        :param max_results: 最大返回數量
        :return: 推薦結果
        """
        request = RecommendationRequest(
            user_id=user_id,
            category=category,
            max_results=max_results
        )
        return self.client.Recommend(request)

    def close(self):
        """
        關閉連接。
        """
        if self.channel:
            self.channel.close()
            print("Connection closed.")


# if __name__ == "__main__":
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
    client = RecommendationClient(connect_address)
    client.connect()
    try:
        response = client.get_recommendations(
            user_id=1,
            category=BookCategory.SCIENCE_FICTION,
            max_results=3
        )
        print(response)
    finally:
        client.close()
