# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0 , 0 , 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.outputLabel = QtWidgets.QLabel(self.frame_6)
        self.outputLabel.setGeometry(QtCore.QRect(-20, 0, 398, 108))
        self.outputLabel.setStyleSheet("color:#fff;\n"
"font: 25pt \"Arial Black\";\n"
"background-color: rgb(0, 0, 0);")
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(-20, 100, 411, 2))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearButton = QtWidgets.QPushButton(self.frame_2)
        self.clearButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(135, 135, 135);\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.parenthesesButton = QtWidgets.QPushButton(self.frame_2)
        self.parenthesesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parenthesesButton.sizePolicy().hasHeightForWidth())
        self.parenthesesButton.setSizePolicy(sizePolicy)
        self.parenthesesButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(135, 135, 135);\n"
"}")
        self.parenthesesButton.setObjectName("parenthesesButton")
        self.horizontalLayout_2.addWidget(self.parenthesesButton)
        self.percentageButton = QtWidgets.QPushButton(self.frame_2)
        self.percentageButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentageButton.sizePolicy().hasHeightForWidth())
        self.percentageButton.setSizePolicy(sizePolicy)
        self.percentageButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(135, 135, 135);\n"
"}")
        self.percentageButton.setObjectName("percentageButton")
        self.horizontalLayout_2.addWidget(self.percentageButton)
        self.plusButton = QtWidgets.QPushButton(self.frame_2)
        self.plusButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        self.plusButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 176, 26);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 199, 27);\n"
"}")
        self.plusButton.setObjectName("plusButton")
        self.horizontalLayout_2.addWidget(self.plusButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sevenButton = QtWidgets.QPushButton(self.frame_3)
        self.sevenButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        self.sevenButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.horizontalLayout_3.addWidget(self.sevenButton)
        self.eightButton = QtWidgets.QPushButton(self.frame_3)
        self.eightButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        self.eightButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.horizontalLayout_3.addWidget(self.eightButton)
        self.nineButton = QtWidgets.QPushButton(self.frame_3)
        self.nineButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        self.nineButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.horizontalLayout_3.addWidget(self.nineButton)
        self.minusButton = QtWidgets.QPushButton(self.frame_3)
        self.minusButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        self.minusButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.minusButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 176, 26);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 199, 27);\n"
"}")
        self.minusButton.setAutoDefault(False)
        self.minusButton.setDefault(False)
        self.minusButton.setFlat(False)
        self.minusButton.setObjectName("minusButton")
        self.horizontalLayout_3.addWidget(self.minusButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fourButton = QtWidgets.QPushButton(self.frame_4)
        self.fourButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        self.fourButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.horizontalLayout_4.addWidget(self.fourButton)
        self.fiveButton = QtWidgets.QPushButton(self.frame_4)
        self.fiveButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        self.fiveButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.horizontalLayout_4.addWidget(self.fiveButton)
        self.sixButton = QtWidgets.QPushButton(self.frame_4)
        self.sixButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        self.sixButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.horizontalLayout_4.addWidget(self.sixButton)
        self.divisionButton = QtWidgets.QPushButton(self.frame_4)
        self.divisionButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divisionButton.sizePolicy().hasHeightForWidth())
        self.divisionButton.setSizePolicy(sizePolicy)
        self.divisionButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 176, 26);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 199, 27);\n"
"}")
        self.divisionButton.setObjectName("divisionButton")
        self.horizontalLayout_4.addWidget(self.divisionButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setEnabled(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.oneButton = QtWidgets.QPushButton(self.frame_5)
        self.oneButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.horizontalLayout_5.addWidget(self.oneButton)
        self.twoButton = QtWidgets.QPushButton(self.frame_5)
        self.twoButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        self.twoButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.horizontalLayout_5.addWidget(self.twoButton)
        self.threeButton = QtWidgets.QPushButton(self.frame_5)
        self.threeButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        self.threeButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.horizontalLayout_5.addWidget(self.threeButton)
        self.timesButton = QtWidgets.QPushButton(self.frame_5)
        self.timesButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timesButton.sizePolicy().hasHeightForWidth())
        self.timesButton.setSizePolicy(sizePolicy)
        self.timesButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 176, 26);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 199, 27);\n"
"}")
        self.timesButton.setObjectName("timesButton")
        self.horizontalLayout_5.addWidget(self.timesButton)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.negativeButton = QtWidgets.QPushButton(self.frame_9)
        self.negativeButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.negativeButton.sizePolicy().hasHeightForWidth())
        self.negativeButton.setSizePolicy(sizePolicy)
        self.negativeButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.negativeButton.setObjectName("negativeButton")
        self.horizontalLayout_6.addWidget(self.negativeButton)
        self.zeroButton = QtWidgets.QPushButton(self.frame_9)
        self.zeroButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.horizontalLayout_6.addWidget(self.zeroButton)
        self.dotButton = QtWidgets.QPushButton(self.frame_9)
        self.dotButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy)
        self.dotButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 179, 179);\n"
"}")
        self.dotButton.setObjectName("dotButton")
        self.horizontalLayout_6.addWidget(self.dotButton)
        self.equalButton = QtWidgets.QPushButton(self.frame_9)
        self.equalButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy)
        self.equalButton.setStyleSheet("QPushButton{\n"
"font: 87 26pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(29, 221, 0);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(17, 255, 0);\n"
"}")
        self.equalButton.setObjectName("equalButton")
        self.horizontalLayout_6.addWidget(self.equalButton)
        self.verticalLayout.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.parenthesesButton.setText(_translate("MainWindow", "()"))
        self.percentageButton.setText(_translate("MainWindow", "%"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.divisionButton.setText(_translate("MainWindow", "/"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.timesButton.setText(_translate("MainWindow", "*"))
        self.negativeButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
