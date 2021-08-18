import sys
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()

   btn1 = QPushButton("btn1")
   btn2 = QPushButton("btn2")
   btn3 = QPushButton("btn3")
   btn4 = QPushButton("btn4")
   btn5 = QPushButton("btn5")
   btn6 = QPushButton("btn6")

   grid = QGridLayout()
   grid.addWidget(btn1,1,1)
   grid.addWidget(btn2,1,3)
   grid.addWidget(btn3,2,2)
   grid.addWidget(btn4,2,3)
   grid.addWidget(btn5,1,2)
   grid.addWidget(btn6,2,1)


   win.setLayout(grid)

   #layout tambahan
   label1 = QLabel("Label1 baris1")
   label2 = QLabel("Label2 baris2")
   lay1 = QVBoxLayout()
   lay1.addWidget(label1)
   lay1.addWidget(label2)
   grid.addLayout(lay1,3,2)
   
   
   
   win.setLayout(grid)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()