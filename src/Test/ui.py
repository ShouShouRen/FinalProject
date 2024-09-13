# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
# import sys

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("PyQt6 文件选择示例")

#         # 创建按钮
#         self.button = QPushButton("选择文件")

#         # 连接按钮的点击信号到回调函数
#         self.button.clicked.connect(self.open_file_dialog)

#         # 设置布局
#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#     # 定义回调函数
#     def open_file_dialog(self):
#         # 打开文件选择对话框
#         file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*)")

#         if file_name:
#             print(f"您选择的文件是：{file_name}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog
# import sys

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("选择列表项示例")

#         # 创建按钮
#         self.button = QPushButton("选择项目")
#         self.button.clicked.connect(self.show_item_dialog)

#         # 设置布局
#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#     def show_item_dialog(self):
#         items = ["苹果", "香蕉", "橘子", "葡萄"]
#         item, ok = QInputDialog.getItem(self, "选择水果", "请选择一种水果：", items, 0, False)

#         if ok and item:
#             print(f"您选择了：{item}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QDialog, QDialogButtonBox
# import sys


# class ListDialog(QDialog):
#     def __init__(self, items):
#         super().__init__()

#         self.setWindowTitle("选择项目")
#         self.selected_items = []

#         # 创建列表部件
#         self.list_widget = QListWidget()
#         self.list_widget.addItems(items)
#         self.list_widget.setSelectionMode(
#             QListWidget.SelectionMode.MultiSelection)  # 设置为多选

#         # 创建按钮盒
#         self.button_box = QDialogButtonBox(
#             QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
#         self.button_box.accepted.connect(self.accept)
#         self.button_box.rejected.connect(self.reject)

#         # 设置布局
#         layout = QVBoxLayout()
#         layout.addWidget(self.list_widget)
#         layout.addWidget(self.button_box)
#         self.setLayout(layout)

#     def accept(self):
#         self.selected_items = [item.text()
#                                for item in self.list_widget.selectedItems()]
#         super().accept()


# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("自定义对话框示例")

#         # 创建按钮
#         self.button = QPushButton("选择项目")
#         self.button.clicked.connect(self.show_list_dialog)

#         # 设置布局
#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#     def show_list_dialog(self):
#         items = ["苹果", "香蕉", "橘子", "葡萄"]
#         dialog = ListDialog(items)
#         if dialog.exec():
#             print("您选择了：")
#             for item in dialog.selected_items:
#                 print(item)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox 示例")

        # 创建下拉列表
        self.combo_box = QComboBox()
        self.combo_box.addItems(["苹果", "香蕉", "橘子", "葡萄"])
        self.combo_box.currentIndexChanged.connect(self.selection_changed)

        # 显示选择结果的标签
        self.label = QLabel("请选择一种水果")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selection_changed(self, index):
        item = self.combo_box.currentText()
        self.label.setText(f"您选择了：{item}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
