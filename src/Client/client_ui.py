import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic

from os.path import dirname, join, splitext
import grpc
from proto import hello_pb2_grpc, hello_pb2
from Utils.parser import Parser


class Client:
    def __init__(self, server_address: str):
        """
        初始化客戶端類，設定 gRPC 服務端位址並建立連線。
        """
        self.server_address = server_address
        self.channel = None
        self.client = None
        self.src_dir: str = dirname(dirname(__file__))
        self.data_dir: str = join(self.src_dir, "Data")
        self.uploads_dir: str = join(self.data_dir, "uploads")
        self.downloads_dir: str = join(self.data_dir, "downloads")

    def connect(self, timeout=5):
        """
        建立與 gRPC 伺服器的連接，等待通道準備好後返回。
        """
        try:
            self.channel = grpc.insecure_channel(self.server_address)
            grpc.channel_ready_future(self.channel).result(timeout=timeout)
            self.client = hello_pb2_grpc.GreeterStub(self.channel)
            print(f"Connected to gRPC server at {self.server_address}")
        except grpc.FutureTimeoutError:
            print(f"Failed to connect to gRPC server at {
                  self.server_address} (timeout after {timeout} seconds)")
            sys.exit(1)
        except grpc.RpcError as e:
            print(f"Failed to connect to gRPC server: {e.details()}")
            sys.exit(1)

    @staticmethod
    def get_filepath(filename: str, extension: str) -> str:
        return f'{filename}{extension}'

    @staticmethod
    def read_to_iter(file_path: str, chunk_size: int = 1024):
        """
        讀取文件並生成上傳流。
        :parm file_path: 文件路徑
        :parm chunk_size: 塊大小
        """
        split_data = splitext(file_path.split('/')[-1])
        filename = split_data[0]
        extension = split_data[1]
        metadata = hello_pb2.MetaData(filename=filename, extension=extension)
        yield hello_pb2.UploadFileRequest(metadata=metadata)
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    entry_request = hello_pb2.UploadFileRequest(
                        chunk_data=chunk)
                    yield entry_request
                else:
                    break

    def upload_file(self, file_path: str, chunk_size: int = 1024) -> hello_pb2.StringResponse:
        """
        上傳文件。

        :param file_path: 文件路徑
        :param chunk_size: 塊大小
        :return: 上傳結果
        :rtype: hello_pb2.StringResponse
        """
        ret = self.client.UploadFile(self.read_to_iter(file_path, chunk_size))
        print("Client Receive: " + ret.message)
        return ret

    def download_file(self, filename: str, extension: str):
        """
        下載文件。
        :param filename: 文件名
        :param extension: 文件擴展名
        :param chunk_size: 塊大小
        """
        response = self.client.DownloadFile(
            hello_pb2.MetaData(filename=filename, extension=extension))
        filename = self.get_filepath(filename, extension)
        for data in response:
            with open(join(self.downloads_dir, filename), mode="ab") as f:
                f.write(data.chunk_data)
        print("Client Receive: Download Complete")

    def close(self):
        """
        關閉連接。
        """
        if self.channel:
            self.channel.close()
            print("Connection closed.")


class MyWindow(QMainWindow):
    def __init__(self, args: list[str]):
        super().__init__()
        uipath = join(dirname(__file__), 'client.ui')
        uic.loadUi(uipath, self)
        self.choose_local.clicked.connect(self.on_ChooseLocal_clicked)
        self.upload.clicked.connect(self.on_Upload_clicked)
        self.selected_file = None
        self.args = args
        connect_address = Parser(self.args).connect_address()
        self.client = Client(connect_address)
        self.client.connect()

    def on_ChooseLocal_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, '選擇文件', '', '所有文件 (*)')
        if file_name:
            print(f"你選擇的文件: {file_name}")
            self.local_dir.setText(file_name)
            self.selected_file = file_name

    def on_Upload_clicked(self):
        if not self.selected_file:
            print("No file selected.")
        else:
            try:
                self.client.upload_file(self.selected_file)
                self.local_dir.setText("上傳成功")
                # client.download_file("info", ".txt")
            except grpc.RpcError as e:
                print(f"RPC Error: {e.details()}")
                self.local_dir.setText("上傳失敗")
    # 關閉前關閉連接

    def closeEvent(self, event):
        self.client.close()
        event.accept()


def client_ui(args: list[str]):
    app = QApplication(sys.argv)
    window = MyWindow(args)
    window.show()
    sys.exit(app.exec())
