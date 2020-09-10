# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OnImageCounter(object):
    def setupUi(self, OnImageCounter):
        OnImageCounter.setObjectName("OnImageCounter")
        OnImageCounter.resize(1044, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OnImageCounter.sizePolicy().hasHeightForWidth())
        OnImageCounter.setSizePolicy(sizePolicy)
        OnImageCounter.setMinimumSize(QtCore.QSize(800, 600))
        OnImageCounter.setMaximumSize(QtCore.QSize(1920, 1080))
        OnImageCounter.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(OnImageCounter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.imageView = QtWidgets.QGraphicsView(self.centralwidget)
        self.imageView.setMinimumSize(QtCore.QSize(0, 0))
        self.imageView.setMaximumSize(QtCore.QSize(1880, 800))
        self.imageView.setBaseSize(QtCore.QSize(0, 0))
        self.imageView.setFrameShape(QtWidgets.QFrame.Box)
        self.imageView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.imageView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.imageView.setObjectName("imageView")
        self.gridLayout.addWidget(self.imageView, 0, 0, 1, 4)
        self.loadImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadImageButton.setObjectName("loadImageButton")
        self.gridLayout.addWidget(self.loadImageButton, 1, 0, 1, 1)
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setObjectName("finishButton")
        self.gridLayout.addWidget(self.finishButton, 1, 1, 1, 1)
        self.resetCounterButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetCounterButton.setObjectName("resetCounterButton")
        self.gridLayout.addWidget(self.resetCounterButton, 1, 2, 1, 1)
        self.usageLabel = QtWidgets.QLabel(self.centralwidget)
        self.usageLabel.setObjectName("usageLabel")
        self.gridLayout.addWidget(self.usageLabel, 1, 3, 2, 1)
        self.counterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.counterLabel.setFont(font)
        self.counterLabel.setObjectName("counterLabel")
        self.gridLayout.addWidget(self.counterLabel, 2, 0, 1, 3)
        OnImageCounter.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(OnImageCounter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1044, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        OnImageCounter.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(OnImageCounter)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(OnImageCounter)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionExit)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(OnImageCounter)
        QtCore.QMetaObject.connectSlotsByName(OnImageCounter)

    def retranslateUi(self, OnImageCounter):
        _translate = QtCore.QCoreApplication.translate
        OnImageCounter.setWindowTitle(_translate("OnImageCounter", "Oocyte Counter for DEPM v1.0"))
        self.loadImageButton.setText(_translate("OnImageCounter", "Load Image\n"
"(Ctrl+L)"))
        self.finishButton.setText(_translate("OnImageCounter", "Finish Count\n"
"(Ctrl+F)"))
        self.resetCounterButton.setText(_translate("OnImageCounter", "Reset counter\n"
"(Ctrl+R)"))
        self.usageLabel.setText(_translate("OnImageCounter", "<html><head/><body><p><span style=\" font-weight:600;\">Click left button</span> to add an egg marker</p><p><span style=\" font-weight:600;\">Click right button</span> to remove an egg marker</p><p><span style=\" font-weight:600; font-style:italic;\">Ctrl</span><span style=\" font-weight:600;\">+left button</span> moves picture to the left</p><p><span style=\" font-weight:600; font-style:italic;\">Ctrl</span><span style=\" font-weight:600;\">+right button</span> moves picture to the right</p></body></html>"))
        self.counterLabel.setText(_translate("OnImageCounter", "Counted Items: 0"))
        self.menuMenu.setTitle(_translate("OnImageCounter", "Menu"))
        self.actionExit.setText(_translate("OnImageCounter", "Exit"))
        self.actionAbout.setText(_translate("OnImageCounter", "About"))
