import sys
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()
        self.setWindowTitle("Uygulama")
        self.setGeometry(200, 200 ,639, 552)
        self.setWindowIcon(QtGui.QIcon("ikon.png"))
        self.setToolTip("İpucu aracı")
        self.arayuzTanimla()

    def arayuzTanimla(self):
        self.katman_ad = QtWidgets.QLabel(self)
        self.katman_ad.setText("Adınız: ")
        self.katman_ad.move(50, 30)

        self.katman_soyad = QtWidgets.QLabel(self)
        self.katman_soyad.setText("Soyadınız: ")
        self.katman_soyad.move(50, 70)

        self.katman_sonuc = QtWidgets.QLabel(self)
        self.katman_sonuc.move(115, 150)
        self.katman_sonuc.resize(200, 33)

        self.yazmaca_ad = QtWidgets.QLineEdit(self)
        self.yazmaca_ad.move(115, 30)
        self.yazmaca_ad.resize(200, 33)

        self.yazmaca_soyad = QtWidgets.QLineEdit(self)
        self.yazmaca_soyad.move(115, 70)
        self.yazmaca_soyad.resize(200, 33)

        self.kayit_dugmesi = QtWidgets.QPushButton(self)
        self.kayit_dugmesi.move(267, 110)
        self.kayit_dugmesi.setText("Sakla")
        self.kayit_dugmesi.resize(47, 33)
        self.kayit_dugmesi.clicked.connect(self.tiklandi)

    def tiklandi(self):
        self.katman_sonuc.setText("Ad-Soyad: " + self.yazmaca_ad.text() + " " + self.yazmaca_soyad.text())

def pencere():
    uyglm = QtWidgets.QApplication(sys.argv)
    pncr = Pencere()
    pncr.show()
    sys.exit(uyglm.exec_())
pencere()
