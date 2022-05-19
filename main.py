from Matrice import MatA
from NN import NearestNeighbor
from Eigenfaces import Eigenfaces
from Lanczos import Lanczos
from PyQt5.QtWidgets import QInputDialog
class Principal:

    def __init__(self, db, db_config, alg, norma, img, gui):
        self.bd = MatA( db_config)
        self.A= self.bd.matA()

        if alg=='NN':
            nr_vecini=self.alegeNrVecini(gui)
            self.solutie=NearestNeighbor(self.A, norma, img, nr_vecini)
        if alg=='Eigenfaces':
            k=self.alegeNivelTrunchiere(gui)
            clasic = self.alegeImplementarea(gui)
            print(clasic)
            if clasic=='Clasic':
                clasic=True
            else:
                clasic=False
            self.solutie=Eigenfaces(self.A, norma, img, k, clasic)
        if alg=='Lanczos':
            k = self.alegeNivelTrunchiere(gui)
            self.solutie=Lanczos(self.bd, norma, img, k)


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
        self.solutie.img=img
        return self.solutie.cautare(False)

    def testeazaAlg(self):
        print('continua testarea')
        self.solutie.testeaza()