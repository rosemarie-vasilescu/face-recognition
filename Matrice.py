import cv2

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la
import time
import statistics

class MatA():
    def __init__(self, db_config):

        self.config=db_config
        self.matA()
    def matA(self):

      self.A = np.zeros([10304, self.config * 40])
      caleBD = r'D:\Facultate\Anul 3\ACS\att_faces (1)'

      for i in range(1, 41):
        caleFolderPers = caleBD + '\s' + str(i) + '\\'
        for j in range(1, self.config+1):
            calePozaAntrenare = caleFolderPers + str(j) + '.pgm'
            #print(calePozaAntrenare)
            # citim poza ca matrice 112 x 92:
            pozaAntrenare = cv2.imread(calePozaAntrenare, 0)
            pozaAntrenare = np.array(pozaAntrenare)

            # vectorizam poza:
            pozaVect = pozaAntrenare.reshape(-1, 1)
            # -1 = Python calculeaza automat numarul de elemente (112 x 92)

            self.A[:, self.config * (i - 1) + j - 1] = pozaVect[:, 0]


      imagine = self.A[:, 2]
      poza = np.reshape(imagine, (112, 92))
      print('matrice')
      return self.A

    def matT(self):
        self.T = np.zeros([10304, 10-self.config * 40])
        caleBD = r'D:\Facultate\Anul 3\TO\att_faces'

        for i in range(1, 41):
            caleFolderPers = caleBD + '\s' + str(i) + '\\'
            for j in range( self.config + 1,11):
                calePozaTestare = caleFolderPers + str(j) + '.pgm'
                print(calePozaTestare)
                # citim poza ca matrice 112 x 92:
                pozaTestare = cv2.imread(calePozaTestare, 0)
                pozaTestare = np.array(pozaTestare)
                pozaVect = pozaTestare.reshape(-1,1)
