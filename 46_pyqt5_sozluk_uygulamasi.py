import sys
from PyQt5 import QtWidgets, QtGui
from sozluk_aktarma import aktarma
import re

class Sozluk(QtWidgets.QMainWindow):
    def __init__(self):
        super(Sozluk, self).__init__()
        self.setWindowTitle("Arı Sözlük")
        self.setGeometry(200, 200 ,500, 250)
        self.arayuzuTanimla()

    def arayuzuTanimla(self):
        self.katman_sozcuk = QtWidgets.QLabel(self)
        self.katman_sozcuk.setText("Aratacağınız sözcüğü giriniz: ")
        self.katman_sozcuk.move(70, 30)
        self.katman_sozcuk.resize(205, 33)

        self.yazmaca_sozcuk = QtWidgets.QLineEdit(self)
        self.yazmaca_sozcuk.move(245, 30)
        self.yazmaca_sozcuk.resize(170, 33)

        self.dugme_aratma = QtWidgets.QPushButton(self)
        self.dugme_aratma.setText("Sözcüğü arat")
        self.dugme_aratma.move(245, 80)
        self.dugme_aratma.clicked.connect(self.arat)

        self.katman_sonuc = QtWidgets.QLabel(self)
        self.katman_sonuc.move(70, 130)
        self.katman_sonuc.resize(300, 33)

    def arat(self):
        sozcuk = (self.yazmaca_sozcuk.text()).capitalize()
        anahtarListesi = list(aktarma.keys())
        degerListesi = list(aktarma.values())

        if sozcuk in aktarma.keys():
            self.katman_sonuc.setText("Sonuç: " + str(degerListesi[anahtarListesi.index(sozcuk)]))
        elif sozcuk in aktarma.values():
            self.katman_sonuc.setText("Sonuç: " + str(anahtarListesi[degerListesi.index(sozcuk)]))
        else:
            self.katman_sonuc.setText("Yanlış bir sözcük arattınız.")
          
def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    aratici = Sozluk()
    aratici.show()
    sys.exit(uyg.exec_())
uygulama()