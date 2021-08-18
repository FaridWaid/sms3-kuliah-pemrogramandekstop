import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

app = QApplication(sys.argv)
#membuat style pada app dengan style fusion
app.setStyle("fusion")
#menambahkan icon pada tampilan window dengan nama file icon 'math.png'
app.setWindowIcon(QIcon('replay.jpg'))

#membuat sebuah main window dengan nama variabel Mwindow
windowx = QWidget()
self = windowx
Mwindow = QMainWindow()


def layoutFilmAction():
    
    windowx = QWidget(self)

    #Membuat media player
    self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface) 

    #Membuat videowidget
    videowidget = QVideoWidget()

    #Menampilkan videowidget ke dalam media player
    self.mediaPlayer.setVideoOutput(videowidget)

    #Membuat open button
    openBtn = QPushButton('Open Video')
    openBtn.setStyleSheet("background-color: #dddddd;")
    openBtn.clicked.connect(Open_file)

    #Membuat play button
    self.playBtn = QPushButton()
    self.playBtn.setStyleSheet("background-color: #dddddd;")
    self.playBtn.setEnabled(False)
    self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
    self.playBtn.clicked.connect(Play_video)

    #Membuat slider
    self.slider = QSlider(Qt.Horizontal)
    self.slider.setStyleSheet("background-color: #dddddd;")
    self.slider.setRange(0,0)
    self.slider.sliderMoved.connect(Set_position)

    #Membuat hbox layout
    hbox = QHBoxLayout()

    #Memasukkan beberapa widget ke dalam hbox
    hbox.addWidget(openBtn)
    hbox.addWidget(self.playBtn)
    hbox.addWidget(self.slider)

    #Membuat vbox layout
    vbox = QVBoxLayout()
    vbox.addWidget(videowidget)
    vbox.addLayout(hbox)

    #Membuat media player signals
    self.mediaPlayer.stateChanged.connect(State_Change)
    self.mediaPlayer.positionChanged.connect(Position_Change)
    self.mediaPlayer.durationChanged.connect(Duration_Change)

    #Layout grid di jadikan layout utama
    windowx.setLayout(vbox)

    #membuat QWidget dengan nama variabel window
    Mwindow.setStyleSheet("background-color: #222831;")

    #menentukan ukuran window, + title dan menampilkan
    Mwindow.setCentralWidget(windowx)
    Mwindow.setGeometry(250,50,1300,980)
    Mwindow.setWindowTitle("Play a Film Action")
    Mwindow.show()
    #sys.exit(app.exec_())


def Open_file():
    filename, _ = QFileDialog.getOpenFileName(self, "Open Video","Action/01.mp4")
    if filename != '':
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.playBtn.setEnabled(True)

def Play_video():
    if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
        self.mediaPlayer.pause()
    else:
        self.mediaPlayer.play()

def State_Change( state):
    if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
    else:
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

def Position_Change(position):
    self.slider.setValue(position)

def Duration_Change( duration):
    self.slider.setRange(0, duration)

def Set_position(position):
    self.mediaPlayer.setPosition(position)
 
 
if __name__ == '__main__':
    layoutFilmAction()
    