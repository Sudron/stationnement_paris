#-------------------------------------------------------------------------------
# Name:        Python Data frame
# Purpose:
#
# Author:      Sebastien SUDRON
#
# Created:     18/06/2019
#------------------------------------------------

import matplotlib
import matplotlib.pyplot as plt
import pandas
import csv
import numpy as np
import pandas as pd


"matplotlib inline"


##print( pandas.__version__ )"affiche la version de pandas



stationnement_df = pandas.read_csv("E:\greta\Exo_pandas\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 ,low_memory=False)




##valeur_Arrond=stationnement_df[ [ 'ARROND', 'LONGUEUR_CALCULEE' ]].agg(['max','min'])

arrond=stationnement_df[(stationnement_df['ARROND']>0) & (stationnement_df['ARROND']<=20)].groupby('ARROND').agg(['min'],['max'])



plt.xlabel('Arrondissements De Paris')

plt.ylabel('Durée de stationnement')

plt.title('Durée minimum et maximun  de stationnement à Paris par arrondissement' )
#creation des double barre min et max
b1 = plt.bar(range(4), [1, 2, 3, 2], width = 0.4, color = 'blue')
b2 = plt.bar([x + 0.4 for x in range(5)], [5,4, 3, 2, 1],
                width = 0.4, color = 'red')
plt.xticks([x + 0.4 for x in range(4)], ['1','2','3','4'])

#affiche la legende par avec emplacement par defaut
plt.legend([b1,b2],['min','max'])

plt.show()

print(arrond)