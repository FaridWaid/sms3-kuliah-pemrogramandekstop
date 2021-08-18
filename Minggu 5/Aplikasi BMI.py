import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


#Membuat class yang didalamnya terdapat QWidget
class BMI(QWidget):
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
        group1 = QGroupBox("Calculator untuk menghitung BMI (Body Mass Index)",self)
        #mengatur semua isi konten yang ada di group1 menjadi tulisan bold berwarna hitam dengan ukuran 15px
        group1.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group1 kedalam layout grid
        grid.addWidget(group1, 1, 0)
        #membuat QVBoxLayout dengan nama variabel vbox
        vbox = QVBoxLayout()
        #membuat vbox menjadi layout utama tetapi berada di dalam group1
        group1.setLayout(vbox)

        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label1 = QLabel(self)
        label1.setText("Masukkan Tinggi Badan Anda (m/meter):")
        vbox.addWidget(label1)
        
        #membuat QLineEdit dengan nama variabel height_input
        self.height_input = QLineEdit(self)
        #mengatur height_input dengan border 0.5 px dan berwarna solid black
        self.height_input.setStyleSheet("border: 0.5px solid black;")
        #memasukkan height_input kedalam layout vbox
        vbox.addWidget(self.height_input)
        #menambahkan addStretch ke dalam vbox agar tertata rapi
        vbox.addStretch()
        
        #membuat label1 dan akan dimasukkan ke dalam layout vbox
        label2 = QLabel(self)
        label2.setText("Masukkan Berat Badan Anda (kg/kilogram):")
        vbox.addWidget(label2)
        
        #membuat QLineEdit dengan nama variabel weight_input
        self.weight_input = QLineEdit(self)
        #mengatur weight_input dengan border 0.5 px dan berwarna solid black
        self.weight_input.setStyleSheet("border: 0.5px solid black;")
        #memasukkan weight_input kedalam layout vbox
        vbox.addWidget(self.weight_input)
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

        #membuat QGroupBox dengan nama variabel group2
        group2 = QGroupBox("Classification BMI",self)
        #mengatur group2 dengan font bol dan ukuran 15px dan berwarna hitam
        group2.setStyleSheet("font: bold 15px; color: black;")
        #memasukkan group2 kedalam layout utama grid
        grid.addWidget(group2, 1, 1)
        #membuat QVBoxLayout yang kedua untuk group2 dengan nama variabel vbox2
        vbox2 = QVBoxLayout()
        #mengatur vbox2 sebagai layout yang berada di dalam group2
        group2.setLayout(vbox2)

        #membuat label 3
        label3 = QLabel(self)
        label3.setText("Berat Badan Kurang: (BMI < 18.5)")
        #mengatur label3 dengan background berwarna orange dan font bold dengan ukuran 20px dan warna tulisan hitam
        label3.setStyleSheet("background-color: orange; font: bold 20px; color: black")
        #memasukkan label3 kedalam layout vbox2
        vbox2.addWidget(label3)

        #membuat label 4
        label4 = QLabel(self)
        label4.setText("Berat Badan Normal: (18.5 <= BMI <= 22.9)")
        #mengatur label3 dengan background berwarna hijau dan font bold dengan ukuran 20px dan warna tulisan hitam
        label4.setStyleSheet("background-color: green; font: bold 20px; color: black")
        #memasukkan label4 kedalam layout vbox2
        vbox2.addWidget(label4)

        #membuat label 5
        label5 = QLabel(self)
        label5.setText("Berat Badan Cenderung Obesitas: (23 <= BMI <= 29.9)")
        #mengatur label3 dengan background berwarna kuning dan font bold dengan ukuran 20px dan warna tulisan hitam
        label5.setStyleSheet("background-color: yellow; font: bold 20px; color: black")
        #memasukkan label5 kedalam layout vbox2
        vbox2.addWidget(label5)

        #membuat label 6
        label6 = QLabel(self)
        label6.setText("Obesitas: (BMI >= 30)")
        #mengatur label3 dengan background berwarna merah dan font bold dengan ukuran 20px dan warna tulisan hitam
        label6.setStyleSheet("background-color: red; font: bold 20px; color: black")
        #memasukkan label6 kedalam layout vbox2
        vbox2.addWidget(label6)

        #connect button to fungsi on_click
        self.cal_button.clicked.connect(self.on_click)
        #membuat grid menjadi layout utama di window
        self.setLayout(grid)
    
    #membuat fungsi on_click yang berisi sistem untuk menghitung nilai BMI
    def on_click(self):   
        #membuat QMessageBox dengan nama variabel notif 
        notif = QMessageBox()
        try:
            #membuat variabel weight dan height yang berisi inputan dari weight_input dan height_input yang akan dirubah menjadi sebuah float
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            #membuat variabel BMI untuk menghitung nilai BMI
            BMI = weight/(height*height)
            #menampilkan nilai BMI pada button hasil
            self.hasil.setText("Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI))
            ############ SISTEM BMI ############
            #jika nilai BMI < 18.5
            if BMI < 18.5:
                #button hasil akan diubah menjadi background berwarna orange dan font bold berukuran wopx dan berwarna hitam
                self.hasil.setStyleSheet("background-color: orange; font: bold 20px; color: black")
                #menampilan sebuah meesage box dengan information 
                notif.information(self, "hasil", "Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI) + "\nCategory: Berat Badan Anda Kurang", notif.Ok)

            #jika nilai 18.5<=BMI<=22.9
            elif 18.5<=BMI<=22.9:
                #button hasil akan diubah menjadi background berwarna hijau dan font bold berukuran wopx dan berwarna hitam
                self.hasil.setStyleSheet("background-color: green; font: bold 20px; color: black")
                #menampilan sebuah meesage box dengan information 
                notif.information(self, "hasil", "Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI) + "\nCategory: Berat Badan Anda Normal", notif.Ok)

            #jika nilai 23<=BMI<=29.9
            elif 23<=BMI<=29.9:
                #button hasil akan diubah menjadi background berwarna kuning dan font bold berukuran wopx dan berwarna hitam
                self.hasil.setStyleSheet("background-color: yellow; font: bold 20px; color: black")
                #menampilan sebuah meesage box dengan information 
                notif.information(self, "hasil", "Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI) + "\nCategory: Berat Badan Anda Cenderung Obesitas", notif.Ok)

            #jika nilai 23<=BMI<=29.9
            elif BMI>= 30:
                #button hasil akan diubah menjadi background berwarna merah dan font bold berukuran wopx dan berwarna hitam
                self.hasil.setStyleSheet("background-color: red; font: bold 20px; color: black")
                #menampilan sebuah meesage box dengan information
                notif.information(self, "hasil", "Hasil Perhitungan BMI Anda: " + str("%.2f" %BMI) + "\nCategory: Berat Badan Anda Obesitas", notif.Ok)

        except:
            #jika pada weight_input dan height_input diisi kosong
            if str(self.weight_input.text()) =="" and str(self.height_input.text()) =="":
                #maka meesage box akan menampilkan sebuah warning
                notif.warning(self, "Maaf Inputan yang Anda Masukkan Salah", "Tolong Masukkan dengan sebuah angka! ", notif.Ok)

            #jika pada weight_input diisi kosong
            elif str(self.weight_input.text()) =="" and str(self.height_input.text()) !="":   
                #maka meesage box akan menampilkan sebuah warning         
                notif.warning(self, "Masukkan Berat Badan Anda Dengan Benar!", "Tolong masukkan berat badan anda dengan sebuah angka! ", notif.Ok)

            #jika pada height_input diisi kosong
            elif str(self.height_input.text()) =="" and str(self.weight_input.text()) !="":      
                #maka meesage box akan menampilkan sebuah warning       
                notif.warning(self, "Masukkan Tinggi Badan Anda Dengan Benar!", "Tolong masukkan tinggi badan anda dengan sebuah angka! ", notif.Ok)
            #jika yang diiskan selain angka dan kosongana
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
    ex.setGeometry(100,100,500,250)
    #membuat judul window
    ex.setWindowTitle("BMI (Body Mass Index) Calculator")
    #menampilan isi dari variabel ex
    ex.show()
    #membuat system exit
    sys.exit(app.exec_())