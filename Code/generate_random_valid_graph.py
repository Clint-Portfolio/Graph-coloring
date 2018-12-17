import sys
from helpers import generate_random_country, provinces, country_to_number, cost

if __name__ == '__main__':
    writefile = open("random_valid_resultsA_D.txt", "w")
    countries, neighbors = provinces(sys.argv[1])
    neighborlist = country_to_number(countries, neighbors)
    full_transmitter_list = ["A", "B", "C", "D"]
    transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41],
                             [19, 20, 21, 23, 36, 37, 38],
                             [16, 17, 31, 33, 36, 56, 57],
                             [3, 34, 36, 39, 41, 43, 58]]
    for i in range(1000000):
        new_country = "".join(generate_random_country(neighborlist,
                                                      full_transmitter_list))
        writefile.write(f"{new_country};")
        for transmitter_cost in transmitter_cost_list:
            writestring = str(cost(new_country, transmitter_cost,
                                   full_transmitter_list))
            writefile.write(f"{writestring};")
        writefile.write("\n")
