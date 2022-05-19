import pickle

import cv2
from NN import NearestNeighbor
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
import time

class Eigenfaces:
    def __init__(self,db, norma, poza_cautata, k, clasic, nr_poze_antrenare):
        self.A=db.A
        self.RC = np.zeros([10304, 40])

        self.k=k
        self.norma=norma
        self.poza_cautata=poza_cautata
        self.nr_poze_antrenare = nr_poze_antrenare
        self.clasic = clasic
        self.rezultate_testare = []
        self.timpi_preproc = []
        for it in range(0, 40):
            i = it * self.nr_poze_antrenare
            self.RC[:, it] = np.mean(self.A[:, i:i + self.nr_poze_antrenare], axis=1)

        if clasic:

            self.preprocesareOptimizata()
        else:
            self.preprocesareOptimizata_clase()

    def preprocesareOptimizata(self):
        B = self.A
        self.medie = np.mean(self.A, axis=1)
        self.A = (self.A.T - self.medie).T
        cov = np.dot(self.A.T, self.A)
        d, v = np.linalg.eig(cov)
        v = np.dot(self.A, v)
        indx = np.argsort(d)
        indx = indx[:len(indx) - self.k - 1:-1]
        self.HQPB = v[:, indx]
        self.proiectii = np.dot(self.A.T, self.HQPB)
        print("HQPB: ", self.HQPB.shape)
        print("proiectii: ", self.proiectii.shape)
        self.A = B


    def preprocesareOptimizata_clase(self):
        RCB = self.RC
        global B
        B = self.A

        self.A = self.RC
        self.medie = np.mean(self.A, axis=1)
        self.A = (self.A.T - self.medie).T

        cov = np.dot(self.A.T, self.A)
        d, v = np.linalg.eig(cov)
        v = np.dot(self.A, v)
        indx = np.argsort(d)
        indx = indx[:len(indx) - self.k - 1:-1]
        self.HQPB = v[:, indx]

        self.proiectii = np.dot(self.A.T, self.HQPB)

        self.A = RCB



    def cautare(self):
        print('inainte', self.poza_cautata.shape)
        self.poza_cautata = self.poza_cautata - self.medie
        print('dupa', self.poza_cautata.shape)
        print('hqpb', self.HQPB.shape)
        print('proiectii', self.proiectii.shape)
        self.poza_cautata = np.dot(self.poza_cautata, self.HQPB)
        print('pr', self.poza_cautata.shape)
        nn = NearestNeighbor(self.proiectii.T, self.poza_cautata, self.norma)
        pozitia= nn.NN()
        print(pozitia,'pozitie clasic')
        return pozitia//self.nr_poze_antrenare;

    def cautare_clase(self):
        self.poza_cautata = self.poza_cautata - self.medie
        self.poza_cautata = np.dot(self.poza_cautata, self.HQPB)
        nn = NearestNeighbor(self.proiectii.T, self.poza_cautata, self.norma)
        pozitia = nn.NN()
        print(pozitia,'pozitie rep')
        return pozitia;

    def testeaza(self):
        print('testeaza eigen')
        nrbaze_bck=self.k
        for i in [20,40,60,80,100]:
            self.k=i

            if self.clasic:
                tic=time.perf_counter()
                self.preprocesareOptimizata()
                toc=time.perf_counter()
                timp=toc-tic
                self.timpi_preproc.append(timp)
                print(timp)
            else:
                tic = time.perf_counter()
                self.preprocesareOptimizata_clase()
                toc = time.perf_counter()
                timp = toc - tic
                self.timpi_preproc.append(timp)

            self.variazaNorma()
        self.k=nrbaze_bck

        if self.clasic:
            fisier = open('eig' + str(self.nr_poze_antrenare) + '.txt', 'wb')
            pickle.dump(self.rezultate_testare, fisier)
            fisier.close()
            fisier = open('eig_pre' + str(self.nr_poze_antrenare) + '.txt', 'wb')
            pickle.dump(self.timpi_preproc, fisier)
            fisier.close()
        else:

            fisier = open('eigC' + str(self.nr_poze_antrenare) + '.txt', 'wb')
            pickle.dump(self.rezultate_testare, fisier)
            fisier.close()
            fisier = open('eigC_pre' + str(self.nr_poze_antrenare) + '.txt', 'wb')
            pickle.dump(self.timpi_preproc, fisier)
            fisier.close()
        pass

        pass

    def variazaNorma(self):
        norma_initiala=self.norma
        print('norma')
        #pentru norma L1
        self.norma='1'
        self.testeazaAlg()

        #pentru norma L2
        self.norma='2'
        self.testeazaAlg()

        #pentru norma Inf
        self.norma='infinit'
        self.testeazaAlg()

        #pentru norma Cos
        self.norma='cosinus'
        self.testeazaAlg()

        #restauram norma utilizatorului
        self.norma=norma_initiala

    def testeazaAlg(self):

        nr_poze_testare = 10 - self.nr_poze_antrenare
        TP=0
        suma_timp = 0
        print('testeazaalg')
        caleBD = r'D:\Facultate\Anul 3\ACS\att_faces (1)'

        for i in range(1, 41):
            caleFolderPers = caleBD + '\s' + str(i) + '\\'
            print(caleFolderPers)
            for j in range(self.nr_poze_antrenare + 1, 11):
                calePozaTestare = caleFolderPers + str(j) + '.pgm'
                #print(calePozaTestare)
                # citim poza ca matrice 112 x 92:
                pozaTestare = cv2.imread(calePozaTestare, 0)
                pozaTestare = np.array(pozaTestare)
                pozaVect = pozaTestare.reshape(-1, )
                self.poza_cautata=pozaVect

                tic = time.perf_counter()
                if self.clasic:
                  rezultat = self.cautare()
                  print('rezultat',rezultat)
                else:
                  rezultat = self.cautare_clase()
                  print('rezultatclase',rezultat)
                toc = time.perf_counter() - tic
                suma_timp += toc

                print('i',i)
                if rezultat+1==i:
                   TP += 1


        precizie = TP / (nr_poze_testare * 40)
        durata_medie = suma_timp / (nr_poze_testare * 40)


        self.rezultate_testare.append((precizie,durata_medie))
        print(self.rezultate_testare)
        print('norma este=', self.norma)
        print('precizie=', precizie, ' TP:', TP)
        print('durata_medie=', durata_medie)