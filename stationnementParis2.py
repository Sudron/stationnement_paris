#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastien SUDRON
#
# Created:     20/06/2019
# Copyright:   (c) Élève 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas
import csv
import numpy as np

import matplotlib.pyplot as plt



# import du fichier heart.txt avec pandas dans la variable df (df = DataFrame)
##df = pandas.read_csv( "stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 , low_memory=False)
df = pandas.read_csv("E:\greta\DataPythonCSV\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';',header = 0,low_memory=False) # Lire un fichier texte

selectArrond=input('Choisir un arrondissement')



tdf=df[ ( (df["ARROND"] == int(selectArrond)) ) ].groupby(['ARROND','REGPAR']).size().reset_index(name='FREQ')
tdfMin=tdf.groupby(["ARROND","FREQ"]).min()
tdfMax=tdf.groupby(["ARROND","FREQ"]).max()
tdfConc=pandas.concat([tdfMin,tdfMax], axis=0)

ListTypeStationnement=[]
##[0, 0, 0, 0, 0,0,0.4,0]listExplod
listExplod=[]



ListFrequence=[]
for frequence in tdf['FREQ']:

    ListFrequence.append(frequence)

    if frequence==max(tdf['FREQ']) or frequence==min(tdf['FREQ']):
        nbrExplod=0.1
    else:
        nbrExplod=0

    listExplod.append(nbrExplod)

for typeStationnement in tdf['REGPAR']:

    ListTypeStationnement.append(typeStationnement)







titre="""Les types de stationnements interdits les plus et moins populaires \n pour le """+str(selectArrond)+""" eme arrondissement de Paris """
# fix size of figure
plt.figure(figsize = (10, 10))
x = ListFrequence
plt.pie(x, labels = ListTypeStationnement,
           colors = ['red', 'green', 'yellow','cyan','magenta','khaki','tomato','brown'],
           explode = listExplod,
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.9,
           shadow = False)
plt.legend( loc=(1,1), prop = {'size': 9})
plt.suptitle(titre)

plt.show()