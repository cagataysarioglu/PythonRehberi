import sys
from PyQt5 import QtWidgets
from ari_sozluk import Ui_Ana_Pencere
from sozluk_aktarma import aktarma
import re

class Uygulama(QtWidgets.QMainWindow):
    def __init__(self):
        super(Uygulama, self).__init__()

        self.arayuz = Ui_Ana_Pencere()
        self.arayuz.setupUi(self)

        self.arayuz.aratmaDugmesi.clicked.connect(self.arat)

        self.arayuz.onayKutusu_1.stateChanged.connect(self.durumGoster)
        self.arayuz.onayKutusu_2.stateChanged.connect(self.durumGoster)
        self.arayuz.onayKutusu_3.stateChanged.connect(self.durumGoster)

        self.arayuz.farkliAbecedeGoster.clicked.connect(self.onaylilariAl)

        self.arayuz.hataliEvet.toggled.connect(self.durumGoster)
        self.arayuz.hataliHayir.toggled.connect(self.durumGoster)

        self.arayuz.sorunBildirDugmesi.clicked.connect(self.hataBildir)
    
    def arat(self):
        sozcuk = (self.arayuz.sozcukGirdisi.text()).capitalize()
        anahtarListesi = list(aktarma.keys())
        degerListesi = list(aktarma.values())

        if sozcuk in aktarma.keys():
            self.arayuz.aramaSonucu.setText(str(degerListesi[anahtarListesi.index(sozcuk)]))
        elif sozcuk in aktarma.values():
            self.arayuz.aramaSonucu.setText(str(anahtarListesi[degerListesi.index(sozcuk)]))
        else:
            self.arayuz.aramaSonucu.setText("Yanlış bir sözcük arattınız.")

    def onaylilariAl(self):
        secim = ""
        icerikler = self.arayuz.anaPencereAraci.findChildren(QtWidgets.QCheckBox)
        for i in icerikler:
            if i.isChecked():
                secim += i.text() + "\n"
        self.arayuz.aramaSonucu.setText(secim)

    def durumGoster(self, deger):
        onayKutusu = self.sender()

        print(deger)
        print(onayKutusu.text())
        print(onayKutusu.isChecked())

    def hataBildir(self):
        sorunBildirIcerigi = self.arayuz.bildirimGrubu.findChildren(QtWidgets.QRadioButton)
        for r in sorunBildirIcerigi:
            if r.isChecked():
                self.arayuz.bildirimDonutu.setText("Bildiriminiz alınmıştır.")

def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pencere = Uygulama()
    pencere.show()
    sys.exit(uyg.exec_())
uygulama()