from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Start import Principal
from matplotlib import pyplot as plt
PLACEHOLDER='Placeholder.png'
import numpy as np
import pickle
import traceback
class Ui_MainWindow(QtWidgets.QWidget):
    _img=PLACEHOLDER

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbAlegereBD = QtWidgets.QGroupBox(self.centralwidget)
        self.gbAlegereBD.setGeometry(QtCore.QRect(410, 10, 301, 80))
        self.gbAlegereBD.setObjectName("gbAlegereBD")
        self.rbORL = QtWidgets.QRadioButton(self.gbAlegereBD)
        self.rbORL.setGeometry(QtCore.QRect(20, 30, 82, 21))
        self.rbORL.setObjectName("rbORL")
        self.rbORL.setChecked(True)
        self.rbEssex = QtWidgets.QRadioButton(self.gbAlegereBD)
        self.rbEssex.setGeometry(QtCore.QRect(110, 30, 82, 21))
        self.rbEssex.setObjectName("rbEssex")
        self.rbEssex.setEnabled(False)
        self.rbCTOVF = QtWidgets.QRadioButton(self.gbAlegereBD)
        self.rbCTOVF.setGeometry(QtCore.QRect(200, 30, 82, 21))
        self.rbCTOVF.setObjectName("rbCTOVF")
        self.rbCTOVF.setEnabled(False)
        self.gbConfigBD = QtWidgets.QGroupBox(self.centralwidget)
        self.gbConfigBD.setGeometry(QtCore.QRect(410, 110, 301, 131))
        self.gbConfigBD.setObjectName("gbConfigBD")
        self.rb6040 = QtWidgets.QRadioButton(self.gbConfigBD)
        self.rb6040.setGeometry(QtCore.QRect(10, 30, 181, 21))
        self.rb6040.setObjectName("rb6040")
        self.rb8020 = QtWidgets.QRadioButton(self.gbConfigBD)
        self.rb8020.setGeometry(QtCore.QRect(10, 60, 181, 21))
        self.rb8020.setObjectName("rb8020")
        self.rb8020.setChecked(True)
        self.rb9010 = QtWidgets.QRadioButton(self.gbConfigBD)
        self.rb9010.setGeometry(QtCore.QRect(10, 90, 191, 21))
        self.rb9010.setObjectName("rb9010")
        self.gbAlegeAlg = QtWidgets.QGroupBox(self.centralwidget)
        self.gbAlegeAlg.setGeometry(QtCore.QRect(410, 260, 301, 121))
        self.gbAlegeAlg.setObjectName("gbAlegeAlg")
        self.rbNN = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbNN.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rbNN.setObjectName("rbNN")
        self.rbNN.setChecked(True)
        self.rbCOD = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbCOD.setGeometry(QtCore.QRect(20, 60, 82, 16))
        self.rbCOD.setObjectName("rbCOD")
        self.rbTensori = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbTensori.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.rbTensori.setObjectName("rbTensori")
        self.rbEigenfaces = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbEigenfaces.setGeometry(QtCore.QRect(160, 30, 82, 21))
        self.rbEigenfaces.setObjectName("rbEigenfaces")
        self.rbLanczos = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbLanczos.setGeometry(QtCore.QRect(160, 60, 82, 16))
        self.rbLanczos.setObjectName("rbLanczos")
        self.rbElanbi = QtWidgets.QRadioButton(self.gbAlegeAlg)
        self.rbElanbi.setGeometry(QtCore.QRect(160, 90, 82, 16))
        self.rbElanbi.setObjectName("rbElanbi")
        self.gbAlegeNorma = QtWidgets.QGroupBox(self.centralwidget)
        self.gbAlegeNorma.setGeometry(QtCore.QRect(410, 400, 301, 91))
        self.gbAlegeNorma.setObjectName("gbAlegeNorma")
        self.rbL1 = QtWidgets.QRadioButton(self.gbAlegeNorma)
        self.rbL1.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rbL1.setObjectName("rbL1")
        self.rbL1.setChecked(True)
        self.rbL2 = QtWidgets.QRadioButton(self.gbAlegeNorma)
        self.rbL2.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rbL2.setObjectName("rbL2")
        self.rbInfinit = QtWidgets.QRadioButton(self.gbAlegeNorma)
        self.rbInfinit.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.rbInfinit.setObjectName("rbInfinit")
        self.rbCosinus = QtWidgets.QRadioButton(self.gbAlegeNorma)
        self.rbCosinus.setGeometry(QtCore.QRect(150, 60, 82, 17))
        self.rbCosinus.setObjectName("rbCosinus")
        self.pushbIncarca = QtWidgets.QPushButton(self.centralwidget)
        self.pushbIncarca.setGeometry(QtCore.QRect(420, 500, 101, 23))
        self.pushbIncarca.setObjectName("pushbIncarca")
        self.pushbCauta = QtWidgets.QPushButton(self.centralwidget)
        self.pushbCauta.setGeometry(QtCore.QRect(640, 500, 75, 23))
        self.pushbCauta.setObjectName("pushbCauta")
        self.pushbCauta.setEnabled(False)
        self.labGasit = QtWidgets.QLabel(self.centralwidget)
        self.labGasit.setGeometry(QtCore.QRect(736, 22, 361, 511))
        self.labGasit.setText("")
        self.labGasit.setPixmap(QtGui.QPixmap("Placeholder.png"))
        self.labGasit.setScaledContents(True)
        self.labGasit.setObjectName("labGasit")
        self.labCautat = QtWidgets.QLabel(self.centralwidget)
        self.labCautat.setGeometry(QtCore.QRect(26, 22, 361, 511))
        self.labCautat.setText("")
        self.labCautat.setPixmap(QtGui.QPixmap("Placeholder.png"))
        self.labCautat.setScaledContents(True)
        self.labCautat.setObjectName("labCautat")
        self.pushbAplica = QtWidgets.QPushButton(self.centralwidget)
        self.pushbAplica.setGeometry(QtCore.QRect(530, 500, 101, 23))
        self.pushbAplica.setObjectName("pushbAplica")
        self.pushbStatistici = QtWidgets.QPushButton(self.centralwidget)
        self.pushbStatistici.setGeometry(QtCore.QRect(570, 530, 141, 21))
        self.pushbStatistici.setObjectName("pushbStatistici")
        self.pushbStatistici.setEnabled(True)
        self.pushbTesteaza = QtWidgets.QPushButton(self.centralwidget)
        self.pushbTesteaza.setGeometry(QtCore.QRect(420, 530, 131, 23))
        self.pushbTesteaza.setObjectName("pushbTesteaza")
        self.pushbTesteaza.setEnabled(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushbAplica.clicked.connect(self.pregatesteDate)
        self.pushbIncarca.clicked.connect(self.incarca)
        self.pushbCauta.clicked.connect(self.cauta)
        self.pushbTesteaza.clicked.connect(self.testeaza)
        self.pushbStatistici.clicked.connect(self.afisazaStatistici)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gbAlegereBD.setTitle(_translate("MainWindow", "Alegeti baza de date"))
        self.rbORL.setText(_translate("MainWindow", "ORL"))
        self.rbEssex.setText(_translate("MainWindow", "Essex"))
        self.rbCTOVF.setText(_translate("MainWindow", "CTOVF"))
        self.gbConfigBD.setTitle(_translate("MainWindow", "Configurati baza de date"))
        self.rb6040.setText(_translate("MainWindow", "60% training 40% testing"))
        self.rb8020.setText(_translate("MainWindow", "80% training 20% testing"))
        self.rb9010.setText(_translate("MainWindow", "90% training 10% testing"))
        self.gbAlegeAlg.setTitle(_translate("MainWindow", "Alegeti algoritmul"))
        self.rbNN.setText(_translate("MainWindow", "NN"))
        self.rbCOD.setText(_translate("MainWindow", "COD"))
        self.rbTensori.setText(_translate("MainWindow", "Tensori"))
        self.rbEigenfaces.setText(_translate("MainWindow", "Eigenfaces"))
        self.rbLanczos.setText(_translate("MainWindow", "Lanczos"))
        self.rbElanbi.setText(_translate("MainWindow", "Elanbi"))
        self.gbAlegeNorma.setTitle(_translate("MainWindow", "Alegeti norma"))
        self.rbL1.setText(_translate("MainWindow", "L1"))
        self.rbL2.setText(_translate("MainWindow", "L2"))
        self.rbInfinit.setText(_translate("MainWindow", "Infinit"))
        self.rbCosinus.setText(_translate("MainWindow", "Cosinus"))
        self.pushbIncarca.setText(_translate("MainWindow", "Incarca o imagine"))
        self.pushbCauta.setText(_translate("MainWindow", "Cauta"))
        self.pushbAplica.setText(_translate("MainWindow", "Aplica Algoritmul"))
        self.pushbStatistici.setText(_translate("MainWindow", "Afisati Statistici"))
        self.pushbTesteaza.setText(_translate("MainWindow", "Testeaza"))

    def pregatesteDate(self):
        #restrictioneaza imaginea ce poate fi folosit la png, jpg, formatul
        #folosit in orl, etc


        self.db_config=self.returneazaDBC()
        self.alg=self.returneazaAlg()
        self.norma=self.returneazNorma()
        self.hub = Principal( self.db_config, self.alg, self.norma, self._img,self)


        algoritmi = {'COD': 'COD',
                     'Tensori': 'Tensori',
                     'Eigenfaces': 'Eigenfaces',
                     'Lanczos': 'Lanczos',
                     'Elanbi': 'Elanbi', }

        # ADAUGA RESTUL ALGORITMILOR PE MASURA CE II IMPLEMENTEZI
        #NN nu mai are de mai multa pregatire, dar celelalte alg au nevoie, asa ca punem una bucata switch
        #si daca e nevoie de mai multe pregatiri, atunci le facem, daca nu, e bine

        self.pushbCauta.setEnabled(True)
        self.pushbTesteaza.setEnabled(True)

    # def returneazaDB(self):
    #     alegeBD_c = self.gbAlegereBD.children()
    #
    #     for child in alegeBD_c:
    #         if child.isChecked():
    #             return child.text()
    #
    #     return ''

    def returneazaDBC(self):

        if self.rb6040.isChecked():
            config = 6
        elif self.rb8020.isChecked():
            config= 8
        elif self.rb9010.isChecked():
            config = 9
        return config

    def returneazaAlg(self):

        if self.rbNN.isChecked():
            alg = 'NN'
        elif self.rbEigenfaces.isChecked():
            alg = 'Eigenfaces'
        elif self.rbLanczos.isChecked():
            alg = 'Lanczos'
        return alg



    def returneazNorma(self):

        if self.rbL1.isChecked():
            norma= '1'
        elif self.rbL2.isChecked():
            norma = '2'
        elif self.rbInfinit.isChecked():
            norma = 'infinit'
        elif self.rbCosinus.isChecked():
            norma = 'cosinus'
        return norma

    def cauta(self):
        print('cauta')
        pers_poza=self.hub.cautaPoza(self._img)
        print(pers_poza+1,'cauta')
        director='D:\\Facultate\\Anul 3\\ACS\\att_faces (1)\\s'+str(pers_poza+1)+'\\'+'1.pgm'
        self.labGasit.setPixmap(QtGui.QPixmap(director))
        pass

    def testeaza(self):
        #print('incepe testarea')
        self.hub.testeazaAlg()
        pass

    def incarca(self):
        Tk().withdraw()
        self._img = askopenfilename()
        print('ok')
        if(self._img != ''):
            self.arataImg1(self._img)

    def arataImg1(self, img):
        print(img)
        self.labCautat.setPixmap(QtGui.QPixmap(img))

    def afisazaStatistici(self):
        algoritmi=['NN','Eigenfaces', 'Lanczos']
        alg, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege algoritmul", "Alg:", algoritmi, 0, False)

        if  alg=='NN':
            impartire = ['60-40', '80-20', '90-10']
            ratie, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege modul de impartire al bazei de date", "Nr:", impartire, 0, False)
            if ratie=='60-40':
                self.afisazaStatNN(0)
            if ratie=='80-20':
                self.afisazaStatNN(1)
            if ratie == '90-10':
                self.afisazaStatNN(2)

        if alg=='Eigenfaces':
            impartire = ['60-40', '80-20', '90-10']
            ratie, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege modul de impartire al bazei de date", "Nr:",
                                                              impartire, 0, False)
            optiuni=['Da','Nu']
            clase, okPressed = QtWidgets.QInputDialog.getItem(self, "Foloseste reprezentanti de clase?", "",
                                                              optiuni, 0, False)
            if clase=='Da':
                clase=True
            else:
                clase = False
            if ratie=='60-40':
                self.afisazaStatEF(ratie, clase)
            if ratie=='80-20':
                self.afisazaStatEF(ratie, clase)
            if ratie == '90-10':
                self.afisazaStatEF(ratie, clase)

        if alg == 'Lanczos':
            impartire = ['60-40', '80-20', '90-10']
            ratie, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege modul de impartire al bazei de date",
                                                              "Nr:",
                                                              impartire, 0, False)

            if ratie == '60-40':
                self.afisazaStatLan(ratie)
            if ratie == '80-20':
                self.afisazaStatLan(ratie)
            if ratie == '90-10':
                self.afisazaStatLan(ratie)

    def afisazaStatNN(self, multiplu_de_32):
        with open('statisticiNN.txt','r') as f:
            rezultate=f.read()


        rezultate=rezultate.split()
        rezultate = np.double(rezultate[:])

        norme=['norma 1', 'norma 2', 'norma inf', 'norma cos']
        i=0+(32*multiplu_de_32)
        while (i<len(rezultate)):
            precizii=[rezultate[i],rezultate[i+2],rezultate[i+4],rezultate[i+6]]
            timpi=[rezultate[i+1], rezultate[i+3],rezultate[i+5], rezultate[i+7]]
            print(precizii)
            print(timpi)
            fig, ax=plt.subplots(1, 2, sharey='none',figsize=(12,8))
            ax[0].bar(norme, precizii)
            ax[0].set_ylabel('Precizie')
            ax[1].bar(norme, timpi)
            ax[1].set_ylabel('Timp mediu de cautare')

            ax[0].set_ylim([0,1])
            if (i%32<8):
                fig.suptitle('Statistici NN')
            elif i%32<16:
                fig.suptitle('Statistici KNN unde k=3')
            elif i%32<24:
                fig.suptitle('Statistici KNN unde k=5')
            else:
                fig.suptitle('Statistici KNN unde k=7')
            plt.show()
            i+=8
            if (i%32==0):
                break

    def afisazaStatEF(self,rata, clase):

        if clase == True:
            fisier=open('eigC'+rata[0]+'.txt', 'rb')
            print('fisierdeschis')
        else:
            fisier = open('eig' + rata[0] + '.txt', 'rb')
        stat=pickle.load(fisier)
        print(stat)
        fisier.close()
        norme = ['norma 1', 'norma 2', 'norma inf', 'norma cos']

        if clase == True:
            fisier=open('eigC_pre'+rata[0]+'.txt','rb')
        else:
            fisier = open('eig_pre' + rata[0] + '.txt', 'rb')
        timp_pre=pickle.load(fisier)
        fisier.close()

        timpi=[]
        precizii=[]
        for i in range(len(stat)):
            precizii.append(stat[i][0])
            timpi.append(stat[i][1])
        print(precizii)
        nr_baze = ['20', '40', '60','80','100']
        ratie, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege nivelul de trunchiere", "Lvl:",
                                                          nr_baze, 0, False)

        multiplier=int(int(ratie)/5-4)

        print(precizii)
        print(timpi)

        aratPre=[]
        aratTmp=[]

        for i in range(4):

            aratPre.append(precizii[multiplier+i])
            aratTmp.append(timpi[multiplier + i])

        fig, ax = plt.subplots(1, 2, sharey='none', figsize=(12, 8))
        ax[0].bar(norme, aratPre)
        ax[0].set_ylabel('Precizie')
        ax[1].bar(norme, aratTmp)
        ax[1].set_ylabel('Timp mediu de cautare')
        ax[0].set_ylim([0, 1])
        plt.show()

        fig, ax = plt.subplots()
        ax.plot(nr_baze, timp_pre)
        ax.set(xlabel='nivelul de trunchiere', ylabel='timp(s)', title='timpul de preprocesare')
        plt.show()


    def afisazaStatLan(self,rata):
        fisier = open('lanczos' + rata[0] + '.txt', 'rb')
        stat=pickle.load(fisier)
        fisier.close()
        norme = ['norma 1', 'norma 2', 'norma inf', 'norma cos']

        fisier = open('lanczos_pre' + rata[0] + '.txt', 'rb')
        timp_pre = pickle.load(fisier)
        fisier.close()

        timpi=[]
        precizii=[]
        for i in range(len(stat)):
            precizii.append(stat[i][0])
            timpi.append(stat[i][1])

        nr_baze = ['20', '40', '60','80','100']
        ratie, okPressed = QtWidgets.QInputDialog.getItem(self, "Alege nivelul de trunchiere", "Lvl:",
                                                          nr_baze, 0, False)
        multiplier=int(int(ratie)/5-4)
        #5k si 4 norme
        print(precizii)
        print(timpi)

        aratPre=[]
        aratTmp=[]

        for i in range(4):
            print(multiplier, i, len(precizii), len(timpi))
            try:
                print(precizii[multiplier+i])
                print(timpi[multiplier + i])
                aratPre.append(precizii[multiplier+i])
                aratTmp.append(timpi[multiplier + i])

            except:
                traceback.print_exc()
                sys.exit()
        print(aratPre)
        print(aratTmp)

        fig, ax = plt.subplots(1, 2, sharey='none', figsize=(12, 8))
        ax[0].bar(norme, aratPre)
        ax[0].set_ylabel('Precizie')
        ax[1].bar(norme, aratTmp)
        ax[1].set_ylabel('Timp mediu de cautare')
        ax[0].set_ylim([0, 1])
        plt.show()

        fig, ax = plt.subplots()
        ax.plot(nr_baze, timp_pre)
        ax.set(xlabel='nivelul de trunchiere', ylabel='timp(s)', title='timpul de preprocesare')
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())