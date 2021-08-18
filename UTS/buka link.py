import sys
import PyQt5.QtWidgets import *
import PyQt5.QtGui import *

self.button = QPushButton('DEMO', clicked=self.generateContent)
self.textBrowser = QTextBrowser()
self.textBrowser.setOpenExternalLinks(True)


def generateContent(self):
    self.textBrowser.moveCursor(QTextCursor.Start)
    self.textBrowser.append('Hello World')
    self.textBrowser.append('<a href=https://www.google.com/> Google </a>')