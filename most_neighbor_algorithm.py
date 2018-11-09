# Clint Nieuwendijk
# Simple, extremely greedy algorithm to assign 'colors' to nodes in a graph
# Technically only 4 'colors' are needed, but for simplicity and solvabilliy sake
# 5 'colors' are initiated

import sys
from nodes_test import Node

neighborcount = 0
countrylist = []
transmitter_list = ["A", "B", "C", "D", "E"]

graphtype = ""
while graphtype not in ["simple", "single", "double"]:
    print("Graphtype (simple, single, double)")
    graphtype = input(" >").lower()

nr_of_nodes = 0
while nr_of_nodes < 4:
    nr_of_nodes = int(input("number of nodes (at least 4): "))

if graphtype == "simple":
    # generate a simple graph of type:
    #  0-0-0-0-... etc.
    for i in range(0, nr_of_nodes):
        if i == 0:
            countrylist.append(Node(i, None, [1]))
        elif i == nr_of_nodes - 1:
            countrylist.append(Node(i, None, [i - 1]))
        else:
            countrylist.append(Node(i, None, [i - 1, i + 1]))

elif graphtype == "single":
    # generate a single triple edge graph of type
    #   0
    # / | \
    # 0-0-0-0-0-0-... etc.
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

else:
    # generate a double triple edge graph of type:
    #   0
    # / | \
    # 0-0-0-0-0-0-... etc.
    #   \ | /
    #     0
    for i in range(0, nr_of_nodes):
        if i == 0:
            countrylist.append(Node(i, None, [1, nr_of_nodes]))
        elif i <= 2:
            countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes, nr_of_nodes + 1]))
        elif i == 3:
            countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes]))
        elif i == nr_of_nodes - 1:
            countrylist.append(Node(i, None, [i - 1]))
        else:
            countrylist.append(Node(i, None, [i - 1, i + 1]))

    countrylist.append(Node(len(countrylist), None, [0, 1, 2]))
    countrylist.append(Node(len(countrylist), None, [1, 2, 3]))


# find node with most neighbors
most_neighbored_countries = []
for node in countrylist:
    if len(node.neighbors) > neighborcount:
        # most_neighbored_countries.append(countrylist.index(node))
        neighborcount = len(node.neighbors)

for node in countrylist:
    if len(node.neighbors) == neighborcount:
        most_neighbored_countries.append(node.name)

# country with most neighbors gets the least used color
for node in most_neighbored_countries:
    countrylist[node].changetype(transmitter_list[::-1], countrylist)

# change color of country accordingly
for node in countrylist:
    if node.trans_type == None:
        node.changetype(transmitter_list, countrylist)

# for node in most_neighbored_countries:
#     countrylist[node].changetype(transmitter_list, countrylist)
if graphtype in ["single", "double"]:
    print(" " + countrylist[-2].trans_type)
for node in countrylist[:-2]:
    print(node.trans_type, end = "")
if graphtype == "double":
    print()
    print("  " + countrylist[-1].trans_type)
