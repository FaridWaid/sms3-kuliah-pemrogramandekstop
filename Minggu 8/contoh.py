import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtSql

#global declaration
app = QApplication(sys.argv)
win = QWidget()
lb1 = QLabel("Open Koneksi")
btn2 = QPushButton("Create Table")
btn3 = QLineEdit()

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
model = QtSql.QSqlTableModel()

tableview = QTableView()


def window():    
    parent1 = QFormLayout()

    #row1    
    btn1 = QPushButton("Open")
    btn1.clicked.connect(open_koneksi)
    parent1.addRow(lb1, btn1)

    #create tabel
    lb2 = QLabel("Create table")    
    btn2.setEnabled(False)
    #btn2.clicked.connect(create_table)
    parent1.addRow(lb2, btn2)

    #create tabel
    lb3 = QLabel("Search")    
    #btn2.clicked.connect(create_table)
    parent1.addRow(lb3, btn3)
    #filter_proxy_model = QSortFilterProxyModel()
    #filter_proxy_model.setSourceModel(model)
    #filter_proxy_model.setFilterCaseSesitivity(Qt.CaseInsensitive)
    #filter_proxy_model.setFilterkeyColumn(0)
    #btn3.textChanged.connect(filter_proxy_model.setFilterRegExp)
    

    parent1.addRow(lb1)

    #table view
    parent1.addRow(tableview)

    #add row
    btnAdd = QPushButton("Insert Row")
    btnAdd.clicked.connect(add_row)
    parent1.addRow(btnAdd)

    win.setLayout(parent1)
    win.setWindowTitle("database")
    win.show()
    sys.exit(app.exec_())


def open_koneksi():    
    db.setDatabaseName('test.db')	
    if not db.open():
        lb1.setText("Koneksi NOT OK")
        btn2.setEnabled(False)
    else:
        lb1.setText("Koneksi OK")
        btn2.setEnabled(True)
        read_data()
        pass


#def search_table():
   


def read_data():    
    #model = QtSql.QSqlTableModel()
    model.setTable('mahasiswa') 
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    tableview.setModel(model)


def add_row():
    model.insertRow(0)


if __name__ == "__main__":
    window()