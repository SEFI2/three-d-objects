# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 708)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(770, 0, 351, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addButtons = QHBoxLayout()
        self.addButtons.setObjectName(u"addButtons")
        self.addSphere = QPushButton(self.verticalLayoutWidget)
        self.addSphere.setObjectName(u"addSphere")

        self.addButtons.addWidget(self.addSphere)

        self.addBox = QPushButton(self.verticalLayoutWidget)
        self.addBox.setObjectName(u"addBox")

        self.addButtons.addWidget(self.addBox)


        self.verticalLayout.addLayout(self.addButtons)

        self.deleteObject = QPushButton(self.verticalLayoutWidget)
        self.deleteObject.setObjectName(u"deleteObject")

        self.verticalLayout.addWidget(self.deleteObject)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.currentObjectsView = QListView(self.verticalLayoutWidget)
        self.currentObjectsView.setObjectName(u"currentObjectsView")

        self.horizontalLayout.addWidget(self.currentObjectsView)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 691, 571))
        self.objectsLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.objectsLayout.setObjectName(u"objectsLayout")
        self.objectsLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(770, 230, 378, 191))
        self.horizontalLayout_3 = QHBoxLayout(self.verticalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.showInfo = QPushButton(self.verticalLayoutWidget_3)
        self.showInfo.setObjectName(u"showInfo")

        self.verticalLayout_2.addWidget(self.showInfo)

        self.updateInfo = QPushButton(self.verticalLayoutWidget_3)
        self.updateInfo.setObjectName(u"updateInfo")

        self.verticalLayout_2.addWidget(self.updateInfo)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.size1 = QTextEdit(self.verticalLayoutWidget_3)
        self.size1.setObjectName(u"size1")

        self.horizontalLayout_4.addWidget(self.size1)

        self.size2 = QTextEdit(self.verticalLayoutWidget_3)
        self.size2.setObjectName(u"size2")

        self.horizontalLayout_4.addWidget(self.size2)

        self.size3 = QTextEdit(self.verticalLayoutWidget_3)
        self.size3.setObjectName(u"size3")

        self.horizontalLayout_4.addWidget(self.size3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rColor = QTextEdit(self.verticalLayoutWidget_3)
        self.rColor.setObjectName(u"rColor")

        self.horizontalLayout_2.addWidget(self.rColor)

        self.bColor = QTextEdit(self.verticalLayoutWidget_3)
        self.bColor.setObjectName(u"bColor")

        self.horizontalLayout_2.addWidget(self.bColor)

        self.gColor = QTextEdit(self.verticalLayoutWidget_3)
        self.gColor.setObjectName(u"gColor")

        self.horizontalLayout_2.addWidget(self.gColor)

        self.aColor = QTextEdit(self.verticalLayoutWidget_3)
        self.aColor.setObjectName(u"aColor")

        self.horizontalLayout_2.addWidget(self.aColor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.objectInfoWidget = QTableWidget(self.centralwidget)
        self.objectInfoWidget.setObjectName(u"objectInfoWidget")
        self.objectInfoWidget.setGeometry(QRect(770, 430, 381, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addSphere.setText(QCoreApplication.translate("MainWindow", u"Add sphere", None))
        self.addBox.setText(QCoreApplication.translate("MainWindow", u"Add box", None))
        self.deleteObject.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.showInfo.setText(QCoreApplication.translate("MainWindow", u"Show Info", None))
        self.updateInfo.setText(QCoreApplication.translate("MainWindow", u"Update Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RGB Color:", None))
    # retranslateUi

