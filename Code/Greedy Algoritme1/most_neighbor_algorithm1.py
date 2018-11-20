# Clint Nieuwendijk
# Simple, extremely greedy algorithm to assign 'colors' to nodes in a graph
# Technically only 4 'colors' are needed, but for simplicity and solvabilliy sake
# 5 'colors' are initiated

import sys
from nodes_test import Node

countrylist = []
transmitter_list = ["A", "B", "C", "D", "E"]

# graphtype = ""
# while graphtype not in ["simple", "single", "double", "triple"]:
#     print("Graphtype (simple, single, double, triple)")
#     graphtype = input("> ").lower()
#
# nr_of_nodes = 0
# while nr_of_nodes < 5:
#     nr_of_nodes = int(input("number of nodes (at least 5: "))
#
# if graphtype == "simple":
#     # generate a simple graph of type:
#     #  0-0-0-0-... etc.
#     for i in range(0, nr_of_nodes):
#         if i == 0:
#             countrylist.append(Node(i, None, [1]))
#         elif i == nr_of_nodes - 1:
#             countrylist.append(Node(i, None, [i - 1]))
#         else:
#             countrylist.append(Node(i, None, [i - 1, i + 1]))
#
# elif graphtype == "single":
#     # generate a single triple edge graph of type
#     #   0
#     # / | \
#     # 0-0-0-0-0-0-... etc.
#     for i in range(0, nr_of_nodes):
#         if i == 0:
#             countrylist.append(Node(i, None, [1, nr_of_nodes]))
#         elif i <= 2:
#             countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes]))
#         elif i == nr_of_nodes - 1:
#             countrylist.append(Node(i, None, [i - 1]))
#         else:
#             countrylist.append(Node(i, None, [i - 1, i + 1]))
#
#     countrylist.append(Node(len(countrylist), None, [0, 1, 2]))
#
# elif graphtype == "triple":
#     # generate a double triple edge graph of type:
#     #   0
#     # / | \
#     # 0-0-0-0-0-0-... etc.
#     #   \ | /
#     #     0
#     for i in range(0, nr_of_nodes):
#         if i == 0:
#             countrylist.append(Node(i, None, [1, nr_of_nodes]))
#         elif i <= 2:
#             countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes, nr_of_nodes + 1]))
#         elif i == 3:
#             countrylist.append(Node(i, None, [i - 1, i + 1, nr_of_nodes]))
#         elif i == nr_of_nodes - 1:
#             countrylist.append(Node(i, None, [i - 1]))
#         else:
#             countrylist.append(Node(i, None, [i - 1, i + 1]))
#
#     countrylist.append(Node(len(countrylist), None, [0, 1, 2]))
#     countrylist.append(Node(len(countrylist), None, [1, 2, 3]))
#
# else:

    # generate a triple node graph of type:
    #   0----0
    # / | \/ |\
    # 0-0-0-0-0-0-... etc.
    #   \ | /
    #     0
nodetop1 = Node(7, None, [0, 1, 2, 8])
nodetop2 = Node(8, None, [2, 3, 4, 7])
nodebottom = Node(9, None, [1, 2, 3])


countrylist.append(Node(0, None, [1, nodetop1.name]))
countrylist.append(Node(1, None, [0, 2, nodetop1.name, nodebottom.name]))
countrylist.append(Node(2, None, [1, 3, nodetop1.name, nodebottom.name, nodetop2.name]))
countrylist.append(Node(3, None, [2, 4, nodebottom.name, nodetop2.name]))
countrylist.append(Node(4, None, [3, 5, nodetop2.name]))
countrylist.append(Node(5, None, [4, 6]))
countrylist.append(Node(6, None, [5]))

countrylist.append(nodetop1)
countrylist.append(nodetop2)
countrylist.append(nodebottom)

for node in countrylist:
     print(node.name, end = "")
print()

# find nodes with most neighbors
def most_neighbors(countrylist):
    neighborcount = 0
    most_neighbored_countries = []
    for node in countrylist:
        if len(node.neighbors) > neighborcount:
            neighborcount = len(node.neighbors)

    for node in countrylist:
        if len(node.neighbors) == neighborcount:
            most_neighbored_countries.append(node.name)

    return(most_neighbored_countries)



# country with most neighbors gets the least used color
for node in most_neighbors(countrylist):
    countrylist[node].changetype(transmitter_list[::-1], countrylist)

# change color of country accordingly
for node in countrylist:
    if node.trans_type == None:
        node.changetype(transmitter_list, countrylist)

for node in most_neighbors(countrylist):
    countrylist[node].changetype(transmitter_list, countrylist)


print(" " + countrylist[7].trans_type, end = "")
print(" " + countrylist[8].trans_type, end = "")
print()
for node in countrylist[:-3]:
    print(node.trans_type, end = "")
print()
print("  " + countrylist[9].trans_type)
