#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     01/07/2019
# Copyright:   (c) Administrator 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


##import easygui as a
##a.msgbox("开始")

import easygui
import tkinter
import os
from PIL import Image
from PIL import ImageTk
##from PIL.ImageTk import PhotoImage

taches = easygui.buttonbox("PRESENTATION PROJET Stationnement Paris",
    image = "F:\python\projet stationne/acceuil.gif",
    choices = ['Tache 1', 'Tache 2', 'Tache 3'] )
easygui.msgbox ("##### " + taches)

root = tkinter.Tk()
##global tache_1
tache_1 = tkinter.PhotoImage(file = 'F:\python\projet stationne/tache 1.gif')
label_img = tkinter.Label(root, image = tache_1)
label_img.pack()