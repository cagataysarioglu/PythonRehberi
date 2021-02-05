import sys
from PyQt5 import QtWidgets, QtCore
from qt_tarih_zaman import Ui_AnaPencere

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.arayuz = Ui_AnaPencere()
        self.arayuz.setupUi(self)

        self.arayuz.dgm.clicked.connect(self.hesapla)

    def hesapla(self):
        baslangic = self.arayuz.tarihBaslangic.date()
        bitis = self.arayuz.tarihBitis.date()
        print(baslangic, bitis)

        print("Aydaki günler: {0}".format(baslangic.daysInMonth()))
        print("Yıldaki günler: {0}".format(baslangic.daysInYear()))

        print("Toplam gün: {0}".format(baslangic.daysTo(bitis)))

        imdi = QtCore.QDate.currentDate()
        print("Bugüne dek toplam gün: {0}".format(baslangic.daysTo(imdi)))


def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(uyg.exec_())
uygulama()