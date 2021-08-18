import sys
from PyQt5.QtWidgets import *

#Membuat class 
class Example(QWidget):
   #Membuat method init dengan memanggil beberapa fungsi yang nanti akan ditampilkan
   def __init__(self):
      super().__init__()
      self.CheckBox()
      self.Labeling()
      self.RadioButton()
      self.lineEdit()
   #Membuat fungsi labeling, dalam fungsi ini hanya terdapat fungsi khusus untuk label, seperti menampilkan tulisan, mengatur ukuran font,background
   #dan letak label yang akan ditampilkan
   def Labeling(self):
      textLabel = QLabel(self)
      textLabel1 = QLabel(self)
      textLabel1.setStyleSheet("font: 18px;")
      textLabel2 = QLabel(self)
      textLabel2.setStyleSheet("font: 18px;")
      textLabel3 = QLabel(self)
      textLabel3.setStyleSheet("font: 18px;")
      textLabel4 = QLabel(self)
      textLabel4.setStyleSheet("font: 18px;")
      textLabel.setText("Input Biodata")
      textLabel.setStyleSheet("Background-color:#aacedf; color:red; font:bold 40px;")
      textLabel.setGeometry(10,30,975,50)

      textLabel1.setText("Name")
      textLabel1.move(10,100)

      textLabel2.setText("Addres")
      textLabel2.move(10,150)

      textLabel3.setText("Hobby")
      textLabel3.move(10,240)

      textLabel4.setText("Status")
      textLabel4.move(10,340)

   #Membuat fungsi line edit dan juga mengatur ukuran serta letak line edit tersebut
   def lineEdit(self):
      lineEdit = QLineEdit(self)
      lineEdit.setGeometry(80,100,905,35)

      lineEdit2 = QLineEdit(self)
      lineEdit2.setGeometry(80,150,905,35)

      lineEdit3 = QLineEdit(self)
      lineEdit3.setGeometry(80,190,905,35)

   #Membuat fungsi checkbox dan juga mengatur ukuran serta letak checkbox tersebut
   def CheckBox(self):
      checkbox1 = QCheckBox('Makan', self)
      checkbox1.move(80, 240)
      checkbox1.setStyleSheet("font: 18px;")

      checkbox2 = QCheckBox('Tidur', self)
      checkbox2.move(80, 270)
      checkbox2.setStyleSheet("font: 18px;")

      checkbox3 = QCheckBox('Main', self)
      checkbox3.move(80, 300)
      checkbox3.setStyleSheet("font: 18px;")

   #Membuat fungsi RadioButton dan juga mengatur ukuran serta letak RadioButton tersebut
   def RadioButton(self):
      radiobutton1 = QRadioButton("Pelajar", self)
      radiobutton1.move(80,340)
      radiobutton1.setStyleSheet("font: 18px;")

      radiobutton2 = QRadioButton("Pegawai", self)
      radiobutton2.move(80,370)
      radiobutton2.setStyleSheet("font: 18px;")

      radiobutton3 = QRadioButton("Wiraswasta", self)
      radiobutton3.move(80,400)
      radiobutton3.setStyleSheet("font: 18px;")


if __name__ == '__main__':
   #Inisisalisai pyqt
   app = QApplication(sys.argv)
   ex = Example()

   #Menentukan ukuran window dan title untuk menampilkan
   ex.setGeometry(50,50,1000,500)
   ex.setWindowTitle("PyQt")
   ex.show()
   sys.exit(app.exec_())