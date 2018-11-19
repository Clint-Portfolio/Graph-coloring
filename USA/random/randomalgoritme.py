# Rosa SLagt
# 11040548

"""
A random function for the distribution of transmission frequencies in a given country
"""

import csv
import random
from bs4 import BeautifulSoup
from helpers import *


def random(provincies, buurlanden):  
    provinces = (provinces("buurlanden_NL.csv"))[0]
    zendmast_met_land = {}
    
for poging in range(10):
        
    for provincie in provincies: 
        zendmast = random.randrange(7)
        zendmast_met_land [provincie] = zendmast

    
    

if __name__ == "__main__":
    random(provincies, buurlanden)
