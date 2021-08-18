import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import *
from PyQt5.QtCore import *
from action import FilmAction
from advanture import FilmAdvanture
from comedy import FilmComedy
from crime import FilmCrime
from drama import FilmDrama
from login import Login

class Home(QWidget):
    #membuat fungsi dengan nama window_go
    def window_go(self, Mwindow):
        #membuat QWidget dengan nama variabel window
        window = QWidget()

        #menginisialisai sebuah menu bar di dalam main window sengan nama variabel bar
        self.bar = Mwindow.menuBar()
        self.bar.setStyleSheet("background-color: #eeeeee;")
        self.file0 = self.bar.addMenu("Home")
        #menambahkan menu 'Open' ke dalam bar dan di inisialisasi ke variabel file1
        self.file1 = self.bar.addMenu("Genre")
        #menambahkan QAction "Rumus Kecepatan" di dalam menubar open dengan inisialisasi ke variabel file1a
        self.file1a = QAction("Action")
        #menambahkan QAction "Rumus Debit" di dalam menubar open dengan inisialisasi ke variabel file1b
        self.file1b = QAction("Advanture")
        #menambahkan QAction "Rumus Debit" di dalam menubar open dengan inisialisasi ke variabel file1b
        self.file1c = QAction("Comedy")
        #menambahkan QAction "Rumus Debit" di dalam menubar open dengan inisialisasi ke variabel file1b
        self.file1d = QAction("Crime")
        #menambahkan QAction "Rumus Debit" di dalam menubar open dengan inisialisasi ke variabel file1b
        self.file1e = QAction("Drama")
        #memasukkan file1a ke dalam menu bar file1
        self.file1.addAction(self.file1a)
        #memasukkan file1b ke dalam menu bar file1
        self.file1.addAction(self.file1b)
        #memasukkan file1b ke dalam menu bar file1
        self.file1.addAction(self.file1c)
        #memasukkan file1b ke dalam menu bar file1
        self.file1.addAction(self.file1d)
        #memasukkan file1b ke dalam menu bar file1
        self.file1.addAction(self.file1e)

        self.file0.triggered.connect(self.open_home)
        self.file1a.triggered.connect(self.open_action)
        self.file1b.triggered.connect(self.open_advanture)
        self.file1c.triggered.connect(self.open_comedy)
        self.file1d.triggered.connect(self.open_crime)
        self.file1e.triggered.connect(self.open_drama)

        #membuat sebuah grid layout dengan nama variabel grid
        grid = QGridLayout()
        #membuat sebuah label dengan dengan nama variabel label
        label = QLabel("Disclaimer!",window)
        #mengatur posisi label menjadi align center
        label.setAlignment(QtCore.Qt.AlignCenter)
        #mengatur label dengan warna magenta, font bold dan berukuran 35px, dan menggunakan border berukuran 2px dan berwarna solid black
        label.setStyleSheet("color: #0a043c; font: bold 35px; border: 2px solid black;")
        #memasukkan label ke dalam layout grid
        grid.addWidget(label)

        #membuat layout grid menjadi layout kedua yang berada di dalam main window
        window.setLayout(grid)
        
        #menentukan ukuran window, + title dan menampilkan
        Mwindow.setCentralWidget(window)
        Mwindow.setGeometry(50,50,1300,300)
        Mwindow.setWindowTitle("Menu Home")

    #membuat fungsi Rumus_Kecepatan
    def open_home(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = Users()
        self.ui.window_go(self.window)
        self.window.show()

    #membuat fungsi Rumus_Kecepatan
    def open_action(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = FilmAction()
        self.ui.Layout(self.window)
        self.window.show()
     

    #membuat fungsi Rumus_Kecepatan
    def open_advanture(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = FilmAdvanture()
        self.ui.Layout(self.window)
        self.window.show()
   

    #membuat fungsi Rumus_Kecepatan
    def open_comedy(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = FilmComedy()
        self.ui.Layout(self.window)
        self.window.show()
   

    #membuat fungsi Rumus_Kecepatan
    def open_crime(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = FilmCrime()
        self.ui.Layout(self.window)
        self.window.show()


    #membuat fungsi Rumus_Kecepatan
    def open_drama(self):
        #memanggil/menampilkan aplikasi Rumus_Dasar_Kecepatan
        self.window = QtWidgets.QMainWindow()
        self.ui = FilmDrama()
        self.ui.Layout(self.window)
        self.window.show()
    


if __name__ == '__main__':
    #menampilakna semua widget yang ada di fungsi window_go
    #Inisisalisai pyqt
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    #membuat style pada app dengan style fusion
    app.setStyle("fusion")
    #menambahkan icon pada tampilan window dengan nama file icon 'math.png'
    app.setWindowIcon(QIcon('replay.jpg'))
    #membuat sebuah main window dengan nama variabel Mwindow
    Mwindow = QMainWindow()
    ui = Home()
    ui.window_go(Mwindow)
    Mwindow.show()
    sys.exit(app.exec_())