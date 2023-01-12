import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import fft
import random


class Stats:
    def __init__(self,ensemble,time):
        self.processes = ensemble
        self.time = time
        self.lenP = len(self.processes)        
        self.lenT = len(self.time) 
        self.dt = self.time[1]-self.time[0]
        self.ACF_All = np.zeros((self.lenP,self.lenP))

        for i in range(self.lenP):
            for j in range(self.lenP):
                ACF = self.calcACFbetween(i,j)
                self.ACF_All[i][j] = ACF
        
               
    def PlotMRandSamples(self,m):
        rands = random.sample(range(1, self.lenP), m)
        for i in rands:
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
        
    
    def plotACF(self):
        
        print(self.ACF_All)
        x = np.arange(0,self.lenP,1)
        X,Y = np.meshgrid(x,x)
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, self.ACF_All, cmap=cm.coolwarm,linewidth=0, antialiased=False)
        plt.show()
        
        
    def calcMeanAll(self):
        return np.mean(self.processes)
        
    def calcACFbetween(self, ith, jth):
        I = self.processes[:self.lenP, ith]
        J = self.processes[:self.lenP, jth]
        return sum(I*J)/self.lenP
    
    def calcTimeMeanOf(self,n):
        return np.mean(self.processes[n])
    
    def calcTimeACFOf(self,n,tau):
        process1 = self.processes[n][:-tau]
        process2 = self.processes[n][tau:]
        return sum(process1*process2)*self.dt
        
    def plotPSD(self):
        ACFfft = fft.fft2(self.ACF_All)
        ACFfft_abs = np.abs(ACFfft)
        ACFfft_sqrd = ACFfft_abs**2
        print(len(ACFfft_sqrd),len(ACFfft[0]))
        ACFfft_prob = np.mean(ACFfft_sqrd, axis=0) * self.dt 
        plt.plot(ACFfft_prob)
        plt.show()
    
    def calcAvgPower(self):
        pass
        