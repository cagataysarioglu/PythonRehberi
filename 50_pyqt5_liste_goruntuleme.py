import sys
from PyQt5 import QtWidgets
from qt_liste_goruntuleme import Ui_AnaPencere

class Pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.arayuz = Ui_AnaPencere()
        self.arayuz.setupUi(self)

        # Öğrencileri yükle
        self.ogrencileriYukle()

        # Yeni öğrenci ekle
        self.arayuz.dgmEkle.clicked.connect(self.ogrenciEkle)

        # Öğrenciyi düzenle
        self.arayuz.dgmDuzenle.clicked.connect(self.ogrenciyiDuzenle)

        # Öğrenciyi sil
        self.arayuz.dgmSil.clicked.connect(self.ogrenciyiSil)

        # Öğrenciyi yukarıya taşı
        self.arayuz.dgmYukariya.clicked.connect(self.yukariyaTasi)

        # Öğrenciyi aşağıya taşı
        self.arayuz.dgmAsagiya.clicked.connect(self.asagiyaTasi)

        # Öğrencileri sırala
        self.arayuz.dgmSirala.clicked.connect(self.ogrencileriSirala)

        # Çık
        self.arayuz.dgmCik.clicked.connect(self.cikis)

    def ogrencileriYukle(self):
        self.arayuz.listeAraci.addItems(["Kürşad", "Sencer", "Mete", "Bumin", "Gökçe", "Bengü", "Konuralp", "Ezgi"])
        self.arayuz.listeAraci.setCurrentRow(0)

    def ogrenciEkle(self):
        mevcutIndis = self.arayuz.listeAraci.currentRow()
        metin, tamam = QtWidgets.QInputDialog.getText(self, "Ekle", "Öğrenci Adı")
        
        if tamam and metin is not None:
            self.arayuz.listeAraci.insertItem(mevcutIndis, metin)

    def ogrenciyiDuzenle(self):
        indis = self.arayuz.listeAraci.currentRow()
        secim = self.arayuz.listeAraci.item(indis)
        
        if secim is not None:
            metin, tamam = QtWidgets.QInputDialog.getText(self, "Düzenle", "Öğrenci Adı", QtWidgets.QLineEdit.Normal, secim.text())
            if metin and tamam is not None:
                secim.setText(metin)

    def ogrenciyiSil(self):
        indis = self.arayuz.listeAraci.currentRow()
        secim = self.arayuz.listeAraci.item(indis)
        
        if secim is None:
            return

        soru = QtWidgets.QMessageBox.question(self, "Kaldır", secim.text() + " adlı öğrenciyi kaldırmak istiyor musunuz?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if soru == QtWidgets.QMessageBox.Yes:
            secim = self.arayuz.listeAraci.takeItem(indis)
            del secim

    def yukariyaTasi(self):
        indis = self.arayuz.listeAraci.currentRow()
        if indis >= 1:
            secim = self.arayuz.listeAraci.takeItem(indis)
            self.arayuz.listeAraci.insertItem(indis - 1, secim)
            self.arayuz.listeAraci.setCurrentItem(secim)

    def asagiyaTasi(self):
        indis = self.arayuz.listeAraci.currentRow()
        if indis < self.arayuz.listeAraci.count() - 1:
            secim = self.arayuz.listeAraci.takeItem(indis)
            self.arayuz.listeAraci.insertItem(indis + 1, secim)
            self.arayuz.listeAraci.setCurrentItem(secim)

    def ogrencileriSirala(self):
        self.arayuz.listeAraci.sortItems()

    def cikis(self):
        quit()

def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(uyg.exec_())
uygulama()
