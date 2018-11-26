from helpers import *
from generate_triple_graph import generate_single
import sys

# countrylist = generate_triple()
# full_transmitter_list = ["A", "B", "C", "D", "E", "F", "G"]
# transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41], [19, 20, 21, 23, 36, 37, 38], [16, 17, 31, 33, 36, 56, 57], [3, 34, 36, 39, 41, 43, 58]]
#
# list_of_transmitter_lists = []
# for i in range(4, len(full_transmitter_list) + 1):
#     list_of_transmitter_lists.append(full_transmitter_list[:i])

def full_greedy(transmitter_list, transmitter_cost_list, neighbor_list=generate_triple()):
    starting_node = 0
    results = {}
    for most_neighbored_countries in range(0, len(neighbor_list)):
        most_neighbored_countrieslist = {}
        for i in range(0, len(neighbor_list)):
            countrylist = greedy(neighbor_list, transmitter_list, i, most_neighbored_countries)
            if type(countrylist) == list:
                trans_count = []

                for letter in transmitter_list:
                    trans_count.append(countrylist.count(letter))

                most_neighbored_countrieslist[i] = trans_count
            else:
                countrylist = neighbor_list

        results[most_neighbored_countries] = most_neighbored_countrieslist

    lowest_cost_positions = []
    lowest_cost = 58**len(neighbor_list)


    for transmitter_cost in transmitter_cost_list:
        for most_neighbor_key in results.keys():
            for starting_node_key in results[most_neighbor_key].keys():
                total_cost = calculate_cost(results[most_neighbor_key][starting_node_key], transmitter_cost)
                if total_cost < lowest_cost:
                    lowest_cost = total_cost
                    lowest_cost_positions = []
                elif total_cost == lowest_cost:
                    lowest_cost_positions.append([starting_node_key, most_neighbor_key, transmitter_cost])
    print()
    print("The lowest cost found is: " + str(lowest_cost))
    print("Unique graph colorings found are: ")
    print()

    already_generated = []
    for i in lowest_cost_positions:
        countrylist = greedy(neighbor_list, transmitter_list, i[0], i[1])
        if countrylist not in (x[0] for x in already_generated):
            for node in countrylist:
                print(node, end = "")
            print()
            already_generated.append([countrylist, i[2]])
    return(already_generated)
