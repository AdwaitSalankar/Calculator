from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.percent())
        self.percentButton.setGeometry(QtCore.QRect(10, 160, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(120, 160, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(230, 160, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(340, 160, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(120, 270, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(230, 270, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(340, 270, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 270, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(120, 370, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(230, 370, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(340, 370, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 370, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(120, 470, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(230, 470, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(340, 470, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 470, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(120, 570, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(230, 570, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(340, 570, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 570, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Removing Character
    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    # Percentage
    def percent(self):
        screen = self.outputLabel.text()
        try:
            value = float(screen)
            percentage = value/100
            self.outputLabel.setText(str(percentage))
        except:
            self.outputLabel.setText("ERROR")

    # Math
    def math_it(self):
        # Grabbing
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")


    # Changing from positive/negative
    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-",""))
        else:
            self.outputLabel.setText(f'-{screen}')

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self,pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # To check zero
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
                # concatenate
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())