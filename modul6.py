# Import Package
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit , QLabel,QMessageBox, QTableWidget, QVBoxLayout, QTableWidgetItem, QHeaderView
import pymysql.cursors
import sys

# Membuat Class Barang dengan turunan dari QWidget
class Menu(QWidget):
    # Menjalankan Konstruktor
    def __init__(self):
        super().__init__()
        # Memanggil Tampilan
        self.tampilan()
    #     Membuat Fungsi Koneksi Database
    def dbConnection(self):
        # Menggunakan Try dan catch untuk melakukan koneksi database
        try:
            self.db = pymysql.connect('kprikaryasehat.site', 'kprikary_kuliah', 'unijoyo2020', 'kprikary_resto')
        except Exception as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)
    def tampilan(self):
        # Membuat Koneksi Database
        self.dbConnection()
        # Membuat Label
        menu = QLabel("Nama Menu:")
        keterangan = QLabel("Keterangan:")
        harga = QLabel("Harga:")
        satuan = QLabel("Satuan: ")
        # Membuat Inputan dan menjadikan sebagai global
        self.inMenu = QLineEdit(self)
        self.inKeterangan = QLineEdit(self)
        self.inharga = QLineEdit(self)
        self.inSatuan = QLineEdit(self)
        # Membuat Tabel Widget
        self.tableData = QTableWidget()
        # Membuat Button
        tambah = QPushButton("Tambah")
        btHapus = QPushButton("Hapus")
        btEdit = QPushButton("Edit")
        btUpdate = QPushButton("Update")


        # Membuat Layout Grid
        layout = QGridLayout()
        layout.addWidget(menu,0,0)
        layout.addWidget(self.inMenu, 0, 1)
        layout.addWidget(keterangan, 1, 0)
        layout.addWidget(self.inKeterangan, 1, 1)
        layout.addWidget(harga, 2, 0)
        layout.addWidget(self.inharga, 2, 1)
        layout.addWidget(satuan, 3, 0)
        layout.addWidget(self.inSatuan, 3, 1)
        layout.addWidget(tambah,4,0)
        layout.addWidget(btHapus, 4, 1)
        layout.addWidget(btEdit, 5, 0)
        layout.addWidget(btUpdate, 5, 1)
        layout.addLayout(self.tampilData(), 7, 0, 5, 0)

        # Membuat Signal Dan Slot Saat Di Klik
        tambah.clicked.connect(self.tambahData)
        btHapus.clicked.connect(self.hapusData)
        btEdit.clicked.connect(self.editData)
        btUpdate.clicked.connect(self.updateData)


        # Menampilkan Layout dan window
        self.setLayout(layout)
        self.setWindowTitle("Input Barang")
        self.setGeometry(200, 300, 500, 500)
        self.show()

    # Slot Saat tambah Data
    def tambahData(self):
        # Mengambil Text inputan
        menu = str(self.inMenu.text())
        keterangan = str(self.inKeterangan.text())
        harga = int(self.inharga.text())
        satuan = str(self.inSatuan.text())
        # Mendefinisikan Cursor
        cur = self.db.cursor()
        id = self.db.cursor()
        # Menjalankan Perintah SQL
        id.execute("SELECT idmenu FROM menu1 ORDER BY idmenu DESC LIMIT 1")
        # Mengambil Satu Data
        idMenu = id.fetchone()
        # Membuat Id Auto Increment
        idMenu = idMenu[0] + 1
        # Menuliskan Perintah SQL
        sql = "INSERT INTO menu1(idmenu,idmenukat,idresto,namamenu,keterangan,filegambar,harga,satuan) VALUES ('%d','%d','%d','%s','%s','%s','%d','%s')" % (idMenu, 1, 3,menu,keterangan,'https://img-global.cpcdn.com/recipes/84fae0149dbe9168/751x532cq70/telor-balado-foto-resep-utama.jpg',harga,satuan)
        # MenjalanKan Perintah Try
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Mengcommit agar perubahan Tersimpan
            self.db.commit()
            # Membuat Notifikasi Berhasil Tambah Data
            QMessageBox.about(self, 'Berhasil', 'Berhasil Menambah Data')
            # Mengubah Inputan Agar Menjadi Kosong
            self.inMenu.setText("")
            self.inKeterangan.setText("")
            self.inharga.setText("")
            self.inSatuan.setText("")
            # Menampilkan Data
            self.tampilData()
            id.close()
            cur.close()
        # Jika Terjadi Error
        except:
            # Merollback data
            self.db.rollback()
            print("Gagal")
    # Fungsi Hapus Data
    def hapusData(self):
        # Mengambil Data Yang Di pilih
        index = self.tableData.selectedIndexes()[0]
        id = self.tableData.model().data(index)
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah SQL Untuk Menghapus Data
        sql = "DELETE FROM menu1 WHERE idmenu = '%s' " % (id)
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Commit Ke Database Agar Perubahan Tersimpan
            self.db.commit()
            # Menampilkan Data
            self.tampilData()
            print("Berhasil")
        except:
            # Merollback data
            self.db.rollback()
            print("Gagal")

    # Slot Saat Menampilkan Data
    def tampilData(self):
        # Membuat Cursor
        cur = self.db.cursor()
        # Mengeksekusi perintah sql
        cur.execute("SELECT * FROM menu1")
        # Mengambil Semua Data
        data = cur.fetchall()
        # Menjadikan Data bentuk list
        record = list(data)
        # Membuat VBOX Layout
        vbox = QVBoxLayout()
        # Membuat Baris Yang Akan Ditampilkan DI table
        self.tableData.setRowCount(len(record)+1)
        # Membuat Kolom yang akan ditampilkan di table
        self.tableData.setColumnCount(5)
        # Membuat Header
        self.tableData.setItem(0, 0, QTableWidgetItem("ID Menu"))
        self.tableData.setItem(0, 1, QTableWidgetItem("Nama Menu"))
        self.tableData.setItem(0, 2, QTableWidgetItem("Keterangan"))
        self.tableData.setItem(0, 3, QTableWidgetItem("Harga"))
        self.tableData.setItem(0, 4, QTableWidgetItem("Satuan"))
        # Menampilkan Data Yang Diambil Dari SQL
        for i in range(len(record)):
            baris = i + 1
            self.tableData.setItem(baris, 0, QTableWidgetItem(str(record[i][0])))
            self.tableData.setItem(baris, 1, QTableWidgetItem(str(record[i][3])))
            self.tableData.setItem(baris, 2, QTableWidgetItem(str(record[i][4])))
            self.tableData.setItem(baris, 3, QTableWidgetItem(str(record[i][6])))
            self.tableData.setItem(baris, 4, QTableWidgetItem(str(record[i][7])))
        # Membuat Agar Table Strech
        self.tableData.horizontalHeader().setStretchLastSection(True)
        self.tableData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Menambahkan table widget ke layout
        vbox.addWidget(self.tableData)
        cur.close()
        return vbox
    def editData(self):
        # Mengambil Data Yang DIpilih
        index = self.tableData.selectedIndexes()[0]
        id = self.tableData.model().data(index)
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah Mencari Data Bedasarkan ID
        sql = "SELECT * FROM menu1 WHERE idmenu = '%s' " % (id)
        # Eksekusi Perintah SQL
        cur.execute(sql)
        # Mengambil Satu Data
        data = cur.fetchone()
        # Menyimpan Data Id Di variabel idEdit
        self.idEdit = data[0]
        # Menampilkan Data Ke Textbox
        self.inMenu.setText(data[3])
        self.inKeterangan.setText(data[4])
        self.inharga.setText(str(data[6]))
        self.inSatuan.setText(data[7])
    # Fungsi Update Data
    def updateData(self):
        # Mengambil Data Dari Inputan
        menu = str(self.inMenu.text())
        keterangan = str(self.inKeterangan.text())
        harga = int(self.inharga.text())
        satuan = str(self.inSatuan.text())
        # Membuat Cursor
        cur = self.db.cursor()
        # Perintah SQL Update
        sql = "UPDATE menu1 SET namamenu = '%s', keterangan = '%s', harga = '%d', satuan = '%s' WHERE idmenu = '%d'" % (menu,keterangan,harga,satuan,self.idEdit)
        try:
            # Eksekusi Perintah SQL
            cur.execute(sql)
            # Commit DB Agar Terjadi Perubahan DI database
            self.db.commit()
            # Membuat Message Box
            QMessageBox.about(self, 'Berhasil', 'Berhasil Update Data')
            self.inMenu.setText("")
            self.inKeterangan.setText("")
            self.inharga.setText("")
            self.inSatuan.setText("")
            self.tampilData()
            print("Berhasil")
        except:
            self.db.rollback()
            print("Gagal")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Menu()
    sys.exit(app.exec_())


