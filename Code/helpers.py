# Helper functions for 'radio russia' algorithm


def provinces(INPUT_CSV):
    # open excel file
    with open(INPUT_CSV, newline='') as csvfile:
        lines = csvfile.readlines()
        #print(lines[0])

        list_provinces = []
        list_neighbors = []
        # loop over lines to get (neighboring) provinces
        for line in lines:
            split_list = line.split(';')
            provinces = split_list[0]
            #print(type(provinces))

            # The provinces were strings and I put it in a list
            list_provinces.append(provinces)

            province_neigbours = split_list[1].split(', ')

            province_neigbours[-1] = province_neigbours[-1].strip()
            list_neighbors.append(province_neigbours)

        return(list_provinces, list_neighbors)


def land_naar_nummer(provincies, buurlanden_nl):
    # maakt woordenboek met provincie en indexnummer
    provincies_dic = {"Noord-Holland" : 0, "Zuid-Holland" : 1, "Utrecht" : 2, "Zeeland" : 3, "Noord-Brabant": 4, "Groningen" : 5, "Drente" : 6, "Friesland" : 7, "Flevoland" : 8, "Overijssel" : 9, "Gelderland" : 10, "Limburg" : 11}

    buurlanden_cijfers = []

    # koppelt de provincie aan buurtlanden met het reeds gemaakte dictionary indexnummer
    for provincie in buurlanden_nl:
        buurlanden_provincie = []
        
        for buurland in provincie:
            if buurland in provincies_dic:
                buurlanden_provincie.append(provincies_dic[buurland])
        
        buurlanden_cijfers.append(buurlanden_provincie)

    return buurlanden_cijfers

class Node(object):

    def __init__(self, name, transmitter_type, neighbors):
        self.name = name
        self.trans_type = transmitter_type
        self.neighbors = neighbors

    # check for the color of neighbors and change accordingly
    def changetype(self, transmitter_list, nodelist):
        a = 0
        type_found = False

        # iterate through colors until a suitable color has been found
        while (a < len(transmitter_list)) or not type_found:
            type_found = True
            check_type = transmitter_list[a]
            # check if type is a suitable type
            for node in self.neighbors:
                if nodelist[node].trans_type == check_type:
                    type_found = False
                    break
            if type_found == True:
                self.trans_type = check_type
                break
            a += 1

            if a == len(transmitter_list):
                return False

        return True

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

    return countrylist

def numbers_to_nodes(neighborlist):
    nodelist = []
    for i in range(0, len(countrylist)):
        nodelist.append(Node(i, None, neighborlist[i]))
    return(nodelist)

# find node with most neighbors
def most_neighbors(countrylist):
    most_neighbored_countries = []
    for node in countrylist:
        if len(node.neighbors) > neighborcount:
            neighborcount = len(node.neighbors)

    for node in countrylist:
        if len(node.neighbors) == neighborcount:
            most_neighbored_countries.append(node.name)

    return(most_neighbored_countries)

"""
This greedy algorithm takes 4 arguments: The list of countries, the list of available transmitters,
The starting country (or node), and an argument to find the most neighbored countries.
The program will first find the highest number of neighbors any node has in the list, and then add the nodes with that many minus the last argument to a list.
This to test if there is an optimum to be found for prefilling the most neighbored countries.
The program will then run over the list from left to right (and back to 0 if at the end of the list), changing the type of the nodes accordingly.
If no suitable type has been found, it simply returns False.
"""
def greedy(countrylist, transmitter_list, starting_node, find_most_neighbors=0):
    neighborcount = 0
    most_neighbored_countries = []
    countrytranslist = []

    for node in countrylist:
        if len(node.neighbors) > neighborcount:
            neighborcount = len(node.neighbors)

    for node in countrylist:
        if len(node.neighbors) >= neighborcount - find_most_neighbors:
            most_neighbored_countries.append(node.name)

    # country with most neighbors gets the least used color
    for node in most_neighbored_countries:
        countrylist[node].changetype(transmitter_list[::-1], countrylist)

    # change color of country accordingly
    for i in range(starting_node, starting_node + len(countrylist)):
        if countrylist[i % len(countrylist)].trans_type == None:
            if not countrylist[i % len(countrylist)].changetype(transmitter_list, countrylist):
                return False

    for node in most_neighbored_countries:
        countrylist[node].changetype(transmitter_list, countrylist)

    for node in countrylist:
        countrytranslist.append(node.trans_type)

    return(countrytranslist)
