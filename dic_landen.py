
# test dictionaries voor de provincies
provincies = ["Noord-Holland", "Noord-Brabant", "Utrecht"]


#losse lijsten buurlanden
buurland_nh = ["Utrecht"]
buurland_nb = [ "Utrecht"]
buurland_ut = ["Noord-Holland", "Noord-Brabant"]

buurlanden_nl = []
# grote lijst met de buurlanden
buurlanden_nl.append(buurland_nh)
buurlanden_nl.append(buurland_nb)
buurlanden_nl.append(buurland_ut)


def land_naar_nummer(provincies, buurlanden_nl):
    index = 0
    provincies_dic = {}
    for provincie in provincies:
        provincies_dic [provincie] = index
        index+=1


    buurlanden_cijfers = []
    buurland_provincie = []

    lijst = False

    for provincie in buurlanden_nl:
        if lijst == True:
            buurlanden_cijfers.append(buurland_provincie)
            buurland_provincie = []
        for land in provincie:
            if land in provincies_dic:
                buurland_provincie.append(provincies_dic[land])
                lijst = True

    buurlanden_cijfers.append(buurland_provincie)

    print(provincies_dic)
    print(buurlanden_cijfers)
    print(buurlanden_nl)

land_naar_nummer(provincies, buurlanden_nl)