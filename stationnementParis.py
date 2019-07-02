#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Élève
#
# Created:     20/06/2019
# Copyright:   (c) Élève 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import matplotlib
import matplotlib.pyplot as plt
import pandas
import csv
import numpy as np
import pandas as pd


##"matplotlib inline"


##print( pandas.__version__ )"affiche la version de pandas



stationnement_df = pandas.read_csv("E:\greta\DataPythonCSV\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 ,low_memory=False)




##valeur_Arrond=stationnement_df[ [ 'ARROND', 'LONGUEUR_CALCULEE' ]].agg(['max','min'])

df_max=stationnement_df[(stationnement_df[ 'ARROND' ]<21) & (stationnement_df[ 'ARROND' ]>0)].LONGUEUR_CALCULEE.groupby(stationnement_df.ARROND).agg(['max'])
df_min=stationnement_df[(stationnement_df[ 'ARROND' ]<21) & (stationnement_df[ 'ARROND' ]>0)].LONGUEUR_CALCULEE.groupby(stationnement_df.ARROND).agg(['min'])

df_min_max=pd.concat([df_max,df_min],axis=1).reset_index()

df_min_max=df_min_max.set_axis(['Arrondissement','max','min'] , axis=1 ,inplace=False)

for  row in df_min_max:

    listarrond=df_min_max['Arrondissement']
    listmin=round(df_min_max['max'],2)
    listmax=round(df_min_max['min'],2)



ind = np.arange(len(listmax))  # the x locations for the groups
width = 0.45  # the width of the bars

fig, ax = plt.subplots()
# fix size of figure
plt.gcf().set_size_inches(15, 5)
rects1 = ax.bar(ind - width/2, listmax, width, yerr=1,
                label='Minimum')
rects2 = ax.bar(ind + width/2, listmin, width, yerr=1,
                label='Maximun')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Durée de stationnement en minute')
ax.set_title('Stationnement à Paris')
ax.set_xticks(ind)
ax.set_xticklabels(listarrond)
ax.legend()
plt.xlabel('Arrondissements De Paris')

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