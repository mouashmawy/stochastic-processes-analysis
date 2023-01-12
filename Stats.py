import matplotlib.pyplot as plt
import numpy as np


class Stats:
    def __init__(self,ensemble,time):
        self.processes = ensemble
        self.time = time
        self.lenP = len(self.processes)        
        self.lenT = len(self.time) 
        self.dt = self.time[1]-self.time[0]
               
    def Plot_n_samples(self,n):
        for i in range(self.lenP):
            plt.plot(self.time,self.processes[i])
        plt.show()
    
    def plotSampleN(self,number):
        plt.plot(self.time,self.processes[number])
        plt.show()
    
    def plotEnsembleMean(self):
        EnsembleMean = np.mean(self.processes,axis=0)
        plt.plot(self.time,EnsembleMean)
        print(len(EnsembleMean))
        print(len(EnsembleMean))
        print(len(self.time))
        plt.show()
        
    def calcMeanAll(self):
        return np.mean(self.processes)
        
    def calcACFbetween(self, ith, jth):
        I = self.processes[:self.lenP, ith]
        J = self.processes[:self.lenP, jth]
        return sum(I*J)/self.lenP
    
    def calcTimeMeanOf(self,n):
        return np.mean(self.processes[n])
    
    def calcTimeACFOf(self,n,i,j):
        tau = abs(j-i)
        process1 = self.processes[n][:-tau]
        process2 = self.processes[n][tau:]
        return sum(process1*process2)*self.dt
        
    
    
    def plotPSD(self):
        pass 
    
    def calcAvgPower(self):
        pass
        