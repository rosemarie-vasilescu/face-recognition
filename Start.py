from Matrice import MatA
from NN import NearestNeighbor
from kNN import kNearestNeighbor
from Eigenfaces import Eigenfaces
from Lanczos import Lanczos
import cv2
import time
import statistics
import math
from PyQt5.QtWidgets import QInputDialog
class Principal:

    def __init__(self, db_config, alg, norma, img, gui):
        self.A = MatA( db_config)
        print(self.A)
        self.A.matA()
        self.alg=alg
        print(alg)
        if alg=='NN':
            nr_vecini=self.alegeNrVecini(gui)
            print(nr_vecini)
            self.solutie=kNearestNeighbor(self.A, norma, img, nr_vecini,db_config)
        if alg=='Eigenfaces':
            k=self.alegeNivelTrunchiere(gui)
            global clasic
            clasic = self.alegeImplementarea(gui)

            if clasic=='Clasic':
                clasic=True
            else:
                clasic=False
            self.solutie=Eigenfaces(self.A, norma, img, k, clasic,db_config)
        if alg=='Lanczos':
            k = self.alegeNivelTrunchiere(gui)
            print('k')
            self.solutie=Lanczos(self.A, norma, img, k,db_config)


        # ADAUGA RESTUL ALGORITMILOR PE MASURA CE II IMPLEMENTEZI



    def alegeNrVecini(self, gui):
        items = ('1','3','5','7', '9', '11')
        item, okPressed = QInputDialog.getItem(gui, "Alege numarul de vecini", "Nr:", items, 0, False)
        if okPressed and item:
            return int(item)

    def alegeNivelTrunchiere(self, gui):
        items = ('20','40','60','80', '100')
        item, okPressed = QInputDialog.getItem(gui, "Alege nivelul de trunchiere", "Nr:", items, 0, False)
        if okPressed and item:
            return int(item)

    def alegeImplementarea(self, gui):
        items = ('Clasic','Cu reprezentanti de clase')
        item, okPressed = QInputDialog.getItem(gui, "Alege implementarea", "Imp:", items, 0, False)
        if okPressed and item:
            return item

    def cautaPoza(self, img):
        print(img)
        poza_cautata = cv2.imread(img, 0)
        poza_cautata = poza_cautata.reshape(-1, )
        self.solutie.poza_cautata=poza_cautata
        print('cautapoza')

        if self.alg=='Eigenfaces':

            if clasic==True:
                return self.solutie.cautare()
            elif clasic == False:
                return self.solutie.cautare_clase()
        else:
            return self.solutie.cautare()

    def testeazaAlg(self):
        print('continua testarea')
        self.solutie.testeaza()