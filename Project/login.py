import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sqlite3
import sqlite3 as mdb
import playFilmAction, playFilmAdvanture, playFilmComedy, playFilmCrime, playFilmDrama


class Login(QWidget):
    ##################################### -LOGIN- ##################################### 
    #membuat fungsi dengan nama Loginwindow
    def Loginwindow(self, Mwindow):
        #membuat QWidget dengan nama variabel window
        window = QWidget()

        grid = QGridLayout()
        
        tab = QTabWidget(self)

        grid.addWidget(tab, 0,0)

        group1 = QGroupBox(self)
        group2 = QGroupBox(self)

        #membuat sebuah form layout dengan nama variabel form dan form2
        form = QFormLayout()
        form2 = QFormLayout()

        group1.setLayout(form)
        group2.setLayout(form2)

        tab.addTab(group1,"Login")
        tab.addTab(group2,"Registration")
        tab.setStyleSheet("background-color: #ffc7c7; font:bold 15px roboto;")

        label = QLabel("Registration",self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        form2.addRow(label)
        label.setStyleSheet("font:bold 20px;")
        
        gambar = QPixmap("replay_ok.png")
        gambar_ok = gambar.scaled(350, 200)

        label0 = QLabel(self)
        label0.setPixmap(gambar_ok)
        label0.setAlignment(QtCore.Qt.AlignCenter)
        label0.setStyleSheet("height: 10px;")
        form2.addRow(label0)

        self.usernamereg = QLineEdit()
        self.usernamereg.setPlaceholderText("Masukkan Username")
        form2.addRow(self.usernamereg)
        self.usernamereg.setStyleSheet("background-color: #f6f6f6; height: 35px; font:bold 15px;")

        self.passwordreg = QLineEdit()
        self.passwordreg.setEchoMode(QLineEdit.Password)
        self.passwordreg.setPlaceholderText("Masukkan Password")
        form2.addRow(self.passwordreg)
        self.passwordreg.setStyleSheet("background-color: #f6f6f6; height: 35px; font:bold 15px;")

        self.passwordreg2 = QLineEdit()
        self.passwordreg2.setEchoMode(QLineEdit.Password)
        self.passwordreg2.setPlaceholderText("Konfirmasi Password")
        form2.addRow(self.passwordreg2)
        self.passwordreg2.setStyleSheet("background-color: #f6f6f6; height: 35px; font:bold 15px;")

        signup = QPushButton("Sign Up")
        form2.addRow(signup)
        signup.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        
        #Ketika button di klik akan memanggi fungsi masing - masing
        signup.clicked.connect(self.regis_user)

        label = QLabel("Login",self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        form.addRow(label)
        label.setStyleSheet("font:bold 20px;")

        gambar = QPixmap("replay_ok.png")
        gambar_ok = gambar.scaled(350, 200)

        label0 = QLabel(self)
        label0.setPixmap(gambar_ok)
        label0.setAlignment(QtCore.Qt.AlignCenter)
        label0.setStyleSheet("height: 10px;")
        form.addRow(label0)

        self.usernameln = QLineEdit()
        self.usernameln.setPlaceholderText("Masukkan Username")
        form.addRow(self.usernameln)
        self.usernameln.setStyleSheet("background-color: #f6f6f6; height: 35px; font:bold 15px;")

        self.passwordln = QLineEdit()
        self.passwordln.setEchoMode(QLineEdit.Password)
        self.passwordln.setPlaceholderText("Masukkan Password")
        form.addRow(self.passwordln)
        self.passwordln.setStyleSheet("background-color: #f6f6f6; height: 35px; font:bold 15px;")

        signin = QPushButton("Sign In")
        form.addRow(signin)
        signin.setStyleSheet("background-color: #ffd369; font:bold 15px;  height: 35px;")

        signin.clicked.connect(self.cek_user)

        #membuat layout grid menjadi layout kedua yang berada di dalam main window
        window.setLayout(grid)
        
        #menentukan ukuran Main window, + title dan menampilkan
        Mwindow.setCentralWidget(window)
        Mwindow.setStyleSheet("background-color: #222831;")
        Mwindow.setGeometry(700,250,500,300)
        Mwindow.setWindowTitle("Menu Login")

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

    def cek_user(self):
        self.OpenDatabase()
        notif = QMessageBox()
        usernamelog = str(self.usernameln.text())
        pass1log = str(self.passwordln.text())
        #Mendefinisikan Query
        query = QtSql.QSqlQuery()
        connection = sqlite3.connect("test.db")
        cek = connection.execute("SELECT username,password FROM users WHERE username = ? AND password = ? ",(usernamelog,pass1log))
        if usernamelog == "admin" and pass1log == "123":
            notif.information(self, "Login Berhasil", "Selamat Datang di Halaman Admin! ")
            self.open_admin()
        elif (len(cek.fetchall()) > 0):
            notif.information(self, "Login Berhasil", "Selamat Datang di Halaman User! ")
            self.open_user()
        else:
            notif.warning(self, "Login Gagal", "Username Dan Password Anda Tidak Cocok!", notif.Ok)

    def createTabelUsers(self): 
        query = QtSql.QSqlQuery() 
        query.exec_("create table users(" "username varchar(20) primary key, " 
        "password varchar(20))") 
        print ("True")

    def regis_user(self):
        self.OpenDatabase()
        self.createTabelUsers()
        notif = QMessageBox()
        username = str(self.usernamereg.text())
        pass1 = str(self.passwordreg.text())
        pass2 = str(self.passwordreg2.text())
        #Mendefinisikan Query
        query = QtSql.QSqlQuery() 
        if pass1 != pass2:
            notif.warning(self, "Konfirmasi Password Salah", "Tolong Masukkan password dengan benar! ", notif.Ok)
        else:
            #Menjalankan Perintah Sql
            query.prepare("INSERT INTO users VALUES ('" + username + "', '" + pass1 + "')")
            query.exec_()
            notif.information(self, "Selamat!", "Anda Berhasil Membuat Akun!")
            self.usernamereg.setText("")
            self.passwordreg.setText("")
            self.passwordreg2.setText("")

    #membuat fungsi open_user
    def open_user(self):
        #memanggil/menampilkan aplikasi window_go
        self.window_go(Mwindow)

    #membuat fungsi open_admin
    def open_admin(self):
        self.Admin(Mwindow)

    ##################################### -END OF LOGIN- #####################################

    ##################################### -USER- #####################################
    def window_go(self, Mwindow):
        #membuat QWidget dengan nama variabel window
        window = QWidget()

        #menginisialisai sebuah menu bar di dalam main window sengan nama variabel baruser
        self.baruser = Mwindow.menuBar()
        self.baruser.setStyleSheet("background-color: #eeeeee;")
        self.file0user = self.baruser.addMenu("Home")
        #menambahkan menu 'Recommendation' ke dalam bar dan di inisialisasi ke variabel file1user
        self.file1user = self.baruser.addMenu("Recommendation")
        #menambahkan QAction "Close Application" di dalam menubar home dengan inisialisasi ke variabel file0user
        self.file0auser = QAction("Close Application")
        #menambahkan QAction "List of Reccomendation" di dalam menubar Recommendation dengan inisialisasi ke variabel file1auser
        self.file1auser = QAction("List of Recommendation")
        #memasukkan file0auser ke dalam menu bar file0user
        self.file0user.addAction(self.file0auser)
        #memasukkan file1user ke dalam menu bar file1auser
        self.file1user.addAction(self.file1auser)

        self.file0auser.triggered.connect(self.open_home)
        self.file1auser.triggered.connect(self.open_recom)

        #membuat sebuah Vbox layout dengan nama variabel vbox
        vbox = QVBoxLayout()

        gambar = QPixmap("replay_ok.png")
        gambar_ok = gambar.scaled(500, 300)

        label0 = QLabel(self)
        label0.setPixmap(gambar_ok)
        label0.setAlignment(QtCore.Qt.AlignCenter)
        label0.setStyleSheet("height: 10px;")
        vbox.addWidget(label0)

        #membuat sebuah label dengan dengan nama variabel label
        label = QLabel("Intructions For The Users! \n - Tidak semua list film yang ada di table terdapat videonya "
        "\n - Film yang disediakan berdsarkan ID kemudian diikuti judul dan tahun rilis film"
        "\n - Untuk menonton film pilih dulu film dengan menekan tombol open video pada layout play film"
        "\n - Dimohon untuk pause video sebelum menutup layout play film",window)
        #mengatur posisi label menjadi align center
        label.setAlignment(QtCore.Qt.AlignCenter)
        #mengatur label dengan warna, font bold dan berukuran 25px
        label.setStyleSheet("color: #0a043c; font: bold 25px;")
        #memasukkan label ke dalam layout vbox
        vbox.addWidget(label)

        #membuat layout vbox menjadi layout kedua yang berada di dalam main window
        window.setLayout(vbox)
        window.setStyleSheet("background-color: #ffc7c7; font:bold 15px roboto; border: 2px solid black; ")
        
        #menentukan ukuran main window, + title dan menampilkan
        Mwindow.setCentralWidget(window)
        Mwindow.setGeometry(350,250,1300,300)
        Mwindow.setWindowTitle("Menu Home")

    #membuat fungsi open_home
    def open_home(self):
        #Menutup Main Window
        Mwindow.close()

    #membuat fungsi open_recom
    def open_recom(self):
        #memanggil/menampilkan aplikasi LayoutRecommendation
        self.LayoutRecommendation(Mwindow)
     
    ##################################### -END OF USER- #####################################

    ##################################### -ADMIN- #####################################
    def Admin(self, Mwindow):

        #menginisialisai sebuah menu bar di dalam main window sengan nama variabel barAdmin
        self.barAdmin = Mwindow.menuBar()
        self.barAdmin.setStyleSheet("background-color: #eeeeee;")
        self.file0 = self.barAdmin.addMenu("Home")
        self.file0a = QAction("Close Application")
        self.file1 = self.barAdmin.addMenu("Recommendation")
        self.file1a = QAction("List of Recommendation")
        self.file1.addAction(self.file1a)
        self.file0.addAction(self.file0a)

        self.file0a.triggered.connect(self.open_home)
        self.file1a.triggered.connect(self.open_recom)

        window = QWidget()
        #Membuat Grid Layout
        grid = QGridLayout()
        window.setStyleSheet("background-color: #ffc7c7; font:bold 15px roboto;")

        open_database = QPushButton("Open Database")
        grid.addWidget(open_database,1,0,1,3)
        open_database.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 20px;")

        add_data = QLabel("Tambah Data or Update Data:")
        grid.addWidget(add_data,2,0,1,0)

        add_id = QLabel("ID:")
        grid.addWidget(add_id,3,0)

        self.Id = QLineEdit(self)
        grid.addWidget(self.Id,3,1,1,2)
        self.Id.setStyleSheet("background-color: #f6f6f6;")

        add_judul = QLabel("Judul:")
        grid.addWidget(add_judul,4,0)

        self.Judul = QLineEdit(self)
        grid.addWidget(self.Judul,4,1,1,2)
        self.Judul.setStyleSheet("background-color: #f6f6f6;")

        tahun_rilis = QLabel("Tahun Rilis FIlm:")
        grid.addWidget(tahun_rilis,5,0)

        self.Tahun = QLineEdit(self)
        grid.addWidget(self.Tahun,5,1,1,2)
        self.Tahun.setStyleSheet("background-color: #f6f6f6;")

        add_genre = QLabel("Genre:")
        grid.addWidget(add_genre,6,0)

        self.Genre = QLineEdit(self)
        grid.addWidget(self.Genre,6,1,1,2)
        self.Genre.setStyleSheet("background-color: #f6f6f6;")

        add_sinopsis = QLabel("Sinopsis:")
        grid.addWidget(add_sinopsis,7,0)

        self.Sinopsis = QTextEdit(self)
        grid.addWidget(self.Sinopsis,7,1,1,2)
        self.Sinopsis.setStyleSheet("background-color: #f6f6f6;")

        add_rating = QLabel("Rating:")
        grid.addWidget(add_rating,8,0)

        self.Rating = QLineEdit(self)
        grid.addWidget(self.Rating,8,1,1,2)
        self.Rating.setStyleSheet("background-color: #f6f6f6;")

        add_review = QLabel("Review:")
        grid.addWidget(add_review,9,0)

        self.Review = QTextEdit(self)
        grid.addWidget(self.Review,9,1,1,2)
        self.Review.setStyleSheet("background-color: #f6f6f6;")

        add_tgl = QLabel("Tanggal Input Data:")
        grid.addWidget(add_tgl,10,0)

        self.tgl_input = QDateEdit(self)
        self.tgl_input.setMaximumDate(QtCore.QDate(2020,12,31))
        grid.addWidget(self.tgl_input,10,1,1,2)
        self.tgl_input.setStyleSheet("background-color: #f6f6f6;")

        add_button = QPushButton("Tambah Data")
        grid.addWidget(add_button,11,0,1,0)
        add_button.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 20px;")

        add_edit = QPushButton("Edit Data")
        grid.addWidget(add_edit,12,0)
        add_edit.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 20px;")

        add_update = QPushButton("Update Data")
        grid.addWidget(add_update,12,1,1,1)
        add_update.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 20px;")

        add_cancel = QPushButton("Cancel Edit")
        grid.addWidget(add_cancel,12,2,1,2)
        add_cancel.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 20px;")

        search = QLabel("Cari Data:")
        grid.addWidget(search,13,0)
        
        self.Cari = QLineEdit(self)
        grid.addWidget(self.Cari,13,1)
        self.Cari.setStyleSheet("background-color: #f6f6f6;")

        search_button = QPushButton("Cari")
        grid.addWidget(search_button,13,2)
        search_button.setStyleSheet("background-color: #54e346; font:bold 15px; height: 20px;")

        add_delete = QPushButton("Delete Data")
        grid.addWidget(add_delete,14,0,1,0)
        add_delete.setStyleSheet("background-color: #ec0101; font:bold 15px; height: 20px;")

        #Membuat widget table view yang diberi nama "Data" dan akan dimasukkan ke dalam layout Grid
        self.tableview = QTableView(self)
        self.tableview.setObjectName("Data")
        self.tableview.horizontalHeader().setStretchLastSection(True)
        self.tableview.setWordWrap(True)
        self.tableview.verticalHeader().setVisible(False)
        grid.addWidget(self.tableview,15,0,1,0)
        self.tableview.setStyleSheet("background-color: #f6f6f6;")
        self.tableview.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")

        #Ketika button di klik akan memanggi fungsi masing - masing
        open_database.clicked.connect(self.OpenDatabaseAdmin)
        add_button.clicked.connect(self.tambahData)
        search_button.clicked.connect(self.filterData)
        add_edit.clicked.connect(self.editData)
        add_update.clicked.connect(self.updateData)
        add_cancel.clicked.connect(self.cancelData)
        add_delete.clicked.connect(self.hapusData)

        #Layout grid di jadikan layout utama
        window.setLayout(grid)

        #menentukan ukuran main window, + title dan menampilkan
        Mwindow.setCentralWidget(window)
        Mwindow.setStyleSheet("background-color: #222831;")
        Mwindow.setGeometry(250,40,1300,980)
        Mwindow.setWindowTitle("Menu Admin")

    def OpenDatabaseAdmin(self):
        #Mendeklarasikan database
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #Membuat nama database
        self.db.setDatabaseName('test.db')
        #Mengecek Database Apakah sudah terkoneksi atau belum
        if self.db.open():
            print('Berhasil membuka Database')
            self.createTabel()
            self.tampilDataListfilm()
            
        else:
            print('Gagal membuka Database!')

    def createTabel(self): 
        query = QtSql.QSqlQuery() 
        query.exec_("create table listfilm(" "id integer primary key AUTOINCREMENT, " 
        "judul varchar(20), tahun_rilis int(10), genre varchar(20), sinopsis varchar(200), rating int(10), review varchar(400), tgl_input varchar(15))") 
        print ("True")

    #Fungsi untuk menampilankan data di dalam table
    def tampilDataListfilm(self):
        #Membuat Model
        model = QSqlQueryModel()
        #Mendefinisikan sql
        sql = "SELECT * FROM listfilm"
        #Mengeksekusi Model Query
        model.setQuery(sql)
        #Mengeset Data Model Ke table view
        self.tableview.setModel(model)
        #self.tableview.setWindowTitle(title)
        return self.tableview

    #Fungsi tambah Data ke dalam tabel mahasiswa
    def tambahData(self):
        #Mengambil Text inputan
        self.OpenDatabaseAdmin()
        Id = str(self.Id.text())
        Judul = str(self.Judul.text())
        Tahun = str(self.Tahun.text())
        Genre = str(self.Genre.text())
        Sinopsis = str(self.Sinopsis.toPlainText())
        Review = str(self.Review.toPlainText())
        Rating = str(self.Rating.text())
        Tgl_Input = str(self.tgl_input.text())
        query = QtSql.QSqlQuery()
        #Menjalankan Perintah Sql
        query.prepare("INSERT INTO listfilm VALUES ('" + Id + "','" + Judul + "', '" + Tahun + "', '" + Genre + "', '" + Sinopsis + "', '" + Rating + "', '" + Review + "', '" + Tgl_Input + "')")
        #Mengecek apakah query berjalan dengan baik
        if query.exec_():
            self.Id.setText("")
            self.Judul.setText("")
            self.Tahun.setText("")
            self.Genre.setText("")
            self.Sinopsis.setText("")
            self.Review.setText("")
            self.Rating.setText("")
            #Menampilkan Data
            self.tampilDataListfilm()
        else:
            #Apabila error akan menampilkan errornya ke dalam terminal
            print("Insert Error: ", query.lastError().text())
        
    #Fungsi Filter Data
    def filterData(self):
        #Membuat Model
        model = QSqlQueryModel()
        #Mengambil Inputan filter
        filter_search = str(self.Cari.text())
        sql = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%' OR tgl_input LIKE '%"+str(filter_search)+"%'"
        self.Cari.setText("")
        #Mengeksekusi Model Query
        model.setQuery(sql)
        #Mengeset Data Model Ke table view
        self.tableview.setModel(model)
        #mengembalikan nilai table view
        return self.tableview

    def hapusData(self):
        # Mengambil Data Yang Di klik
        select = self.tableview.selectedIndexes()[0]
        Id = str(self.tableview.model().data(select))
        Judul = str(self.tableview.model().data(select))
        Tahun = str(self.tableview.model().data(select))
        Genre = str(self.tableview.model().data(select))
        Sinopsis = str(self.tableview.model().data(select))
        Review = str(self.tableview.model().data(select))
        Rating = str(self.tableview.model().data(select))
        Tgl_Input = str(self.tableview.model().data(select))
        # Mendefinisikan Query
        query = QSqlQuery()
        # Menjalankan Perintah Query
        query.prepare("DELETE from listfilm WHERE (id = '" + Id + "'OR judul = '" + Judul + "'OR tahun_rilis = '" + Tahun + "'OR genre = '" + Genre + "'OR sinopsis = '" + Sinopsis + "'OR rating = '" + Rating + "'OR review = '" + Review + "'OR tgl_input = '" + Tgl_Input + "')")
        query.exec_()
        if query.exec_():
            print("Hapus Data Success")
            self.tampilDataListfilm()
        else:
            print("del_records Error: ", query.lastError().text())

    def editData(self):
        model = QSqlQueryModel()
        connection = sqlite3.connect("test.db")
        # Mengambil Data Yang Di klik
        select = self.tableview.selectedIndexes()[0]
        Id = str(self.tableview.model().data(select))
        # Mendefinisikan Query
        # Menjalankan Perintah Query
        # Eksekusi Perintah SQL
        waw = connection.execute("SELECT * FROM listfilm WHERE id = '%s' " % (Id))
        # Mengambil Satu Data
        data = waw.fetchall()
        self.Id.setText(str(data[0][0]))
        self.Judul.setText(str(data[0][1]))
        self.Tahun.setText(str(data[0][2]))
        self.Genre.setText(str(data[0][3]))
        self.Sinopsis.setText(str(data[0][4]))
        self.Rating.setText(str(data[0][5]))
        self.Review.setText(str(data[0][6]))

    def updateData(self):
        # Mengambil Data Yang Di input
        Id = str(self.Id.text())
        Judul = str(self.Judul.text())
        Tahun = str(self.Tahun.text())
        Genre = str(self.Genre.text())
        Sinopsis = str(self.Sinopsis.toPlainText())
        Review = str(self.Review.toPlainText())
        Rating = str(self.Rating.text())
        Tgl_Input = str(self.tgl_input.text())
        #Mendefinisikan Query
        query =  QtSql.QSqlQuery()
        #Menjalankan Perintah Sql
        query.prepare("""UPDATE listfilm SET judul=:Judul, tahun_rilis=:Tahun, genre=:Genre, sinopsis=:Sinopsis, rating=:Rating, review=:Review, tgl_input=:Tgl_Input WHERE id =:Id""")
        query.bindValue(":Id", Id)
        query.bindValue(":Judul", Judul)
        query.bindValue(":Tahun", Tahun)
        query.bindValue(":Genre", Genre)
        query.bindValue(":Sinopsis", Sinopsis)
        query.bindValue(":Review", Review)
        query.bindValue(":Rating", Rating)
        query.bindValue(":Tgl_Input", Tgl_Input)
        if query.exec_():
            self.Id.setText("")
            self.Judul.setText("")
            self.Tahun.setText("")
            self.Genre.setText("")
            self.Sinopsis.setText("")
            self.Review.setText("")
            self.Rating.setText("")
            #Menampilkan Data
            self.tampilDataListfilm()
        else:
            #Apabila error akan menampilkan errornya ke dalam terminal
            print("Insert Error: ", query.lastError().text())

    def cancelData(self):
        self.Id.setText("")
        self.Judul.setText("")
        self.Tahun.setText("")
        self.Genre.setText("")
        self.Sinopsis.setText("")
        self.Review.setText("")
        self.Rating.setText("")

    ##################################### -END OF ADMIN- #####################################

    ##################################### -LIST OF FILM BASED ON GENRE- #####################################
    def LayoutRecommendation(self, Mwindow):
        windowx = QWidget(self)
        
        gridx = QGridLayout()
        
        tabx = QTabWidget(self)
        tabx.setStyleSheet("background-color: #ffc7c7; font:bold 15px roboto;")

        gridx.addWidget(tabx, 0,0)

        groupAct = QGroupBox(self)
        groupAdv = QGroupBox(self)
        groupCom = QGroupBox(self)
        groupCri = QGroupBox(self)
        groupDra = QGroupBox(self)
        groupHor = QGroupBox(self)

        #membuat sebuah grid layout dengan nama variabel grid
        form = QFormLayout()
        formAdvanture = QFormLayout()
        formComedy = QFormLayout()
        formCrime = QFormLayout()
        formDrama = QFormLayout()
        formHorror = QFormLayout()

        groupAct.setLayout(form)
        groupAdv.setLayout(formAdvanture)
        groupCom.setLayout(formComedy)
        groupCri.setLayout(formCrime)
        groupDra.setLayout(formDrama)
        groupHor.setLayout(formHorror)

        tabx.addTab(groupAct,"Action")
        tabx.addTab(groupAdv,"Advanture")
        tabx.addTab(groupCom,"Comedy")
        tabx.addTab(groupCri,"Crime")
        tabx.addTab(groupDra,"Drama")
        tabx.addTab(groupHor,"Horror")
        
##################################### - ACTION - #####################################
        btn = QPushButton("Open Data Action")
        btn.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        
        #membuat QWidget dengan nama variabel window
        Mwindow.setStyleSheet("background-color: #222831;")

        self.add_cari = QLineEdit(self)
        self.add_cari.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cari.setPlaceholderText("Cari Film")
        btn_cari = QPushButton("Cari")
        btn_cari.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidget = QTableWidget()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidget.setColumnWidth(0,10)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(4,550)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,730)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.verticalScrollBar().maximum()
        self.tableWidget.verticalScrollBar().setValue(0)
        self.tableWidget.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setWordWrap(True)

        btnPlayAction = QPushButton("Play Film Action")
        btnPlayAction.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        form.addRow(btn)
        form.addRow(btn_cari,self.add_cari)
        form.addRow(self.tableWidget)
        form.addRow(btnPlayAction)

        btn_cari.clicked.connect(self.filterDataAction)
        btn.clicked.connect(self.tampilDataAction)
        btnPlayAction.clicked.connect(self.PlayFilmAction)

        ##################################### - END OF ACTION - #####################################

        ##################################### - ADVANTURE - #####################################

        btnAdvanture = QPushButton("Open Data Advanture")
        btnAdvanture.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        
        self.add_cariAdvanture = QLineEdit(self)
        self.add_cariAdvanture.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cariAdvanture.setPlaceholderText("Cari Film")
        btn_cariAdvanture = QPushButton("Cari")
        btn_cariAdvanture.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidgetAdvanture = QTableWidget()
        self.tableWidgetAdvanture.setAlternatingRowColors(True)
        self.tableWidgetAdvanture.setColumnCount(8)
        self.tableWidgetAdvanture.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetAdvanture.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetAdvanture.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetAdvanture.verticalHeader().setVisible(False)
        self.tableWidgetAdvanture.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetAdvanture.verticalHeader().setStretchLastSection(False)
        self.tableWidgetAdvanture.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetAdvanture.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidgetAdvanture.setColumnWidth(0,10)
        self.tableWidgetAdvanture.setColumnWidth(1,100)
        self.tableWidgetAdvanture.setColumnWidth(4,550)
        self.tableWidgetAdvanture.setColumnWidth(5,50)
        self.tableWidgetAdvanture.setColumnWidth(6,730)
        self.tableWidgetAdvanture.resizeRowsToContents()
        self.tableWidgetAdvanture.verticalScrollBar().maximum()
        self.tableWidgetAdvanture.verticalScrollBar().setValue(0)
        self.tableWidgetAdvanture.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidgetAdvanture.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidgetAdvanture.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidgetAdvanture.setWordWrap(True)

        btnPlayAdvanture = QPushButton("Play Film Advanture")
        btnPlayAdvanture.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        formAdvanture.addRow(btnAdvanture)
        formAdvanture.addRow(btn_cariAdvanture,self.add_cariAdvanture)
        formAdvanture.addRow(self.tableWidgetAdvanture)
        formAdvanture.addRow(btnPlayAdvanture)

        btn_cariAdvanture.clicked.connect(self.filterDataAdvanture)
        btnAdvanture.clicked.connect(self.tampilDataAdvanture)
        btnPlayAdvanture.clicked.connect(self.PlayFilmAdvanture)

        ##################################### - END OF ADVANTURE - #####################################

        ##################################### - COMEDY - #####################################

        btnComedy = QPushButton("Open Data Comedy")
        btnComedy.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        
        self.add_cariComedy = QLineEdit(self)
        self.add_cariComedy.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cariComedy.setPlaceholderText("Cari Film")
        btn_cariComedy = QPushButton("Cari")
        btn_cariComedy.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidgetComedy = QTableWidget()
        self.tableWidgetComedy.setAlternatingRowColors(True)
        self.tableWidgetComedy.setColumnCount(8)
        self.tableWidgetComedy.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetComedy.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetComedy.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetComedy.verticalHeader().setVisible(False)
        self.tableWidgetComedy.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetComedy.verticalHeader().setStretchLastSection(False)
        self.tableWidgetComedy.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetComedy.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidgetComedy.setColumnWidth(0,10)
        self.tableWidgetComedy.setColumnWidth(1,100)
        self.tableWidgetComedy.setColumnWidth(4,550)
        self.tableWidgetComedy.setColumnWidth(5,50)
        self.tableWidgetComedy.setColumnWidth(6,730)
        self.tableWidgetComedy.resizeRowsToContents()
        self.tableWidgetComedy.verticalScrollBar().maximum()
        self.tableWidgetComedy.verticalScrollBar().setValue(0)
        self.tableWidgetComedy.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidgetComedy.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidgetComedy.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidgetComedy.setWordWrap(True)

        btnPlayComedy = QPushButton("Play Film Comedy")
        btnPlayComedy.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        formComedy.addRow(btnComedy)
        formComedy.addRow(btn_cariComedy,self.add_cariComedy)
        formComedy.addRow(self.tableWidgetComedy)
        formComedy.addRow(btnPlayComedy)

        btn_cariComedy.clicked.connect(self.filterDataComedy)
        btnComedy.clicked.connect(self.tampilDataComedy)
        btnPlayComedy.clicked.connect(self.PlayFilmComedy)

        ##################################### - END OF COMEDY - #####################################

        ##################################### - CRIME - #####################################

        btnCrime = QPushButton("Open Data Crime")
        btnCrime.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        
        self.add_cariCrime = QLineEdit(self)
        self.add_cariCrime.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cariCrime.setPlaceholderText("Cari Film")
        btn_cariCrime = QPushButton("Cari")
        btn_cariCrime.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidgetCrime = QTableWidget()
        self.tableWidgetCrime.setAlternatingRowColors(True)
        self.tableWidgetCrime.setColumnCount(8)
        self.tableWidgetCrime.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetCrime.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetCrime.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCrime.verticalHeader().setVisible(False)
        self.tableWidgetCrime.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetCrime.verticalHeader().setStretchLastSection(False)
        self.tableWidgetCrime.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetCrime.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidgetCrime.setColumnWidth(0,10)
        self.tableWidgetCrime.setColumnWidth(1,100)
        self.tableWidgetCrime.setColumnWidth(4,550)
        self.tableWidgetCrime.setColumnWidth(5,50)
        self.tableWidgetCrime.setColumnWidth(6,730)
        self.tableWidgetCrime.resizeRowsToContents()
        self.tableWidgetCrime.verticalScrollBar().maximum()
        self.tableWidgetCrime.verticalScrollBar().setValue(0)
        self.tableWidgetCrime.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidgetCrime.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidgetCrime.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidgetCrime.setWordWrap(True)

        btnPlayCrime = QPushButton("Play Film Crime")
        btnPlayCrime.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        formCrime.addRow(btnCrime)
        formCrime.addRow(btn_cariCrime,self.add_cariCrime)
        formCrime.addRow(self.tableWidgetCrime)
        formCrime.addRow(btnPlayCrime)

        btn_cariCrime.clicked.connect(self.filterDataCrime)
        btnCrime.clicked.connect(self.tampilDataCrime)
        btnPlayCrime.clicked.connect(self.playFilmCrime)

        ##################################### - END OF CRIME - #####################################

        ##################################### - DRAMA - #####################################

        btnDrama = QPushButton("Open Data Drama")
        btnDrama.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow

        self.add_cariDrama = QLineEdit(self)
        self.add_cariDrama.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cariDrama.setPlaceholderText("Cari Film")
        btn_cariDrama = QPushButton("Cari")
        btn_cariDrama.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidgetDrama = QTableWidget()
        self.tableWidgetDrama.setAlternatingRowColors(True)
        self.tableWidgetDrama.setColumnCount(8)
        self.tableWidgetDrama.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDrama.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetDrama.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDrama.verticalHeader().setVisible(False)
        self.tableWidgetDrama.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDrama.verticalHeader().setStretchLastSection(False)
        self.tableWidgetDrama.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetDrama.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidgetDrama.setColumnWidth(0,10)
        self.tableWidgetDrama.setColumnWidth(1,100)
        self.tableWidgetDrama.setColumnWidth(4,550)
        self.tableWidgetDrama.setColumnWidth(5,50)
        self.tableWidgetDrama.setColumnWidth(6,730)
        self.tableWidgetDrama.resizeRowsToContents()
        self.tableWidgetDrama.verticalScrollBar().maximum()
        self.tableWidgetDrama.verticalScrollBar().setValue(0)
        self.tableWidgetDrama.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidgetDrama.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidgetDrama.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidgetDrama.setWordWrap(True)

        btnPlayDrama = QPushButton("Play Film Drama")
        btnPlayDrama.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        formDrama.addRow(btnDrama)
        formDrama.addRow(btn_cariDrama,self.add_cariDrama)
        formDrama.addRow(self.tableWidgetDrama)
        formDrama.addRow(btnPlayDrama)

        btn_cariDrama.clicked.connect(self.filterDataDrama)
        btnDrama.clicked.connect(self.tampilDataDrama)
        btnPlayDrama.clicked.connect(self.playFilmDrama)

        btnHorror = QPushButton("Open Data Horror")
        btnHorror.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")
        #membuat sebuah main window dengan nama variabel Mwindow
        

        self.add_cariHorror = QLineEdit(self)
        self.add_cariHorror.setStyleSheet("background-color: #eeeeee; font:bold 15px; height: 35px;")
        self.add_cariHorror.setPlaceholderText("Cari Film")
        btn_cariHorror = QPushButton("Cari")
        btn_cariHorror.setStyleSheet("background-color: #54e346; font:bold 15px; height: 35px;")

        self.tableWidgetHorror = QTableWidget()
        self.tableWidgetHorror.setAlternatingRowColors(True)
        self.tableWidgetHorror.setColumnCount(8)
        self.tableWidgetHorror.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetHorror.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetHorror.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetHorror.verticalHeader().setVisible(False)
        self.tableWidgetHorror.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetHorror.verticalHeader().setStretchLastSection(False)
        self.tableWidgetHorror.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidgetHorror.setHorizontalHeaderLabels(("Id", "Judul", "Tahun Rilis", "Genre", "Sinopsis","Rating","Review","Tanggal Input"))
        self.tableWidgetHorror.setColumnWidth(0,10)
        self.tableWidgetHorror.setColumnWidth(1,100)
        self.tableWidgetHorror.setColumnWidth(4,550)
        self.tableWidgetHorror.setColumnWidth(5,50)
        self.tableWidgetHorror.setColumnWidth(6,730)
        self.tableWidgetHorror.resizeRowsToContents()
        self.tableWidgetHorror.verticalScrollBar().maximum()
        self.tableWidgetHorror.verticalScrollBar().setValue(0)
        self.tableWidgetHorror.setStyleSheet("background-color: #eeeeee; border:2px #ffd369;")
        self.tableWidgetHorror.horizontalHeader().setStyleSheet("background-color: #ffd369; font:bold 15px;")
        self.tableWidgetHorror.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidgetHorror.setWordWrap(True)

        btnPlayHorror = QPushButton("Play Film Horror")
        btnPlayHorror.setStyleSheet("background-color: #ffd369; font:bold 15px; height: 35px;")

        formHorror.addRow(btnHorror)
        formHorror.addRow(btn_cariHorror,self.add_cariHorror)
        formHorror.addRow(self.tableWidgetHorror)
        formHorror.addRow(btnPlayHorror)

        btn_cariHorror.clicked.connect(self.filterDataHorror)
        btnHorror.clicked.connect(self.tampilDataHorror)
        btnPlayHorror.clicked.connect(self.PlayFilmHorror)

        #Layout grid di jadikan layout utama
        windowx.setLayout(gridx)

        #menentukan ukuran window, + title dan menampilkan
        #membuat QWidget dengan nama variabel window
        Mwindow.setStyleSheet("background-color: #222831;")
        Mwindow.setCentralWidget(windowx)
        Mwindow.setGeometry(0,35,2200,1000)
        Mwindow.setWindowTitle("List of Film Based on Genre")

        ##################################### - END OF DRAMA - #####################################

    ##################################### -END LIST OF FILM BASED ON GENRE- #####################################

    ##################################### -LIST OF ACTION- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataAction(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Action' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataAction(self):
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
    ##################################### -END LIST OF ACTION- #####################################

    ##################################### -LIST OF ADVANTURE- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataAdvanture(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Advanture' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidgetAdvanture.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetAdvanture.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetAdvanture.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataAdvanture(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cariAdvanture.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidgetAdvanture.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetAdvanture.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetAdvanture.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cariAdvanture.setText("")

    ##################################### -END LIST OF ADVANTURE- #####################################

    ##################################### -LIST OF COMEDY- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataComedy(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Comedy' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidgetComedy.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetComedy.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetComedy.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataComedy(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cariComedy.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidgetComedy.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetComedy.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetComedy.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cariComedy.setText("")

    ##################################### -END LIST OF COMEDY- #####################################

    ##################################### -LIST OF CRIME- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataCrime(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Crime' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidgetCrime.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetCrime.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetCrime.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataCrime(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cariCrime.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidgetCrime.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetCrime.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetCrime.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cariCrime.setText("")
    ##################################### -END LIST OF CRIME- #####################################

    ##################################### -LIST OF DRAMA- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataDrama(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Drama' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidgetDrama.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetDrama.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetDrama.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataDrama(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cariDrama.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidgetDrama.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetDrama.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetDrama.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cariDrama.setText("")
    ##################################### -END LIST OF DRAMA- #####################################

     ##################################### -LIST OF DRAMA- #####################################
    #Fungsi untuk menampilankan data di dalam table
    def tampilDataHorror(self):
        self.connection = sqlite3.connect("test.db")
        query = "SELECT * FROM listfilm WHERE genre LIKE 'Horror' ORDER BY rating DESC"
        result = self.connection.execute(query)
        self.tableWidgetHorror.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetHorror.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetHorror.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

    #Fungsi Filter Data
    def filterDataHorror(self):
        self.connection = sqlite3.connect("test.db")
        filter_search = str(self.add_cariHorror.text())
        query = "SELECT * FROM listfilm WHERE id LIKE '%"+str(filter_search)+"%' OR judul LIKE '%"+str(filter_search)+"%' OR tahun_rilis LIKE '%"+str(filter_search)+"%' OR genre LIKE '%"+str(filter_search)+"%'"
        result = self.connection.execute(query)
        self.tableWidgetHorror.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetHorror.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetHorror.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
        self.add_cariHorror.setText("")
    ##################################### -END LIST OF DRAMA- #####################################

    ##################################### -EXPORT NEW WINDOW FILM- #####################################
    def PlayFilmAction(self):
        playFilmAction.layoutFilmAction()

    def PlayFilmAdvanture(self):
        playFilmAdvanture.layoutFilmAdvanture()

    def PlayFilmComedy(self):
        playFilmComedy.layoutFilmComedy()

    def playFilmCrime(self):
        playFilmCrime.layoutFilmCrime()

    def playFilmDrama(self):
        playFilmDrama.layoutFilmDrama()

    def PlayFilmHorror(self):
        playFilmDrama.layoutFilmDrama()

    ##################################### -END OF EXPORT NEW WINDOW FILM- #####################################


if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #membuat style pada app dengan style fusion
    app.setStyle("fusion")
    #menambahkan icon pada tampilan window dengan nama file icon 'replay_ok.png'
    app.setWindowIcon(QIcon('replay_ok.png'))
    #membuat sebuah main window dengan nama variabel Mwindow
    window2 = QWidget()
    Mwindow = QMainWindow()
    ui = Login()
    ui.Loginwindow(Mwindow)
    #menampilkan isi mainwiondow dan membuat sistem exit
    Mwindow.show()
    sys.exit(app.exec_())