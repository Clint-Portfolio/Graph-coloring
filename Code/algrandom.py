# Rosa SLagt
# 11040548

"""
A random function for the distribution of transmission frequencies in a given country
"""

import csv
from bs4 import BeautifulSoup
from helpers import *
import random 
def random_function(provinces, transmitters):  
       
        transmitter_country = []     

        for province in provinces: 
                transmitter = random.randrange(len(transmitters))
                transmitter_country.append(transmitters[transmitter])

        return(transmitter_country)

if __name__ == "__main__":
        big_list = []    
        for i in range(100000):
                # which transmitters are used
                big_list.append(random_function(provinces,['A', 'B', 'C', 'D', 'E']))