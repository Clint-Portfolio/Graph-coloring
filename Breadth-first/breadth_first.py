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

# ik probeerde de land_naar_nummers te gebruiken maar dat werkte niet.
# a = provinces("buurlanden_NL.csv")
# nummers = land_naar_nummer(a[0], a[1])
#print(nummers)


province_list = (provinces("buurlanden_NL.csv"))[0]
#print(province_list)

list_neighbors = (provinces("buurlanden_NL.csv"))[1]
#print(list_neighbors)

#search root of the graph and add to queue + # begin bij de meest linker van het rijtje van provincies
left_provinces = province_list[0]
#print(province_list[0])


# het beginpunt kan elk land zijn
for i in range(len(list_neighbors)):
    provinces = province_list[i]
    neigbours = list_neighbors[i]
    print(provinces, neigbours)

    #if there is a node: if there is a neigbouring country
    for neigbour in neigbours:




	#if there is a solution: stop searching and give a solution
	#if there is not a solution: add all children
# if queue is empty, stop searching
