import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class FormulaMath(QWidget):
   #Membuat fungsi init untuk inisialisasi class FormulaMath
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #memanggil fungsi RumusDasar yang sudah dibuat agar ditampilkan hasilnya
        self.RumusDasar()

    #membuat fungsi dengan nama RumusDasar
    def RumusDasar(self):
        #membuat grid layout dengan nama variabel grid
        grid = QGridLayout()
        #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
        grid.setContentsMargins(10,10,10,10)

        #membuat sebuag QTabWidget dengan nama variabel tab
        tab = QTabWidget(self)
        #mengatur semua isi konten yang ada di tab menjadi tulisan bold berwarna hitam dengan ukuran 15px
        tab.setStyleSheet("font: bold 15px; color: black;")

        #membuat sebuag QTabWidget dengan nama variabel tab2
        tab2 = QTabWidget(self)
        #mengatur semua isi konten yang ada di tab2 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        tab2.setStyleSheet("font: bold 15px; color: black;")

        #membuat QVBoxLayout dengan nama variabel vbox,vbox2,vbox3,vbox4,vbox5,vbox6
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()
        vbox6 = QVBoxLayout()

        #membuat 6 buah groupbox dengan nama RWaktu, RKecepatan, RJarak, RDebit, RVolume, RWaktuD
        RWaktu = QGroupBox(self)
        RKecepatan = QGroupBox(self)
        RJarak = QGroupBox(self)
        RDebit = QGroupBox(self)
        RVolume = QGroupBox(self)
        RWaktuD = QGroupBox(self)

        #membuat vbox,vbox2,vbox3,vbox4,vbox5,vbox6 masing-masing menjadi layout utama tetapi berada di dalam RWaktu, RKecepatan, RJarak, RDebit, RVolume, RWaktuD
        RWaktu.setLayout(vbox)
        RKecepatan.setLayout(vbox2)
        RJarak.setLayout(vbox3)
        RDebit.setLayout(vbox4)
        RVolume.setLayout(vbox5)
        RWaktuD.setLayout(vbox6)

        #memasukkan RWaktu, RKecepatan, RJarak kedalam variabel tab atau QTabWidget
        tab.addTab(RWaktu,"Mencari Waktu")
        tab.addTab(RKecepatan,"Mencari Kecepatan")
        tab.addTab(RJarak,"Mencari Jarak")
        #memasukkan RDebit, RVolume, RWaktuD kedalam variabel tab2 atau QTabWidget
        tab2.addTab(RDebit,"Mencari Debit")
        tab2.addTab(RVolume,"Mencari Volume")
        tab2.addTab(RWaktuD,"Mencari Waktu")

        #membuat label dan diatur menjadi tulisan bold berwarna merah dengan ukuran 15px
        label = QLabel(self)
        label.setText("Rumus Dasar Kecepatan:")
        label.setStyleSheet("font: bold 15px; color: red;")
        #membuat label0 dan diatur menjadi tulisan bold berwarna merah dengan ukuran 15px
        label0 = QLabel(self)
        label0.setText("Rumus Dasar Debit:")
        label0.setStyleSheet("font: bold 15px; color: red;")

        #memasukkan label, label0, tab, tab2 kedalam layout utama grid
        grid.addWidget(label,1,0)
        grid.addWidget(label0,1,1)
        grid.addWidget(tab, 2, 0)
        grid.addWidget(tab2, 2, 1)

        #------------------------- KELOMPOK 1 KECEPATAN -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label1 = QLabel(self)
        label1.setText("Masukkan Jarak:")
        vbox.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel jarak
        self.jarak = QLineEdit(self)
        #mengatur jarak dengan border 0.5 px dan berwarna solid black
        self.jarak.setStyleSheet("border: 0.5px solid black;")
        #memasukkan jarak kedalam layout vbox
        vbox.addWidget(self.jarak)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Kecepatan:")
        vbox.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel kecepatan
        self.kecepatan = QLineEdit(self)
        #mengatur kecepatan dengan border 0.5 px dan berwarna solid black
        self.kecepatan.setStyleSheet("border: 0.5px solid black;")
        #memasukkan kecepatan kedalam layout vbox
        vbox.addWidget(self.kecepatan)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox
        vbox.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable hasil
        self.hasil = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.hasil.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox
        vbox.addWidget(self.hasil)

        #connect button to fungsi on_click
        self.cal_button.clicked.connect(self.on_click)
        #------------------------- END OF KELOMPOK 1 KECEPATAN -------------------------#

        #------------------------- KELOMPOK 2 KECEPATAN -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox2
        label1 = QLabel(self)
        label1.setText("Masukkan Jarak:")
        vbox2.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel jarak2
        self.jarak2 = QLineEdit(self)
        #mengatur jarak2 dengan border 0.5 px dan berwarna solid black
        self.jarak2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan jarak2 kedalam layout vbox2
        vbox2.addWidget(self.jarak2)
        #menambahkan addStretch ke dalam vbox2 agar tertata rapi
        vbox2.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox2
        label2 = QLabel(self)
        label2.setText("Masukkan Waktu:")
        vbox2.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel waktu2
        self.waktu2 = QLineEdit(self)
        #mengatur waktu2 dengan border 0.5 px dan berwarna solid black
        self.waktu2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan waktu2 kedalam layout vbox2
        vbox2.addWidget(self.waktu2)
        #menambahkan addStretch ke dalam vbox2 agar tertata rapi
        vbox2.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox2
        vbox2.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox2 agar tertata rapi
        vbox2.addStretch(1)

        #membuat sebuah button dengan nama variable hasil
        self.hasil2 = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil2.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.hasil2.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox2
        vbox2.addWidget(self.hasil2)

        #connect button to fungsi on_click2
        self.cal_button.clicked.connect(self.on_click2)
        #------------------------- END OF KELOMPOK 2 KECEPATAN -------------------------#

        #------------------------- KELOMPOK 3 KECEPATAN -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox3
        label1 = QLabel(self)
        label1.setText("Masukkan Kecepatan:")
        vbox3.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel kecepatan3
        self.kecepatan3 = QLineEdit(self)
        #mengatur kecepatan3 dengan border 0.5 px dan berwarna solid black
        self.kecepatan3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan kecepatan3 kedalam layout vbox3
        vbox3.addWidget(self.kecepatan3)
        #menambahkan addStretch ke dalam vbox3 agar tertata rapi
        vbox3.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox3
        label2 = QLabel(self)
        label2.setText("Masukkan Waktu:")
        vbox3.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel waktu3
        self.waktu3 = QLineEdit(self)
        #mengatur waktu3 dengan border 0.5 px dan berwarna solid black
        self.waktu3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan waktu3 kedalam layout vbox3
        vbox3.addWidget(self.waktu3)
        #menambahkan addStretch ke dalam vbox3 agar tertata rapi
        vbox3.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox3
        vbox3.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox3 agar tertata rapi
        vbox3.addStretch(1)

        #membuat sebuah button dengan nama variable hasil
        self.hasil3 = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil3.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.hasil3.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox3
        vbox3.addWidget(self.hasil3)

        #connect button to fungsi on_click3
        self.cal_button.clicked.connect(self.on_click3)
        #------------------------- END OF KELOMPOK 3 KECEPATAN -------------------------#

        #------------------------- KELOMPOK 1 DEBIT -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox4
        label1 = QLabel(self)
        label1.setText("Masukkan Volume:")
        vbox4.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel volume1
        self.volume1 = QLineEdit(self)
        #mengatur volume1 dengan border 0.5 px dan berwarna solid black
        self.volume1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan volume1 kedalam layout vbox4
        vbox4.addWidget(self.volume1)
        #menambahkan addStretch ke dalam vbox4 agar tertata rapi
        vbox4.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox4
        label2 = QLabel(self)
        label2.setText("Masukkan Waktu:")
        vbox4.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel waktud1
        self.waktud1 = QLineEdit(self)
        #mengatur waktud1 dengan border 0.5 px dan berwarna solid black
        self.waktud1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan waktud1 kedalam layout vbox4
        vbox4.addWidget(self.waktud1)
        #menambahkan addStretch ke dalam vbox4 agar tertata rapi
        vbox4.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox4
        vbox4.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox4 agar tertata rapi
        vbox4.addStretch(1)

        #membuat sebuah button dengan nama variable hasil4
        self.hasil4 = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil4.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil4 dengan setDisabled agar tidak daat diklik
        self.hasil4.setDisabled(True)
        #memasukkan button hasil4 ke dalam layout vbox4
        vbox4.addWidget(self.hasil4)

        #connect button to fungsi on_click4
        self.cal_button.clicked.connect(self.on_click4)
        #------------------------- END OF KELOMPOK 1 DEBIT -------------------------#

        #------------------------- KELOMPOK 2 DEBIT -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox5
        label1 = QLabel(self)
        label1.setText("Masukkan Debit:")
        vbox5.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel debit2
        self.debit2 = QLineEdit(self)
        #mengatur debit2 dengan border 0.5 px dan berwarna solid black
        self.debit2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan debit2 kedalam layout vbox5
        vbox5.addWidget(self.debit2)
        #menambahkan addStretch ke dalam vbox2 agar tertata rapi
        vbox5.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox5
        label2 = QLabel(self)
        label2.setText("Masukkan Waktu:")
        vbox5.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel waktud2
        self.waktud2 = QLineEdit(self)
        #mengatur waktud2 dengan border 0.5 px dan berwarna solid black
        self.waktud2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan waktud2 kedalam layout vbox5
        vbox5.addWidget(self.waktud2)
        #menambahkan addStretch ke dalam vbox5 agar tertata rapi
        vbox5.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox5
        vbox5.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox5 agar tertata rapi
        vbox5.addStretch(1)

        #membuat sebuah button dengan nama variable hasil5
        self.hasil5 = QPushButton("Hasil", self)
        ##mengatur hasil5 dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil5.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil5 dengan setDisabled agar tidak daat diklik
        self.hasil5.setDisabled(True)
        #memasukkan button hasil5 ke dalam layout vbox4
        vbox5.addWidget(self.hasil5)

        #connect button to fungsi on_click5
        self.cal_button.clicked.connect(self.on_click5)
        #------------------------- END OF KELOMPOK 2 DEBIT -------------------------#

        #------------------------- KELOMPOK 3 DEBIT -------------------------#
        #membuat label1 dan akan dimasukkan ke dalam layout vbox6
        label1 = QLabel(self)
        label1.setText("Masukkan Volume:")
        vbox6.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel volume3
        self.volume3 = QLineEdit(self)
        #mengatur volume3 dengan border 0.5 px dan berwarna solid black
        self.volume3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan volume3 kedalam layout vbox6
        vbox6.addWidget(self.volume3)
        #menambahkan addStretch ke dalam vbox6 agar tertata rapi
        vbox6.addStretch()
        
        #membuat label2 dan akan dimasukkan ke dalam layout vbox6
        label2 = QLabel(self)
        label2.setText("Masukkan Debit:")
        vbox6.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel debit3
        self.debit3 = QLineEdit(self)
        #mengatur debit3 dengan border 0.5 px dan berwarna solid black
        self.debit3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan debit3 kedalam layout vbox6
        vbox6.addWidget(self.debit3)
        #menambahkan addStretch ke dalam vbox6 agar tertata rapi
        vbox6.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.cal_button = QPushButton("Calculate", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.cal_button.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox6
        vbox6.addWidget(self.cal_button)
        #menambahkan addStretch ke dalam vbox6 agar tertata rapi
        vbox6.addStretch(1)

        #membuat sebuah button dengan nama variable hasil6
        self.hasil6 = QPushButton("Hasil", self)
        ##mengatur hasil6 dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil6.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil6 dengan setDisabled agar tidak daat diklik
        self.hasil6.setDisabled(True)
        #memasukkan button hasil6 ke dalam layout vbox6
        vbox6.addWidget(self.hasil6)

        #connect button to fungsi on_click6
        self.cal_button.clicked.connect(self.on_click6)
        #------------------------- END OF KELOMPOK 3 DEBIT -------------------------#

        #membuat grid menjadi layout utama di window
        self.setLayout(grid)


    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai Waktu
    def on_click(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Jarak dan Kecepatan yang berisi inputan dari jarak dan kecepatan yang akan dirubah menjadi sebuah float
            Jarak = float(self.jarak.text())
            Kecepatan = float(self.kecepatan.text()) 
            #membuat variabel Waktu untuk menghitung nilai waktu  
            Waktu = Jarak/Kecepatan
            #menampilkan nilai Waktu pada button hasil
            self.hasil.setText("Nilai Waktu: " + str("%.2f" %Waktu))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada jarak dan kecepatan diisi kosong
            if str(self.jarak.text()) =="" and str(self.kecepatan.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada jarak diisi kosong
            elif str(self.jarak.text()) =="" and str(self.kecepatan.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Jarak Dengan Benar!", "Tolong masukkan nilai jarak dengan sebuah angka! ", notif.Ok)

            #jika pada kecepatan diisi kosong
            elif str(self.jarak.text()) !="" and str(self.kecepatan.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Kecepatan Dengan Benar!", "Tolong masukkan nilai kecepatan dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

    #membuat fungsi on_click2 yang berisi sistem untuk menghitung nilai Kecepatan
    def on_click2(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Jarak2 dan Waktu2 yang berisi inputan dari jarak2 dan waktu2 yang akan dirubah menjadi sebuah float
            Jarak2 = float(self.jarak2.text())
            Waktu2 = float(self.waktu2.text())
            #membuat variabel Kecepatan2 untuk menghitung nilai Kecepatan  
            Kecepatan2 = Jarak2/Waktu2
            #menampilkan nilai Kecepatan pada button hasil
            self.hasil2.setText("Nilai Kecepatan: " + str("%.2f" %Kecepatan2))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada jarak2 dan waktu2 diisi kosong
            if str(self.jarak2.text()) =="" and str(self.waktu2.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada jarak2 diisi kosong
            elif str(self.jarak2.text()) =="" and str(self.waktu2.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Jarak Dengan Benar!", "Tolong masukkan nilai jarak dengan sebuah angka! ", notif.Ok)

            #jika pada waktu2 diisi kosong
            elif str(self.jarak2.text()) !="" and str(self.waktu2.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Waktu Dengan Benar!", "Tolong masukkan nilai waktu dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

    #membuat fungsi on_click3 yang berisi sistem untuk menghitung nilai Jarak
    def on_click3(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Kecepatan3 dan Waktu3 yang berisi inputan dari kecepatan3 dan waktu3 yang akan dirubah menjadi sebuah float
            Kecepatan3 = float(self.kecepatan3.text())
            Waktu3 = float(self.waktu3.text()) 
            #membuat variabel Jarak3 untuk menghitung nilai Jarak  
            Jarak3 = Kecepatan3*Waktu3
            #menampilkan nilai Jarak3 pada button hasil
            self.hasil3.setText("Nilai Jarak: " + str("%.2f" %Jarak3))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada kecepatan3 dan waktu3 diisi kosong
            if str(self.kecepatan3.text()) =="" and str(self.waktu3.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada kecepatan3 diisi kosong
            elif str(self.kecepatan3.text()) =="" and str(self.waktu3.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Kecepatan Dengan Benar!", "Tolong masukkan nilai kecepatan dengan sebuah angka! ", notif.Ok)

            #jika pada waktu3 diisi kosong
            elif str(self.kecepatan3.text()) !="" and str(self.waktu3.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Waktu Dengan Benar!", "Tolong masukkan nilai waktu dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

    #membuat fungsi on_click4 yang berisi sistem untuk menghitung nilai Debit
    def on_click4(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Volume dan Waktud yang berisi inputan dari volume1 dan waktud1 yang akan dirubah menjadi sebuah float
            Volume = float(self.volume1.text())
            Waktud = float(self.waktud1.text()) 
            #membuat variabel Debit untuk menghitung nilai debit  
            Debit = Volume/Waktud
            #menampilkan nilai debit pada button hasil4
            self.hasil4.setText("Nilai Debit: " + str("%.2f" %Debit))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada volume1 dan waktud1 diisi kosong
            if str(self.volume1.text()) =="" and str(self.waktud1.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada jarak volume1 kosong
            elif str(self.volume1.text()) =="" and str(self.waktud1.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Volume Dengan Benar!", "Tolong masukkan nilai volume dengan sebuah angka! ", notif.Ok)

            #jika pada waktud1 diisi kosong
            elif str(self.volume1.text()) !="" and str(self.waktud1.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Waktu Dengan Benar!", "Tolong masukkan nilai waktu dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

    #membuat fungsi on_click5 yang berisi sistem untuk menghitung nilai Volume
    def on_click5(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Debit2 dan Waktud2 yang berisi inputan dari debit2 dan waktud2 yang akan dirubah menjadi sebuah float
            Debit2 = float(self.debit2.text())
            Waktud2 = float(self.waktud2.text())
            #membuat variabel Volume2 untuk menghitung nilai Volume  
            Volume2 = Debit2 * Waktud2
            #menampilkan nilai Volume pada button hasil5
            self.hasil5.setText("Nilai Kecepatan: " + str("%.2f" %Volume2))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada debit2 dan waktud2 diisi kosong
            if str(self.debit2.text()) =="" and str(self.waktud2.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada debit2 diisi kosong
            elif str(self.debit2.text()) =="" and str(self.waktud2.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Debit Dengan Benar!", "Tolong masukkan nilai debit dengan sebuah angka! ", notif.Ok)

            #jika pada waktud2 diisi kosong
            elif str(self.debit2.text()) !="" and str(self.waktud2.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Waktu Dengan Benar!", "Tolong masukkan nilai waktu dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

    #membuat fungsi on_click6 yang berisi sistem untuk menghitung nilai Waktu
    def on_click6(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel Volume3 dan Debit3 yang berisi inputan dari volume3 dan debit3 yang akan dirubah menjadi sebuah float
            Volume3 = float(self.volume3.text())
            Debit3 = float(self.debit3.text()) 
            #membuat variabel Waktud3 untuk menghitung nilai Waktu  
            Waktud3 = Volume3/Debit3
            #menampilkan nilai Waktud3 pada button hasil6
            self.hasil6.setText("Nilai Jarak: " + str("%.2f" %Waktud3))
        ############ SISTEM VALIDASI INPUT ############
        except:
            #jika pada volume3 dan debit3 diisi kosong
            if str(self.volume3.text()) =="" and str(self.debit3.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada volume3 diisi kosong
            elif str(self.volume3.text()) =="" and str(self.debit3.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Nilai Volume Dengan Benar!", "Tolong masukkan nilai volume dengan sebuah angka! ", notif.Ok)

            #jika pada debit3 diisi kosong
            elif str(self.volume3.text()) !="" and str(self.debit3.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Debit Dengan Benar!", "Tolong masukkan nilai debit dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongan
            else:
                #maka meesage box akan menampilkan sebuah warning 
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)


if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #mengatur style di window menjadi style fusion
    app.setStyle("fusion")
    #menambahkan icon pada window
    app.setWindowIcon(QIcon('math.png'))
    #membuat variabel ex yang berisi class FormulaMath
    ex = FormulaMath()

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,1000,300)
    #membuat judul window
    ex.setWindowTitle("Rumus - Rumus Dasar Matematika")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())