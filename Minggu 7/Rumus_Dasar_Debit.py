import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#GLOBAL
#Inisisalisai pyqt
app = QApplication(sys.argv)
#mengatur style di window menjadi style fusion
app.setStyle("fusion")
#menambahkan icon pada window
app.setWindowIcon(QIcon('math.png'))

#membuat variabel ex yang berisi fungsi QWidget
ex = QWidget()
#variabel self berisi nilai ex yang berarti berisi QWidget
self = ex

#membuat QLineEdit dengan nama variabel volume1  
self.volume1 = QLineEdit(self)
#membuat QLineEdit dengan nama variabel waktud1
self.waktud1 = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button
self.cal_button = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil4
self.hasil4 = QPushButton("Hasil", self)

#membuat QLineEdit dengan nama variabel debit2 
self.debit2 = QLineEdit(self)
#membuat QLineEdit dengan nama variabel waktud2
self.waktud2 = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button2
self.cal_button2 = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil5
self.hasil5 = QPushButton("Hasil", self)

#membuat QLineEdit dengan nama variabel volume3 
self.volume3 = QLineEdit(self)
#membuat QLineEdit dengan nama variabel debit3
self.debit3 = QLineEdit(self)
#membuat sebuah button dengan nama variable cal_button3
self.cal_button3 = QPushButton("Calculate", self)
#membuat sebuah button dengan nama variable hasil6
self.hasil6 = QPushButton("Hasil", self)


#membuat fungsi dengan nama Layout
def Layout():
    #membuat grid layout dengan nama variabel grid
    grid = QGridLayout()
    #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
    grid.setContentsMargins(10,10,10,10)

    #membuat sebuag QTabWidget dengan nama variabel tab2
    tab2 = QTabWidget(self)
    #mengatur semua isi konten yang ada di tab2 menjadi tulisan bold berwarna hitam dengan ukuran 15px
    tab2.setStyleSheet("font: bold 15px; color: black;")

    #membuat QVBoxLayout dengan nama variabel vbox4,vbox5,vbox6
    vbox4 = QVBoxLayout()
    vbox5 = QVBoxLayout()
    vbox6 = QVBoxLayout()

    #membuat 3 buah groupbox dengan nama RDebit, RVolume, RWaktuD
    RDebit = QGroupBox(self)
    RVolume = QGroupBox(self)
    RWaktuD = QGroupBox(self)

    #membuat vbox4,vbox5,vbox6 masing-masing menjadi layout utama tetapi berada di dalam RDebit, RVolume, RWaktuD
    RDebit.setLayout(vbox4)
    RVolume.setLayout(vbox5)
    RWaktuD.setLayout(vbox6)

    #memasukkan RDebit, RVolume, RWaktuD kedalam variabel tab2 atau QTabWidget
    tab2.addTab(RDebit,"Mencari Debit")
    tab2.addTab(RVolume,"Mencari Volume")
    tab2.addTab(RWaktuD,"Mencari Waktu")

    #membuat label0 dan diatur menjadi tulisan bold berwarna merah dengan ukuran 15px
    label0 = QLabel(self)
    label0.setText("Rumus Dasar Debit:")
    label0.setStyleSheet("font: bold 15px; color: red;")

    #memasukkan label0, tab2 kedalam layout utama grid
    grid.addWidget(label0,1,1)
    grid.addWidget(tab2, 2, 1)

    #------------------------- KELOMPOK 1 DEBIT -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox4
    label1 = QLabel(self)
    label1.setText("Masukkan Volume:")
    vbox4.addWidget(label1)
    
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
    
    #mengatur waktud1 dengan border 0.5 px dan berwarna solid black
    self.waktud1.setStyleSheet("border: 0.5px solid black;")
    #memasukkan waktud1 kedalam layout vbox4
    vbox4.addWidget(self.waktud1)
    #menambahkan addStretch ke dalam vbox4 agar tertata rapi
    vbox4.addStretch(1)
    
    #mengatur cal_button dengan background berwarna #33f8c7
    self.cal_button.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button kedalam layout vbox4
    vbox4.addWidget(self.cal_button)
    #menambahkan addStretch ke dalam vbox4 agar tertata rapi
    vbox4.addStretch(1)
    
    ##mengatur hasil4 dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil4.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil4 dengan setDisabled agar tidak daat diklik
    self.hasil4.setDisabled(True)
    #memasukkan button hasil4 ke dalam layout vbox4
    vbox4.addWidget(self.hasil4)

    #connect button to fungsi on_click4
    self.cal_button.clicked.connect(on_click4)
    #------------------------- END OF KELOMPOK 1 DEBIT -------------------------#

    #------------------------- KELOMPOK 2 DEBIT -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox5
    label1 = QLabel(self)
    label1.setText("Masukkan Debit:")
    vbox5.addWidget(label1)
    
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
    
    #mengatur waktud2 dengan border 0.5 px dan berwarna solid black
    self.waktud2.setStyleSheet("border: 0.5px solid black;")
    #memasukkan waktud2 kedalam layout vbox5
    vbox5.addWidget(self.waktud2)
    #menambahkan addStretch ke dalam vbox5 agar tertata rapi
    vbox5.addStretch(1)
    
    #mengatur cal_button2 dengan background berwarna #33f8c7
    self.cal_button2.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button2 kedalam layout vbox5
    vbox5.addWidget(self.cal_button2)
    #menambahkan addStretch ke dalam vbox5 agar tertata rapi
    vbox5.addStretch(1)

    ##mengatur hasil5 dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil5.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil5 dengan setDisabled agar tidak daat diklik
    self.hasil5.setDisabled(True)
    #memasukkan button hasil5 ke dalam layout vbox4
    vbox5.addWidget(self.hasil5)

    #connect button to fungsi on_click5
    self.cal_button2.clicked.connect(on_click5)
    #------------------------- END OF KELOMPOK 2 DEBIT -------------------------#

    #------------------------- KELOMPOK 3 DEBIT -------------------------#
    #membuat label1 dan akan dimasukkan ke dalam layout vbox6
    label1 = QLabel(self)
    label1.setText("Masukkan Volume:")
    vbox6.addWidget(label1)
    
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
    
    #mengatur debit3 dengan border 0.5 px dan berwarna solid black
    self.debit3.setStyleSheet("border: 0.5px solid black;")
    #memasukkan debit3 kedalam layout vbox6
    vbox6.addWidget(self.debit3)
    #menambahkan addStretch ke dalam vbox6 agar tertata rapi
    vbox6.addStretch(1)
    
    #mengatur cal_button dengan background berwarna #33f8c7
    self.cal_button3.setStyleSheet("background-color: #33f8c7;")
    #memasukkan cal_button kedalam layout vbox6
    vbox6.addWidget(self.cal_button3)
    #menambahkan addStretch ke dalam vbox6 agar tertata rapi
    vbox6.addStretch(1)
    
    ##mengatur hasil6 dengan font bold dan ukuran 20px dan berwarna hitam
    self.hasil6.setStyleSheet("font: bold 20px; color: black")
    #mengatur button hasil6 dengan setDisabled agar tidak daat diklik
    self.hasil6.setDisabled(True)
    #memasukkan button hasil6 ke dalam layout vbox6
    vbox6.addWidget(self.hasil6)

    #connect button to fungsi on_click6
    self.cal_button3.clicked.connect(on_click6)
    #------------------------- END OF KELOMPOK 3 DEBIT -------------------------#
    
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

#membuat fungsi on_click4 yang berisi sistem untuk menghitung nilai Debit
def on_click4():   
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
def on_click5():   
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
def on_click6():   
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
    #memanggil fungsi Layout untuk menampilkan seluruh isi widget
    Layout()
    