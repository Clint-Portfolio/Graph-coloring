
"""
Gemaakt door: Rosa
Programaatje dat een nummer aan een specifieke provincie hangt,
zodat het met andere programma's te interpeteren is.

"""
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


# test dictionaries voor de provincies
provincies = ["Noord-Holland", "Noord-Brabant", "Utrecht"]


#losse lijsten buurlanden
buurland_nh = ["Utrecht"]
buurland_nb = [ "Utrecht"]
buurland_ut = ["Noord-Holland", "Noord-Brabant"]

# grote lijst met de buurlanden
buurlanden_nl = []

buurlanden_nl.append(buurland_nh)
buurlanden_nl.append(buurland_nb)
buurlanden_nl.append(buurland_ut)



def land_naar_nummer(provincies, buurlanden_nl):

    # maakt woordenboek met provincie en indexnummer
    # index = 0
    provincies_dic = {"Noord-Holland" : 0, "Zuid-Holland" : 1, "Utrecht" : 2, "Zeeland" : 3, "Noord-Brabant": 4, "Groningen" : 5, "Drente" : 6, "Friesland" : 7, "Flevoland" : 8, "Overijssel" : 9, "Gelderland" : 10, "Limburg" : 11}
    
    # for provincie in provincies:
    #     provincies_dic[provincie] = index
    #     index+=1

    buurlanden_cijfers = []

    # dat er niet eerst een lege lijst gereturned wordt
    # lijst = False
    # koppelt de provincie aan buurtlanden met het reeds gemaakte dictionary indexnummer
    for provincie in buurlanden_nl:
        buurlanden_provincie = []
        
        for buurland in provincie:
            if buurland in provincies_dic:
                buurlanden_provincie.append(provincies_dic[buurland])
        
        buurlanden_cijfers.append(buurlanden_provincie)


        # if lijst == True:
        #     buurlanden_cijfers.append(buurland_provincie)
        #     buurland_provincie = []
        # for land in provincie:
        #     if land in provincies_dic:
        #         buurland_provincie.append(provincies_dic[land])
        #         lijst = True
    # dat de laatste provinsie ook toegevoegd wordt

    return buurlanden_cijfers

"""
om te testen kunnen de volgende printstatements uitgevoerd worden
    #print(provincies_dic)
    #print(buurlanden_cijfers)
    #print(buurlanden_nl)
"""



buurlanden_cijfers = land_naar_nummer(input[0], input[1])

print(buurlanden_cijfers)
print(input[1])



