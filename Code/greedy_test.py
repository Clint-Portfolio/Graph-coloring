from helpers import *

countrylist, neighborlist = provinces("buurlanden_NL.csv")
print(countrylist, neighborlist)
neighborlist = land_naar_nummer(countrylist, neighborlist)
print(countrylist, neighborlist)

print(greedy(countrylist, neighborlist))
