#-*- coding:utf8 -*-
import os
os.system("sudo apt-get install python-pyqt5")
import sys
import Ui_untitled
import MySQLdb
from PyQt5 import QtCore, QtGui, QtWidgets


class MainDialog(QtWidgets.QDialog, Ui_untitled.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.selectButton.clicked.connect(self.selectFile)
        self.sqlButton.clicked.connect(self.getSQL)
        self.filePath = ""
        self.sql = ""

    def selectFile(self):
        self.fileDialog = QtWidgets.QFileDialog(self)
        try:
            self.filePath = self.fileDialog.getOpenFileName()[0]
            file = open(self.filePath, "r")
            self.m3uText.setPlainText(file.read())
        except IOError:
            print "io error"
    
    def getSQL(self):
        iptvtext = self.m3uText.toPlainText()
        # iptvtext = open(self.filePath, "r").read()
        iptvtext = iptvtext.replace("#EXTINF:0,", "").replace("#EXTINF:-1,", "").replace("EXTINF:-1,", "").replace("#EXTM3U", "").replace(".ts", ".ts | ");
        array = iptvtext.split("|")
        self.sql = ""
        for item in array:
			try:
				channel = item.split("http")
				name = channel[0].rstrip().lstrip()
				url = "http"+channel[1].rstrip()
				try:
					self.sql = self.sql+"INSERT INTO channels (title, rtmp, image, cat_id, sira) VALUES ('"+MySQLdb.escape_string(name)+"', '"+MySQLdb.escape_string(url)+"', '','0', '0');\n";
				except:
					print("error")
			except:
				print("index error")
        self.sqlText.setPlainText(self.sql)
					


app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()