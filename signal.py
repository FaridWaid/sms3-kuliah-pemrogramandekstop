import sys
from PyQt5.QtWidgets import (QApplication, QGridLayout,
QPushButton, QWidget)
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Calculator')
layout = QGridLayout()
layout.addWidget(QPushButton('Cls'), 0, 0)
layout.addWidget(QPushButton('Back'), 0, 1)
layout.addWidget(QPushButton('Close'), 0, 3)
layout.addWidget(QPushButton('Close'), 0, 4)
for x in range(1):
    for y in range(7, 11):
        layout.addWidget(QPushButton(str(y)))
    layout.addWidget(QPushButton('/'), 1, 4)
    for y in range(4, 7):
        layout.addWidget(QPushButton(str(y)))
    layout.addWidget(QPushButton('*'), 2, 3)
    for y in range(1, 4):
        layout.addWidget(QPushButton(str(y)))
    layout.addWidget(QPushButton('-'), 3, 3)
layout.addWidget(QPushButton('0'), 4, 0)
layout.addWidget(QPushButton('.'), 4, 1)
layout.addWidget(QPushButton('='), 4, 2)
layout.addWidget(QPushButton('+'), 4, 3)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
