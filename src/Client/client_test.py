from typing import NoReturn
import webview
import os
import json

from Utils.parser import Parser


class Api:
    def __init__(self, args: list[str], base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
        from .client import Client
        self.client_obj = Client
        self.base_dir = base_dir
        self.server_upload_dir = os.path.join(base_dir, "Data/uploads")
        self.local_storage_dir = os.path.join(base_dir, "Data/localStorage")
        self.client_download_dir = os.path.join(
            self.local_storage_dir, "downloads")

        self.path_mapping = {
            "uploads": self.server_upload_dir,
            "downloads": self.client_download_dir,
            "localStorage": self.local_storage_dir
        }
        self.isLogin = False

        # self.connect_address = Parser(args).connect_address()
        self.client = None

    def login(self, host: str, port: str, username: str, password: str) -> str:
        self.client = self.client_obj(f"{host}:{port}")
        if self.isLogin:
            return json.dumps({"message": "Already logged in"})
        self.isConnected = self.client.connect()
        if not self.isConnected:
            return json.dumps({"error": "Connection failed"})
        self.isLogin = self.client.login(username, password)
        if not self.isLogin:
            return json.dumps({"error": "Login failed"})
        return json.dumps({"message": "Login successful"})

    def upload_file(self, file_path: str) -> str:
        pass

    def download_file(self, file_path: str) -> str:
        pass

    def delete_file(self, file_path: str) -> str:
        pass

    def close(self) -> str:
        if self.isLogin:
            self.client.close()
            self.isLogin = False
        return json.dumps({"message": "Connection closed"})

    def get_local_children(self, path: str) -> str:
        if path in self.path_mapping:
            full_path = self.path_mapping[path]
        else:
            found = False
            for _, root_path in self.path_mapping.items():
                if path.startswith(root_path):
                    full_path = path
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Invalid path or path not under allowed directories"})
        try:
            children = []
            for entry in os.listdir(full_path):
                entry_path = os.path.join(full_path, entry)
                is_leaf = not os.path.isdir(entry_path)
                children.append({
                    "title": entry,
                    "key": entry_path,
                    "isLeaf": is_leaf
                })
            return json.dumps(children)
        except Exception as e:
            return json.dumps({"error": str(e)})

    def get_server_children(self, path: str) -> str:
        pass


def client_test(args: list[str]) -> NoReturn:
    api = Api(args)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, 'dist/index.html')
    webview.create_window(
        'File Uploader', index_path, js_api=api, resizable=True, width=1000, height=885)
    webview.start(debug=True)
