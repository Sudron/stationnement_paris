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
#from PIL import Image

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

def doMainTache2_1():
    refreshPicture(image_MainTache2_1)
def doMainTache2_2():
    refreshPicture(image_MainTache2_2)
def doMainTache2_3():
    refreshPicture(image_MainTache2_3)
def doMainTache2_4():
    refreshPicture(image_MainTache2_4)
def doMainTache2_5():
    refreshPicture(image_MainTache2_5)
def doMainTache2_6():
    refreshPicture(image_MainTache2_6)
def doMainTache2_7():
    refreshPicture(image_MainTache2_7)
def doMainTache2_8():
    refreshPicture(image_MainTache2_8)
def doMainTache2_9():
    refreshPicture(image_MainTache2_9)
def doMainTache2_10():
    refreshPicture(image_MainTache2_10)
def doMainTache2_11():
    refreshPicture(image_MainTache2_11)
def doMainTache2_12():
    refreshPicture(image_MainTache2_12)
def doMainTache2_13():
    refreshPicture(image_MainTache2_13)
def doMainTache2_14():
    refreshPicture(image_MainTache2_14)
def doMainTache2_15():
    refreshPicture(image_MainTache2_15)
def doMainTache2_16():
    refreshPicture(image_MainTache2_16)
def doMainTache2_17():
    refreshPicture(image_MainTache2_17)
def doMainTache2_18():
    refreshPicture(image_MainTache2_18)
def doMainTache2_19():
    refreshPicture(image_MainTache2_19)
def doMainTache2_20():
    refreshPicture(image_MainTache2_20)

def doMainTache3():
    refreshPicture(image_MainTache3)




_workFolder = "D:\Dev\ProjetStationnement\TKINTER"
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
statmenu = Menu(menubar, tearoff=0)
statmenu_sub = Menu(statmenu, tearoff=0)
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
menubar.add_cascade(label="Statistiques", menu=statmenu)

statmenu.add_command(label="...par arrondissement", command=doMainTache1)
filemenu.add_separator()

statmenu.add_cascade(label="...par type de stationnement", menu=statmenu_sub)
statmenu_sub.add_command(label="tous les arrondissements", command=doMainTache2)
statmenu_sub.add_command(label="1e ARRON", command=doMainTache2_1)
statmenu_sub.add_command(label="2e ARRON", command=doMainTache2_2)
statmenu_sub.add_command(label="3e ARRON", command=doMainTache2_3)
statmenu_sub.add_command(label="4e ARRON", command=doMainTache2_4)
statmenu_sub.add_command(label="5e ARRON", command=doMainTache2_5)
statmenu_sub.add_command(label="6e ARRON", command=doMainTache2_6)
statmenu_sub.add_command(label="7e ARRON", command=doMainTache2_7)
statmenu_sub.add_command(label="8e ARRON", command=doMainTache2_8)
statmenu_sub.add_command(label="9e ARRON", command=doMainTache2_9)
statmenu_sub.add_command(label="10e ARRON", command=doMainTache2_10)
statmenu_sub.add_command(label="11e ARRON", command=doMainTache2_11)
statmenu_sub.add_command(label="12e ARRON", command=doMainTache2_12)
statmenu_sub.add_command(label="13e ARRON", command=doMainTache2_13)
statmenu_sub.add_command(label="14e ARRON", command=doMainTache2_14)
statmenu_sub.add_command(label="15e ARRON", command=doMainTache2_15)
statmenu_sub.add_command(label="16e ARRON", command=doMainTache2_16)
statmenu_sub.add_command(label="17e ARRON", command=doMainTache2_17)
statmenu_sub.add_command(label="18e ARRON", command=doMainTache2_18)
statmenu_sub.add_command(label="19e ARRON", command=doMainTache2_19)
statmenu_sub.add_command(label="20e ARRON", command=doMainTache2_20)

filemenu.add_separator()
statmenu.add_command(label="...par mois", command=doMainTache3)

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

##bard = Image.o"D:\Dev\ProjetStationnement\TKINTER\Accueil.png")
##
##bardejov = PhotoImage(bard)


image_Accueil = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\Accueil.png')
image_MainTache1 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache1.png')
image_MainTache1.width = 640
image_MainTache1.height = 480

image_MainTache2 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache2.png')
image_MainTache2.width = 640
image_MainTache2.height = 480

image_MainTache3 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\MainTache3.png')
image_MainTache3.width = 640
image_MainTache3.height = 480

image_MainTache2_1 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-1e.png')
image_MainTache2_2 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-2e.png')
image_MainTache2_3 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-3e.png')
image_MainTache2_4 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-4e.png')
image_MainTache2_5 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-5e.png')
image_MainTache2_6 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-6e.png')
image_MainTache2_7 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-7e.png')
image_MainTache2_8 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-8e.png')
image_MainTache2_9 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-9e.png')
image_MainTache2_10 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-10e.png')
image_MainTache2_11 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-11e.png')
image_MainTache2_12 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-12e.png')
image_MainTache2_13 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-13e.png')
image_MainTache2_14 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-14e.png')
image_MainTache2_15 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-15e.png')
image_MainTache2_16 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-16e.png')
image_MainTache2_17 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-17e.png')
image_MainTache2_18 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-18e.png')
image_MainTache2_19 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-19e.png')
image_MainTache2_20 = PhotoImage(file='D:\Dev\ProjetStationnement\TKINTER\mainTache2-20e.png')

#with image_MainTache2_1,image_MainTache2_2: width=640; height=480



root.mainloop()
