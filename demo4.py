
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
import os,sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtWidgets import QInputDialog,       QWidget, QListWidgetItem


class Ui_Form(object):
    def browsefolder(self):



        fname=QFileDialog.getOpenFileName(None,'Open File', '', 'All Files (*);;PNG Files (*.png);;jpg Files (*jpg)')
        # fname=QFileDialog.getOpenFileName(None,'Open File', '', 'All Files (*)')

        # fname=QFileDialog.getExistingDirectory(None,'Open File', '/home/infiniteai/Desktop/ro ')

        # self.lineEdit.setText(fname)
 
        self.pixmap = QPixmap(fname[0])
        self.img_label.setPixmap(self.pixmap)
        # print(fname[0])
        a=fname[0]
        global f
        s = f"{a}"
        f=os.path.split(s)[-1]
        print(f)



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 583)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(119, 118, 123);")
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_widget = QtWidgets.QWidget(self.main_widget)
        self.top_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")



        self.lineEdit = QtWidgets.QLineEdit(self.top_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);;")

        self.horizontalLayout_2.addWidget(self.lineEdit)
        
        self.pushButton = QtWidgets.QPushButton(self.top_widget)
        self.pushButton.clicked.connect(self.browsefolder)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);;")
        self.horizontalLayout_2.addWidget(self.pushButton)



        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.top_widget)
        self.bottom_widget = QtWidgets.QWidget(self.main_widget)
        self.bottom_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.main_bottom_widget = QtWidgets.QWidget(self.bottom_widget)
        self.main_bottom_widget.setObjectName("main_bottom_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.main_bottom_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.img_horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.img_horizontalLayout_5.setObjectName("img_horizontalLayout_5")


        self.img_label = QtWidgets.QLabel(self.main_bottom_widget)
        self.img_label.setText("")
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")
        
        self.img_horizontalLayout_5.addWidget(self.img_label)



        self.gridLayout.addLayout(self.img_horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.main_bottom_widget)
        self.verticalLayout.addWidget(self.bottom_widget)
        self.horizontalLayout.addWidget(self.main_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
