import webview
import os

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, 'dist/index.html')
    window = webview.create_window(
        'test', index_path, resizable=False, width=1000, height=885)
    webview.start()
