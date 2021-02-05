import sys
from PyQt5 import QtWidgets
from qt_calisma import Ui_AnaPencere

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()
        
        self.arayuz = Ui_AnaPencere()
        self.arayuz.setupUi(self)

        kombo = self.arayuz.komboKentler

        # kombo.addItem("Ankara")
        # kombo.addItem("Trabzon")
        # kombo.addItems(["İstanbul", "Erzurum", "Antalya"])

        self.arayuz.dgmSecimleriYukle.clicked.connect(self.secimleriYukle)
        self.arayuz.dgmSecimleriGetir.clicked.connect(self.secimleriGetir)
        self.arayuz.dgmSecimleriGetir.clicked.connect(self.secimleriTemizle)
        self.arayuz.dgmCikis.clicked.connect(self.diyalogGoruntule)

        self.arayuz.komboKentler.currentIndexChanged.connect(self.secilmisDegismisIndis)
        self.arayuz.komboKentler.currentIndexChanged[str].connect(self.secilmisDegismisMetin)

    def secimleriYukle(self):
        kentler = ["İstanbul", "Erzurum", "Antalya"]

        self.arayuz.komboKentler.addItems(kentler)

    def secimleriGetir(self):
        print(self.arayuz.komboKentler.currentText())
        print(self.arayuz.komboKentler.currentIndex())

        sayac = self.arayuz.komboKentler.count()
        for indis in range(sayac):
            print(self.arayuz.komboKentler.itemText(indis))

    def secimleriTemizle(self):
        self.arayuz.komboKentler.clear()

    def secilmisDegismisIndis(self, indis):
        print(indis)

    def secilmisDegismisMetin(self, metin):
        print(metin)

    def diyalogGoruntule(self):
        islem = QtWidgets.QMessageBox.question(self, "Uygulamayı Kapat", "Emin misiniz?", QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Ok)
        if islem == QtWidgets.QMessageBox.Ok:
            print("Evet tıklandı")
            QtWidgets.qApp.quit()
        else:
            print("Hayır tıklandı")

    #     ileti = QtWidgets.QMessageBox()

    #     ileti.setWindowTitle("Uygulamayı Kapat")
    #     ileti.setText("Emin misiniz?")
    #     ileti.setIcon(QtWidgets.QMessageBox.Warning)
    #     ileti.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore)
    #     ileti.setDefaultButton(QtWidgets.QMessageBox.Ok)
    #     ileti.setDetailedText("Ayrıntılar...")
    #     ileti.buttonClicked.connect(self.acilirDugme)

    #     x = ileti.exec_()

    # def acilirDugme(self, i):
    #     print(i.text())

    #     if i.text() == "OK":
    #         print("TAMAM")
    #         QtWidgets.qApp.quit()
    #     elif i.text() == "Cancel":
    #         print("ÇIKIŞ")
    #     else:
    #         print("REDDET")

def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(uyg.exec_())
uygulama()
