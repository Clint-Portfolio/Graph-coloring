"""
Clint Nieuwendijk
10300414
A hardcoded script to generate a graph of type:
generate a triple node graph of type:
  0----0
/ | \/ |\
0-0-0-0-0-0-0-0
  \ | /
    0

It is also located in the helpers.py document
"""

def generate_triple():
    countrylist = []

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

    return(countrylist)
