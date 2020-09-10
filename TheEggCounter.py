#!/usr/bin/env python3

# TheEggCounter.py
# 
# A tiny application suited for counting eggs for the estimation
# of DEPM (Daily Egg Production Method) fecundity parameter
# (But you could count many other things on a picture...)
# 
# Copyright 2014,2020 Jorge Tornero Nunez http://imasdemase.com
# 
# This file is part of TheEggCounter, V1.0
# 
# TheEggCounter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# TheEggCounter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with TheEggCounter.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
from PyQt5 import QtGui, QtCore, QtWidgets
from counter_gui import Ui_OnImageCounter as CounterGUI
from aboutdialog import Ui_aboutDialog as AboutDialog

class ItemCounter(QtWidgets.QMainWindow):
    """
    This class provides a Main Window with a graphic view 
    where an image with items to be counted is placed and
    counting such items can be performed using the mouse
    """
    
    # Defines the color for marker and its outline
    markerPen = QtGui.QPen(QtGui.QColor(QtCore.Qt.black))
    markerBrush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.red))
    textPen = QtGui.QPen(QtGui.QColor(QtCore.Qt.yellow))
    
                
    def __init__(self, screenWidth = 1280, screenHeight = 1024):
      
        QtWidgets.QMainWindow.__init__(self)
        self.setGeometry(0, 0, screenWidth, screenHeight)
        self.countingWindow = CounterGUI()
        self.translateUi()
        self.countingWindow.setupUi(self)
        self.resize(screenWidth,screenHeight)
        self.scene = QtWidgets.QGraphicsScene()
        self.countingWindow.imageView.setScene(self.scene)
        
        # Reimplementation of keypress event management
        self.keyPressEvent = self.manageCounterKeyboardEvent
        
        self.setItemCount(0)
        self.countingWindow.finishButton.setEnabled(False)
        self.countingWindow.resetCounterButton.setEnabled(False)
        self.connectSignals()
        
        
    def translateUi(self):
        """
        This function localizates GUI and related messages
        """
        # We get the running dir and the locale
        self.running_dir = os.path.dirname(__file__)
        locale = QtCore.QLocale().name()
        
        # Generation of paths for localization files, must be inside
        # i18n folder and their name should be like:
        # theeggcounter_[LOCALE].qm
        # counter_gui_[LOCALE].qm
        # aboutdialog_[LOCALE].qm
        # WHere [LOCALE] is the name of the locale following BCP47 guidelines
        # You can create your own translations by creating new files with 
        # QtLinguist.
        
        mainTranslatorPath = os.path.join(\
            self.running_dir, 'i18n', 'theeggcounter_{0}.qm'.format(locale))
        UiTranslatorPath = os.path.join(\
            self.running_dir, 'i18n', 'counter_gui_{0}.qm'.format(locale))
        aboutTranslatorPath = os.path.join(\
            self.running_dir, 'i18n', 'aboutdialog_{0}.qm'.format(locale))
        
        
        # Localization
        self.mainTranslator = QtCore.QTranslator()
        self.UiTranslator = QtCore.QTranslator()
        self.aboutTranslator = QtCore.QTranslator()
       
        self.mainTranslator.load(mainTranslatorPath)
        self.UiTranslator.load(UiTranslatorPath)
        self.aboutTranslator.load(aboutTranslatorPath)
                
        QtCore.QCoreApplication.installTranslator(self.mainTranslator)
        QtCore.QCoreApplication.installTranslator(self.UiTranslator)
        QtCore.QCoreApplication.installTranslator(self.aboutTranslator)
        
    def connectSignals(self):
        """
        Connects GUI buttons as well as menu actions with their event handlers
        """
        self.countingWindow.loadImageButton.clicked.connect(self.loadImage)
        self.countingWindow.resetCounterButton.clicked.connect(self.resetCounter)
        self.countingWindow.finishButton.clicked.connect(self.finishCount)
        self.countingWindow.actionExit.triggered.connect(self.exitCounter)
        self.countingWindow.actionAbout.triggered.connect(self.about)
        
        
    def loadImage(self):
        """
        Loads an image from disk and displays it
        """
        filenameDialog = QtWidgets.QFileDialog.getOpenFileName(None,
                    self.tr("Select an image to load"),
                    options=QtWidgets.QFileDialog.DontUseNativeDialog)
        
        self.filename = filenameDialog[0]

        pixmap = QtGui.QPixmap(self.filename)
        pixmap = pixmap.scaledToHeight(\
          self.countingWindow.imageView.height(),QtCore.Qt.SmoothTransformation)
        self.pixmap = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap)
        #self.pixmap = QtWidgets.QGraphicsPixmapItem(pixmap, scene = self.scene)
        
        # Reimplementation of the mousePressEvent of the pixmap
        self.pixmap.mousePressEvent = self.manageCounterMouseEvent
                
        # We calculate the width of the pixmap and subsequently, the step
        # for scrolling the view. The view shift is calculated so visibility
        # of all the markers is guaranteed while scrolling the view
        
        self.pixmapWidth = pixmap.width()
        self.viewShift = self.pixmapWidth / ((self.pixmapWidth\
          / self.countingWindow.imageView.width()) + 1) 
        
        # Sets the scrollbar to the leftmost part of the image
        self.countingWindow.imageView.horizontalScrollBar().setValue(0)
        
        # Once loaded the file, we enable the Finish Count button
        self.countingWindow.finishButton.setEnabled(True)
        self.countingWindow.resetCounterButton.setEnabled(True)
    
    def resetCounter(self):
        """
        This function just resets the counter, so we
        remove only markers and keep the image. This is done
        by removing only those items with type() equal to 4,
        which means that is an ellipse
        """
        
        self.setItemCount(0)
        
        for item in self.scene.items():
            if item.type() == 4:
                self.scene.removeItem(item)
            
    
    def manageCounterMouseEvent(self, event):
        """
        This function manages the mouse events over the image:
        Left button adds a marker and increases the count.
        Right button removes a marker and decreases the count
        Left + Ctrl moves the view to the right
        Right + Ctrl moves the view to the left
        """
        
        keyboardModifier = event.modifiers()
        pressedMouseButton = event.button()
        
        # We must get the position of the scroll bar and.
        #viewShift = self.pixmapWidth/((self.pixmapWidth/self.countingWindow.imageView.width())+1)
        viewPosition = self.countingWindow.imageView.horizontalScrollBar().value()
        
        # Left mouse click management
        if pressedMouseButton == QtCore.Qt.LeftButton:
            if keyboardModifier == QtCore.Qt.NoModifier:
                # Adds a marker in the position of the click
                # taking into account the diameter of the marker
                posx = event.pos().x()
                posy = event.pos().y()
                self.scene.addEllipse(posx-3.5, posy-3.5, 7, 7, self.markerPen, self.markerBrush)
                self.setItemCount(self.itemCount + 1)
                  
            elif keyboardModifier == QtCore.Qt.ControlModifier:
                # Moves view to the right
                self.countingWindow.imageView.horizontalScrollBar().setValue(viewPosition - self.viewShift)
        
        # Right mouse click management
        elif pressedMouseButton == QtCore.Qt.RightButton:
            if keyboardModifier == QtCore.Qt.NoModifier:
                # Removes the marker under the cursor  
                posx = event.pos().x()
                posy = event.pos().y()
                itemToDelete = self.scene.itemAt(posx,posy,QtGui.QTransform())
                if itemToDelete.type() == 4: # Means is an ellipse (marker)
                    self.scene.removeItem(itemToDelete)
                    self.setItemCount(self.itemCount - 1)
                  
            elif keyboardModifier == QtCore.Qt.ControlModifier:
                # Moves view to the left
                self.countingWindow.imageView.horizontalScrollBar().setValue(viewPosition + self.viewShift)    
      
    def manageCounterKeyboardEvent(self, event):
        """
        This function handles the keyboard events of the dialog
        """
        
        keyPressed = event.key()
        keyboardModifier = event.modifiers()
        # Shorcut for loading images        
        if (keyPressed == QtCore.Qt.Key_L and keyboardModifier == QtCore.Qt.ControlModifier):
            self.loadImage()
        
        # Shorcut for finishing the count    
        elif (keyPressed == QtCore.Qt.Key_F and keyboardModifier == QtCore.Qt.ControlModifier and self.countingWindow.finishButton.isEnabled() == True):
            self.finishCount()
        
            # Shorcut for resetting the count
        elif (keyPressed == QtCore.Qt.Key_R and keyboardModifier == QtCore.Qt.ControlModifier and self.countingWindow.resetCounterButton.isEnabled() == True):
            self.resetCounter()
        
    def finishCount(self):
        """
        This function ask for confirmation when the user has finished counting
        and wants to mark the image file as counted.
        It adds the suffix _cntd to the file and also inserts the number of items
        counted in the top right corner of the image.
        Additionally, it completely resets the view removing the markers and the pixmap
        from it.
        """
        
        # We get some info from the image file 
        fileInfo = QtCore.QFileInfo(self.filename)
        suffix = fileInfo.completeSuffix()
        basename = fileInfo.baseName()
        newFilename = basename + '_ctnd.' + suffix
        filePath = fileInfo.absolutePath()
        destinationFile = filePath + '/' + newFilename
            
        # Firstly we ask for confirmation
        confirmation = QtWidgets.QMessageBox(None)
        confirmation.setWindowTitle(self.tr("Confirmation Dialog"))
        confirmation.setText(self.tr(u"<center>This action will:<ol><li>Remove all markers</li><li>Unload the image</li><li>Insert the number of counted items in the image</li><li>Create file %s</li></ol><br><b>Do you want to proceed with the above?</b><center>") %newFilename)
        btn1 = confirmation.addButton(self.tr(u"Accept"), QtWidgets.QMessageBox.YesRole)
        
        if confirmation.exec_() == 0: # User agrees
           
            # We will load again the image file, because we scaled it
            # when first loaded
            pixmap = QtGui.QPixmap(self.filename)
            
            # We create a painter on the pixmap to be able to
            # draw on it
            painter = QtGui.QPainter(pixmap)
            painter.setPen(self.textPen)
            font = QtGui.QFont("Arial", 30)
            painter.setFont(font)
            pixmapWidth = pixmap.width()
            
            countText = self.tr(u"Count: %s") %self.getItemCount()
            fm = QtGui.QFontMetrics(font)
            countTextHeight = fm.boundingRect(countText).height()
                       
            painter.drawText(QtCore.QPoint(pixmapWidth / 2, countTextHeight + 5), countText )
            # End the painter is mandatory
            painter.end()
            
            # Now saves the filename appending the count marker
            pixmap.save(destinationFile)
            
            # Removing items and pixmap froom scene
            for item in self.scene.items():
                self.scene.removeItem(item)
            
            # Finally we set the count to zero and disable the finish count button
            # as well as the reset count button
            self.setItemCount(0)
            self.countingWindow.finishButton.setEnabled(False)
            self.countingWindow.resetCounterButton.setEnabled(False)
            
            
            
    def setItemCount(self, count):
        """
        Sets the count to a integer value and displays its value
        """
        self.itemCount = count
        text = self.tr(u"Counted items: %s") %count
        self.countingWindow.counterLabel.setText(text)
          
    def getItemCount(self):
        """
        Returns the number of items counted
        """
        return self.itemCount
      
    def about(self):
        """
        Shows an about dialog with license and some simple help
        """
        dialog = QtWidgets.QDialog()
        aboutDialog = AboutDialog()
        aboutDialog.setupUi(dialog)
        dialog.exec_()
      
    def exitCounter(self):
        """
        Function to exit the dialog, asking for confirmation
        """
        confirmation = QtWidgets.QMessageBox(None)
        confirmation.setWindowTitle(self.tr("Exiting TheEggCounter"))
        confirmation.setText(self.tr("""<center>Are you sure you want to exit?</b>
            </center>"""))
        btn1 = confirmation.addButton(self.tr("Accept"), QtWidgets.QMessageBox.YesRole)
        btn2 = confirmation.addButton(self.tr("No, thanks"), QtWidgets.QMessageBox.YesRole)
        if confirmation.exec_() == 0:
          self.close()
          

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    # We get the screen size to set the size of the counter
    primaryScreen = app.desktop().primaryScreen()
    screenWidth = app.desktop().screenGeometry(primaryScreen).width()
    screenHeight = app.desktop().screenGeometry(primaryScreen).height()
    itemCounter = ItemCounter(screenWidth, screenHeight)
    itemCounter.show()
    
    sys.exit(app.exec_())
