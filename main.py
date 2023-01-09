import matplotlib.pyplot as plt
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
                
        
    def getEnsemble(self, ensemble="x"):
        if ensemble=="x":   
            return self.ensembleX, self.time
        elif ensemble=="y":
            return self.ensembleY, self.time
     



class Stat:
    def __init__(self,ensemble,time):
        self.processes = ensemble
        self.time = time
        
        
    def plotMsamples(self,number):
        for n in range(len(self.processes)):
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
        pass
    
    def calcMeanOf(self,n):
        mean = np.mean(self.processes[n])
        return mean
        
    def test(self):
        p.genfromtxt('t.csv', delimiter=',')
        
        pass
    
    
    
def main():
    ens = Ensembles()
    ensemble,time = ens.getEnsemble("y")
    plot = Stat(ensemble,time)
    plot.plotSampleN(50)
    
    
if __name__ == "__main__":
    main()