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
        self.processes = None
        self.time = None
        self.statsApp =None

        self.additionalWindow1 = None
        self.fileNameText = None
        self.highestNumText = None
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
        self.scaleM = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleNLabel = Label(self.frame2, text="Process N", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleN = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleILabel = Label(self.frame2, text="ith column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleI = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        self.scaleJLabel = Label(self.frame2, text="jth column", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.scaleJ = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR,relief=tk.RAISED, length=OPTIONS_MENU_LENGTH)

        
        self.scaleMLabel.grid(row=0, column=0)
        self.ScaleM.grid(row=1,column=0)
        self.scaleNLabel.grid(row=0, column=1)
        self.scaleN.grid(row=1,column=1)
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

        self.plotSampleN_btn = Button(self.frame4, text='Plot Sample N', command=self.plotSampleN, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.PlotMsamples_btn = Button(self.frame4, text='Plot M Samples', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotMean_btn = Button(self.frame4, text='Plot Mean', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotACF_btn = Button(self.frame4, text='Plot ACF', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcTimeMean_btn = Button(self.frame4, text='Calc Time Mean', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcTimeACF_btn = Button(self.frame4, text='Calc Time ACF', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.calcAllMean_btn = Button(self.frame4, text='Calc All Mean', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plot3DACF_btn = Button(self.frame4, text='Plot 3D ACF', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotPSD_btn = Button(self.frame4, text='Plot PSD', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        self.plotPwrAvg_btn = Button(self.frame4, text='show Avg Pwr', command=self.ps, fg=FG_CLR, bg=BK_CLR, padx=15, pady=10, borderwidth=2, width=BTN_WIDTH)
        
        
        self.plotSampleN_btn.grid(row=0,column=0)
        self.PlotMsamples_btn.grid(row=0,column=1)
        self.plotMean_btn.grid(row=1,column=0)
        self.plotACF_btn.grid(row=1,column=1)
        self.calcTimeMean_btn.grid(row=2, column=0)
        self.calcTimeACF_btn.grid(row=2, column=1)
        self.calcAllMean_btn.grid(row=3,column=0)
        self.plot3DACF_btn.grid(row=3,column=1)
        self.plotPSD_btn.grid(row=4,column=0)
        self.plotPwrAvg_btn.grid(row=4,column=1)
        

        ##########frame 5
        self.frame5 = tk.Frame(self.master, bg=BK_CLR, padx=10, pady=0)
        self.result = Label(self.frame5, text="\n", font='Arial 15 bold', bg=BK_CLR, fg="#ff0000")
        self.result.grid(row=0, column=0)


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

        self.ensemble  = Ensembles()
        
        self.processes, self.time = self.ensemble.getEnsemble(choice)
        
        self.statsApp = Stats(self.processes, self.time)

    def plotSampleN(self):
        self.validate()
        self.statsApp.plotSampleN(self.scaleN.get())
    

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
    
    def ps(self):
        pass

root = tk.Tk()
GUIApp(root)
root.mainloop()