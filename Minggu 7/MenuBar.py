import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
#import aplikasi Rumus_Dasar_Kecepatan
import Rumus_Dasar_Kecepatan
#import aplikasi Rumus_Dasar_Debit
import Rumus_Dasar_Debit


#membuat fungsi dengan nama window_go
def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    #membuat style pada app dengan style fusion
    app.setStyle("fusion")
    #menambahkan icon pada tampilan window dengan nama file icon 'math.png'
    app.setWindowIcon(QIcon('math.png'))
    #membuat sebuah main window dengan nama variabel Mwindow
    Mwindow = QMainWindow()
    #membuat QWidget dengan nama variabel window
    window = QWidget()

    #menginisialisai sebuah menu bar di dalam main window sengan nama variabel bar
    bar = Mwindow.menuBar()
    #menambahkan menu 'Open' ke dalam bar dan di inisialisasi ke variabel file1
    file1 = bar.addMenu("Open")
    #menambahkan QAction "Rumus Kecepatan" di dalam menubar open dengan inisialisasi ke variabel file1a
    file1a = QAction("Rumus Kecepatan")
    #menambahkan QAction "Rumus Debit" di dalam menubar open dengan inisialisasi ke variabel file1b
    file1b = QAction("Rumus Debit")
    #memasukkan file1a ke dalam menu bar file1
    file1.addAction(file1a)
    #memasukkan file1b ke dalam menu bar file1
    file1.addAction(file1b)

    #membuat sebuah signal ketika file1a di klik maka akan dialihkan ke fungsi Rumus_Kecepatan
    file1a.triggered.connect(Rumus_Kecepatan)
    #membuat sebuah signal ketika file1b di klik maka akan dialihkan ke fungsi Rumus_Debit
    file1b.triggered.connect(Rumus_Debit)

    #membuat sebuah grid layout dengan nama variabel grid
    grid = QGridLayout()
    #membuat sebuah label dengan dengan nama variabel label
    label = QLabel("Rumus - Rumus Dasar Kecepatan dan Debit",window)
    #mengatur posisi label menjadi align center
    label.setAlignment(QtCore.Qt.AlignCenter)
    #mengatur label dengan warna magenta, font bold dan berukuran 35px, dan menggunakan border berukuran 2px dan berwarna solid black
    label.setStyleSheet("color: magenta; font: bold 35px; border: 2px solid black;")
    #memasukkan label ke dalam layout grid
    grid.addWidget(label)

    #membuat layout grid menjadi layout kedua yang berada di dalam main window
    window.setLayout(grid)
    
    #menentukan ukuran window, + title dan menampilkan
    Mwindow.setCentralWidget(window)
    Mwindow.setGeometry(50,50,1300,300)
    Mwindow.setWindowTitle("Menu Bar")
    Mwindow.show()
    sys.exit(app.exec_())

#membuat fungsi Rumus_Kecepatan
def Rumus_Kecepatan():
    #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
    Rumus_Dasar_Kecepatan.Layout()
#membuat fungsi Rumus_Debit
def Rumus_Debit():
    #memanggil/menampilkan aplikasi Rumus_Dasar_Debit
    Rumus_Dasar_Debit.Layout()

if __name__ == '__main__':
    #menampilakna semua widget yang ada di fungsi window_go
    window_go()