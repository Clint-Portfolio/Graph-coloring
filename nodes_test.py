# Clint Nieuwendijk
# The Node class used to work in the most neighbor algorithm

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
