
"""
Gemaakt door: Rosa
Programaatje dat een nummer aan een specifieke provincie hangt,
zodat het met andere programma's te interpeteren is.

"""




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

"""
om te testen kunnen de volgende printstatements uitgevoerd worden
    #print(provincies_dic)
    #print(buurlanden_cijfers)
    #print(buurlanden_nl)
"""
land_naar_nummer(provincies, buurlanden_nl)