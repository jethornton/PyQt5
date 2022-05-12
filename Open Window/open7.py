#!/usr/bin/python3

import sys
from PyQt5 import uic
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

def window():
	app = QApplication(sys.argv)
	w = QWidget()
	btn = QPushButton(w)
	btn.setText("Hello World!")
	btn.move(100,50)
	btn.clicked.connect(showdialog)
	w.setWindowTitle("PyQt Dialog demo")
	w.show()
	sys.exit(app.exec_())

def showdialog():
	dlg = QDialog()
	b1 = QPushButton("ok",dlg)
	b1.move(50,50)
	#b1.clicked.connect(closedlg(dlg))
	dlg.setWindowTitle("Dialog")# 9. PyQt5 — QDialog Class
	dlg.setWindowModality(Qt.ApplicationModal)
	dlg.exec_()

def closedlg(dlg):
	dlg.close()

if __name__ == '__main__':
	window()
