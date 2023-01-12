import numpy as np
from math import pi, e, pow, sqrt,sin
from DEF import *
class Ensembles:
    def __init__(self):
        
        self.time = np.genfromtxt('samples/t.csv', delimiter=',')
        timeLength = len(self.time)
        
        ## X
        self.ensembleX = np.genfromtxt('samples/x.csv', delimiter=',')
        
        ## Y
        SAMPLES_NUM = 100
        Y_mean = 0
        Y_var = 1
        self.ensembleY = np.zeros(shape=(SAMPLES_NUM,timeLength))
        betas = np.array(list(range(SAMPLES_NUM)))
        
        for x in range(len(betas)):
            for t in range(len(self.time)):
                beta = 1/sqrt(2*pi*Y_var) * pow(e,(-pow(x-Y_mean,2)/(2*Y_var)))
                
                self.ensembleY[x][t] = beta*sin(2*pi*self.time[t])
        
        ## Z
        self.ensembleZ = self.ensembleX * self.ensembleY
        
        ## P
        self.ensembleP = self.ensembleX * self.ensembleY
        
        ## M
        self.ensembleM = self.ensembleX * self.ensembleY
        
        # ## file
        # if not choiceOrFile in [X_,Y_,Z_,P_,M_]:
        #     try:
        #         self.ensembleX = np.genfromtxt(choiceOrFile, delimiter=',')
        #     except:
        #         print("file not found")
                

    def getEnsemble(self, wantEns):
        
        if wantEns == X_:
            return self.ensembleX, self.time
        elif wantEns == Y_:
            return self.ensembleY, self.time
        elif wantEns == Z_:
            return self.ensembleZ, self.time
        elif wantEns == P_:
            return self.ensembleP, self.time
        elif wantEns == M_:
            return self.ensembleM, self.time
        
        
