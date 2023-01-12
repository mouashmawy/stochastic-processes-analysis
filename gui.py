import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Button, Label, Entry, Scale, OptionMenu, filedialog
from DEF import *
from Stats import Stats
from Ensembles import Ensembles
class GUIApp:
    def __init__(self, master):

        self.master = master
        self.master.config(bg=BK_CLR)
        self.master.title('T-Stat App - Text File Statistics ')
        self.master.minsize(500, 400)
        
        self.ensemble = None
        self.time = None

        self.additionalWindow1 = None
        self.fileNameText = None
        self.highestNumText = None
        self.statsApp = None
        ##########frame 1
        self.frame1 = tk.Frame(self.master,bg=BK_CLR, padx=50,pady=20)
        self.welcome = Label(self.frame1, text="Welcome in SP App", font='Arial 20 bold', bg=BK_CLR, fg=FG_CLR)
        
        self.chooseEnsembleLabel = Label(self.frame1, text="Choose Ensemble", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        options=[ X_,Y_,Z_,P_,M_,Choose_]
        clicked = tk.StringVar()
        clicked.set(X_)
        self.EnsemblesOptions = OptionMenu(self.frame1, clicked, *options, command=self.calculating)
        self.EnsemblesOptions.config(bg=BK_CLR, fg=FG_CLR, width=30, activebackground=BK_CLR, activeforeground=FG_CLR, font='Arial 11')
        self.space = Label(self.frame1, text="", font='Arial 10 bold', bg=BK_CLR, fg=FG_CLR)

        self.welcome.grid(row=0,column=0)
        self.space.grid(row=1, column=0)
        self.chooseEnsembleLabel.grid(row=2,column=0)
        self.EnsemblesOptions.grid(row=3,column=0)
        

        ##########frame 2
        self.frame2 = tk.Frame(self.master,bg=BK_CLR, padx=10,pady=10)
        
        self.scaleMLabel = Label(self.frame2, text="M samples", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.ScaleM = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleNLabel = Label(self.frame2, text="Process N", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.ScaleN = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleILabel = Label(self.frame2, text="ith column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.ScaleI = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleJLabel = Label(self.frame2, text="jth column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.ScaleJ = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        
        self.scaleMLabel.grid(row=0, column=0)
        self.ScaleM.grid(row=1,column=0)
        self.scaleNLabel.grid(row=0, column=1)
        self.ScaleN.grid(row=1,column=1)
        self.scaleILabel.grid(row=2, column=0)
        self.ScaleI.grid(row=3,column=0)
        self.scaleJLabel.grid(row=2, column=1)
        self.ScaleJ.grid(row=3,column=1)

        ##########frame 3
        self.frame3 = tk.Frame(self.master,bg=BK_CLR,padx=10,pady=10)
            #self.enterButton = Button(self.frame3, text='ENTER', command=self.calculating,bg=FG_CLR, padx=15, pady=10, borderwidth=4)
        self.processingLabel = Label(self.frame3, text="Enter file name and number...", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
            # self.enterButton.grid(row=0,column=0)
        self.processingLabel.grid(row=1,column=0)

        ##########frame 4
        self.frame4 = tk.Frame(self.master, bg=BK_CLR, padx=10, pady=10)

        self.freqButton = Button(self.frame4, text='Freq graph', command=self.showFreqGraph, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.numHighestButton = Button(self.frame4, text='Most Freq', command=self.showHighestFreq, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.PMFButton = Button(self.frame4, text='show PMF', command=self.showPMF, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.CDFButton = Button(self.frame4, text='show CDF', command=self.showCDF, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.someStatsButton = Button(self.frame4, text='some stats', command=self.showStats, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.exitButton = Button(self.frame4, text='Clear All...', command=self.clearAll, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)

        self.freqButton.grid(row=0,column=0)
        self.numHighestButton.grid(row=0,column=1)
        self.PMFButton.grid(row=1,column=0)
        self.CDFButton.grid(row=1,column=1)
        self.someStatsButton.grid(row=2, column=0)
        self.exitButton.grid(row=2, column=1)

        ##########frame 5
        self.frame5 = tk.Frame(self.master, bg=BK_CLR, padx=10, pady=0)
        self.welcome = Label(self.frame5, text="", font='Arial 20 bold', bg=BK_CLR, fg=FG_CLR)
        self.welcome.grid(row=0, column=0)


        #frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()


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

        self.ensemble  = Ensembles(choice)
        
        ensemble,time = self.ensemble.getEnsemble()
        
        # self.highestNumText =self.MScale.get()
        # self.statsApp = Stats(ensemble,time)
        # self.statsApp.calc()
        # self.processingLabel.config(text=f"processing {self.fileNameText} file with {self.highestNumText} most frequent...",font="Arial 12 bold")


    def showFreqGraph(self):
        if (self.validate()):
            return
        self.statsApp.freqPlot()



    def showPMF(self):
        if (self.validate()):
            return
        self.statsApp.PMF()


    def showCDF(self):
        if (self.validate()):
            return
        self.statsApp.CDF()

    def showHighestFreq(self):
        if(self.validate()):
            return

        self.additionalWindow1 = tk.Toplevel(self.master,bg=BK_CLR)
        HighestLabel = Label(self.additionalWindow1, text=f"{self.highestNumText} most frequent letters", font='Arial 18 bold', bg=BK_CLR, fg=FG_CLR,pady=20,padx=20)
        HighestLabel.pack()


        listOfHighest = self.statsApp.getHighestList()
        self.createTable(self.additionalWindow1,listOfHighest).pack()

    def showStats(self):
        if (self.validate()):
            return

        self.additionalWindow1 = tk.Toplevel(self.master,bg=BK_CLR)
        self.additionalWindow1.minsize(400, 250)

        self.statsLabel = Label(self.additionalWindow1, text="Some Statistics", font='Arial 18 bold', bg=BK_CLR, fg=FG_CLR,pady=20)

        list = self.statsApp.getStatistics()
        tableFrame = self.createTable(self.additionalWindow1, list)

        self.statsLabel.pack()
        tableFrame.pack()


    def validate(self):
        try:
            self.calculating()
        except:
            self.processingLabel.config(text=f"FILE NOT FOUND",font="Arial 12 bold")
            return 1

        if self.additionalWindow1 != None:
            self.additionalWindow1.destroy()
        self.EnsemblesOptions.config(state=tk.DISABLED, disabledbackground=BK_CLR, disabledforeground=DSBLD_CLR)
        plt.close('all')


    def createTable(self, TableFrame, list):
        table = tk.Frame(TableFrame, bg=BK_CLR, padx=10, pady=10)
        for i in range(len(list)):
            for j in range(len(list[0])):
                e = Entry(table, width=10, bg=BK_CLR,fg=FG_CLR, font=('Arial', 16, 'bold')
                          ,disabledbackground=BK_CLR,disabledforeground=FG_CLR)
                e.grid(row=i, column=j)
                e.insert(tk.END, list[i][j])
                e.config(state=tk.DISABLED)
        return table

root = tk.Tk()
GUIApp(root)
root.mainloop()