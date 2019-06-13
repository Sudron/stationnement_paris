#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Élève
#
# Created:     11/06/2019
# Copyright:   (c) Élève 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas
import csv
import numpy as np

##print( pandas.__version__ )

#OnlineNewsPopularity.csv

df = pandas.read_csv("E:\greta\Exo_pandas\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 ,low_memory=False)

##print(df.shape)
##print(df)
##print(df.describe())
##print(df.columns.values)

##at_time(temps [, asof, axe])	Sélectionnez des valeurs à un moment de la journée particulier (par ex.

##print(df.columns[17:18])#affiche la colonne 17

##warning sur les colonnes
## Index(['PLAGE_HOR3_DEBUT'], dtype='object')
## Index(['PLAGE_HOR3_FIN'], dtype='object')
####Index(['STV'], dtype='object')
##print(df.columns.values)
##print(df.describe())

##print(df['ARROND'])
##
##df.loc['ID':'LONGUEUR_CALCULEE']
totalDelignePourArrondissement=[]
##qt=0
##for i in df['ARROND']:
##    if i==11:

totalDelignePourArrondissement=df[['ARROND','LONGUEUR_CALCULEE']].head(2)

##test

print(totalDelignePourArrondissement)

