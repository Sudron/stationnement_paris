#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     20/06/2019
# Copyright:   (c) Administrator 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import pandas
import csv
import numpy as np

import matplotlib.pyplot as plt

# import du fichier heart.txt avec pandas dans la variable df (df = DataFrame)
df = pandas.read_csv( "F:\python\projet stationne\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 , low_memory=False)

tdf = df[ ( df["ARROND"] < 21 ) & ( df[ "ARROND"] > 0) ].groupby(['ARROND', 'REGPAR']).size().reset_index(name='FREQ')
# 用size命令把regpar分组计算的结果命名为“FREQ”

tdf_max =tdf.groupby(['ARROND'])["FREQ"].max()
# 利用前面的结果建第二个表格。求freq的最大值
tdf_min =tdf.groupby(['ARROND'])["FREQ"].min()
# 利用前面的结果建第二个表格。求freq的最大值. 这里只能写两行代码。
##tdf4  = pd.concat([tdf2,tdf3],axis = 1).reset_index()

print(tdf_max)
print(tdf_min)
