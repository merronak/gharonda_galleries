# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full_demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, QScrollArea, QApplication, QPushButton, QHBoxLayout,
                             QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from threading import *
from os import listdir
import os,json

class Ui_Form(object):


#     self.to=window.localStorage.setItem('myapi','['test1', 'test2', 'test3']');

    def fun(self,str_i):
        self.img_btn[str_i].clicked.connect(lambda:self.close(str_i))

    def browsefolder(self):
        
        global rect

        self.screen = app.primaryScreen()

        # print('Screen: %s' % self.screen.name())

        # self.size = size_modelscreen.size()

        # print('Size: %d x %d' % (self.size.width(), self.size.height()))

        rect = self.screen.availableGeometry()
        
        print('Available: %d x %d' % (rect.width(), rect.height()))
        s=int(rect.width()/6)
        se=int(rect.height()/1.7)

        a=os.getcwd()
        # print(a)
        self.rowheight = 230  # the height of one row
        self.labelwidth = s  #
        self.labelheight = se  #

        self.row_picnum = 5 


        # imgName, imgType = QFileDialog.getOpenFileNames(self)
        # print(imgName)

        # global fname
        fname=QFileDialog.getOpenFileNames(None,'Open File', '', 'All Files (*);;PNG Files (*.png);;jpg Files (*jpg)')

        print(fname)
        # self.pixmap = QPixmap(fname[0])
        # self.img_label.setPixmap(self.pixmap)
        # # print(fname[0])
        # a=fname[0]
        # global f
        # s = f"{a}"
        # f=os.path.split(s)[-1]
        # print(f)




        image_address = fname[0]
        # print(image_address)
        # get the number of image
        if image_address is not None:
            total = len(image_address)
        else:
            total = 0

        #  calculate the row number needed

        self.img_btn=[]
        print(total)
        self.label=[]
        for ui in range(0, len(image_address)):
                self.label.append(QLabel)
                self.img_btn.append(QtWidgets.QPushButton(self.btn_widget))


        if total % self.row_picnum == 0:
            rows = int(total / self.row_picnum)
        else:
            rows = int(total / self.row_picnum) + 1

        # display the image one by one
        for i in range(total):
            global str_i
            str_i=i
        

            self.img_btn[i] = QtWidgets.QPushButton(self.btn_widget)
            self.img_btn[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #     self.img_btn.clicked.connect(self.close)
            self.fun(str_i)

            self.img_btn[i].setText('close')
            self.img_btn[i].setStyleSheet("background-color:  rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Poppins SemiBold\";\n"
"white-space: break-spaces;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:9px;\n"
"border-color: rgb(0, 0, 0);\n"
"padding:6px\n"
"")
        #     self.img_btn.setMinimumSize(QtCore.QSize(214, 31))
        #     self.img_btn.setMaximumSize(QtCore.QSize(214, 31))
            self.img_btn[i].setObjectName("img_btn")
            self.horizontalLayout_5.addWidget(self.img_btn[i])
            
            per_picture = image_address[i]
            photo = QPixmap(per_picture)
            width = photo.width()
            height = photo.height()
            tmp_image = photo.toImage()
            size = QSize(width, height)
            photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            
            self.tmp = QWidget(self.bottom_data_widget)
            self.tmp_layout = QHBoxLayout()
            self.tmp.setLayout(self.tmp_layout)
            # self.# use the label to display image
            self.label[i] = QLabel()
            self.label[i].setFixedSize(self.labelwidth, self.labelheight)
            self.label[i].setStyleSheet("border:1px solid gray")  
            self.label[i].setPixmap(photo)
            self.label[i].setScaledContents(True)
            self.horizontalLayout_3.addWidget(self.tmp)
            self.tmp_layout.addWidget(self.label[i])
            self.tmp.move(190 * (i % self.row_picnum), self.rowheight * int(i / self.row_picnum))
            # self.tmp.show()



            self.tmp.move(190 * (i % self.row_picnum), self.rowheight * int(i / self.row_picnum))


    def setupUi(self, Form):
        global rect

        self.screen = app.primaryScreen()

        # print('Screen: %s' % self.screen.name())

        # self.size = size_modelscreen.size()

        # print('Size: %d x %d' % (self.size.width(), self.size.height()))

        rect = self.screen.availableGeometry()
        Form.setObjectName("Form")
        Form.resize(rect.width(), rect.height())
        self.main_gridLayout = QtWidgets.QGridLayout(Form)
        self.main_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_gridLayout.setObjectName("main_gridLayout")
        self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_widget = QtWidgets.QWidget(self.main_widget)
        self.top_widget.setMinimumSize(QtCore.QSize(0, 150))
        self.top_widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.top_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_widget = QtWidgets.QWidget(self.top_widget)
        self.logo_widget.setMinimumSize(QtCore.QSize(307, 150))
        self.logo_widget.setMaximumSize(QtCore.QSize(307, 150))
        self.logo_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo_widget.setAutoFillBackground(False)
        self.logo_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.logo_widget.setObjectName("logo_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.logo_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.logo_widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/14.11.22_Gharonda Galleries_Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.logo_widget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mang_widget = QtWidgets.QWidget(self.top_widget)
        self.mang_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.mang_widget.setObjectName("mang_widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.mang_widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout.addWidget(self.mang_widget)
        self.button_widget = QtWidgets.QWidget(self.top_widget)
        self.button_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.button_widget.setObjectName("button_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.button_widget)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_widget = QtWidgets.QWidget(self.button_widget)
        self.btn_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.btn_widget.setObjectName("btn_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_label = QtWidgets.QLabel(self.btn_widget)
        self.btn_label.setObjectName("btn_label")
        self.horizontalLayout_2.addWidget(self.btn_label)
        self.browse_btn = QtWidgets.QPushButton(self.btn_widget)
        self.browse_btn.clicked.connect(self.browsefolder)
        self.browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_btn.setMinimumSize(QtCore.QSize(214, 31))
        self.browse_btn.setMaximumSize(QtCore.QSize(214, 31))
        self.browse_btn.setStyleSheet("background-color:  rgb(210, 174, 109);\n"
"color: rgb(0, 0, 0);\n"
"font: 63 10pt \"Poppins SemiBold\";\n"
"white-space: break-spaces;\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:9px;\n"
"border-color: rgb(62, 62, 62);\n"
"padding:6px\n"
"")
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout_2.addWidget(self.browse_btn)
        self.gridLayout_4.addWidget(self.btn_widget, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.button_widget)
        self.verticalLayout.addWidget(self.top_widget)
        self.bottom_widget = QtWidgets.QWidget(self.main_widget)
        self.bottom_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_widget.setObjectName("bottom_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_data_widget = QtWidgets.QWidget(self.bottom_widget)
        self.btn_data_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_data_widget.setObjectName("btn_data_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.btn_data_widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.btn_data_widget)
        self.bottom_data_widget = QtWidgets.QWidget(self.bottom_widget)
        self.bottom_data_widget.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.bottom_data_widget.setObjectName("bottom_data_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottom_data_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.bottom_data_widget)
        self.verticalLayout.addWidget(self.bottom_widget)
        self.main_gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def close(self,str_i):
        print(str_i)
        self.label[str_i].hide()
        self.img_btn[str_i].hide()
        # r=[]
        # r=str_i
        # print(r) 
        




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_label.setText(_translate("Form", "Add Project for Compare"))
        self.browse_btn.setText(_translate("Form", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
