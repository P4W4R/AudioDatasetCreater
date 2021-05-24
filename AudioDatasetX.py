import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sounddevice as sd
from scipy.io.wavfile import write
import time


class rpcode(QDialog):
    def __init__(self):
        super(rpcode, self).__init__()
        loadUi('design.ui', self)
        self.Return = 0
        self.fs = 16000
        self.a = 0
        self.Text.setText('Click on Start...')
        self.START.clicked.connect(self.STARTVOICERECORDING)

    @pyqtSlot()

    def loopThis(self):
        for i in range(200) :
            Duration = 5
            self.a = sd.rec(int(Duration * self.fs), self.fs, 1)
            sd.wait()
            fileName = time.strftime("%Y%M%d-%H%M%S")
            write('F:/Dataset Creator/Datasets/' + fileName + '.wav', self.fs, self.a)
            print('\n saved ' + fileName + '.wav')



    def STARTVOICERECORDING(self):
        self.Text.setText('Recording... just close the app if you wanna stop collecting dataset')
        self.loopThis()
        self.Text.setText('Done... Click on to start again')

app = QApplication(sys.argv)
window = rpcode()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')
