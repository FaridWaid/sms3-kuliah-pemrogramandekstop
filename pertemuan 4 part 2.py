import sys
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   #parent1 = QHBoxLayout()

   #layout baru : hbox, horizontal
   ln1 = QLineEdit("trunojoyo")
   ln2 = QLineEdit("Madura")
   grid = QGridLayout()
   hbox = QHBoxLayout()
   hbox.addWidget(ln1)
   hbox.addWidget(ln2)
   
   vbox = QVBoxLayout()

   #ini di vbox
   b1 = QPushButton("Button1")
   b2 = QPushButton("Button2")
   b3 = QPushButton()
   b3.setText("Button 3")
   b2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
   #b2.setSizePolicy(QSizePolicy.Exp

   txt1 = QLabel("belajar pyqt")   
   
   vbox.addWidget(b1)
   vbox.addWidget(b3)   
   vbox.addWidget(txt1)
   vbox.addWidget(b2)
   
   #set layout
   #parent1.addLayout(vbox)
   #parent1.addLayout(hbox)
   
   win.setLayout(vbox)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()