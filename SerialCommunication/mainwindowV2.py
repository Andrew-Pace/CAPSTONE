# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 780)

        self.sliderBox = QtWidgets.QGroupBox(MainWindow)
        self.sliderBox.setGeometry(QtCore.QRect(20, 10, 741, 611))
        self.sliderBox.setCheckable(False)
        self.sliderBox.setObjectName("sliderBox")

        self.groupBox = QtWidgets.QGroupBox(self.sliderBox)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 211, 581))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 51))  # Adjusted width to 191 for symmetry
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")

        self.motorSlider = QtWidgets.QSlider(self.groupBox)
        self.motorSlider.setGeometry(QtCore.QRect(30, 50, 91, 461))
        self.motorSlider.setOrientation(QtCore.Qt.Vertical)
        self.motorSlider.setObjectName("motorSlider")

        self.motorMax = QtWidgets.QLineEdit(self.groupBox)
        self.motorMax.setGeometry(QtCore.QRect(140, 50, 61, 20))  # Adjusted width to 61 for symmetry
        self.motorMax.setObjectName("motorMax")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 30, 91, 21))  # Adjusted width to 91 for symmetry
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight)
        self.label_3.setObjectName("label_3")

        self.motorMin = QtWidgets.QLineEdit(self.groupBox)
        self.motorMin.setGeometry(QtCore.QRect(140, 520, 61, 20))  # Adjusted width to 61 for symmetry
        self.motorMin.setObjectName("motorMin")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(110, 500, 91, 21))  # Adjusted width to 91 for symmetry
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight)
        self.label_4.setObjectName("label_4")

        self.motorCounter = QtWidgets.QLCDNumber(self.groupBox)
        self.motorCounter.setGeometry(QtCore.QRect(30, 520, 91, 51))
        self.motorCounter.setObjectName("motorCounter")

        self.groupBox_2 = QtWidgets.QGroupBox(self.sliderBox)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 20, 211, 581))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 191, 51))  # Adjusted width to 191 for symmetry
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")

        self.pitchSlider = QtWidgets.QSlider(self.groupBox_2)
        self.pitchSlider.setGeometry(QtCore.QRect(30, 50, 91, 461))
        self.pitchSlider.setOrientation(QtCore.Qt.Vertical)
        self.pitchSlider.setObjectName("pitchSlider")

        self.servoMax = QtWidgets.QLineEdit(self.groupBox_2)
        self.servoMax.setGeometry(QtCore.QRect(140, 50, 61, 20))  # Adjusted width to 61 for symmetry
        self.servoMax.setObjectName("servoMax")

        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(110, 30, 91, 21))  # Adjusted width to 91 for symmetry
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight)
        self.label_8.setObjectName("label_8")

        self.servoMin = QtWidgets.QLineEdit(self.groupBox_2)
        self.servoMin.setGeometry(QtCore.QRect(140, 520, 61, 20))  # Adjusted width to 61 for symmetry
        self.servoMin.setObjectName("servoMin")

        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(110, 500, 91, 21))  # Adjusted width to 91 for symmetry
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight)
        self.label_9.setObjectName("label_9")

        self.pitchCounter = QtWidgets.QLCDNumber(self.groupBox_2)
        self.pitchCounter.setGeometry(QtCore.QRect(30, 520, 91, 51))
        self.pitchCounter.setObjectName("pitchCounter")

        self.openFile = QtWidgets.QPushButton(self.sliderBox)
        self.openFile.setGeometry(QtCore.QRect(250, 30, 251, 31))
        self.openFile.setObjectName("openFile")

        self.clockLabel = QtWidgets.QLabel(self.sliderBox)
        self.clockLabel.setGeometry(QtCore.QRect(230, 5, 300, 25))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.clockLabel.setFont(font)
        self.clockLabel.setObjectName("clockLabel")
        self.clockLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.readout = QtWidgets.QTextEdit(self.sliderBox)
        self.readout.setGeometry(QtCore.QRect(220, 80, 300, 400))
        self.readout.setObjectName("readout")
        self.readout.setReadOnly(True)
        self.readout.document().setDocumentMargin(10)


        self.looseButton = QtWidgets.QPushButton(self.sliderBox)
        self.looseButton.setGeometry(QtCore.QRect(230, 500, 280, 100))
        self.looseButton.setObjectName("looseButton")
        self.looseButton.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;  /* Bright red background */
                color: white;  /* White text */
                border: 2px solid #c0392b;  /* Darker red border */
                border-radius: 10px;  /* Rounded corners */
                font-size: 20px;  /* Larger font size */
                font-weight: bold;  /* Bold text */
                padding: 15px 30px;  /* Extra padding for a substantial look */
                text-transform: uppercase;  /* Uppercase text for emphasis */
            }
            QPushButton:hover {
                background-color: #c0392b;  /* Darker red on hover */
            }
            QPushButton:pressed {
                background-color: #a93226;  /* Even darker red on press */
            }
        """)

        self.fileLabel = QtWidgets.QLabel(self.sliderBox)
        self.fileLabel.setGeometry(QtCore.QRect(250, 60, 251, 16))
        self.fileLabel.setText("")
        self.fileLabel.setObjectName("fileLabel")

        self.armButton = QtWidgets.QPushButton(MainWindow)
        self.armButton.setGeometry(QtCore.QRect(20, 650, 565, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.armButton.setFont(font)
        self.armButton.setObjectName("armButton")

        self.liveButton = QtWidgets.QPushButton(MainWindow)
        self.liveButton.setGeometry(QtCore.QRect(590, 650, 171, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.liveButton.setFont(font)
        self.liveButton.setCheckable(False)
        self.liveButton.setChecked(False)
        self.liveButton.setObjectName("liveButton")

        self.pitchCounter.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pitchCounter.setStyleSheet("""
            QLCDNumber {
                background-color: #bbbbbb;
                color: blue;
                border: 2px solid black;
                border-radius: 5px;
            }
        """)
        self.motorCounter.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.motorCounter.setStyleSheet("""
            QLCDNumber {
                background-color: #bbbbbb;
                color: blue;
                border: 2px solid black;
                border-radius: 5px;
            }
        """)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.sliderBox.setTitle("")
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Testy-Mcspin"))
        self.sliderBox.setTitle(_translate("MainWindow", "Controls"))
        self.groupBox.setTitle(_translate("MainWindow", "Motor"))
        self.label.setText(_translate("MainWindow", "Motor"))
        self.motorMax.setPlaceholderText(_translate("MainWindow", "2000"))
        self.label_3.setText(_translate("MainWindow", "Max Motor "))
        self.motorMin.setPlaceholderText(_translate("MainWindow", "1000"))
        self.label_4.setText(_translate("MainWindow", "Min Motor "))
        self.groupBox_2.setTitle(_translate("MainWindow", "Motor"))
        self.label_7.setText(_translate("MainWindow", "Pitch"))
        self.servoMax.setPlaceholderText(_translate("MainWindow", "2000"))
        self.label_8.setText(_translate("MainWindow", "Max Servo"))
        self.servoMin.setPlaceholderText(_translate("MainWindow", "1000"))
        self.label_9.setText(_translate("MainWindow", "Min Servo"))
        self.openFile.setText(_translate("MainWindow", "Open File"))
        self.armButton.setText(_translate("MainWindow", "CLICK TO ARM"))
        self.liveButton.setText(_translate("MainWindow", "LIVE CONTROL"))
        self.pitchCounter.setObjectName(_translate("MainWindow", "pitchCounter"))
        self.motorCounter.setObjectName(_translate("MainWindow", "motorCounter"))
        self.looseButton.setText(_translate("MainWindow", ""))
        self.clockLabel.setText(_translate("MainWindow", "Clock Loading..."))
        self.readout.setStyleSheet("""
                QTextEdit {
                    background: transparent;
                    color: black;
                    border: none;
                    font-family: Courier;
                    font-size: 5px;  /* Very small font size */
                    font-weight: bold;
                }
            """)

        self.readout.setHtml(_translate("MainWindow", """
                <html>
                    <head/>
                    <body style="line-height: 1.2; margin: 0; padding: 0;">
                        <p>System Readout...</p>
                    </body>
                </html>
            """))
        # Apply styles

        styles = [
            # (self.sliderBox, """
            #         background-color: #FA6400;
            #         border: 3px solid black;
            #     """),
            # (self.groupBox, """
            #     background-color: #f8f8f8;
            #     border: 1px solid black;
            # """),
            (self.label, "color: black;"),
            (self.motorMax, "background-color: lightyellow;"),
            (self.label_3, "color: darkred;"),
            (self.motorMin, "background-color: lightyellow;"),
            (self.label_4, "color: darkred;"),
            (self.groupBox_2, "background-color: #f8f8f8;"),
            (self.label_7, "color: black;"),
            (self.servoMax, "background-color: lightyellow;"),
            (self.label_8, "color: darkred;"),
            (self.servoMin, "background-color: lightyellow;"),
            (self.label_9, "color: darkred;"),
            # (self.armButton, "background-color: orange; color: white;"),
            (self.liveButton, "background-color: purple; color: white;"),
            (self.sliderBox, """
                    QGroupBox {
                        background-color: #FA6400;
                        border: 2px solid black;
                        border-radius: 10px;
                    }
                    QGroupBox::title {
                        color: darkblue;
                        background-color: #f0f0f0;
                        padding: 5px;
                        font-size: 16px;
                        font-weight: bold;
                        subcontrol-origin: margin;
                        subcontrol-position: top center;
                    }
                """),
            (self.groupBox, """
                            QGroupBox {
                                background-color: #F8F8F8;
                                border: 2px solid black;
                                border-radius: 10px;
                            }
                            QGroupBox::title {
                                color: darkblue;
                                background-color: #f0f0f0;
                                padding: 5px;
                                font-size: 16px;
                                subcontrol-origin: margin;
                                subcontrol-position: top center;
                            }
                        """),
            (self.groupBox_2, """
                            QGroupBox {
                                background-color: #F8F8F8;
                                border: 2px solid black;
                                border-radius: 10px;
                            }
                            QGroupBox::title {
                                color: darkblue;
                                background-color: #f0f0f0;
                                padding: 5px;
                                font-size: 16px;
                                subcontrol-origin: margin;
                                subcontrol-position: top center;
                            }
                        """),
            (self.openFile, """
                            QPushButton {
                                background-color: lightcoral;
                                color: white;
                                border-radius: 10px;
                                border: 2px solid black;
                                font-size: 16px;
                                font-weight: bold;
                                box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                            }
                            QPushButton:hover {
                                background-color: #809259;
                            }
                            QPushButton:pressed {
                                background-color: #d32f2f;
                            }
                        """),
        ]
        for widget, style in styles:
            widget.setStyleSheet(style)
