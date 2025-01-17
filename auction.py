# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auction.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 601, 501))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("background.png"))
        self.bg.setObjectName("bg")
        self.bid = QtWidgets.QPushButton(Form)
        self.bid.setGeometry(QtCore.QRect(410, 440, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bid.setFont(font)
        self.bid.setStyleSheet("background-color:rgb(115, 102, 84); color: rgb(219, 195, 160)\n"
"")
        self.bid.setDefault(False)
        self.bid.setObjectName("bid")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 440, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.name1 = QtWidgets.QLabel(Form)
        self.name1.setGeometry(QtCore.QRect(30, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setStyleSheet("background-color:rgb(219, 195, 160)")
        self.name1.setText("")
        self.name1.setAlignment(QtCore.Qt.AlignCenter)
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QLabel(Form)
        self.name2.setGeometry(QtCore.QRect(170, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setStyleSheet("background-color:rgb(219, 195, 160)")
        self.name2.setText("")
        self.name2.setAlignment(QtCore.Qt.AlignCenter)
        self.name2.setObjectName("name2")
        self.name4 = QtWidgets.QLabel(Form)
        self.name4.setGeometry(QtCore.QRect(450, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name4.setFont(font)
        self.name4.setStyleSheet("background-color:rgb(219, 195, 160)")
        self.name4.setText("")
        self.name4.setAlignment(QtCore.Qt.AlignCenter)
        self.name4.setObjectName("name4")
        self.name3 = QtWidgets.QLabel(Form)
        self.name3.setGeometry(QtCore.QRect(310, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name3.setFont(font)
        self.name3.setStyleSheet("background-color:rgb(219, 195, 160)")
        self.name3.setText("")
        self.name3.setAlignment(QtCore.Qt.AlignCenter)
        self.name3.setObjectName("name3")
        self.pic1 = QtWidgets.QLabel(Form)
        self.pic1.setGeometry(QtCore.QRect(40, 280, 100, 91))
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("off.png"))
        self.pic1.setObjectName("pic1")
        self.pic2 = QtWidgets.QLabel(Form)
        self.pic2.setGeometry(QtCore.QRect(180, 280, 100, 91))
        self.pic2.setText("")
        self.pic2.setPixmap(QtGui.QPixmap("off.png"))
        self.pic2.setObjectName("pic2")
        self.pic3 = QtWidgets.QLabel(Form)
        self.pic3.setGeometry(QtCore.QRect(320, 280, 100, 91))
        self.pic3.setText("")
        self.pic3.setPixmap(QtGui.QPixmap("off.png"))
        self.pic3.setObjectName("pic3")
        self.pic4 = QtWidgets.QLabel(Form)
        self.pic4.setGeometry(QtCore.QRect(460, 280, 100, 91))
        self.pic4.setText("")
        self.pic4.setPixmap(QtGui.QPixmap("off.png"))
        self.pic4.setObjectName("pic4")
        self.start = QtWidgets.QLabel(Form)
        self.start.setEnabled(True)
        self.start.setGeometry(QtCore.QRect(0, 0, 601, 501))
        self.start.setText("")
        self.start.setPixmap(QtGui.QPixmap("start.png"))
        self.start.setObjectName("start")
        self.yourname = QtWidgets.QLineEdit(Form)
        self.yourname.setGeometry(QtCore.QRect(150, 290, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yourname.setFont(font)
        self.yourname.setObjectName("yourname")
        self.getin = QtWidgets.QPushButton(Form)
        self.getin.setGeometry(QtCore.QRect(230, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.getin.setFont(font)
        self.getin.setStyleSheet("background-color:rgb(115, 102, 84); color: rgb(219, 195, 160)\n"
"")
        self.getin.setDefault(False)
        self.getin.setObjectName("getin")
        self.price1 = QtWidgets.QLabel(Form)
        self.price1.setGeometry(QtCore.QRect(30, 250, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.price1.setFont(font)
        self.price1.setStyleSheet("background-image:url(\"say.png\");")
        self.price1.setAlignment(QtCore.Qt.AlignCenter)
        self.price1.setObjectName("price1")
        self.price2 = QtWidgets.QLabel(Form)
        self.price2.setGeometry(QtCore.QRect(170, 250, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.price2.setFont(font)
        self.price2.setStyleSheet("background-image:url(\"say.png\");")
        self.price2.setAlignment(QtCore.Qt.AlignCenter)
        self.price2.setObjectName("price2")
        self.price3 = QtWidgets.QLabel(Form)
        self.price3.setGeometry(QtCore.QRect(310, 250, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.price3.setFont(font)
        self.price3.setStyleSheet("background-image:url(\"say.png\");")
        self.price3.setAlignment(QtCore.Qt.AlignCenter)
        self.price3.setObjectName("price3")
        self.price4 = QtWidgets.QLabel(Form)
        self.price4.setGeometry(QtCore.QRect(450, 250, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.price4.setFont(font)
        self.price4.setStyleSheet("background-image:url(\"say.png\");")
        self.price4.setAlignment(QtCore.Qt.AlignCenter)
        self.price4.setObjectName("price4")
        self.item = QtWidgets.QLabel(Form)
        self.item.setGeometry(QtCore.QRect(354, 30, 190, 170))
        self.item.setText("")
        self.item.setPixmap(QtGui.QPixmap("item1.png"))
        self.item.setObjectName("item")
        self.host = QtWidgets.QLabel(Form)
        self.host.setGeometry(QtCore.QRect(179, 20, 171, 140))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.host.setFont(font)
        self.host.setStyleSheet("background-image:url(\"host_say.png\");")
        self.host.setAlignment(QtCore.Qt.AlignCenter)
        self.host.setObjectName("host")
        self.time_left = QtWidgets.QLabel(Form)
        self.time_left.setGeometry(QtCore.QRect(50, 0, 51, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.time_left.setFont(font)
        self.time_left.setStyleSheet("")
        self.time_left.setAlignment(QtCore.Qt.AlignCenter)
        self.time_left.setObjectName("time_left")
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(0, 0, 61, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.bg.raise_()
        self.bid.raise_()
        self.lineEdit.raise_()
        self.name1.raise_()
        self.name2.raise_()
        self.name4.raise_()
        self.name3.raise_()
        self.pic1.raise_()
        self.pic2.raise_()
        self.pic3.raise_()
        self.pic4.raise_()
        self.price1.raise_()
        self.price2.raise_()
        self.price3.raise_()
        self.price4.raise_()
        self.item.raise_()
        self.host.raise_()
        self.time_left.raise_()
        self.time_label.raise_()
        self.start.raise_()
        self.yourname.raise_()
        self.getin.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bid.setText(_translate("Form", "BID"))
        self.getin.setText(_translate("Form", "Enter"))
        self.price1.setText(_translate("Form", "200"))
        self.price2.setText(_translate("Form", "200"))
        self.price3.setText(_translate("Form", "200"))
        self.price4.setText(_translate("Form", "200"))
        self.price1.setVisible(False)
        self.price2.setVisible(False)
        self.price3.setVisible(False)
        self.price4.setVisible(False)
        self.item.setVisible(False)
        self.host.setText(_translate("Form", "Waiting for\nOther\nParticipants"))
        self.time_left.setText(_translate("Form", "30"))
        self.time_label.setText(_translate("Form", "Time:"))
