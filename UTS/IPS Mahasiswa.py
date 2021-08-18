import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


#Membuat class yang didalamnya terdapat QWidget
class IPS(QWidget):
    totalBayar = 0
   #Membuat fungsi init untuk inisialisasi class BMI
    def __init__(self):
        #untuk mengembalikan semua atribut dan method yang ada
        super().__init__()
        #memanggil fungsi BMI_Calculate yang sudah dibuat agar ditampilkan hasilnya
        self.IPS_Calculate()

    #membuat fungsi BMI calculate
    def IPS_Calculate(self):
        #membuat grid layout dengan nama variabel grid
        grid = QGridLayout()
        #mengatur batas pada isi conten layout grid yaitu batas kana,kiri,atas,bawah bernilai 10
        grid.setContentsMargins(10,10,10,10)

        #membuat sebuag QGroupBox dengan nama variabel group1
        group1 = QGroupBox("Hitung IPS Online",self)
        #mengatur semua isi konten yang ada di group1 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        group1.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group1 kedalam layout grid
        grid.addWidget(group1, 1, 0)
        #membuat sebuag QGroupBox dengan nama variabel group1
        group2 = QGroupBox("Hitung IPS Online",self)
        #mengatur semua isi konten yang ada di group1 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        group2.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group1 kedalam layout grid
        grid.addWidget(group2, 1, 1)
        #membuat QVBoxLayout dengan nama variabel vbox
        vbox = QFormLayout()
        #membuat QVBoxLayout dengan nama variabel vbox
        vbox2 = QVBoxLayout()
        #membuat QVBoxLayout dengan nama variabel vbox
        group1.setLayout(vbox)
        group2.setLayout(vbox2)
        
        

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 1:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label1,self.nama1)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Besar SKS 1:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label2,self.sks1)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label3 = QLabel(self)
        label3.setText("Masukkan Nilai Mata Kuliah 1:")

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label3,self.nilai1)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label4 = QLabel(self)
        label4.setText("Masukkan Nama Mata Kuliah 2:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label4,self.nama2)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label5 = QLabel(self)
        label5.setText("Masukkan Besar SKS 2:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label5,self.sks2)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label6 = QLabel(self)
        label6.setText("Masukkan Nilai Mata Kuliah 2:")

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label6,self.nilai2)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label7 = QLabel(self)
        label7.setText("Masukkan Nama Mata Kuliah 3:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label7,self.nama3)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label8 = QLabel(self)
        label8.setText("Masukkan Besar SKS 3:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label8,self.sks3)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label9 = QLabel(self)
        label9.setText("Masukkan Nilai Mata Kuliah 3:")

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label9,self.nilai3)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label10 = QLabel(self)
        label10.setText("Masukkan Nama Mata Kuliah 4:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label10,self.nama4)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label11 = QLabel(self)
        label11.setText("Masukkan Besar SKS 4:")
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label11,self.sks4)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label12 = QLabel(self)
        label12.setText("Masukkan Nilai Mata Kuliah 4:")


        #membuat QLineEdit dengan nama variabel height_input
        self.nilai4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label12,self.nilai4)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label13 = QLabel(self)
        label13.setText("Masukkan Nama Mata Kuliah 5:")

        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label13,self.nama5)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label14 = QLabel(self)
        label14.setText("Masukkan Besar SKS 5:")

        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label14,self.sks5)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label15 = QLabel(self)
        label15.setText("Masukkan Nilai Mata Kuliah 5:")


        #membuat QLineEdit dengan nama variabel height_input
        self.nilai5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label15,self.nilai5)

        
        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label16 = QLabel(self)
        label16.setText("Masukkan Nama Mata Kuliah 6:")

        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label16,self.nama6)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label17 = QLabel(self)
        label17.setText("Masukkan Besar SKS 6:")

        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label17,self.sks6)


        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label18 = QLabel(self)
        label18.setText("Masukkan Nilai Mata Kuliah 6:")


        #membuat QLineEdit dengan nama variabel height_input
        self.nilai6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addRow(label18,self.nilai6)


        #membuat sebuah button dengan nama variable cal_button
        self.hitung = QPushButton("Hitung!", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.hitung.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout vbox
        vbox2.addWidget(self.hitung)
        #menambahkan addStretch ke dalam vbox agar tertata rapi)

        #membuat sebuah button dengan nama variable hasil
        self.hasil = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.hasil.setDisabled(True)
        #memasukkan button hasil ke dalam layout vbox
        vbox2.addWidget(self.hasil)

        
        #connect button to fungsi on_click
        self.hitung.clicked.connect(self.on_click)
        #connect button to fungsi on_click
        #membuat grid menjadi layout utama di window
        self.setLayout(grid)
    
    
    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai BMI
    def on_click(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        #membuat variabel weight dan height yang berisi inputan dari weight_input dan height_input yang akan dirubah menjadi sebuah float
        SKS1 = float(self.sks1.text())
        SKS2 = float(self.sks2.text())
        SKS3 = float(self.sks3.text())
        SKS4 = float(self.sks4.text())
        SKS5 = float(self.sks5.text())
        SKS6 = float(self.sks6.text())

        if self.nilai1.text() or self.nilai2.text() or self.nilai3.text() or self.nilai4.text() or self.nilai5.text() or self.nilai6.text() == "A":
            float(self.nilai1.text()) or float(self.nilai2.text()) or float(self.nilai3.text()) or float(self.nilai4.text()) or float(self.nilai5.text()) or float(self.nilai6.text()) == 4
        elif self.nilai1.text() or self.nilai2.text() or self.nilai3.text() or self.nilai4.text() or self.nilai5.text() or self.nilai6.text() == "B":
            float(self.nilai1.text()) or float(self.nilai2.text()) or float(self.nilai3.text()) or float(self.nilai4.text()) or float(self.nilai5.text()) or float(self.nilai6.text()) == 3
        elif self.nilai1.text() or self.nilai2.text() or self.nilai3.text() or self.nilai4.text() or self.nilai5.text() or self.nilai6.text() == "C":
            float(self.nilai1.text()) or float(self.nilai2.text()) or float(self.nilai3.text()) or float(self.nilai4.text()) or float(self.nilai5.text()) or float(self.nilai6.text()) == 2
        elif self.nilai1.text() or self.nilai2.text() or self.nilai3.text() or self.nilai4.text() or self.nilai5.text() or self.nilai6.text() == "D":
            float(self.nilai1.text()) or float(self.nilai2.text()) or float(self.nilai3.text()) or float(self.nilai4.text()) or float(self.nilai5.text()) or float(self.nilai6.text()) == 1
        else:
            float(self.nilai1.text()) or float(self.nilai2.text()) or float(self.nilai3.text()) or float(self.nilai4.text()) or float(self.nilai5.text()) or float(self.nilai6.text()) == 0
        
        Nilai1 = float(self.nilai1.text()) * SKS1
        Nilai2 = float(self.nilai2.text()) * SKS2
        Nilai3 = float(self.nilai3.text()) * SKS3
        Nilai4 = float(self.nilai4.text()) * SKS4
        Nilai5 = float(self.nilai5.text()) * SKS5
        Nilai6 = float(self.nilai6.text()) * SKS6
        
        
        Total_Nilai = Nilai1 + Nilai2 + Nilai3 + Nilai4 + Nilai5 + Nilai6
        Total_Sks = SKS1 + SKS2 + SKS3 +  SKS4 + SKS5 + SKS6

        Nilai_IP = Total_Nilai/Total_Sks

        if 3 < Nilai_IP <= 4:
            Nilai_IP = "A"
        elif 2 < Nilai_IP <= 3:
            Nilai_IP = "B"
        elif 1 < Nilai_IP <= 2:
            Nilai_IP = "C"
        elif 0 < Nilai_IP <= 1:
            Nilai_IP = "D"
        else:
            Nilai_IP = "E"
        #menampilkan nilai BMI pada button hasil
        self.hasil.setText("Total Nilai Anda: " + str("%.2f" %Total_Nilai) + "\nTotal_Sks Anda: " + str("%.2f" %Total_Sks) + "\nIP Anda: " + str(Nilai_IP) )
        #notif.information(self, "Hasil IP anda", , notif.Ok)
        
if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    #mengatur style di window menjadi style fusion
    app.setStyle("fusion")
    #menambahkan icon pada window
    app.setWindowIcon(QIcon('bmi_logo.ico'))
    #membuat variabel ex yang berisi class BMI
    ex = IPS()

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,1500,450)
    #membuat judul window
    ex.setWindowTitle("IPS Mahasiswa")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())   