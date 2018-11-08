# Clint Nieuwendijk
# Simple, extremely greedy algorithm to assign 'colors' to nodes in a graph
# Technically only 4 'colors' are needed, but for simplicity and solvabilliy sake
# 5 'colors' are initiated

import sys
from nodes_test import Node

country = 0
neighborcount = 0
countrylist = []
transmitter_list = ["A", "B", "C", "D", "E"]

# generate a simple graph of type
#   0
# / | \
# 0-0-0-0-0-0.. etc.
nr_of_nodes = 0
while nr_of_nodes < 3:
    nr_of_nodes = int(input("number of nodes: "))
for i in range(0, nr_of_nodes):
    if i == 0:
        countrylist.append(Node(i, None, [1, nr_of_nodes]))
    elif i <= 2:
        countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes]))
    elif i == nr_of_nodes - 1:
        countrylist.append(Node(i, None, [i - 1]))
    else:
        countrylist.append(Node(i, None, [i - 1, i + 1]))

countrylist.append(Node(len(countrylist), None, [0, 1, 2]))

# find node with most neighbors
for node in countrylist:
    if len(node.neighbors) > neighborcount:
        country = countrylist.index(node)
        neighborcount = len(node.neighbors)

# country with most neighbors gets the least used color
countrylist[country].trans_type = transmitter_list[-1]

# change color of country accordingly
for node in countrylist:
    if node.trans_type == None:
        node.changetype(transmitter_list, countrylist)
    print(node.trans_type, end = "")
