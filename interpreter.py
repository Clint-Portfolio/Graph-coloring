# Name: Liora Rosenberg
# Student number: 11036435
"""
This script interprets an excel file and then outputs a list of provinces (list_provinces) and a list of neighbouring provinces (province_neigbour).
"""

import csv
from bs4 import BeautifulSoup

# import csv file
INPUT_CSV = "buurlanden_NL.csv"

def provinces(INPUT_CSV):
    # open excel file
    with open(INPUT_CSV, newline='') as csvfile:
        lines = csvfile.readlines()
        #print(lines[0])

        list_provinces = []

        # loop over lines to get (neighboring) provinces
        for line in lines:
            split_list = line.split(';')
            provinces = split_list[0].strip('/r/n')
            #print(type(provinces))

            # The provinces were strings and I put it in a list
            list_provinces.append(provinces)

            province_neigbours = split_list[1]
            province_neigbour = province_neigbours.split(',')

            province_neigbour[-1] = province_neigbour[-1].rstrip()
            print(province_neigbour)

        print(list_provinces)

if __name__ == "__main__":
    provinces(INPUT_CSV)
