import sys
from PyQt5 import QtWidgets
from qt_tablo_goruntuleme import Ui_AnaPencere

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.arayuz = Ui_AnaPencere()
        self.arayuz.setupUi(self)

        self.urunleriYukle()
        self.arayuz.dgmUrunEkle.clicked.connect(self.urunleriEkle)
        self.arayuz.tabloUrunler.doubleClicked.connect(self.ciftTiklandi)

    def ciftTiklandi(self):
        for i in self.arayuz.tabloUrunler.selectedItems():
            print(i.row(), i.column(), i.text())

    def urunleriEkle(self):
        urun_adi = self.arayuz.grdUrunAdi.text()
        fiyat = self.arayuz.grdUrunFiyati.text()

        if urun_adi and fiyat is not None:
            satirSayaci = self.arayuz.tabloUrunler.rowCount()
            self.arayuz.tabloUrunler.insertRow(satirSayaci)
            self.arayuz.tabloUrunler.setItem(satirSayaci, 0, QtWidgets.QTableWidgetItem(urun_adi))
            self.arayuz.tabloUrunler.setItem(satirSayaci, 1, QtWidgets.QTableWidgetItem(fiyat))

    def urunleriYukle(self):

        urunler = [
            {"urun_adi": "MSI GP62", "fiyat": 7000},
            {"urun_adi": "MSI GP71", "fiyat": 7600},
            {"urun_adi": "MSI GT80", "fiyat": 8000}
        ]

        self.arayuz.tabloUrunler.setRowCount(len(urunler))
        self.arayuz.tabloUrunler.setColumnCount(2)
        self.arayuz.tabloUrunler.setHorizontalHeaderLabels(("urun_adi", "fiyat"))
        self.arayuz.tabloUrunler.setColumnWidth(0, 130)
        self.arayuz.tabloUrunler.setColumnWidth(1, 70)

        satirIndisi = 0
        for urun in urunler:
            self.arayuz.tabloUrunler.setItem(satirIndisi,0, QtWidgets.QTableWidgetItem(urun["urun_adi"]))
            self.arayuz.tabloUrunler.setItem(satirIndisi,1, QtWidgets.QTableWidgetItem(str(urun["fiyat"])))
            satirIndisi += 1


        # self.arayuz.tabloUrunler.setItem(0,0, QtWidgets.QTableWidgetItem("MSI GP62"))
        # self.arayuz.tabloUrunler.setItem(0,1, QtWidgets.QTableWidgetItem("7000"))
        # self.arayuz.tabloUrunler.setItem(1,0, QtWidgets.QTableWidgetItem("MSI GP71"))
        # self.arayuz.tabloUrunler.setItem(1,1, QtWidgets.QTableWidgetItem("7600"))





def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(uyg.exec_())
uygulama()