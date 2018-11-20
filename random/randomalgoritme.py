# Rosa SLagt
# 11040548

"""
A random function for the distribution of transmission frequencies in a given country
"""

import csv
import random
from bs4 import BeautifulSoup
from helpers import 

def random(provinces):  
       
        zendmast_met_land = []     

        for provincie in provinces: 
                zendmast = random.randrange(7)
                zendmast_met_land [provincie] = zendmast

        return(zendmast_met_land)

if __name__ == "__main__":
        provinces = (provinces("buurlanden_NL.csv"))[0]
        big_list = []    
        for i in range(100):
                big_list.append(random(provinces))