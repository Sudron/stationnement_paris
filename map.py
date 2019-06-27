#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     27/06/2019
# Copyright:   (c) Administrator 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from gmplot import *   #制图
import pandas
import webbrowser

df = pandas.read_csv( "F:\python\projet stationne\stationnement-sur-voie-publique-stationnement-interdit.csv", sep = ';', header = 0 , low_memory=False)

geo_point_2d = df['geo_point_2d']
print(geo_point_2d)
    # 提取列名为geo_point_2d这一列。坐标。这列有两个内容，要把它分成两列。



def googlemap (coordonnees):
    gmap = gmplot.GoogleMapPlotter(48.853,2.35,12) # centrage de la map

    latitude = []
    longitude = []

    for i in range(len(geo_point_2d)):
        x = geo_point_2d[i].split(',')
        latitude.append(float(x[0]))
        longitude.append(float(x[1]))

    gmap.heatmap(latitude,longitude)
    gmap.scatter(latitude,longitude,color = 'red',size = 25,marker = False)
    # Affichage de la dispersion des anomalies

    gmap.apikey = "AIzaSyBjZiASHmMIG7fW5-3hBJ_brgk25u3kLM4"
    gmap.draw("map.html")
    webbrowser.open("map.html")

googlemap(geo_point_2d)