import sys,os
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, QScrollArea, QApplication, QPushButton, QHBoxLayout,
                             QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from threading import *
from os import listdir

class Picture(QWidget):

    def ae(self):
        # self.tmp2.hide()
        print('hi')

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.mywidth = pwidth
        # self.myheight = pheight
        self.rowheight = 230  # the height of one row
        self.labelwidth = 1920  #
        self.labelheight = 1080  #
        self.row_picnum = 5  #  the number of picture displayed per row

        # self.setFixedSize(pwidth, pheight)
        layout = QGridLayout()
        self.setLayout(layout)

        # init the display area
        self.sc = QScrollArea(self)
        self.sc_layout = QHBoxLayout()
        self.sc.setLayout(self.sc_layout)
        # self.sc.setMinimumSize(self.mywidth, self.myheight)
        btn = QPushButton(self)
        btn.setText('ok')
        btn.clicked.connect(self.showimage)
        layout.addWidget(self.sc, 1, 0)
        layout.addWidget(btn, 0, 0)
    


    def showimage(self):
        imgName, imgType = QFileDialog.getOpenFileNames(self)
        print(imgName)



#####################################################################################################################################################        # global f

        # s = f"{imgName}"
        # f=os.path.split(s)[-1]
        # print(f)

#####################################################################################################################################################
        # for images in os.listdir(imgName):
 

        #     if (images.endswith(".png") or images.endswith(".jpg")
        #         or images.endswith(".jpeg")):
        #         print(images,'*******************')

#####################################################################################################################################################





        image_address = imgName
        # get the number of image
        if image_address is not None:
            total = len(image_address)
        else:
            total = 0

        #  calculate the row number needed
        print(total)
        if total % self.row_picnum == 0:
            rows = int(total / self.row_picnum)
        else:
            rows = int(total / self.row_picnum) + 1

        # display the image one by one
        for i in range(total):
            # set the image
            per_picture = image_address[i]
            photo = QPixmap(per_picture)
            width = photo.width()
            height = photo.height()
            tmp_image = photo.toImage()
            size = QSize(width, height)
            photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            tmp = QWidget(self)
            tmp_layout = QVBoxLayout()
            tmp.setLayout(tmp_layout)
            # use the label to display image


            pushButton = QPushButton()
            # pushButton.setFixedSize(self.labelwidth)
            pushButton.clicked.connect(self.ae)
            pushButton.setText('close')
            pushButton.setObjectName("pushButton")
            tmp_layout.addWidget(pushButton)

            label = QLabel()
            label.setFixedSize(self.labelwidth, self.labelheight)
            label.setStyleSheet("border:1px solid gray")  
            label.setPixmap(photo)
            # label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignCenter)
            # label.setScaledContents(True)
            label.setScaledContents(True)
            self.sc_layout.addWidget(tmp)
            tmp_layout.addWidget(label)



            tmp.move(190 * (i % self.row_picnum), self.rowheight * int(i / self.row_picnum))


            # pushButton.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignCenter)
            # horizontalLayout_2.addWidget(self.pushButton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pic = Picture()
    pic.show()
    sys.exit(app.exec_())
