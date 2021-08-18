        import sys
        from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QRadioButton, QGridLayout, QGroupBox, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QTableView, QTabWidget, QSizePolicy, QTextEdit, QDateTimeEdit, QSpinBox, QSlider, QScrollBar, QScrollArea, QDial, QProgressBar
        from PyQt5.QtCore import *
        from PyQt5.QtGui import *

        def window_go():
            # Inisialisasi PyQt
            app = QApplication(sys.argv)
            window = QWidget()


            label = QLabel(window)
            label.setText("Style:")
            label.move(10,10)
            dropdown = QComboBox(window)
            dropdown.addItem("Fusion")
            dropdown.addItem("Fusion 1")
            dropdown.addItem("Fusion 2")
            dropdown.addItem("Fusion 3")
            dropdown.move(50,16)
            dropdown.resize(80,20)
            
            inputCheck = QCheckBox("Use style's standard palette", window)
            inputCheck.move(150,17)
            inputCheck.resize(180, 20)
            inputCheck.setChecked(True)
            inputCheck = QCheckBox("Disabe Widgets", window)
            inputCheck.move(330, 13)


            grid = QGridLayout()
            grid.setContentsMargins(10,50,10,40)  

            group = QGroupBox("Group Contoh")
            grid.addWidget(group, 0, 0)
            vbox = QVBoxLayout()
            group.setLayout(vbox)
            inputRadio = QRadioButton("Radio button 1", window)
            vbox.addWidget(inputRadio)
            inputRadio = QRadioButton("Radio button 2", window)
            vbox.addWidget(inputRadio)
            inputRadio = QRadioButton("Radio button 3", window)
            vbox.addWidget(inputRadio)
            inputCheck = QCheckBox("Tri-state checkbox")
            inputCheck.setTristate(True)
            inputCheck.setCheckState(True)
            vbox.addWidget(inputCheck)

            group = QGroupBox("Group Contoh")
            grid.addWidget(group, 0, 1)
            vbox = QVBoxLayout()
            vbox.setContentsMargins(5,5,5,70)
            group.setLayout(vbox)
            button = QPushButton(window)
            button.setText("Default Push Button")
            button.setDefault(True)
            button.resize(200, 30)
            vbox.addWidget(button)
            button = QPushButton(window)
            button.setText("Toggle Push Button")
            button.setDisabled(True)
            button.resize(200, 30)
            vbox.addWidget(button)
            button = QPushButton(window)
            button.setText("Flat Push Button")
            button.setFlat(True)
            button.resize(200, 30)
            vbox.addWidget(button)

            
            
            tab = QTabWidget(window)
            tab.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
            table = QTableWidget(5,5, window)
            text = QTextEdit(window)
            grid.addWidget(tab, 1, 0)

            tab1 = QWidget()
            hbox = QHBoxLayout()
            hbox.setContentsMargins(5,5,5,5)
            hbox.addWidget(table)
            tab1.setLayout(hbox)
            tab.addTab(tab1, "Tabel")

            tab2 = QWidget()
            hbox = QHBoxLayout()
            hbox.setContentsMargins(5,5,5,5)
            hbox.addWidget(text)
            tab2.setLayout(hbox)
            tab.addTab(tab2, "Text Edit")

            group = QGroupBox("Group 3")
            group.setCheckable(True)
            group.setChecked(True)
            grid.addWidget(group, 1, 1)
            window.setLayout(grid)
            vbox = QVBoxLayout()
            group.setLayout(vbox)
            pw = QLineEdit(window)
            pw.setEchoMode(QLineEdit.Password)
            pw.setText("pass")
            vbox.addWidget(pw)

            num = QSpinBox(window)
            num.setValue(50)
            vbox.addWidget(num)

            tgl = QDateTimeEdit(window)
            vbox.addWidget(tgl)

            hbox = QHBoxLayout()
            vbox2 = QVBoxLayout()
            vbox.addLayout(hbox)    
            slider = QSlider(Qt.Horizontal,window)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(30)
            hbox.addLayout(vbox2)
            vbox2.addWidget(slider)

            scroll = QScrollBar(Qt.Horizontal, window)
            scroll.setMinimum(0)
            scroll.setMaximum(10)
            scroll.setValue(3)
            vbox2.addWidget(scroll)

            dial = QDial()
            dial.setMinimum(0)
            dial.setMaximum(100)
            dial.setValue(30)
            hbox.addWidget(dial)


            progress = QProgressBar(window)
            progress.setGeometry(10, 440, 580, 20)
            progress.setValue(22)
            progress.setAlignment(Qt.AlignCenter)

            # Menyiapkan window
            window.setGeometry(100,100,600,430)
            window.setWindowTitle("PyQt")
            window.show()
            sys.exit(app.exec_())


        window_go()