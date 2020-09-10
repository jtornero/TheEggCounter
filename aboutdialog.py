# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        aboutDialog.resize(470, 613)
        self.gridLayout = QtWidgets.QGridLayout(aboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(aboutDialog)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.aboutTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aboutLabel = QtWidgets.QLabel(self.aboutTab)
        self.aboutLabel.setObjectName("aboutLabel")
        self.gridLayout_2.addWidget(self.aboutLabel, 0, 0, 1, 1)
        self.licenseText = QtWidgets.QTextBrowser(self.aboutTab)
        self.licenseText.setObjectName("licenseText")
        self.gridLayout_2.addWidget(self.licenseText, 1, 0, 1, 1)
        self.tabWidget.addTab(self.aboutTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.textBrowser = QtWidgets.QTextBrowser(self.helpTab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 431, 520))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.helpTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.closeButton = QtWidgets.QDialogButtonBox(aboutDialog)
        self.closeButton.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.closeButton.setCenterButtons(True)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 1, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        self.tabWidget.setCurrentIndex(0)
        self.closeButton.rejected.connect(aboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About TheEggCounter"))
        self.aboutLabel.setText(_translate("aboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">TheEggCounter</span></p><p align=\"center\">A tiny application suited for counting eggs for the estimation</p><p align=\"center\">of DEPM (Daily Egg Production Method) fecundity parameter</p><p align=\"center\">(But you could count many other things on a picture...)</p><p align=\"center\"><span style=\" font-size:medium; font-weight:600;\">Version 2.0</span></p><p align=\"center\">© 2014, 2020 Jorge Tornero<br/><a href=\"http://imasdemase.com\"><span style=\" text-decoration: underline; color:#006e28;\">http://imasdemase.com</span></a></p><p align=\"center\"><a href=\"http://imasdemase.com\"><span style=\" text-decoration: underline; color:#006e28;\">@imasdemase</span></a></p></body></html>"))
        self.licenseText.setDocumentTitle(_translate("aboutDialog", "License"))
        self.licenseText.setHtml(_translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>License</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600;\">Version 3, 29 June 2007</span><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.<br /><br />This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.<br /><br />You should have received a copy of the GNU General Public License along with this program. If not, see:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.gnu.org/licenses\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#006e28;\">http://www.gnu.org/licenses</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("aboutDialog", "About"))
        self.textBrowser.setHtml(_translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:600;\">The EggCounter</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">How-to</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">To count eggs (or whatever) over a image with TheEggCounter, follow these simple steps:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">1. Load a image file for counting items on it</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">, clicking on the button </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:italic;\">Load image</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> or pressing Ctrl+L. It will load the image and fit it to TheEggCounter viewport height.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">You can scroll the image</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> by using the scrollbar or just clicking Ctrl+Left/Right button to scroll the image in the desired direction, so the count can be done on the whole picture.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">2. Left click over an item to count it</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> and place a marker over it, so you will not count it twice. Unless you want to do it, of course...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">3. Finish your count</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> with the button </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:italic;\">Finish count</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> or press Ctrl+F. It will save a copy of your image with the text </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:italic;\">_cntd</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> appended to it. In addition, it will place a text into the new file with the number of objects counted in the middle of the upper side of your image. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">If you just want to record your count,</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> you can override this behavior by just loading a new image as described in step 1.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">While counting,</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> you can:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">- Remove any deployed marker</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> clicking right mouse button over it, decreasing the count accordingly.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">- </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">Reset the count</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">, removing all deployed markers, by clicking the button </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:italic;\">Reset count</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> or pressing Ctrl+R</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpTab), _translate("aboutDialog", "Help"))
