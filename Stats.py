import matplotlib.pyplot as plt
import numpy as np


class Stats:
    def __init__(self,ensemble,time):
        self.processes = ensemble
        self.time = time
        self.lenP = len(self.processes)        
        self.lenT = len(self.time) 
               
    def plotMsamples(self,number):
        for n in range(number):
            plt.plot(self.time,self.processes[n])
        plt.show()
    
    def plotSampleN(self,number):
        plt.plot(self.time,self.processes[number])
        plt.show()
    
    def plotEnsembleMean(self):
        EnsembleMean = np.mean(self.processes,axis=0)
        plt.plot(self.time,EnsembleMean)
        print(len(EnsembleMean))
        print(len(self.time))
        plt.show()
        
    def plotACFbetween(self, ith, jth):
        I = self.processes[:self.lenP, ith]
        J = self.processes[:self.lenP, jth]
        return sum(I*J)/self.lenP
    
    def calcMeanOf(self,n):
        mean = np.mean(self.processes[n])
        return mean
    
    def calcTimeACF(self):
        pass
    
    def plotPSD(self):
        pass 
    
    def calcAvgPower(self):
        pass
        