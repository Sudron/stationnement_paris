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
import datetime as dt
import matplotlib.pyplot as plt

# QUELS MOIS AFFICHENT LA DUREE DE STATIONNEMENT EN "STATIONNEMENT INTERDITS" LA PLUS COURTE ET LA DUREE LA PLUS LONGUE

df = pandas.read_csv("D:\Dev\ProjetStationnement\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';',header = 0,low_memory=False) # Lire un fichier texte

_datereleve = df["DATERELEVE"].values
_annee = [my_str.split("-")[0] for my_str in _datereleve ]
_mois = [my_str.split("-")[1] for my_str in _datereleve]


df["annee_DATERELEVE"]=_annee
df["mois_DATERELEVE"]=_mois

### RUPTURE PAR MOIS
tdf1=df[ ( df["annee_DATERELEVE"] == "2017" )]
tdf1=tdf1[ ["mois_DATERELEVE", "LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['max','min'])

### TOUS MOIS CONFONDUS


print(tdf1)
