import pickle
import math
import cv2
from NN import NearestNeighbor
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
import time

class Lanczos:
    def __init__(self,db, norma, poza_cautata, k,nr_poze_antrenare):
        self.A=db.A
        self.B=self.A
        self.k=k
        self.norma=norma
        self.poza_cautata=poza_cautata
        self.nr_poze_antrenare = nr_poze_antrenare
        self.rezultate_testare = []
        self.timpi_preproc = []
        self.preprocesare()

    def preprocesare(self):
        B = self.A
        q = np.zeros((10304, 1))
        Q = q
        Q = np.hstack((Q, np.ones((10304, 1))))
        Q[:, 1] = Q[:, 1] / la.norm(Q[:, 1])
        beta = 0

        for i in range(1, self.k + 1):
            omega = np.dot(self.A, np.dot(self.A.T, Q[:, i])) - np.dot(beta, Q[:, i - 1])
            alfa = np.dot(omega, Q[:, i])
            omega = omega - np.dot(alfa, Q[:, i])
            beta = la.norm(omega, 2)
            q = omega / beta
            q = q.reshape((10304, 1))
            Q = np.hstack((Q, q))

        self.HQPB = Q[:, 2:self.k + 2]
        self.proiectii = np.dot(self.A.T, self.HQPB)
        # print(HQPB)

        print("HQPB: ", self.HQPB.shape)
        print("proiectii: ", self.proiectii.shape)
        self.A = B
        # return proiectii, HQPB, Q

    def cautare(self):

        print('poza cautata', self.poza_cautata.shape)
        print('hqpb', self.HQPB.shape)
        print('proiectii', self.proiectii.shape)
        self.poza_cautata = np.dot(self.poza_cautata, self.HQPB)
        print('pr', self.poza_cautata.shape)

        nn = NearestNeighbor(self.proiectii.T, self.poza_cautata, self.norma)
        pozitia=nn.NN()
        print('pozitia de la cautare',pozitia//self.nr_poze_antrenare)
        return pozitia//self.nr_poze_antrenare;

    def testeaza(self):
        print('testeaza lanczos')
        nrbaze_bck=self.k
        for i in [20,40,60,80,100]:
            self.k=i


            tic=time.perf_counter()
            self.preprocesare()
            toc=time.perf_counter()
            timp=toc-tic
            self.timpi_preproc.append(timp)
            print(timp)
            self.variazaNorma()
        self.k=nrbaze_bck

        fisier=open('lanczos'+str(self.nr_poze_antrenare)+'.txt','wb')
        pickle.dump(self.rezultate_testare,fisier)
        fisier.close()
        fisier = open('lanczos_pre' + str(self.nr_poze_antrenare) + '.txt', 'wb')
        pickle.dump(self.timpi_preproc, fisier)
        fisier.close()

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
                print(calePozaTestare)
                # citim poza ca matrice 112 x 92:
                pozaTestare = cv2.imread(calePozaTestare, 0)
                pozaTestare = np.array(pozaTestare)
                pozaVect = pozaTestare.reshape(-1, )
                self.poza_cautata=pozaVect
                tic = time.perf_counter()
                rezultat = self.cautare()
                print('rezultat',rezultat)
                toc = time.perf_counter() - tic
                suma_timp += toc
                print('persoana,i',rezultat)
                print(i)
                if rezultat+1==i:
                   TP += 1


        precizie = TP / (nr_poze_testare * 40)
        durata_medie = suma_timp / (nr_poze_testare * 40)


        self.rezultate_testare.append((precizie,durata_medie))
        print(self.rezultate_testare)
        print('norma este=', self.norma)
        print('precizie=', precizie, ' TP:', TP)
        print('durata_medie=', durata_medie)