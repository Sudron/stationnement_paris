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
df = pandas.read_csv("D:\Dev\ProjetStationnement\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';',header = 0,low_memory=False) # Lire un fichier texte

# SELECTION D'UN ARRONDISSEMENT
#selectArrond=input('Choisir un arrondissement')
#tdf=df[ ( (df["ARROND"] == int(selectArrond)) ) ].groupby(['ARROND','REGPAR']).size().reset_index(name='FREQ')

# TOUT ARRONDISSEMENT CONFONDUS
tdf=df[ ( (df["ARROND"] > 0) & (df["ARROND"] < 21) & ( df["REGPAR"] != None))].groupby(['REGPAR']).size().reset_index(name='FREQ')
tdfMin=tdf.groupby(["REGPAR","FREQ"]).min()
tdfMax=tdf.groupby(["REGPAR","FREQ"]).max()
tdfConc=pandas.concat([tdfMin,tdfMax], axis=0)

ListTypeStationnement=[]
##[0, 0, 0, 0, 0,0,0.4,0]listExplod
listExplod=[]

ListFrequence=[]
for frequence in tdf['FREQ']:

    ListFrequence.append(frequence)

    if frequence==max(tdf['FREQ']) or frequence==min(tdf['FREQ']):
        nbrExplod=0.5
    else:
        nbrExplod=0

    listExplod.append(nbrExplod)

for typeStationnement in tdf['REGPAR']:

    ListTypeStationnement.append(typeStationnement)




titre="""Les types de stationnements interdits les plus et moins populaires \n à Paris, tous les arrondissements cofondus"""

plt.figure(figsize = (5, 5))
x = ListFrequence
plt.pie(x, labels = ListTypeStationnement,
           colors = ['red', 'green', 'yellow','cyan','magenta','blue','gray','brown'],
           explode = listExplod,
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 0.8,
           shadow = True)
plt.legend( loc=(1,1), prop = {'size': 9})
plt.suptitle(titre)

print(tdf)

plt.show()