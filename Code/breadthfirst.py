# Name: Liora Rosenberg
# Student number: 11036435
"""
This script interprets an excel file and then outputs a list of provinces (list_provinces) and a list of neighbouring provinces (province_neigbour).
"""

import csv
from helpers import *
import copy


def breadth_first(list_neigbors, transmitter_list, list_color_node, current_node=0):
    var = len(list_color_node)
    new_node_color_list = []

    for list in list_color_node:

        for i in color(list, list_neigbors, transmitter_list, current_node):
            new_node_color_list.append(i)

    for i in new_node_color_list:
        list_color_node.append(i)

    for i in range(var):
        list_color_node.pop(0)

    for list in list_color_node:
        for buurland in list_neigbors[current_node]:
            if list[buurland] is None:
                breadth_first(list_neigbors, transmitter_list, list_color_node, buurland)

    return(list_color_node)


def color(list_to_check, list_neigbors, list_color, node_to_check):

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
    transmitter_list = ['A','B','C','D']
    list_neigbors = generate_triple(True)
    list_color_node = []
    starting_list = []


    for i in range(len(list_neigbors)):
        starting_list.append(None)

    list_color_node.append(starting_list)
    print(depth_first(list_neigbors, transmitter_list, list_color_node))
