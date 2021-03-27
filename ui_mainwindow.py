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
        self.verticalLayoutWidget.setGeometry(QRect(790, 0, 295, 311))
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list = QListWidget(self.verticalLayoutWidget)
        self.list.setObjectName(u"list")

        self.horizontalLayout.addWidget(self.list)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 771, 611))
        self.objectsLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.objectsLayout.setObjectName(u"objectsLayout")
        self.objectsLayout.setContentsMargins(0, 0, 0, 0)
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
    # retranslateUi

