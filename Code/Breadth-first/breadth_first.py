# Name: Liora Rosenberg
# Student number: 11036435
"""
This script interprets an excel file and then outputs a list of provinces (list_provinces) and a list of neighbouring provinces (province_neigbour).
"""

import csv
from bs4 import BeautifulSoup

#import functie from documentnaam
from helpers import provinces
from helpers import land_naar_nummer

province_list = (provinces("buurlanden_NL.csv"))[0]
#print(province_list)

list_neighbors = (provinces("buurlanden_NL.csv"))[1]
#print(list_neighbors)

list_color = ['A','B','C','D','E']
list_color_node = []

# maak een lijst gevult met none
for i in range(len(province_list)):
    list_color_node.append(None)
print(list_color_node)

# pak node 0: meest linker provincie
left_provinces = province_list[0]
print(province_list[0])

# buren en daar stop je 0 in en je lijst van buren. je kijkt in de lijst wat de buren van. recursief
#def provinces(buurland):
    # for buurland in list_neighbors:
        # if province has no neigbours stop
        #if list_neigbors = []:
        #    return
        # if province has neigbours find them
        #else:
        #    return(provinces(list_neigbors[buurland-1]))
        # if neigbouringprovince for original province has no neigbourprovinces go back to original province and find neigbouringprovince


#def provincies()
#a = provinces("buurlanden_NL.csv")
#nummers = land_naar_nummer(a[0], a[1])
#print(nummers)

# def check_color(list_color)
