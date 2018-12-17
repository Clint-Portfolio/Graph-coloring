import sys
from helpers import generate_random_country, provinces, country_to_number, cost

if __name__ == '__main__':
    countries, neighbors = provinces(sys.argv[1])
    neighborlist = country_to_number(countries, neighbors)
    full_transmitter_list = ["A", "B", "C", "D", "E", "F", "G"]
    transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41],
                             [19, 20, 21, 23, 36, 37, 38],
                             [16, 17, 31, 33, 36, 56, 57],
                             [3, 34, 36, 39, 41, 43, 58]]
    iterations = 100000
    length_transmitter_list = len(full_transmitter_list)
    for length in range(3, length_transmitter_list, 1):
        print(full_transmitter_list[length])
        writefile = open(f"random_valid_resultsA_{full_transmitter_list[length]}_{str(iterations)}.csv", "w")
        for i in range(iterations):
            new_country = "".join(generate_random_country(neighborlist,
                                                          full_transmitter_list))
            writefile.write(f"{new_country};")
            for transmitter_cost in transmitter_cost_list:
                writestring = str(cost(new_country, transmitter_cost,
                                       full_transmitter_list))
                if transmitter_cost[0] == 3:
                    writefile.write(f"{writestring}\n")
                else:
                    writefile.write(f"{writestring};")
