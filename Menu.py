#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Élève
#
# Created:     01/07/2019
# Copyright:   (c) Élève 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import easygui
from tkinter.filedialog import *
#from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style


#Retourne l'image redimensionée(si nécessaire)
def refreshPicture(_image):
    #_image = PhotoImage(file=filepath)
    label1 = Label(root, width=root.winfo_screenwidth,image=_image)
    label1.place(x=0, y=0)


def donothing():
##   filewin = Toplevel(root)
##   button = Button(filewin, text="Do nothing button")
##   button.pack()
   easygui.msgbox("Version 1.0","About this application")



def doAbout():
    easygui.msgbox("Version 1.0","About this application")

def doOpen():
    easygui.msgbox("Version 1.0","Open file ....")

def doSaveAs():
    easygui.msgbox("Version 1.0","Save as ....")

def doMainTache1():
    refreshPicture(image_MainTache1)
def doMainTache2():
    refreshPicture(image_MainTache2)
def doMainTache3():
    refreshPicture(image_MainTache3)




_workFolder = "D:\Dev\ProjetStationnement\TKINTER"
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
statmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Ouvrir", command=doOpen)
filemenu.add_separator()
filemenu.add_command(label="Enregistrer sous...", command=doSaveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

# << Arrondissements de Paris affichant la durée de stationnement la plus longue / la plus courte >>
# << "Stationnements interdits” les plus / les moins populaires >>    #  par arrondissements de Paris
# << "Les Mois affichant la durée de stationnement la plus longue / la plus courte" >>

statmenu.add_command(label="...par arrondissement", command=doMainTache1)
statmenu.add_command(label="...par type de stationnement", command=doMainTache2)
statmenu.add_command(label="...par mois", command=doMainTache3)
menubar.add_cascade(label="Statistiques", menu=statmenu)
statmenu.add_separator()

helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="A propos...", command=donothing)
menubar.add_cascade(label="Aide", menu=helpmenu)

root.config(menu=menubar)
#root.geometry("640x480")

# --------------
# ROOT GEOMETRY
# --------------

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

_image = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\Accueil.png')
label1 = Label(root, image=_image)
label1.place(x=0, y=0)

image_Accueil = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\Accueil.png')
image_MainTache1 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache1.png')
image_MainTache1.width = ws
image_MainTache1.height = hs

image_MainTache2 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache2.png')
image_MainTache2.width = ws
image_MainTache2.height = hs

image_MainTache3 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache3.png')
image_MainTache3.width = ws
image_MainTache3.height = hs

root.mainloop()
