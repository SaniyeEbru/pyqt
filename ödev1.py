from PyQt4.QtGui import *
from PyQt4.QtCore import *
class ogrenciBolum(QDialog):
    def __init__(self,ebeveyn=None):
        super(ogrenciBolum,self).__init__(ebeveyn)
        grid=QGridLayout()
        self.tablo=QTableWidget()
        self.tablo.resize(400,240)
        self.tablo.setRowCount(5)
        self.tablo.setColumnCount(3)
        grid.addWidget(self.tablo)
        self.tablo.setItem(0,0,QTableWidgetItem("ADI"))
        self.tablo.setItem(0,1,QTableWidgetItem("SOYADI"))
        self.tablo.setItem(0,2,QTableWidgetItem("BOLUM"))
        self.tablo.setItem(1,0,QTableWidgetItem("CAN"))
        self.tablo.setItem(1,1,QTableWidgetItem("AYDIN"))
        self.tablo.setItem(1,2,QTableWidgetItem("YBS"))
        self.tablo.setItem(2,0,QTableWidgetItem("SEMİH"))
        self.tablo.setItem(2,1,QTableWidgetItem("YARAR"))
        self.tablo.setItem(2,2,QTableWidgetItem("YBS"))
        self.tablo.setItem(3,0,QTableWidgetItem("BÜŞRA"))
        self.tablo.setItem(3,1,QTableWidgetItem("DEMİRGÜREŞÇİ"))
        self.tablo.setItem(3,2,QTableWidgetItem("İKTİSAT"))
        self.tablo.show()
        return uyg.exec_()
uyg=QApplication([])
pencere=ogrenciBolum()
pencere.show()
uyg.exec_
