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
df = pandas.read_csv( "stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 , low_memory=False)

tdf=df[ ( df["ARROND"] < 21 ) & ( df[ "ARROND"] > 0) ].LONGUEUR_CALCULEE.groupby(df.ARROND).agg(['max','min'])

print(tdf)
