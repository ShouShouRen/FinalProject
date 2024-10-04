import webview
import os
import json


class Api:
    def __init__(self, base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
        self.base_dir = base_dir
        self.server_upload_dir = os.path.join(base_dir, "Data/uploads")
        self.local_storage_dir = os.path.join(base_dir, "Data/localStorage")
        self.client_download_dir = os.path.join(
            self.local_storage_dir, "downloads")

        # 將目錄名稱映射到具體的路徑
        self.path_mapping = {
            "uploads": self.server_upload_dir,
            "downloads": self.client_download_dir,
            "localStorage": self.local_storage_dir
        }

    def get_children(self, path: str) -> str:
        print(path)
        if path in self.path_mapping:
            full_path = self.path_mapping[path]
        else:
            found = False
            for root, root_path in self.path_mapping.items():
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


if __name__ == '__main__':
    api = Api()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, 'dist/index.html')
    window = webview.create_window(
        'test', index_path, js_api=api, resizable=False, width=1000, height=885)
    webview.start(debug=True)
