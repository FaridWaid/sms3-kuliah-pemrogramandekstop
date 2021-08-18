import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import sqlite3




class FilmCrime(QWidget):
   #Membuat fungsi init untuk inisialisasi class Mahasiswa
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #membuka database
        self.OpenDatabase()
        

    def OpenDatabase(self):
        #Mendeklarasikan database
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #Membuat nama database
        db.setDatabaseName('test.db')
        #Mengecek Database Apakah sudah terkoneksi atau belum
        if db.open():
            print('Berhasil membuka Database')
        else:
            print('Gagal membuka Database!')

    def LayoutCrime(self, Mwindow1):
        btn = QPushButton("Open Data")
        btn.setStyleSheet("background-color: #ffd369; font:bold 15px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        
        #membuat QWidget dengan nama variabel window
        Mwindow1.setStyleSheet("background-color: #222831;")

        #menginisialisai sebuah menu bar di dalam main window sengan nama variabel bar
        self.bar = Mwindow1.menuBar()
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

        #Membuat Grid Layout
        form = QFormLayout()
        

        self.add_cari = QLineEdit("Cari Film",self)
        self.add_cari.setStyleSheet("background-color: #eeeeee;")
        btn_cari = QPushButton("Cari")
        btn_cari.setStyleSheet("background-color: #ffd369; font:bold 15px;")

        self.tableWidget = QTableWidget()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review"))
        self.tableWidget.setColumnWidth(0,10)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(4,300)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.verticalScrollBar().maximum()
        self.tableWidget.verticalScrollBar().setValue(0)
        self.tableWidget.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")

        form.addRow(btn)
        form.addRow(btn_cari,self.add_cari)
        form.addRow(self.tableWidget)

        btn_cari.clicked.connect(self.filterDataCrime)
        btn.clicked.connect(self.tampilDataCrime)

        #Layout grid di jadikan layout utama
        self.setLayout(form)

        #menentukan ukuran window, + title dan menampilkan
        
        Mwindow1.setCentralWidget(self)
        Mwindow1.setGeometry(50,50,1300,1000)
        Mwindow1.setWindowTitle("List of Crime")


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


    #Fungsi untuk menampilankan data di dalam table
    def tampilDataCrime(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Crime' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataCrime(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cari.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cari.setText("")

if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('replay.jpg'))
    Mwindow1 = QMainWindow()
    ui = FilmCrime()
    ui.LayoutCrime(Mwindow1)
    Mwindow1.show()
    sys.exit(app.exec_())

