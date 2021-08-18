import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


#Membuat class yang didalamnya terdapat QWidget
class BMI(QWidget):
    totalBayar = 0
   #Membuat fungsi init untuk inisialisasi class BMI
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #memanggil fungsi BMI_Calculate yang sudah dibuat agar ditampilkan hasilnya
        self.BMI_Calculate()

    #membuat fungsi BMI calculate
    def BMI_Calculate(self):
        #membuat grid layout dengan nama variabel grid
        grid = QGridLayout()
        #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
        grid.setContentsMargins(10,10,10,10)

        #membuat sebuag QGroupBox dengan nama variabel group1
        group1 = QGroupBox("Warung Online",self)
        #mengatur semua isi konten yang ada di group1 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        group1.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group1 kedalam layout grid
        grid.addWidget(group1, 1, 0)
        #membuat QVBoxLayout dengan nama variabel vbox
        vbox = QVBoxLayout()
        #membuat QVBoxLayout dengan nama variabel vbox
        hbox = QHBoxLayout()
        #membuat QVBoxLayout dengan nama variabel vbox
        hbox2 = QHBoxLayout()
        #membuat vbox menjadi layout utama tetapi berada di dalam group1
        group1.setLayout(vbox)
        vbox.addLayout(hbox)
        

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label1 = QLabel(self)
        label1.setText("Masukkan Nomor Makanan Yang Akan Dipesan:")
        vbox.addWidget(label1)
        
        x1 = QLabel("|  (1) Nasi Goreng  | ", self)
        hbox.addWidget(x1)
        x2 = QLabel("(2) Bakso  | ", self)
        hbox.addWidget(x2)
        x3 = QLabel("(3) Pecel  | ", self)
        hbox.addWidget(x3)
        x4 = QLabel("(4) Gado - Gado  | ", self)
        hbox.addWidget(x4)
        x5 = QLabel("(5) Ayam Geprek  |", self)
        hbox.addWidget(x5)

        #membuat QLineEdit dengan nama variabel height_input
        self.makan = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.makan.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addWidget(self.makan)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch()

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label1 = QLabel(self)
        label1.setText("Masukkan Jumlah Makanan Yang Anda Pesan:")
        vbox.addWidget(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.jumlah_makan = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.jumlah_makan.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addWidget(self.jumlah_makan)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch()
        
        vbox.addLayout(hbox2)

        y1 = QLabel("|  (1) Jus Alpukat  | ", self)
        hbox2.addWidget(y1)
        y2 = QLabel("(2) Es Campur  | ", self)
        hbox2.addWidget(y2)
        y3 = QLabel("(3) Es Teh  | ", self)
        hbox2.addWidget(y3)
        y4 = QLabel("(4) Es Jeruk  | ", self)
        hbox2.addWidget(y4)
        y5 = QLabel("(5) Air Putih  | ", self)
        hbox2.addWidget(y5)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Nomor Minuman Yang Akan Dipesan:")
        vbox.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel weight_input
        self.minum = QLineEdit(self)
        #mengatur weight_input dengan border 0.5 px dan berwarna solid black
        self.minum.setStyleSheet("border: 0.5px solid black;")
        #memasukkan weight_input kedalam layout vbox
        vbox.addWidget(self.minum)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Jumlah Minuman Yang Anda Pesan:")
        vbox.addWidget(label2)

        #membuat QLineEdit dengan nama variabel weight_input
        self.jumlah_minum = QLineEdit(self)
        #mengatur weight_input dengan border 0.5 px dan berwarna solid black
        self.jumlah_minum.setStyleSheet("border: 0.5px solid black;")
        #memasukkan weight_input kedalam layout vbox
        vbox.addWidget(self.jumlah_minum)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.pesan = QPushButton("Pesan!", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.pesan.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox
        vbox.addWidget(self.pesan)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable hasil
        self.tagihan = QPushButton("Tagihan", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.tagihan.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.tagihan.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox
        vbox.addWidget(self.tagihan)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Jumlah Uang Anda:")
        vbox.addWidget(label2)

        #membuat QLineEdit dengan nama variabel weight_input
        self.uang_user = QLineEdit(self)
        #mengatur weight_input dengan border 0.5 px dan berwarna solid black
        self.uang_user.setStyleSheet("border: 0.5px solid black;")
        #memasukkan weight_input kedalam layout vbox
        vbox.addWidget(self.uang_user)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable cal_button
        self.bayar = QPushButton("Pesan!", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.bayar.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox
        vbox.addWidget(self.bayar)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch(1)

        #membuat sebuah button dengan nama variable hasil
        self.kembalian = QPushButton("Kembalian", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.kembalian.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.kembalian.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox
        vbox.addWidget(self.kembalian)

        #connect button to fungsi on_click
        self.pesan.clicked.connect(self.on_click)
        #connect button to fungsi on_click
        self.bayar.clicked.connect(self.on_click2)
        #membuat grid menjadi layout utama di window
        self.setLayout(grid)
    
    
    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai BMI
    def on_click(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        #membuat variabel weight dan height yang berisi inputan dari weight_input dan height_input yang akan dirubah menjadi sebuah float
        Makan = int(self.makan.text())
        Jumlah_Makan = int(self.jumlah_makan.text())
        Minum = int(self.minum.text())
        Jumlah_Minum = int(self.jumlah_minum.text())
        total1 = 0
        total2 = 0
        
        #menampilkan nilai BMI pada button hasil
        #self.hasil.setText("Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI))
        #jika pada weight_input dan height_input diisi kosong
        if Makan == 1:
            total1 = 15000 * Jumlah_Makan
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Makan == 2:
            total1 = 14000 * Jumlah_Makan
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Makan == 3:
            total1 = 13000 * Jumlah_Makan
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Makan == 4:
            total1 = 12000 * Jumlah_Makan
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Makan == 5:
            total1 = 11000 * Jumlah_Makan
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        #jika yang diiskan selain angka dan kosongana
        else:
            #maka meesage box akan menampilkan sebuah warning 
            notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

        if Minum == 1:
            total2 = 5000 * Jumlah_Minum
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Minum == 2:
            total2 = 4000 * Jumlah_Minum
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Minum == 3:
            total2 = 3000 * Jumlah_Minum
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Minum == 4:
            total2 = 2000 * Jumlah_Minum
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        elif Minum == 5:
            total2 = 1000 * Jumlah_Minum
            #maka meesage box akan menampilkan sebuah warning
            #notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)
        #jika yang diiskan selain angka dan kosongana
        else:
            #maka meesage box akan menampilkan sebuah warning 
            notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

        totalBayar = total1 + total2
        

        #menampilkan nilai BMI pada button hasil
        self.tagihan.setText("Tagihan Anda: " + str(totalBayar))
        return totalBayar
    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai BMI
    def on_click2(self): 
        nextStep = True  
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        if nextStep == True:
            Uang = int(self.uang_user.text())
            totalKembalian = Uang - totalBayar
            #menampilkan nilai BMI pada button hasil
            self.kembalian.setText("Kembalian Anda: " + str(totalKembalian)) 
                    

if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #mengatur style di window menjadi style fusion
    app.setStyle("fusion")
    #menambahkan icon pada window
    app.setWindowIcon(QIcon('bmi_logo.ico'))
    #membuat variabel ex yang berisi class BMI
    ex = BMI()

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,500,250)
    #membuat judul window
    ex.setWindowTitle("BMI (Body Mass Index) Calculator")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())   