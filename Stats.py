import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import fft
import random
import math


class Stats:
    def __init__(self,ensemble,time, outputFigure):
        
        self.outputFigure = outputFigure
        
        self.processes = ensemble
        self.time = time
        self.lenP = len(self.processes)        
        self.lenT = len(self.time) 
        self.dt = self.time[1]-self.time[0]
        self.ACF_All = np.zeros((self.lenP,self.lenP))

        for i in range(self.lenT):
            for j in range(self.lenT):
                ACF = self.calcACFbetween(i,j)
                self.ACF_All[i][j] = ACF
        
               
    def plotMSamples(self,m):
        rands = random.sample(range(1, self.lenP), m)
        
        
        row = math.ceil(math.sqrt(m))
        coulmn = math.floor(math.sqrt(m))
        
        if row*coulmn < m:
            coulmn += 1
        
        for i in range(len(rands)):
            plot = self.outputFigure.add_subplot(row,coulmn,i+1)
            plot.plot(self.time,self.processes[rands[i]])
            # plotting the graph
    
    def plotSampleN(self,number):
        plot = self.outputFigure.add_subplot(111)
        plot.plot(self.time,self.processes[number])
        
    
    def plotEnsembleMean(self):
        EnsembleMean = np.mean(self.processes,axis=0)
        plot = self.outputFigure.add_subplot(111)
        plot.plot(self.time,EnsembleMean)
        
    
    def plot3DACF(self):
        
        x = np.arange(0,self.lenP,1)
        X,Y = np.meshgrid(x,x)
        plot = self.outputFigure.add_subplot(111, projection='3d')
        plot.plot_surface(X, Y, self.ACF_All, cmap=cm.coolwarm,linewidth=0, antialiased=False)
        
        
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
        x = []
        for process in self.processes:
            ACFfft = fft.fft(process)
            shifted = fft.fftshift(ACFfft)
            abs = np.abs(shifted)
            x.append(abs)
        
        step = np.square(x) / self.lenP
        all_time = (self.time[-1] - self.time[0])
        ACFfft_prob = np.mean(step, axis=0) / all_time
        plot = self.outputFigure.add_subplot(111)
        plot.plot(ACFfft_prob)
    
    def calcAvgPower(self):
        x = []
        for i in range(self.lenT):
            value = self.calcACFbetween(i,i)
            x.append(value)
        return np.sum(x)
        