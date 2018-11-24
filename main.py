"""
The main function of the 4 color problem algorithm. It takes 2 arguments: A CSV file with the node names and node neighbors
The second argument specifies which algorithm is to be used
"""


# Add the file-structure to paths
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", ""))

from helpers import *
from greedy import *

full_transmitter_list = ["A", "B", "C", "D", "E", "F", "G"]
transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41], [19, 20, 21, 23, 36, 37, 38], [16, 17, 31, 33, 36, 56, 57], [3, 34, 36, 39, 41, 43, 58]]


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: main.py csv_file algorithm")
        print("Algorithms implemented are: greedy")
    countries, neighbors = provinces(sys.argv[1])
    countrylist = land_naar_nummer(countries, neighbors)

    if sys.argv[2].lower() == 'greedy':
        best_country = full_greedy(full_transmitter_list, transmitter_cost_list, numbers_to_nodes(countrylist))
        for i in range(len(countries)):
            print(countries[i], end = " ")
            for j in best_country:
                print(j[i], end = "")
            print()

    if sys.argv[2] == "genetic":
        from genetic import *
        generation = genetic(full_transmitter_list[:5], countrylist, 200, 5000, 10)
        print()
        for i in generation[:3]:
            print(i)
            print(calculate_cost(countrylist_to_transmitter_amount(i, full_transmitter_list[:5]), transmitter_cost))
        print()

        for list_position in range(0, len(generation)):
            wrong_neighbors = 0
            for country in range(len(generation[list_position])):
                for neighbor in countrylist[country]:
                    # print(f"{generation[list_position][country]}, {generation[list_position][neighbor]}")
                    if generation[list_position][country] == generation[list_position][neighbor]:
                        wrong_neighbors += 1
            print(f"Wrong neighbors of position {list_position}: {wrong_neighbors // 2}")


        # for i in range(len(countries)):
        #     print(countries[i], end = " ")
        #     print(generation[0][i])
