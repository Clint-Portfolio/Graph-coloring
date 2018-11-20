from helpers import *
from generate_triple_graph import generate_single
import sys

countrylist = generate_triple()
full_transmitter_list = ["A", "B", "C", "D", "E", "F", "G"]
transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41], [19, 20, 21, 23, 36, 37, 38], [16, 17, 31, 33, 36, 56, 57], [3, 34, 36, 39, 41, 43, 58]]
starting_node = 0
results = {}

# for i in transmitter_cost_list:
#     print(i)
#     print((i[0] + i[1] + i[2] + i[3]) / 4)
#     print((i[0] + i[1] + i[2] + i[3] + i[4]) / 5)
#     print((i[0] + i[1] + i[2] + i[3] + i[4] + i[5]) / 6)
#     print((i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6]) / 7)
#     print()
#
# print()
# print()

list_of_transmitter_lists = []
for i in range(4, len(full_transmitter_list) + 1):
    list_of_transmitter_lists.append(full_transmitter_list[:i])

for transmitter_list in list_of_transmitter_lists:
    for most_neighbored_countries in range(0, len(countrylist)):
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

lowest_cost_positions = []
lowest_cost = 58**len(countrylist)


for transmitter_cost in transmitter_cost_list:
    for most_neighbor_key in results.keys():
        for starting_node_key in results[most_neighbor_key].keys():
            # total_cost = 0
            #
            # for i in range(0, len(transmitter_list)):
            #     total_cost += results[most_neighbor_key][starting_node_key][i] * transmitter_cost[i]

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
    countrylist = greedy(generate_triple(), transmitter_list, i[0], i[1])
    if countrylist not in already_generated:
        print("Starting Node: " + str(i[0]))
        print("Most neighbors up to: " + str(i[1]))
        print("Transmitter list: " + ", ".join(str(j) for j in i[2]))
        print(results[i[0]][i[1]])
        print(" " + countrylist[-3], end = "")
        print("-" + countrylist[-2], end = "")
        print()
        for node in countrylist[:-3]:
            print(node, end = "")
        print()
        print("  " + countrylist[-1])
        print()
        already_generated.append(countrylist)
