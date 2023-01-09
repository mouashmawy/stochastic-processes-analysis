import numpy as np
import math

class Ensembles:
    def __init__(self):
        self.time = np.genfromtxt('samples/t.csv', delimiter=',')
        timeLength = len(self.time)
        ## X
        self.ensembleX = np.genfromtxt('samples/x.csv', delimiter=',')
        
        ## Y
        SAMPLES_NUM = 100
        PI = math.pi
        self.ensembleY = np.zeros(shape=(SAMPLES_NUM,timeLength))
        betas = np.array(list(range(SAMPLES_NUM)))/SAMPLES_NUM
        for b in range(len(betas)):
            for t in range(len(self.time)):
                self.ensembleY[b][t] = betas[b]*math.sin(2*PI*self.time[t])
        
        ## Z
        self.ensembleZ = self.ensembleX * self.ensembleY
         ## P
        self.ensembleP = self.ensembleX * self.ensembleY
         ## M
        self.ensembleM = self.ensembleX * self.ensembleY
                

    def getEnsemble(self, ensemble="x"):
        ensemble=ensemble.lower()
        if ensemble=="x":   
            return self.ensembleX, self.time
        elif ensemble=="y":
            return self.ensembleY, self.time
        elif ensemble=="z":
            return self.ensembleZ, self.time
        elif ensemble=="m":
            return self.ensembleP, self.time
        elif ensemble=="p":
            return self.ensembleM, self.time
        
        else:
            print("letter not found")



ens = Ensembles()
ens.getEnsemble('x');