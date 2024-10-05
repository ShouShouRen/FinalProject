import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
# from PyQt6 import uic
from .UI import Ui_mainWindow

from os.path import splitext
import grpc
from Utils.parser import Parser


class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, args: list[str]):
        super().__init__()
        from .client import Client
        self.setupUi(self)
        # uipath = join(dirname(__file__), 'client.ui')
        # uic.loadUi(uipath, self)
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
