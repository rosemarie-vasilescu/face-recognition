import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
import time
import statistics

class NearestNeighbor:
    def __init__(self,A, poza, norma):
        self.A = A
        self.norma=norma
        self.poza=poza
        self.nr_poze_antrenare = int(len(self.A) / 40)
        self.dictionar = {'1': 1, '2': 2, 'infinit': np.inf, 'cosinus': np.cos(180)}

    def NN(self):

        #self.poza = self.poza.reshape(-1, )
        col = len(self.A[:, 2])
        z = np.zeros((len(self.A[0]), 1), dtype=float)
        # print(type(z), np.shape(z))


        for i in range(0, len(self.A[0])):
         #   print(self.A[:,i].shape)
            if self.norma == '1':
                diferenta = self.poza - self.A[:, i]

                z[i] = la.norm(diferenta, 1)
            #    print("z[i] norma 1 : ", z[i], i)
            elif self.norma in self.dictionar.keys() and self.norma == '2':
                diferenta = self.poza - self.A[:, i]
                z[i] = la.norm(diferenta, 2)
             #   print("z[i] norma 2: ", z[i])
            elif self.norma in self.dictionar.keys() and self.norma == 'infinit':
                diefrenta = self.poza - self.A[:, i]
                z[i] = la.norm(diefrenta, np.inf)
           #     print("z[i] norma inf: ", z[i])
            elif self.norma in self.dictionar.keys() and self.norma == 'cosinus':
                numarator = 1 - np.dot(self.poza, self.A[:, i])
                numitor = la.norm(self.poza) * la.norm(self.A[:, i])
                z[i] = numarator / numitor
           #     print("z[i] norma cos: ", z[i])
            else:
                print("Alege o norma corecta")

        self.pozitie = np.argmin(z)

        return self.pozitie;

