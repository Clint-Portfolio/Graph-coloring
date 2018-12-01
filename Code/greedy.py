def full_greedy(neighbor_list, transmitter_list, transmitter_cost_list):
    from helpers import greedy_regular, cost_from_country_list
    countrylist = []
    for most_neighbored_countries in range(0, len(neighbor_list)):
        for starting_node in range(0, len(neighbor_list)):
            countrylist.append(greedy_regular(neighbor_list, transmitter_list, starting_node, most_neighbored_countries))

    lowest_cost_positions = []
    lowest_cost = 58**len(neighbor_list)

    for country in countrylist:
        for transmitter_cost in transmitter_cost_list:
            country_cost = cost_from_country_list(country, transmitter_cost, transmitter_list)
            if country_cost == lowest_cost:
                lowest_cost_positions.append([country, transmitter_cost])
            elif country_cost < lowest_cost:
                lowest_cost = cost_from_country_list(country, transmitter_cost, transmitter_list)
                lowest_cost_positions = [[country, transmitter_cost]]

    print()
    print("The lowest cost found is: " + str(lowest_cost))
    print("Unique graph colorings found are: ")
    print()

    already_generated = []
    for i in lowest_cost_positions:
        if i not in already_generated:
            print(i[0])
            print(i[1])
            already_generated.append(i)
    return(already_generated)


if __name__ == '__main__':
    from helpers import check_for_matching_neighbors, generate_triple
    country = full_greedy(['A', 'B', 'C', 'D', 'E'], [[12, 26, 27, 30, 37, 39, 41], [19, 20, 21, 23, 36, 37, 38]], generate_triple(just_numbers=True))
    for i in country:
        print(i, check_for_matching_neighbors(i, generate_triple(True)))
