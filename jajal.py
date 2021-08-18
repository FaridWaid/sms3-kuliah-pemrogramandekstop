import sys
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()        

    hbox = QHBoxLayout()
    #kelompok 1
    textLabel = QLabel("S\u0332tyles:")
    #textLabel.setText()
    #textLabel.move(10,15)
    combo = QComboBox(win)
    combo.addItem("Fusion")
    combo.addItem("Fusion 1")
    combo.addItem("Fusion 2")
    combo.addItem("Fusion 3")
    #combo.move(55,13)
    hbox.addWidget(textLabel)
    hbox.addWidget(combo)
    hbox.addStretch()

    #kelompok 2
    checkbox = QCheckBox("U\u0332se style's standart palette",win)
    checkbox.setChecked(True)
    #checkbox.move(175,13)
    #checkbox.resize(200,30)
    hbox.addWidget(checkbox)
    hbox.addStretch()

    #kelompok 3
    checkbox = QCheckBox("D\u0332isable widgets",win)
    #checkbox.move(360,13)
    #checkbox.resize(360,30)
    hbox.addWidget(checkbox)
        
    win.setLayout(vbox)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
   window()