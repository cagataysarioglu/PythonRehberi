import sys
from PyQt5 import QtWidgets, QtGui

class Renk(QtWidgets.QWidget):
    def __init__(self, renk):
        super(Renk, self).__init__()
        self.setAutoFillBackground(True)

        renkPaleti = self.palette()
        renkPaleti.setColor(QtGui.QPalette.Window, QtGui.QColor(renk))
        self.setPalette(renkPaleti)

class AnaPencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(AnaPencere, self).__init__()
        self.setGeometry(150, 150, 500, 400)

        sayfaDuzeni = QtWidgets.QVBoxLayout() # QHBoxLayout() de olabilir.
        sayfaDuzeni.addWidget(Renk("turquoise"))
        sayfaDuzeni.addWidget(Renk("yellow"))
        sayfaDuzeni.addWidget(Renk("darkblue"))
        # sayfaDuzeni.setContentsMargins(5, 20, 5, 7)
        sayfaDuzeni.setSpacing(30)

        # sayfaDuzeni = QtWidgets.QGridLayout()
        # sayfaDuzeni.addWidget(Renk("green"), 0,0)
        # sayfaDuzeni.addWidget(Renk("blue"), 0,1)
        # sayfaDuzeni.addWidget(Renk("yellow"), 1,0)
        # sayfaDuzeni.addWidget(Renk("brown"), 1,1)

        pencereAraci = QtWidgets.QWidget()
        pencereAraci.setLayout(sayfaDuzeni)
        self.setCentralWidget(pencereAraci)

def uygulama():
    uyg = QtWidgets.QApplication(sys.argv)
    pnc = AnaPencere()
    pnc.show()
    sys.exit(uyg.exec_())
uygulama()