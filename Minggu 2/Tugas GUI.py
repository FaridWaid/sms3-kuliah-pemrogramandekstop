from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys

#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QMainWindow()
   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   textLabel = QtWidgets.QLabel(window)
   textLabel.setText("Kotak Angka")
   textLabel.move(10,10)
   x = 10
   y = 40
   for i in range (1,6):
      button = QtWidgets.QPushButton(window)
      button.setText(str(i))
      button.setStyleSheet("background-color: #b5c6ea; font: bold 40px; color: red;")
      button.setGeometry(QtCore.QRect(x, y, 50, 45))
      x +=60
    
   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(50,50,500,300)
   window.setWindowTitle("PyQt5 Example")

   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
    window_go()
