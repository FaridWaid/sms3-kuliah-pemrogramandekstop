import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#Inisisalisai pyqt
app = QApplication(sys.argv)
#mengatur style di window menjadi style fusion
app.setStyle("fusion")
#menambahkan icon pada window
app.setWindowIcon(QIcon('math.png'))

#membuat variabel ex yang berisi QWidget
ex = QWidget()
#variabel self berisi nilai ex yang saam saja dengan QWidget
self = ex

#membuat QLineEdit dengan nama variabel jarak 
self.jarak = QLineEdit(self)
#membuat QLineEdit dengan nama variabel kecepatan
self.kecepatan = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button
self.cal_button = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil
self.hasil = QPushButton("Hasil", self)

#membuat QLineEdit dengan nama variabel jarak2
self.jarak2 = QLineEdit(self)
#membuat QLineEdit dengan nama variabel waktu2
self.waktu2 = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button2
self.cal_button2 = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil2
self.hasil2 = QPushButton("Hasil", self)

#membuat QLineEdit dengan nama variabel kecepatan3
self.kecepatan3 = QLineEdit(self)
#membuat QLineEdit dengan nama variabel waktu3
self.waktu3 = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button3
self.cal_button3 = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil3
self.hasil3 = QPushButton("Hasil", self)

#membuat fungsi dengan nama Layout
def Layout():
    #membuat grid layout dengan nama variabel grid
    grid = QGridLayout()
    #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
    grid.setContentsMargins(10,10,10,10)

    #membuat sebuag QTabWidget dengan nama variabel tab
    tab = QTabWidget(self)
    #mengatur semua isi konten yang ada di tab menjadi tulisan bold berwarna hitam dengan ukuran 15px
    tab.setStyleSheet("font: bold 15px; color: black;")

    #membuat QVBoxLayout dengan nama variabel vbox,vbox2,vbox3
    vbox = QVBoxLayout()
    vbox2 = QVBoxLayout()
    vbox3 = QVBoxLayout()

    #membuat 6 buah groupbox dengan nama RWaktu, RKecepatan, RJarak
    RWaktu = QGroupBox(self)
    RKecepatan = QGroupBox(self)
    RJarak = QGroupBox(self)

    #membuat vbox,vbox2,vbox3,vbox4 masing-masing menjadi layout utama tetapi berada di dalam RWaktu, RKecepatan, RJarak
    RWaktu.setLayout(vbox)
    RKecepatan.setLayout(vbox2)
    RJarak.setLayout(vbox3)

    #memasukkan RWaktu, RKecepatan, RJarak kedalam variabel tab atau QTabWidget
    tab.addTab(RWaktu,"Mencari Waktu")
    tab.addTab(RKecepatan,"Mencari Kecepatan")
    tab.addTab(RJarak,"Mencari Jarak")

    #membuat label dan diatur menjadi tulisan bold berwarna merah dengan ukuran 15px
    label = QLabel(self)
    label.setText("Rumus Dasar Kecepatan:")
    label.setStyleSheet("font: bold 15px; color: red;")

    #memasukkan label, tab kedalam layout utama grid
    grid.addWidget(label,1,0)
    grid.addWidget(tab, 2, 0)

    #------------------------- KELOMPOK 1 KECEPATAN -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox
    label1 = QLabel(self)
    label1.setText("Masukkan Jarak:")
    vbox.addWidget(label1)
    
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
    
    #mengatur kecepatan dengan border 0.5 px dan berwarna solid black
    self.kecepatan.setStyleSheet("border: 0.5px solid black;")
    #memasukkan kecepatan kedalam layout vbox
    vbox.addWidget(self.kecepatan)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch(1)

    #mengatur cal_button dengan background berwarna #33f8c7
    self.cal_button.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button kedalam layout vbox
    vbox.addWidget(self.cal_button)
    #menambahkan addStretch ke dalam vbox agar tertata rapi
    vbox.addStretch(1)

    ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil dengan setDisabled agar tidak daat diklik
    self.hasil.setDisabled(True)
    #memasukkan button hasil ke dalam layout vbox
    vbox.addWidget(self.hasil)

    #connect button to fungsi on_click
    self.cal_button.clicked.connect(on_click)
    #------------------------- END OF KELOMPOK 1 KECEPATAN -------------------------#

    #------------------------- KELOMPOK 2 KECEPATAN -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox2
    label1 = QLabel(self)
    label1.setText("Masukkan Jarak:")
    vbox2.addWidget(label1)
    
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
    
    #mengatur waktu2 dengan border 0.5 px dan berwarna solid black
    self.waktu2.setStyleSheet("border: 0.5px solid black;")
    #memasukkan waktu2 kedalam layout vbox2
    vbox2.addWidget(self.waktu2)
    #menambahkan addStretch ke dalam vbox2 agar tertata rapi
    vbox2.addStretch(1)
    
    #mengatur cal_button2 dengan background berwarna #33f8c7
    self.cal_button2.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button2 kedalam layout vbox2
    vbox2.addWidget(self.cal_button2)
    #menambahkan addStretch ke dalam vbox2 agar tertata rapi
    vbox2.addStretch(1)
    
    ##mengatur hasil2 dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil2.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil2 dengan setDisabled agar tidak daat diklik
    self.hasil2.setDisabled(True)
    #memasukkan button hasil2 ke dalam layout vbox2
    vbox2.addWidget(self.hasil2)

    #connect button to fungsi on_click2
    self.cal_button2.clicked.connect(on_click2)
    #------------------------- END OF KELOMPOK 2 KECEPATAN -------------------------#

    #------------------------- KELOMPOK 3 KECEPATAN -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox3
    label1 = QLabel(self)
    label1.setText("Masukkan Kecepatan:")
    
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
    
    #mengatur waktu3 dengan border 0.5 px dan berwarna solid black
    self.waktu3.setStyleSheet("border: 0.5px solid black;")
    #memasukkan waktu3 kedalam layout vbox3
    vbox3.addWidget(self.waktu3)
    #menambahkan addStretch ke dalam vbox3 agar tertata rapi
    vbox3.addStretch(1)
    
    #mengatur cal_button3 dengan background berwarna #33f8c7
    self.cal_button3.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button3 kedalam layout vbox3
    vbox3.addWidget(self.cal_button3)
    #menambahkan addStretch ke dalam vbox3 agar tertata rapi
    vbox3.addStretch(1)
    
    ##mengatur hasil3 dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil3.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil3 dengan setDisabled agar tidak daat diklik
    self.hasil3.setDisabled(True)
    #memasukkan button hasil3 ke dalam layout vbox3
    vbox3.addWidget(self.hasil3)

    #connect button to fungsi on_click3
    self.cal_button3.clicked.connect(on_click3)
    #------------------------- END OF KELOMPOK 3 KECEPATAN -------------------------#

    #membuat grid menjadi layout utama di window
    ex.setLayout(grid)

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,500,300)
    #membuat judul window
    ex.setWindowTitle("Rumus Dasar Debit")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    #sys.exit(app.exec_())

#membuat fungsi on_click yang berisi sistem untuk menghitung nilai Waktu
def on_click():   
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
def on_click2():   
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
def on_click3():   
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

if __name__ == '__main__':
    #memanggil fungsi Layout untuk menampilkan seluruh isi widget
    Layout()