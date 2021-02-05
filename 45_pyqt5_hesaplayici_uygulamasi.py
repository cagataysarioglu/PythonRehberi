import sys
from PyQt5 import QtWidgets, QtGui

class AnaMakine(QtWidgets.QMainWindow):
    def __init__(self):
        super(AnaMakine, self).__init__()
        self.setWindowTitle("Hesaplayıcı")
        self.setGeometry(200, 200 ,500, 500)
        self.arayuzuTanimla()

    def arayuzuTanimla(self):
        self.katman_sayi1 = QtWidgets.QLabel(self)
        self.katman_sayi1.setText("Sayı giriniz: ")
        self.katman_sayi1.move(133, 30)

        self.yazmaca_sayi1 = QtWidgets.QLineEdit(self)
        self.yazmaca_sayi1.move(213, 30)
        self.yazmaca_sayi1.resize(115, 33)

        self.katman_sayi2 = QtWidgets.QLabel(self)
        self.katman_sayi2.setText("Sayı giriniz: ")
        self.katman_sayi2.move(133, 80)

        self.yazmaca_sayi2 = QtWidgets.QLineEdit(self)
        self.yazmaca_sayi2.move(213, 80)
        self.yazmaca_sayi2.resize(115, 33)

        self.dugme_topla = QtWidgets.QPushButton(self)
        self.dugme_topla.setText("Topla")
        self.dugme_topla.move(200, 140)
        self.dugme_topla.clicked.connect(self.hesapla)
        
        self.dugme_cikar = QtWidgets.QPushButton(self)
        self.dugme_cikar.setText("Çıkar")
        self.dugme_cikar.move(200, 190)
        self.dugme_cikar.clicked.connect(self.hesapla)
        
        self.dugme_carp = QtWidgets.QPushButton(self)
        self.dugme_carp.setText("Çarp")
        self.dugme_carp.move(200, 240)
        self.dugme_carp.clicked.connect(self.hesapla)

        self.dugme_bol = QtWidgets.QPushButton(self)
        self.dugme_bol.setText("Böl")
        self.dugme_bol.move(200, 290)
        self.dugme_bol.clicked.connect(self.hesapla)

        self.katman_sonuc = QtWidgets.QLabel(self)
        self.katman_sonuc.setText("Sonuç: ")
        self.katman_sonuc.move(133, 345)

    def hesapla(self):
        gonderen = self.sender().text()
        islem = 0

        if gonderen == "Topla":
            islem = int(self.yazmaca_sayi1.text()) + int(self.yazmaca_sayi2.text())
        elif gonderen == "Çıkar":
            islem = int(self.yazmaca_sayi1.text()) - int(self.yazmaca_sayi2.text())
        elif gonderen == "Çarp":
            islem = int(self.yazmaca_sayi1.text()) * int(self.yazmaca_sayi2.text())
        elif gonderen == "Böl":
          islem = int(self.yazmaca_sayi1.text()) / int(self.yazmaca_sayi2.text())
          
        self.katman_sonuc.setText("Sonuç: " + str(islem))

'''
    def toplama(self):
        islem = int(self.yazmaca_sayi1.text()) + int(self.yazmaca_sayi2.text())
        self.katman_sonuc.setText("Sonuç: " + str(islem))
    def cikarma(self):
        islem = int(self.yazmaca_sayi1.text()) - int(self.yazmaca_sayi2.text())
        self.katman_sonuc.setText("Sonuç: " + str(islem))
    def carpma(self):
        islem = int(self.yazmaca_sayi1.text()) * int(self.yazmaca_sayi2.text())
        self.katman_sonuc.setText("Sonuç: " + str(islem))
    def bolme(self):
        islem = int(self.yazmaca_sayi1.text()) / int(self.yazmaca_sayi2.text())
        self.katman_sonuc.setText("Sonuç: " + str(islem))
'''

def uygulama():
    uyglm = QtWidgets.QApplication(sys.argv)
    hsplyc = AnaMakine()
    hsplyc.show()
    sys.exit(uyglm.exec_())
uygulama()
