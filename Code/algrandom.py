# Rosa SLagt
# 11040548

"""
A random function for the distribution of transmission frequencies in a given country
"""

import csv
from helpers import *
import random
def random_function(provinces, transmitters):

        zendmast_met_land = []

        for provincie in provinces:
                zendmast = random.randrange(len(transmitters))
                zendmast_met_land.append(transmitters[zendmast])

        print(zendmast_met_land)
        return(zendmast_met_land)

if __name__ == "__main__":
        #provinces = (provinces("../data/buurlanden_NL.csv"))[0]
        big_list = []
        for i in range(100):
                big_list.append(random_function(provinces,['A', 'B', 'C', 'D', 'E']))
