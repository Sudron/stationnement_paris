#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     << Quels arrondissements de Paris affichent la durée de stationnement la plus longue / la plus courte >>
#
# Author:      Administrateur
#
# Created:     11/06/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas
import csv
import numpy as np

import matplotlib.pyplot as plt

# import du fichier heart.txt avec pandas dans la variable df (df = DataFrame)
df = pandas.read_csv("D:\Dev\ProjetStationnement\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';',header = 0,low_memory=False) # Lire un fichier texte

# RUPTURE PAR ARRONDISSEMENT
tdf1=df[ ( df["ARROND"] < 21 ) & ( df[ "ARROND"] > 0 & ( df["REGPAR"] != None)) ].groupby(['ARROND','REGPAR']).size().reset_index(name='FREQ')

# SELECTION DE L'ARRONDISSEMENT
_arron = 4
tdf0=df[ ( df["ARROND"] == _arron ) & ( df["REGPAR"] != None) ].groupby(['ARROND','REGPAR']).size().reset_index(name='FREQ')

# TOUS ARRONDISSEMENTS CONFONDUS
tdf2=df[ ( df["REGPAR"] != None) ].groupby(['REGPAR']).size().reset_index(name='FREQ')


tdfMin=tdf1.groupby(["ARROND","FREQ"]).min()
tdfMax=tdf1.groupby(["ARROND","FREQ"]).max()
tdfConc=pandas.concat([tdfMin,tdfMax], axis=0)

print(tdfMin)
print(tdfMax)
print(tdfConc)
print("PAR ARRONDISSEMENTS",tdf1)
print("TOUS ARRONDISSEMENTS CONFONDUS",tdf2)
print("ARRONDISSEMENT = ", _arron,tdf0)