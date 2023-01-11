import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Button, Label, Entry, Scale, OptionMenu
from DEF import *
from Stats import Stats
class GUIApp:
    def __init__(self, master):

        self.master = master
        self.master.config(bg=BK_CLR)
        self.master.title('T-Stat App - Text File Statistics ')
        self.master.minsize(500, 400)

        self.additionalWindow1 = None
        self.fileNameText = None
        self.highestNumText = None
        self.statsApp = None
        ##########frame 1
        self.frame1 = tk.Frame(self.master,bg=BK_CLR, padx=50,pady=20)
        self.welcome = Label(self.frame1, text="Welcome in SP App", font='Arial 20 bold', bg=BK_CLR, fg=FG_CLR)
        self.welcome.grid(row=0,column=0)

        ##########frame 2
        self.frame2 = tk.Frame(self.master,bg=BK_CLR, padx=10,pady=10)
        self.chooseEnsemble = Label(self.frame2, text="Choose Ensemble", font='Arial 11', bg=BK_CLR, fg=FG_CLR)
        self.chooseM = Label(self.frame2, text="Choose M number of graphs", font='Arial 11', bg=BK_CLR, fg=FG_CLR)

        self.space = Label(self.frame2, text="", font='Arial 10 bold', bg=BK_CLR, fg=FG_CLR)
        
        options=[ X_,Y_,Z_,P_,M_,Choose_]
        clicked = tk.StringVar()
        clicked.set(X_)
        self.EnsemblesOptions = OptionMenu(self.frame2, clicked, *options, command={})
        self.EnsemblesOptions.config(bg=BK_CLR, fg=FG_CLR)
        self.MScale = Scale(self.frame2, from_=0, to=20, orient="horizontal", bd=0,activebackground=BK_CLR, bg=BK_CLR, fg=FG_CLR,troughcolor=BK_CLR, length=250,relief=tk.RAISED)


