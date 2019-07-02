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
import pandas
import pandas as pd
import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# QUELS MOIS AFFICHENT LA DUREE DE STATIONNEMENT EN "STATIONNEMENT INTERDITS" LA PLUS COURTE ET LA DUREE LA PLUS LONGUE

df = pandas.read_csv("E:\greta\DataPythonCSV\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';',header = 0,low_memory=False) # Lire un fichier texte

_datereleve = df["DATERELEVE"].values
_annee = [my_str.split("-")[0] for my_str in _datereleve ]
_mois = [my_str.split("-")[1] for my_str in _datereleve]


df["annee_DATERELEVE"]=_annee
df["mois_DATERELEVE"]=_mois

### RUPTURE PAR MOIS
tdf1=df[ (df["annee_DATERELEVE"] == "2017") ]
tdf2=tdf1[ ["mois_DATERELEVE", "LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['max','min'])
#df_max1=df[ ["mois_DATERELEVE"], ["LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['max'])
tt=tdf1[ ["mois_DATERELEVE", "LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['max'])


### TOUS MOIS CONFONDUS
##########################################################################

df_max=df[ ["mois_DATERELEVE","LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['max'])
df_min=df[ ["mois_DATERELEVE","LONGUEUR_CALCULEE"] ].groupby(['mois_DATERELEVE']).agg(['min'])


df_min_max=pd.concat([df_max,df_min],axis=1).reset_index()

df_min_max=df_min_max.set_axis(['mois_DATERELEVE','max','min'] , axis=1 ,inplace=False)


##########################################################################

print(tdf1)


for  row in df_min_max:
##    print(row)

    listDate=df_min_max['mois_DATERELEVE']
    listmax=round(df_min_max['max'],2)
    listmin=round(df_min_max['min'],2)



ind = np.arange(len(listmax))  # the x locations for the groups
width = 0.45  # the width of the bars

fig, ax = plt.subplots()
# fix size of figure
plt.gcf().set_size_inches(15, 5)
rects2 = ax.bar(ind + width/2, listmin, width, yerr=0,
                label='Minimum')
rects1 = ax.bar(ind - width/2, listmax, width, yerr=0,
                label='Maximum')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Durée de stationnement en minutes')
ax.set_title('Quels mois affichent la durée de stationnement la plus longue / la plus courte à Paris ')
ax.set_xticks(ind)
ax.set_xticklabels(listDate)
ax.legend()
plt.xlabel('Mois de relevé')

def autolabel(rects, xpos='right'):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

autolabel(rects1, "center")
autolabel(rects2, "center")

fig.tight_layout()

plt.show()