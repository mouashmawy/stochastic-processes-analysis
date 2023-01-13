import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Button, Label, Entry, Scale, OptionMenu, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from DEF import *
from Stats import Stats
from Ensembles import Ensembles
class GUIApp:
    def __init__(self, master):

        self.master = master


        self.master.config(bg=BK_CLR)
        
        
        self.master.title('T-Stat App - Text File Statistics ')
        self.master.minsize(500, 400)
        
        self.calcFrame = tk.Frame(self.master,bg=BK_CLR, padx=50,pady=20)
        self.outputFrame = tk.Frame(self.master,bg=BK_CLR, padx=50,pady=20)

        
        self.ensemble = None
        self.processes = None
        self.time = None
        self.statsApp =None
        self.clicked = None

        self.additionalWindow1 = None
        self.fileNameText = None
        self.highestNumText = None
        ##########frame 1
        self.frame1 = tk.Frame(self.calcFrame,bg=BK_CLR, padx=50,pady=20)
        self.welcome = Label(self.frame1, text="Welcome in SP App\n", font='Arial 20 bold', bg=BK_CLR, fg=FG_CLR)
        
        self.chooseEnsembleLabel = Label(self.frame1, text="Choose Ensemble", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        options=[ X_,Y_,Z_,P_,M_,Choose_]
        self.clicked = tk.StringVar()
        self.clicked.set(X_)
        self.EnsemblesOptions = OptionMenu(self.frame1, self.clicked, *options, command=self.calculating)
        self.EnsemblesOptions.config(bg=BK_CLR, fg=FG_CLR, width=BTN_WIDTH*2, activebackground=BK_CLR, activeforeground=FG_CLR, font='Arial 11')
        self.space = Label(self.frame1, text="", font='Arial 10 bold', bg=BK_CLR, fg=FG_CLR)

        self.welcome.grid(row=0,column=0)
        self.space.grid(row=1, column=0)
        self.chooseEnsembleLabel.grid(row=2,column=0)
        self.EnsemblesOptions.grid(row=3,column=0)
        

        ##########frame 2
        self.frame2 = tk.Frame(self.calcFrame,bg=BK_CLR, padx=10,pady=10)
        
        self.scaleMLabel = Label(self.frame2, text="M samples", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleM = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleNLabel = Label(self.frame2, text="Process N", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleN = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleILabel = Label(self.frame2, text="ith column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleI = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleJLabel = Label(self.frame2, text="jth column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleJ = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        
        self.scaleMLabel.grid(row=0, column=0)
        self.scaleM.grid(row=1,column=0)
        self.scaleNLabel.grid(row=0, column=1)
        self.scaleN.grid(row=1,column=1)
        self.scaleILabel.grid(row=2, column=0)
        self.scaleI.grid(row=3,column=0)
        self.scaleJLabel.grid(row=2, column=1)
        self.scaleJ.grid(row=3,column=1)

        ##########frame 3
        self.frame3 = tk.Frame(self.calcFrame,bg=BK_CLR,padx=10,pady=10)
            #self.enterButton = Button(self.frame3, text='ENTER', command=self.calculating,bg=FG_CLR, padx=15, pady=10, borderwidth=4)
        self.processingLabel = Label(self.frame3, text="Enter file name and number...", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
            # self.enterButton.grid(row=0,column=0)
        self.processingLabel.grid(row=1,column=0)

        ##########frame 4
        self.frame4 = tk.Frame(self.calcFrame, bg=BK_CLR, padx=10, pady=10)

        self.plotSampleN_btn = Button(self.frame4, text='Plot Sample N', command=self.plotSampleN, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.PlotMSamples_btn = Button(self.frame4, text='Plot M Samples', command=self.plotMSamples, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotMean_btn = Button(self.frame4, text='Plot Mean', command=self.plotEnsembleMean, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcACF_btn = Button(self.frame4, text='Calc ACF', command=self.calcEnsembleACF, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcTimeMean_btn = Button(self.frame4, text='Calc Time Mean', command=self.calcTimeMean, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcTimeACF_btn = Button(self.frame4, text='Calc Time ACF', command=self.calcTimeACF, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcAllMean_btn = Button(self.frame4, text='Calc All Mean', command=self.calcAllMean, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plot3DACF_btn = Button(self.frame4, text='Plot 3D ACF', command=self.plot3DACF, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotPSD_btn = Button(self.frame4, text='Plot PSD', command=self.plotPSD, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotPwrAvg_btn = Button(self.frame4, text='show Avg Pwr', command=self.calcAvgPower, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        
        
        self.plotSampleN_btn.grid(row=0,column=0)
        self.PlotMSamples_btn.grid(row=0,column=1)
        self.plotMean_btn.grid(row=1,column=0)
        self.calcACF_btn.grid(row=1,column=1)
        self.calcTimeMean_btn.grid(row=2, column=0)
        self.calcTimeACF_btn.grid(row=2, column=1)
        self.calcAllMean_btn.grid(row=3,column=0)
        self.plot3DACF_btn.grid(row=3,column=1)
        self.plotPSD_btn.grid(row=4,column=0)
        self.plotPwrAvg_btn.grid(row=4,column=1)
        

        ##########frame 5
        self.frame5 = tk.Frame(self.calcFrame, bg=BK_CLR, padx=10, pady=0)



        #calc frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        
        #-------------------------------------------------------------------------
        #-----------------------------output frame--------------------------------
        #-------------------------------------------------------------------------

        self.outputWindowLabel = Label(self.outputFrame, text="Results can be found here\n", font='Arial 20 bold', bg=BK_CLR, fg=FG_CLR)
        
        
        self.resultLabel = Label(self.outputFrame, text="\n", font='Arial 15 bold', bg=BK_CLR, fg="#ff0000")
        
        self.outputFigure = Figure(figsize = (5, 5),
                dpi = 100)
        self.canvas = FigureCanvasTkAgg(self.outputFigure,
                                    master = self.outputFrame)
        self.canvas.draw()

        
        #output frames
        self.outputWindowLabel.pack()
        self.resultLabel.pack()

        self.canvas.get_tk_widget().pack()

        
        #-------------------------------------------------------------------------
        #-----------------------------window frame--------------------------------
        #-------------------------------------------------------------------------
        self.calcFrame.grid(row=0, column=0)
        self.outputFrame.grid(row=0, column=1)
        


    def openDiag(self,choice):
        if(choice==Choose_):
            fileName= filedialog.askopenfilename()
            return fileName
    
    
    def clearAll(self):
        if self.additionalWindow1 != None:
            self.additionalWindow1.destroy()
        self.EnsemblesOptions.config(state=tk.NORMAL)
        self.EnsemblesOptions.delete(0, "end")
        plt.close('all')
        self.processingLabel.config(text="Enter file name and number...")


    def calculating(self, choice):
        self.EnsemblesOptions.config(state=tk.DISABLED)

        if choice==Choose_:
            self.fileNameText = self.openDiag(choice)
            self.ensemble = Ensembles(self.fileNameText)

        self.ensemble  = Ensembles()
        
        self.processes, self.time = self.ensemble.getEnsemble(choice)
        self.processingLabel.config(text=f"using:: {self.clicked.get()}", fg="#ff0000")
        self.statsApp = Stats(self.processes, self.time, self.outputFigure)
    
    def showCanvas(self):
        self.canvas = FigureCanvasTkAgg(self.outputFigure,
                                    master = self.outputFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        pass
    
    
    def plotSampleN(self):
        self.validate(1)
        self.statsApp.plotSampleN(self.scaleN.get())
        self.showCanvas()
        
    
    def plotMSamples(self):
        self.validate(1)
        self.statsApp.plotMSamples(self.scaleM.get())
        self.showCanvas()

        
    def plotEnsembleMean(self):
        self.validate(1)
        self.statsApp.plotEnsembleMean()
        self.showCanvas()

        
    def calcEnsembleACF(self):
        self.validate()
        i = self.scaleI.get()
        j = self.scaleJ.get()

        ACF = self.statsApp.calcACFbetween(i,j)
        self.resultLabel.config(text=f"Ensemble ACF ({i}&{j}) = {ACF}",font="Arial 12 bold")
        
    def calcTimeMean(self):
        self.validate()
        n= self.scaleN.get()
        mean = self.statsApp.calcTimeMeanOf(n)
        self.resultLabel.config(text=f"Time Mean of Sample #{n} = {mean}",font="Arial 12 bold")
        
    def calcTimeACF(self):
        self.validate()
        n = self.scaleN.get()
        tau = abs(self.scaleI.get()- self.scaleJ.get())
        ACF = self.statsApp.calcTimeACFOf(n,tau)
        self.resultLabel.config(text=f"Time ACF of n({n}) & tau({tau}) = {ACF}",font="Arial 12 bold")
        
    def calcAllMean(self):
        self.validate()
        mean = self.statsApp.calcMeanAll()
        self.resultLabel.config(text=f"Mean of all samples = {mean}",font="Arial 12 bold")

    def plot3DACF(self):
        self.validate(1)
        self.statsApp.plot3DACF()
        self.showCanvas()

        
        
    def plotPSD(self):
        self.validate(1)
        self.statsApp.plotPSD()
        self.showCanvas()
        
    def calcAvgPower(self):
        self.validate()
        power = self.statsApp.calcAvgPower()
        self.resultLabel.config(text=f"Average Power = {power}",font="Arial 12 bold")

        
    def validate(self, cond=0):
        if(cond == 1):
            self.canvas.get_tk_widget().destroy()
            self.outputFigure.clear()
            self.resultLabel.config(text=f"",font="Arial 12 bold")
        else:
            self.canvas.get_tk_widget().destroy()
            self.outputFigure.clear()
            
            self.canvas = FigureCanvasTkAgg(self.outputFigure,
                                        master = self.outputFrame)
            self.canvas.draw()

            self.canvas.get_tk_widget().pack()
            
        
        if self.additionalWindow1 != None:
            self.additionalWindow1.destroy()
        self.EnsemblesOptions.config(state=tk.DISABLED)# , disabledbackground=BK_CLR, disabledforeground=DSBLD_CLR)
        plt.close('all')


