# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter_gui.ui'
#
# Created: Wed Sep 17 08:18:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OnImageCounter(object):
    def setupUi(self, OnImageCounter):
        OnImageCounter.setObjectName(_fromUtf8("OnImageCounter"))
        OnImageCounter.resize(1024, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OnImageCounter.sizePolicy().hasHeightForWidth())
        OnImageCounter.setSizePolicy(sizePolicy)
        OnImageCounter.setMinimumSize(QtCore.QSize(800, 600))
        OnImageCounter.setMaximumSize(QtCore.QSize(1280, 1024))
        OnImageCounter.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(OnImageCounter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imageView = QtGui.QGraphicsView(self.centralwidget)
        self.imageView.setMinimumSize(QtCore.QSize(0, 0))
        self.imageView.setMaximumSize(QtCore.QSize(1250, 768))
        self.imageView.setBaseSize(QtCore.QSize(0, 0))
        self.imageView.setFrameShape(QtGui.QFrame.Box)
        self.imageView.setFrameShadow(QtGui.QFrame.Raised)
        self.imageView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.imageView.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        self.imageView.setObjectName(_fromUtf8("imageView"))
        self.gridLayout.addWidget(self.imageView, 0, 0, 1, 4)
        self.loadImageButton = QtGui.QPushButton(self.centralwidget)
        self.loadImageButton.setObjectName(_fromUtf8("loadImageButton"))
        self.gridLayout.addWidget(self.loadImageButton, 1, 0, 1, 1)
        self.finishButton = QtGui.QPushButton(self.centralwidget)
        self.finishButton.setObjectName(_fromUtf8("finishButton"))
        self.gridLayout.addWidget(self.finishButton, 1, 1, 1, 1)
        self.resetCounterButton = QtGui.QPushButton(self.centralwidget)
        self.resetCounterButton.setObjectName(_fromUtf8("resetCounterButton"))
        self.gridLayout.addWidget(self.resetCounterButton, 1, 2, 1, 1)
        self.usageLabel = QtGui.QLabel(self.centralwidget)
        self.usageLabel.setObjectName(_fromUtf8("usageLabel"))
        self.gridLayout.addWidget(self.usageLabel, 1, 3, 2, 1)
        self.counterLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.counterLabel.setFont(font)
        self.counterLabel.setObjectName(_fromUtf8("counterLabel"))
        self.gridLayout.addWidget(self.counterLabel, 2, 0, 1, 3)
        OnImageCounter.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(OnImageCounter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMenu = QtGui.QMenu(self.menuBar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        OnImageCounter.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(OnImageCounter)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(OnImageCounter)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuMenu.addAction(self.actionExit)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(OnImageCounter)
        QtCore.QMetaObject.connectSlotsByName(OnImageCounter)

    def retranslateUi(self, OnImageCounter):
        OnImageCounter.setWindowTitle(_translate("OnImageCounter", "Oocyte Counter for DEPM v1.0", None))
        self.loadImageButton.setText(_translate("OnImageCounter", "Load Image\n"
"(Ctrl+L)", None))
        self.finishButton.setText(_translate("OnImageCounter", "Finish Count\n"
"(Ctrl+F)", None))
        self.resetCounterButton.setText(_translate("OnImageCounter", "Reset counter\n"
"(Ctrl+R)", None))
        self.usageLabel.setText(_translate("OnImageCounter", "<html><head/><body><p><span style=\" font-weight:600;\">Click left button</span> to add an egg marker</p><p><span style=\" font-weight:600;\">Click right button</span> to remove an egg marker</p><p><span style=\" font-weight:600; font-style:italic;\">Ctrl</span><span style=\" font-weight:600;\">+left button</span> moves picture to the left</p><p><span style=\" font-weight:600; font-style:italic;\">Ctrl</span><span style=\" font-weight:600;\">+right button</span> moves picture to the right</p></body></html>", None))
        self.counterLabel.setText(_translate("OnImageCounter", "Counted Items: 0", None))
        self.menuMenu.setTitle(_translate("OnImageCounter", "Menu", None))
        self.actionExit.setText(_translate("OnImageCounter", "Exit", None))
        self.actionAbout.setText(_translate("OnImageCounter", "About", None))

