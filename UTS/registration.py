import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
#import sqlite3

class Regis(QWidget):
   #Membuat fungsi init untuk inisialisasi class Mahasiswa
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #membuka database
        self.OpenDatabase()
        #self.createTabel()
        #memanggil fungsi Layout yang sudah dibuat agar ditampilkan hasilnya
        self.Regis()
        

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

    #def createTabel(self): 
    #    query = QtSql.QSqlQuery() 
    #    query.exec_("create table users(" "username varchar(20) primary key, " 
    #    "password varchar(20))") 
    #    print ("True")

    def Regis(self):
        #Membuat Grid Layout
        form = QFormLayout()

        label = QLabel("Registration",self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        form.addRow(label)

        self.usernameln = QLineEdit()
        self.usernameln.setPlaceholderText("Masukkan Username")
        form.addRow(self.usernameln)

        self.passwordln = QLineEdit()
        self.passwordln.setEchoMode(QLineEdit.Password)
        self.passwordln.setPlaceholderText("Masukkan Password")
        form.addRow(self.passwordln)

        self.passwordln2 = QLineEdit()
        self.passwordln2.setEchoMode(QLineEdit.Password)
        self.passwordln2.setPlaceholderText("Konfirmasi Password")
        form.addRow(self.passwordln2)

        signup = QPushButton("Sign Up")
        form.addRow(signup)
        signup.setStyleSheet("background-color: #ffc7c7;")

        signin = QPushButton("Sign In")
        form.addRow(signin)
        signin.setStyleSheet("background-color: #ffc7c7;")
        
        #Ketika button di klik akan memanggi fungsi masing - masing
        signup.clicked.connect(self.cek_user)
        #signin.clicked.connect(self.login)

        #Layout grid di jadikan layout utama
        self.setLayout(form)

    def cek_user(self):
        notif = QMessageBox()
        username = str(self.usernameln.text())
        pass1 = str(self.passwordln.text())
        pass2 = str(self.passwordln2.text())
        #Mendefinisikan Query
        query = QtSql.QSqlQuery() 
        if pass1 != pass2:
            notif.warning(self, "Konfirmasi Password Salah", "Tolong Masukkan password dengan benar! ", notif.Ok)
        else:
            #Menjalankan Perintah Sql
            query.prepare("INSERT INTO users VALUES ('" + username + "', '" + pass1 + "')")
            query.exec_()
            notif.information(self, "Selamat!", "Anda Berhasil Membuat Akun!")


if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #mengatur style di window menjadi style fusion
    app.setStyle("fusion")
    app.setWindowIcon(QIcon('replay.jpg'))
    #membuat variabel ex yang berisi class FormulaMath
    ex = Regis()
    ex.setStyleSheet("background-color: #fcf1f1;")
    

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(50,40,500,300)
    #membuat judul window
    ex.setWindowTitle("Halaman Registration")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())