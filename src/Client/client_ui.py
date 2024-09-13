import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic

from os.path import dirname, join, splitext
import grpc
from proto import hello_pb2_grpc, hello_pb2
from Utils.parser import Parser
from google.protobuf import empty_pb2


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

    def list_files(self):
        """
        列出文件。
        """
        response = self.client.ListFiles(empty_pb2.Empty())
        return response.files

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

    def delete_file(self, filename: str, extension: str):
        """
        刪除文件。
        :param filename: 文件名
        :param extension: 文件擴展名
        """
        response = self.client.DeleteFile(
            hello_pb2.MetaData(filename=filename, extension=extension))
        print("Client Receive: " + response.message)

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
        self.login.clicked.connect(self.on_Login_clicked)
        self.choose_local.clicked.connect(self.on_ChooseLocal_clicked)
        self.upload.clicked.connect(self.on_Upload_clicked)
        self.selected_file = None
        self.args = args
        self.stackedWidget.setCurrentIndex(0)
        self.message.hide()
        connect_address = Parser(self.args).connect_address()
        self.client = Client(connect_address)
        self.client.connect()
        self.file_reload()
        self.remote_dir.setCurrentIndex(0)
        self.selected_file1 = self.remote_dir.currentText()
        self.remote_dir.mousePressEvent = self.create_mouse_press_event_handler(
            self.remote_dir.mousePressEvent)
        self.remote_dir.currentIndexChanged.connect(self.on_file_selected)
        self.download.clicked.connect(self.on_Download_clicked)
        self.delete_file.clicked.connect(self.on_Delete_clicked)

    def reset(self):
        self.selected_file = None
        self.selected_file1 = None

    def create_mouse_press_event_handler(self, original_event_handler):
        def new_mouse_press_event(event):
            self.file_reload()
            original_event_handler(event)
        return new_mouse_press_event

    def file_reload(self):
        self.selected_file1 = self.remote_dir.currentText()
        self.remote_dir.blockSignals(True)
        self.remote_dir.clear()
        files = self.client.list_files()
        self.remote_dir.addItems([file for file in files])
        if self.selected_file1:
            index = self.remote_dir.findText(self.selected_file1)
            if index >= 0:
                self.remote_dir.setCurrentIndex(index)
        self.remote_dir.blockSignals(False)

    def on_Login_clicked(self):
        username = self.username.text()
        password = self.password.text()

        if username == 'admin' and password == 'password':
            self.stackedWidget.setCurrentIndex(1)
        else:
            print("Invalid username or password!")
            self.message.show()
            self.message.setText("無效的用戶名或密碼")

    def on_ChooseLocal_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, '選擇文件', '', '所有文件 (*)')
        if file_name:
            self.local_dir.setText(file_name)
            self.selected_file = file_name

    def on_Upload_clicked(self):
        if not self.selected_file:
            print("No file selected.")
            self.local_dir.setText("未選擇文件")
        else:
            try:
                self.client.upload_file(self.selected_file)
                self.local_dir.setText("上傳成功")
                self.file_reload()
            except grpc.RpcError as e:
                print(f"RPC Error: {e.details()}")
                self.local_dir.setText("上傳失敗")
        self.selected_file = None
        self.selected_file1 = self.remote_dir.currentText()

    def on_file_selected(self):
        self.selected_file1 = self.remote_dir.currentText()
        print(f"Selected file: {self.selected_file1}")

    def on_Download_clicked(self):

        if not self.selected_file1:
            print("No file selected.")
            self.local_dir.setText("沒有文件可以下載")
        else:
            try:
                self.client.download_file(*splitext(self.selected_file1))
                self.local_dir.setText("下載成功")
            except grpc.RpcError as e:
                print(f"RPC Error: {e.details()}")
                self.local_dir.setText("下載失敗")

    def on_Delete_clicked(self):
        if not self.selected_file1:
            print("No file selected.")
            self.local_dir.setText("沒有文件可以刪除")
        else:
            try:
                self.client.delete_file(*splitext(self.selected_file1))
                self.local_dir.setText("刪除成功")
                self.file_reload()
                self.remote_dir.setCurrentIndex(0)
                self.selected_file1 = self.remote_dir.currentText()
            except grpc.RpcError as e:
                print(f"RPC Error: {e.details()}")
                self.local_dir.setText("刪除失敗")

    # 關閉前關閉連接
    def closeEvent(self, event):
        self.client.close()
        event.accept()


def client_ui(args: list[str]):
    app = QApplication(sys.argv)
    window = MyWindow(args)
    window.show()
    sys.exit(app.exec())
