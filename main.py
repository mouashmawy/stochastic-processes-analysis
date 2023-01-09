import matplotlib.pyplot as plt
import numpy as np
import math

class Ensembles:
    def __init__(self):
        self.time = np.genfromtxt('t.csv', delimiter=',')
        timeLength = len(self.time)
        ## X
        self.ensembleX = np.genfromtxt('x.csv', delimiter=',')
        
        ## Y
        SAMPLES_NUM = 1000
        PI = math.pi
        self.ensembleY = np.zeros(shape=(SAMPLES_NUM,timeLength))
        betas = np.array(list(range(SAMPLES_NUM+1)))/SAMPLES_NUM
        for beta in betas:
            for t in self.time:
                self.ensembleY[t][beta] = beta*math.sin(2*PI*t)
                
        
    def getX(self):
        return self.ensembleX, self.time
        
     



class Stat:
    def __init__(self,ensemble,time):
        self.processes = ensemble
        self.time = time
        
        
    def plotMsamples(self,number):
        for process in self.processes:
            plt.plot(self.time,process)
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
    x,t = ens.getXandT()
    plot = Stat(x,t)
    plot.plotEnsembleMean()
    
    
if __name__ == "__main__":
    main()