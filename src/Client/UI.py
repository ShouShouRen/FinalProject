# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(429, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(429, 250))
        mainWindow.setMaximumSize(QtCore.QSize(429, 250))
        mainWindow.setAcceptDrops(False)
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(429, 250))
        self.centralwidget.setMaximumSize(QtCore.QSize(429, 250))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 411, 241))
        self.stackedWidget.setMinimumSize(QtCore.QSize(411, 241))
        self.stackedWidget.setMaximumSize(QtCore.QSize(411, 241))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.widget = QtWidgets.QWidget(parent=self.page)
        self.widget.setGeometry(QtCore.QRect(70, 30, 261, 181))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(parent=self.widget)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.login = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.verticalLayout_3.addWidget(self.login)
        self.message = QtWidgets.QLabel(parent=self.widget)
        self.message.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.message.setFont(font)
        self.message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message.setObjectName("message")
        self.verticalLayout_3.addWidget(self.message)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 411, 222))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setMinimumSize(QtCore.QSize(30, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_local = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_local.sizePolicy().hasHeightForWidth())
        self.choose_local.setSizePolicy(sizePolicy)
        self.choose_local.setMinimumSize(QtCore.QSize(198, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.choose_local.setFont(font)
        self.choose_local.setObjectName("choose_local")
        self.horizontalLayout.addWidget(self.choose_local)
        self.upload = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload.sizePolicy().hasHeightForWidth())
        self.upload.setSizePolicy(sizePolicy)
        self.upload.setMinimumSize(QtCore.QSize(197, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.horizontalLayout.addWidget(self.upload)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.local_dir = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local_dir.sizePolicy().hasHeightForWidth())
        self.local_dir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.local_dir.setFont(font)
        self.local_dir.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.local_dir.setDragEnabled(True)
        self.local_dir.setReadOnly(True)
        self.local_dir.setObjectName("local_dir")
        self.verticalLayout.addWidget(self.local_dir)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remote_dir = QtWidgets.QComboBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remote_dir.sizePolicy().hasHeightForWidth())
        self.remote_dir.setSizePolicy(sizePolicy)
        self.remote_dir.setMinimumSize(QtCore.QSize(194, 40))
        self.remote_dir.setObjectName("remote_dir")
        self.horizontalLayout_2.addWidget(self.remote_dir)
        self.download = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy)
        self.download.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.horizontalLayout_2.addWidget(self.download, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.delete_file = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_file.sizePolicy().hasHeightForWidth())
        self.delete_file.setSizePolicy(sizePolicy)
        self.delete_file.setMinimumSize(QtCore.QSize(411, 38))
        self.delete_file.setMaximumSize(QtCore.QSize(411, 38))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delete_file.setFont(font)
        self.delete_file.setObjectName("delete_file")
        self.verticalLayout_2.addWidget(self.delete_file)
        self.stackedWidget.addWidget(self.page_2)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "檔案上下載"))
        self.label.setText(_translate("mainWindow", "帳號:"))
        self.label_2.setText(_translate("mainWindow", "密碼:"))
        self.login.setText(_translate("mainWindow", "登入"))
        self.message.setText(_translate("mainWindow", "None"))
        self.choose_local.setText(_translate("mainWindow", "選取本機檔案"))
        self.upload.setText(_translate("mainWindow", "上傳"))
        self.local_dir.setPlaceholderText(_translate("mainWindow", "選取檔案，並點上傳"))
        self.download.setText(_translate("mainWindow", "下載"))
        self.delete_file.setText(_translate("mainWindow", "刪除"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
