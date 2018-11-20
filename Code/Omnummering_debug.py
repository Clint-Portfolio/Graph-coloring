from helpers import *


provinces, neighbors = provinces("buurlanden_NL.csv")
numberlist = land_naar_nummer(provinces, neighbors)
for i in range(len(provinces)):
    print(provinces[i])
    print(neighbors[i])
    print(numberlist[i])
    print()
