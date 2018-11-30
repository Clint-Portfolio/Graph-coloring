"""
A script to edit the txt created by manually inserting the numbers of neighboring countries/provinces into a readable csv file.
The file is made by numbering provinces and putting the neighboring numbers higher than province N on line N
The last line is the names of the provinces by number
The script will output a csv file as described in ../Data
"""

import sys
import os

if __name__ == '__main__':
    # check if script is executed correctly and the file exists
    if len(sys.argv) != 3:
        print("Usage: make_neighbors.py filename new_filename")
    elif not os.path.isfile(sys.argv[1]):
        print(f"No such file exists: {sys.argv[1]}")
        exit(1)

    # create and/or open both files
    with open(sys.argv[1], "r") as f:
            neighbor_file = f.readlines()

    # convert every line to a list of numbers
    neighbor_number_list = []
    for line in range(len(neighbor_file[:-1])):
        neighbor_file[line] = neighbor_file[line].strip().split()
        country = []
        for i in range(len(neighbor_file[line])):
            country.append(int(neighbor_file[line][i]) - 1)
        neighbor_number_list.append(country)
    country_name_list = neighbor_file[-1].split()

    # insert lower neighbor in higher neighbor
    # includes failsafe in case the neighbor is already mentioned
    for line in range(len(neighbor_number_list)):
        for neighbor in neighbor_number_list[line]:
            if neighbor not in neighbor_number_list[neighbor]:
                neighbor_number_list[neighbor].append(line)

    for i in country_name_list:
        print(country_name_list.index(i) + 1, i)
    # convert number to name by a lookup in the country name list
    writelist = []
    for line in neighbor_number_list:
        print(line)
        country = []
        for neighbor in line:
            country.append(country_name_list[neighbor])
        writelist.append(country)

    writefile = open(sys.argv[2], "a")

    for line in range(0, len(writelist)):
        writefile.write(f"{country_name_list[line]}; {', '.join(set(writelist[line]))}\n")

    print("Succesfully wrote to file!")
    exit(0)
