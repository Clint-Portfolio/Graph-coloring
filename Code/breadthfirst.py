# Name: Liora Rosenberg
# Student number: 11036435
"""
This script interprets an excel file and then outputs a list of provinces (list_provinces) and a list of neighbouring provinces (province_neigbour).
"""
# from collections import deque
import csv
from bs4 import BeautifulSoup

#import functie from documentnaam
from helpers import *

list_color = ['A','B','C','D']
list_color_node = []

# buren en daar stop je 0 in en je lijst van buren. je kijkt in de lijst wat de buren van. recursief
def depth_first(list_neigbors, current_node, list_color_node):
    #list_color_node[current_node] = True
    var = len(list_color_node)
    new_node_color_list = []
    for list in list_color_node:
        #print(list)
        for i in color(list, list_neigbors, list_color, current_node):
            new_node_color_list.append(i)
    for i in new_node_color_list:
        list_color_node.append(i)

    for i in range(var):
        list_color_node.pop(0)

    for list in list_color_node:
        for buurland in list_neigbors[current_node]:
            if list[buurland] is None:
                (depth_first(list_neigbors, buurland, list_color_node))
    # print(list_color_node)
    return(list_color_node)


def color(list_to_check, list_neigbors, list_color, node_to_check):
    import copy
#(list_neigbors, list_color_node[buurland], list_color[0]):
    grand_list = []
    for color in list_color:
        color_found = True
        for neighbour in list_neigbors[node_to_check]:
            if color == list_to_check[neighbour]:
                color_found = False

        if color_found:
            new_list_to_check = copy.deepcopy(list_to_check)
            new_list_to_check[node_to_check] = color
            grand_list.append(new_list_to_check)


    return(grand_list)


if __name__ == '__main__':
    list_neigbors = generate_triple(True)
    list_color_node = []
    starting_list = []
    # maak een lijst gevult met none
    for i in range(len(list_neigbors)):
        starting_list.append(None)
    list_color_node.append(starting_list)
    print(depth_first(list_neigbors, 0, list_color_node))
