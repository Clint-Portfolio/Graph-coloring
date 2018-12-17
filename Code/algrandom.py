# Rosa SLagt
# 11040548

"""
A random function for the distribution of transmission frequencies in a given country.
Restrictions are not implemented.
"""

import csv
from bs4 import BeautifulSoup
from helpers import *
import random 
def random_function(neighbours, transmitters):  
       
        transmitter_country = []     

        for neighbour in neighbours: 
                transmitter = random.randrange(len(transmitters))
                transmitter_country.append(transmitters[transmitter])
                
        print(generate_random_country(neighbours, transmitter_country))

        return(transmitter_country)

if __name__ == "__main__":
        big_list = []    
        for i in range(100000):
                big_list.append(random_function(provinces,['A', 'B', 'C', 'D', 'E']))