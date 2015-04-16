# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eric6\magnet\main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 355)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label.setObjectName("label")
        self.lineEditUrl = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditUrl.setGeometry(QtCore.QRect(70, 20, 531, 20))
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.textBrowserMagnet = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowserMagnet.setGeometry(QtCore.QRect(30, 50, 631, 271))
        self.textBrowserMagnet.setObjectName("textBrowserMagnet")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 20, 51, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBarDisplay = QtWidgets.QStatusBar(MainWindow)
        self.statusBarDisplay.setObjectName("statusBarDisplay")
        MainWindow.setStatusBar(self.statusBarDisplay)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "网址："))
        self.pushButton.setText(_translate("MainWindow", "开始"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

