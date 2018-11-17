from helpers import *
import sys

countrylist = generate_triple()
transmitter_list = ["A", "B", "C", "D", "E"]
transmitter_cost = [3, 34, 36, 39, 41]
starting_node = 0
results = {}

for most_neighbored_countries in range(0, 3):
    most_neighbored_countrieslist = {}
    for i in range(0, len(countrylist)):
        countrylist = greedy(generate_triple(), transmitter_list, i, most_neighbored_countries)
        if type(countrylist) == list:
            trans_count = []
            for letter in transmitter_list:
                trans_count.append(countrylist.count(letter))

            most_neighbored_countrieslist[i] = trans_count
        else:
            print("No suitable graph found")
            countrylist = generate_triple()

    results[most_neighbored_countries] = most_neighbored_countrieslist

total_cost_list = []
lowest_cost_positions = []
lowest_cost = 1000000

for most_neighbor_key in results.keys():
    for starting_node_key in results[most_neighbor_key].keys():
        total_cost = 0
        for i in range(0, len(transmitter_list)):
            total_cost += results[most_neighbor_key][starting_node_key][i]  * transmitter_cost[i]
        total_cost_list.append(total_cost)
        if total_cost < lowest_cost:
            lowest_cost = total_cost
            lowest_cost_positions = []
        elif total_cost == lowest_cost:
            lowest_cost_positions.append([most_neighbor_key, starting_node_key])


print(total_cost_list)
print(lowest_cost_positions)
