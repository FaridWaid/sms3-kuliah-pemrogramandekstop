import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#Membuat class 
class Example(QWidget):
   #Membuat method init dengan memanggil beberapa fungsi yang nanti akan ditampilkan
    def __init__(self):
        super().__init__()
        self.layout1()
        
    def layout1(self):
        #membuat layout grid dan horizontal layout
        grid = QGridLayout()
        grid.setContentsMargins(10,10,10,10)
        hbox = QHBoxLayout()

        #kelompok 1
        textLabel = QLabel("S\u0332tyles:")
        hbox.addWidget(textLabel)
        combo = QComboBox(self)
        combo.addItem("Fusion")
        combo.addItem("Fusion 1")
        combo.addItem("Fusion 2")
        combo.addItem("Fusion 3")
        hbox.addWidget(combo)
        hbox.addStretch()

        #kelompok 2
        checkbox1 = QCheckBox("U\u0332se style's standart palette",self)
        checkbox1.setChecked(True)
        hbox.addWidget(checkbox1)
        hbox.addStretch()

        #kelompok 3
        checkbox2 = QCheckBox("D\u0332isable widgets",self)
        hbox.addWidget(checkbox2)
        grid.addItem(hbox,0,0,1,2)
        
        #grid = QGridLayout()
          

        #group 1
        group1 = QGroupBox("Group 1",self)
        grid.addWidget(group1, 1, 0)
        vbox = QVBoxLayout()
        group1.setLayout(vbox)
        #radiobutton
        Radiobutton1 = QRadioButton("Radio button 1", self)
        vbox.addWidget(Radiobutton1)
        Radiobutton2 = QRadioButton("Radio button 2", self)
        vbox.addWidget(Radiobutton2)
        Radiobutton3 = QRadioButton("Radio button 3", self)
        vbox.addWidget(Radiobutton3)
        #checkbox
        Checkbox = QCheckBox("Tri-state checkbox")
        Checkbox.setTristate(True)
        Checkbox.setCheckState(True)
        vbox.addWidget(Checkbox)

        #group 2
        group2 = QGroupBox("Group 2",self)
        grid.addWidget(group2, 1, 1)
        vbox = QVBoxLayout()
        group2.setLayout(vbox)
        #button
        button1 = QPushButton(self)
        button1.setText("Default Push Button")
        button1.setDefault(True)
        button1.resize(200, 30)
        vbox.addWidget(button1)
        button2 = QPushButton(self)
        button2.setText("Toggle Push Button")
        button2.setDisabled(True)
        button2.resize(200, 30)
        vbox.addWidget(button2)
        button3 = QPushButton(self)
        button3.setText("Flat Push Button")
        button3.setFlat(True)
        button3.resize(200, 30)
        vbox.addWidget(button3)


        #tabel dan text edit
        tab = QTabWidget(self)
        table = QTableWidget(7, 4,self)
        textedit = QTextEdit(self)
        tab.addTab(table,"Table")
        tab.addTab(textedit,"Text Edit")
        grid.addWidget(tab, 2, 0)

        #group 3
        group3 = QGroupBox("Group 3",self)
        grid.addWidget(group3, 2, 1)
        vbox = QVBoxLayout()
        group3.setLayout(vbox)
        #line edit tipe password
        password = QLineEdit("password")
        password.setEchoMode(QLineEdit.Password)
        vbox.addWidget(password)
        #spin box
        spin = QSpinBox()
        spin.setValue(50)
        vbox.addWidget(spin)
        #spin box date time
        dateTime = QDateTimeEdit()
        vbox.addWidget(dateTime)
        hbox = QHBoxLayout()
        vbox2 = QVBoxLayout()
        vbox.addLayout(hbox)
        hbox.addLayout(vbox2)
        #slider
        slider = QSlider(Qt.Horizontal,self)
        slider.setRange(0,100)
        slider.setValue(40)
        vbox2.addWidget(slider)
        #scrollbar
        scrollbar = QScrollBar(Qt.Horizontal,self)
        scrollbar.setMinimum(0)
        scrollbar.setMaximum(10)
        scrollbar.setValue(7)
        vbox2.addWidget(scrollbar)
        #dial
        dial = QDial()
        hbox.addWidget(dial)
        #progressbar
        progressbar = QProgressBar(self)
        progressbar.setValue(22)
        progressbar.setGeometry(10,400,500,30)
        grid.addWidget(progressbar,3,0,1,2)
        self.setLayout(grid)


if __name__ == '__main__':
    #Inisisalisai pyqt
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    ex = Example()

    #Menentukan ukuran window dan title untuk menampilkan
    ex.setGeometry(100,100,600,500)
    ex.setWindowTitle("Styles")
    ex.show()
    sys.exit(app.exec_())