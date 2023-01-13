import numpy as np
from math import pi, e, pow, sqrt,sin
from DEF import *
class Ensembles:
    def __init__(self):
        
        
## X
        self.ensembleX = np.genfromtxt('samples/x.csv', delimiter=',')
        self.timeX = np.genfromtxt('samples/t_x.csv', delimiter=',')
## Y
        try:
            self.ensembleY = np.genfromtxt('samples/y.csv', delimiter=',')
            self.timeY = np.genfromtxt('samples/t_y.csv', delimiter=',')
        except:
            print(55555555555)
## Z
        self.ensembleZ = np.genfromtxt('samples/z.csv', delimiter=',')
        self.timeZ = np.genfromtxt('samples/t_z.csv', delimiter=',')
## P
        self.ensembleP = np.genfromtxt('samples/p.csv', delimiter=',')
        self.timeP = np.genfromtxt('samples/t_p.csv', delimiter=',')
## M
        self.ensembleM = np.genfromtxt('samples/m.csv', delimiter=',')
        self.timeM = np.genfromtxt('samples/t_m.csv', delimiter=',')
                

    def getEnsemble(self, wantEns):
        
        if wantEns == X_:
            return self.ensembleX, self.timeX
        elif wantEns == Y_:
            return self.ensembleY, self.timeY
        elif wantEns == Z_:
            return self.ensembleZ, self.timeZ
        elif wantEns == P_:
            return self.ensembleP, self.timeP
        elif wantEns == M_:
            return self.ensembleM, self.timeM
        else:
            pass        
        
    def generateEnsemble(self, choiceOrFile):
        pass
        
