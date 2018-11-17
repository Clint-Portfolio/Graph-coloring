from helpers import *
import sys

countrylist = generate_triple()
transmitter_list = ["A", "B", "C", "D"]
transmitter_cost_list = [[12, 26, 27, 30, 37], [19, 20, 21, 23, 36], [16, 17, 31, 33, 36], [3, 34, 36, 39, 41]]
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
            countrylist = generate_triple()

    results[most_neighbored_countries] = most_neighbored_countrieslist

total_cost_list = []
lowest_cost_positions = []
lowest_cost = 1000000
for transmitter_cost in transmitter_cost_list:
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
                lowest_cost_positions.append([most_neighbor_key, starting_node_key, transmitter_cost])


print(lowest_cost)
print(lowest_cost_positions)
print()
for i in lowest_cost_positions:
    countrylist = greedy(generate_triple(), transmitter_list, i[0], i[1])
    print(" " + countrylist[7], end = "")
    print("-" + countrylist[8], end = "")
    print()
    for node in countrylist[:-3]:
        print(node, end = "")
    print()
    print("  " + countrylist[9])
    print()
