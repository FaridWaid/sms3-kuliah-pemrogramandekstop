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
        group1 = QGroupBox("Hitung IPS Online",self)
        #mengatur semua isi konten yang ada di group1 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        group1.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group1 kedalam layout grid
        grid.addWidget(group1, 1, 0)
        #membuat QformLayout dengan nama variabel form
        form = QFormLayout()
        #membuat QformLayout dengan nama variabel form
        group1.setLayout(form)
        
        
        Checkbox = QCheckBox("Mata kuliah 1")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 1:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama1)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 1:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks1)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 1:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai1 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai1.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai1)
        #menambahkan addStretch ke dalam form agar tertata rapi
        
        Checkbox = QCheckBox("Mata kuliah 2")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 2:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama2)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 2:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks2)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 2:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai2 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai2.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai2)
        #menambahkan addStretch ke dalam form agar tertata rapi
        
        Checkbox = QCheckBox("Mata kuliah 3")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 3:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama3)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 3:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks3)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 3:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai3 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai3.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai3)
        #menambahkan addStretch ke dalam form agar tertata rapi
        
        Checkbox = QCheckBox("Mata kuliah 4")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 4:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama4)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 4:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks4)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 4:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai4 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai4.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai4)
        #menambahkan addStretch ke dalam form agar tertata rapi
        
        Checkbox = QCheckBox("Mata kuliah 5")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 5:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama5)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 5:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks5)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 5:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai5 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai5.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai5)
        #menambahkan addStretch ke dalam form agar tertata rapi
        
        Checkbox = QCheckBox("Mata kuliah 6")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        form.addRow(Checkbox)
        
        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nama Mata Kuliah 6:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.nama6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nama6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nama6)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Besar SKS 6:")
        #form.addRow(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.sks6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.sks6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.sks6)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat label1 dan akan dimasukkan ke dalam layout form
        label1 = QLabel(self)
        label1.setText("Masukkan Nilai Mata Kuliah 6:")
        #form.addRow(label1)

        #membuat QLineEdit dengan nama variabel height_input
        self.nilai6 = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.nilai6.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout form
        form.addRow(label1,self.nilai6)
        #menambahkan addStretch ke dalam form agar tertata rapi
        

        #membuat sebuah button dengan nama variable cal_button
        self.hitung = QPushButton("Hitung!", self)
        #mengatur cal_button dengan background berwarna #33f8c7
        self.hitung.setStyleSheet("background-color: #33f8c7;")
        #memasukkan cal_button kedalam layout form
        form.addRow(self.hitung)
        #menambahkan addStretch ke dalam form agar tertata rapi)

        #membuat sebuah button dengan nama variable hasil
        self.hasil = QPushButton("Hasil", self)
        ##mengatur hasil dengan font bold dan ukuran 20px dan berwarna hitam
        self.hasil.setStyleSheet("font: bold 20px; color: black")
        #mengatur button hasil dengan setDisabled agar tidak daat diklik
        self.hasil.setDisabled(True)
        #memasukkan button hasil ke dalam layout form
        form.addRow(self.hasil)

        
        #connect button to fungsi on_click
        self.hitung.clicked.connect(self.on_click)
        #connect button to fungsi on_click
        #membuat grid menjadi layout utama di window
        self.setLayout(grid)
    
    
    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai BMI
    def on_click(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
    
        try:
            #membuat variabel weight dan height yang berisi inputan dari weight_input dan height_input yang akan dirubah menjadi sebuah float
            SKS1 = float(self.sks1.text())
            SKS2 = float(self.sks2.text())
            SKS3 = float(self.sks3.text())
            SKS4 = float(self.sks4.text())
            SKS5 = float(self.sks5.text())
            SKS6 = float(self.sks6.text())

            a = float(self.nilai1.text())
            b = (float(self.nilai2.text()))
            c = float(self.nilai3.text())
            d = float(self.nilai4.text())
            e = float(self.nilai5.text())
            f = float(self.nilai6.text())
            
            if 80.0<=a<=100.0:
                a = 4
            elif 68<=a<=79.99:
                a = 3
            elif 56<=a<=67.99:
                a = 2
            elif 45<=a<=55.99:
                a = 1
            else:
                a = 0

            if 80.0<=b<=100.0:
                b = 4
            elif 68<=b<=79.99:
                b = 3
            elif 56<=b<=67.99:
                b = 2
            elif 45<=b<=55.99:
                b = 1
            else:
                b = 0

            if 80.0<=c<=100.0:
                c = 4
            elif 68<=c<=79.99:
                c = 3
            elif 56<=c<=67.99:
                c = 2
            elif 45<=c<=55.99:
                c = 1
            else:
                c = 0

            if 80.0<=d<=100.0:
                d = 4
            elif 68<=d<=79.99:
                d = 3
            elif 56<=d<=67.99:
                d = 2
            elif 45<=d<=55.99:
                d = 1
            else:
                d = 0

            if 80.0<=e<=100.0:
                e = 4
            elif 68<=e<=79.99:
                e = 3
            elif 56<=e<=67.99:
                e = 2
            elif 45<=e<=55.99:
                e = 1
            else:
                e = 0

            if 80.0<=f<=100.0:
                f = 4
            elif 68<=f<=79.99:
                f = 3
            elif 56<=f<=67.99:
                f = 2
            elif 45<=f<=55.99:
                f = 1
            else:
                f = 0

            Nilai1 = a * SKS1
            Nilai2 = b * SKS2
            Nilai3 = c * SKS3
            Nilai4 = d * SKS4
            Nilai5 = e * SKS5
            Nilai6 = f * SKS6

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
            self.hasil.setText("Total Nilai Anda: " + str("%.2f" %Total_Nilai) + "\nTotal SKS Anda: " + str("%.2f" %Total_Sks) + "\nIP Anda: " + str(Nilai_IP) )
            #notif.information(self, "Hasil IP anda", , notif.Ok)
        except:
            #jika pada waktud2 diisi kosong
            if str(self.nilai1.text()) =="" or str(self.nilai2.text()) =="" or str(self.nilai3.text()) =="" or str(self.nilai4.text()) =="" or str(self.nilai5.text()) =="" or str(self.nilai6.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Matkul Anda Dengan Benar!", "Tolong masukkan nilai matkul anda dengan sebuah angka! ", notif.Ok)
            #jika pada waktud2 diisi kosong
            elif str(self.sks1.text()) =="" or str(self.sks2.text()) =="" or str(self.sks3.text()) =="" or str(self.sks4.text()) =="" or str(self.sks5.text()) =="" or str(self.sks6.text()) =="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Nilai Sks Anda Dengan Benar!", "Tolong masukkan nilai sks anda dengan sebuah angka! ", notif.Ok)
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
    app.setWindowIcon(QIcon('bmi_logo.ico'))
    #membuat variabel ex yang berisi class BMI
    ex = BMI()

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,1000,500)
    #membuat judul window
    ex.setWindowTitle("IPS Mahasiswa")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())   