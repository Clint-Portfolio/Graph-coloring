"""
The main function of the 4 color problem algorithm. It takes 3 arguments:
Argument 2 is the algorithm
Argument 3 is the csv file with neighboring countries/provinces
Argument 4 is the file where the results are to be written to.
An example would be:
main.py random Data/ukraine_neighbor_provinces.csv random.txt
"""
# Add the file-structure to paths
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", ""))
os.path.join(directory, "Data")
os.path.join(directory, "Data", "")

from helpers import provinces, land_naar_nummer, check_for_matching_neighbors
from helpers import calculate_cost, countrylist_to_transmitter_amount
from helpers import cost, visualise_graph
from helpers import *
from greedy import full_greedy
from algrandom import random_function
from breadthfirst import breadth_first

full_transmitter_list = ["A", "B", "C", "D", "E", "F", "G"]
transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41],
                         [19, 20, 21, 23, 36, 37, 38],
                         [16, 17, 31, 33, 36, 56, 57],
                         [3, 34, 36, 39, 41, 43, 58]]
colors = ['blue', 'green', 'yellow', 'red', 'purple', 'orange', 'pink']

# def print_histogram(filename):
#     print(filename)
#     pd.read_csv(filename)


if __name__ == '__main__':


    if len(sys.argv) != 4:
        print("Usage: main.py algorithm csv_file result_filename")
        print("Algorithms implemented are: greedy, genetic, breadthfirst and random")
        exit(1)

    countries, neighbors = provinces(sys.argv[2])
    countrylist = land_naar_nummer(countries, neighbors)

    if sys.argv[1].lower() == 'plot':
        readfile = open(sys.argv[3], 'r')
        lines = readfile.readlines()
        for i in lines[:10]:
            visualise_graph(list(i[:-1]), countrylist, full_transmitter_list, colors)

    if sys.argv[1].lower() == 'greedy':
        import networkx as nx
        import matplotlib.pyplot as plt
        # also dependancies are needed for scipy
        best_country = full_greedy(countrylist, full_transmitter_list, transmitter_cost_list)
        writefile = open(sys.argv[3], "w")
        write_lines = []
        for i in best_country:
            write_lines.append([i, ])
        for i in best_country:
            writefile.write(f"Cost: {str(cost(i[0], i[1], full_transmitter_list))} \n")
            writefile.write(f"Cost list: {i[1]}\n")
            graph_string = "".join(i[0])
            writefile.write(f"Graph: {graph_string}\n")
            for country in range(len(countries)):
                writefile.write(countries[country] + " " + i[0][country] + "\n")
            writefile.write("\n\n")

        print(f"\n\n{best_country[0][0]}")
        gr = []
        country_colors = []
        for node in range(len(countrylist)):
            for neighbor in countrylist[node]:
                gr.append((node, neighbor))
            country_colors.append(colors[full_transmitter_list.index(best_country[0][0][node])])
        print(country_colors)

        graph = nx.Graph(gr)
        nx.draw_kamada_kawai(graph, node_color=country_colors)
        plt.show()

    if sys.argv[1] == "genetic":
        from genetic import genetic
        generation = genetic(full_transmitter_list[:5], countrylist,
                             200, 5000, 10)
        print()
        for i in generation[:3]:
            print(i)
            print(cost(i, full_transmitter_list, transmitter_cost_list[0]))
        print()

        for list_position in range(0, len(generation)):
            wrong_neighbors = 0
            for country in range(len(generation[list_position])):
                for neighbor in countrylist[country]:
                    country = generation[list_position][country]
                    neighbor = generation[list_position][neighbor]
                    if country == neighbor:
                        wrong_neighbors += 1
            print(f"Wrong neighbors of position \
                   {list_position}: {wrong_neighbors}")

    if sys.argv[1].lower() == 'breadthfirst':
        starting_list = [[None for i in range(len(neighbors))]]
        best_country = breadth_first(countrylist, full_transmitter_list[:4], starting_list)
        # print(best_country)
        writefile = open(sys.argv[3], "w")
        for i in best_country:
            writefile.write(i + "\n")

    if sys.argv[1] == "random":
        # big list contains the letters with the random function
        big_list = []
        for i in range(100):
                big_list.append(random_function(countries, full_transmitter_list[:5]))
        writefile = open(sys.argv[3], "w")

        for country in big_list:
            for letter in country:
                writefile.write(letter)

            writefile.write(";")
            for transmitter_cost in transmitter_cost_list:

                writefile.write(str(cost_from_country_list(country, transmitter_cost, full_transmitter_list[:5])))
                writefile.write(";")
            writefile.write(str(check_for_matching_neighbors(country, countrylist)))
            writefile.write("\n")

    # print_histogram(sys.argv[3])

    if sys.argv[1] == "depthfirst":
        from depthfirst import depth_first, num_to_colorlist
        depth_first(countrylist, full_transmitter_list[:4])
        # writefile = open(sys.argv[3], "w")
        # for country in all_countries:
        #     writefile.write(f"{country}")
        #
        # gr = []
        # colors = ['blue', 'green', 'yellow', 'red', 'purple', 'orange', 'pink']
        # country_colors = []
        # for node in range(len(countrylist)):
        #     for neighbor in countrylist[node]:
        #         gr.append((node, neighbor))
        #     country_colors.append(colors[full_transmitter_list.index(all_countries[0][node])])
        # print(country_colors)
