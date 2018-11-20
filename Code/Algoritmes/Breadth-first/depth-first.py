# Name: Liora Rosenberg
# Student number: 11036435
"""
This script interprets an excel file and then outputs a list of provinces (list_provinces) and a list of neighbouring provinces (province_neigbour).
"""
from collections import deque
import csv
from bs4 import BeautifulSoup

#import functie from documentnaam
from helpers import *

list_color = ['A','B','C','D','E']
list_color_node = []
grand_list = []

# buren en daar stop je 0 in en je lijst van buren. je kijkt in de lijst wat de buren van. recursief
def depth_first(list_neigbors, current_node, list_color_node):
    list_color_node[current_node] = True
    for buurland in list_neigbors[current_node]:
        print(buurland)

        if list_color_node[buurland] == None:
            return(depth_first(list_neigbors, buurland, list_color_node))

#def color():
    list_color_node[current_node] = True
    #check hoe lang de lijst is
    #for i in lijst verwijder eerste lijst
    #ga naar volgende buur

if __name__ == '__main__':
    list_neigbors = generate_triple(True)

    # maak een lijst gevult met none
    for i in range(len(list_neigbors)):
        list_color_node.append(None)
        print(list_color_node)

    depth_first(list_neigbors, 0, list_color_node)
