import sys
from PyQt5 import QtWidgets, QtGui

def pencere():
    uyglm = QtWidgets.QApplication(sys.argv)
    pncr = QtWidgets.QMainWindow()

    pncr.setWindowTitle("İlk Uygulama")
    pncr.setGeometry(200, 200 ,639, 552)
    pncr.setWindowIcon(QtGui.QIcon("Turk_bayragi_ikonu.png"))
    pncr.setToolTip("İpucu aracı")

    katman_ad = QtWidgets.QLabel(pncr)
    katman_ad.setText("Adınız: ")
    katman_ad.move(50, 30)

    katman_soyad = QtWidgets.QLabel(pncr)
    katman_soyad.setText("Soyadınız: ")
    katman_soyad.move(50, 60)

    yazmaca_ad = QtWidgets.QLineEdit(pncr)
    yazmaca_ad.move(115, 30)

    yazmaca_soyad = QtWidgets.QLineEdit(pncr)
    yazmaca_soyad.move(115, 60)

    def tiklandi(self):
        print("Düğmeye tıklandı. Ad: " + yazmaca_ad.text() + " Soyad: " + yazmaca_soyad.text())

    kayit_dugmesi = QtWidgets.QPushButton(pncr)
    kayit_dugmesi.move(115, 95) # kayit_dugmesi.setGeometry(150, 95, 70, 40)
    kayit_dugmesi.setText("Sakla")
    kayit_dugmesi.clicked.connect(tiklandi)




    pncr.show()
    sys.exit(uyglm.exec_())
pencere()
