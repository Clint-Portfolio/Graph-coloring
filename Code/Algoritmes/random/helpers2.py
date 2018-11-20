# Helper functions for 'radio russia' algorithm


def provinces(INPUT_CSV):
    # open excel file
    with open(INPUT_CSV, newline='') as csvfile:
        lines = csvfile.readlines()
        #print(lines[0])

        list_provinces = []

        # loop over lines to get (neighboring) provinces
        for line in lines:
            split_list = line.split(';')
            provinces = split_list[0].strip('/r/n')

            # The provinces were strings and I put it in a list
            list_provinces.append(provinces)

            province_neigbours = split_list[1]
            province_neigbour = province_neigbours.split(',')

            province_neigbour[-1] = province_neigbour[-1].rstrip()

        return(list_provinces)


def land_naar_nummer(provincies, buurlanden_nl):

    # maakt woordenboek met provincie en indexnummer
    index = 0
    provincies_dic = {}
    for provincie in provincies:
        provincies_dic [provincie] = index
        index+=1


    buurlanden_cijfers = []
    buurland_provincie = []

    # dat er niet eerst een lege lijst gereturned wordt
    lijst = False
    # koppelt de provincie aan buurtlanden met het reeds gemaakte dictionary indexnummer
    for provincie in buurlanden_nl:
        if lijst == True:
            buurlanden_cijfers.append(buurland_provincie)
            buurland_provincie = []
        for land in provincie:
            if land in provincies_dic:
                buurland_provincie.append(provincies_dic[land])
                lijst = True
    # dat de laatste provinsie ook toegevoegd wordt
    buurlanden_cijfers.append(buurland_provincie)

    return(buurland_provincie)


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

        if a == len(transmitter_list) + 1:
            return False

def numbers_to_nodes(neighborlist):
    nodelist = []
    for i in range(0, len(countrylist)):
        nodelist.append(Node(i, None, neighborlist[i]))
    return(nodelist)

def greedy(countrylist, transmitter_list):
    most_neighbored_countries = []
    for node in countrylist:
        if len(node.neighbors) > neighborcount:
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

    for node in most_neighbored_countries:
        countrylist[node].changetype(transmitter_list, countrylist)

    return(countrylist)
