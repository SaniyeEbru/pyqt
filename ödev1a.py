from PyQt4.QtCore import *
from PyQt4.QtGui import *
class personelDevirHızı(QDialog):
    def __init__(self,ebeveyn=None):
        super(personelDevirHızı,self).__init__(ebeveyn)
        grid=QGridLayout()

        grid.addWidget(QLabel("işten çıkanların sayısı:"),0,0)
        self.istenCikan=QLineEdit()
        grid.addWidget(self.istenCikan,0,1)

        grid.addWidget(QLabel("ortalama personel sayısı:"),1,0)
        self.ortalamaPersonel=QLineEdit()
        grid.addWidget(self.ortalamaPersonel,1,1)

        hesaplaDugme=QPushButton("hesapla")
        grid.addWidget(hesaplaDugme,2,1)
        self.connect(hesaplaDugme,SIGNAL('pressed()'),self.hesapla)

        self.setLayout(grid)
        self.setWindowTitle("personel devir hızı")
        self.resize(250,150)
    def hesapla(self):
        ic=int(self.istenCikan.text())
        op=int(self.ortalamaPersonel.text())
        devirhızı=(ic/op)*100



uygulama=QApplication([])
pencere=personelDevirHızı()
pencere.show()
uygulama.exec_

        
        
