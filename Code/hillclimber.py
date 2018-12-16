def hillclimb(neighborlist, transmitter_list, cost_list, iterations):
    import random
    import copy
    from helpers import cost, generate_random_country, check_for_matching_neighbors
    iterating_list = generate_random_country(neighborlist, transmitter_list)
    best_found = 0
    while best_found < iterations:
        cheapest_cost = cost(iterating_list, cost_list, transmitter_list)
        # print(f"{cheapest_cost}")
        changing_node = random.randrange(len(iterating_list))
        random_color = copy.deepcopy(transmitter_list)
        random_color.remove(iterating_list[changing_node])
        for color in random_color:
            new_countrylist = copy.deepcopy(iterating_list)
            new_countrylist[changing_node] = color
            if cost(new_countrylist, cost_list, transmitter_list) < cheapest_cost and not check_for_matching_neighbors(new_countrylist, neighborlist):
                iterating_list = new_countrylist
                cheapest_cost = cost(new_countrylist, cost_list, transmitter_list)
                break

        best_found += 1
    return iterating_list, cheapest_cost


def full_hillclimb(neighborlist, transmitter_list, list_of_cost_lists, generations=10, iterations=100):
    from helpers import cost
    cheapest_cost_per_list = []

    for cost_list in list_of_cost_lists:
        cheapest_country_cost = cost_list[-1] * len(neighborlist)
        cheapest_country = []

        for iteration in range(generations):
            countrylist, cheapest_cost = hillclimb(neighborlist, transmitter_list, cost_list, iterations)

            if cheapest_cost < cheapest_country_cost:
                cheapest_country_cost = cheapest_cost
                cheapest_country = countrylist

        cheapest_cost_per_list.append(cheapest_country)

    # for country in range(len(cheapest_cost_per_list)):
    #     print(cost(cheapest_cost_per_list[country], list_of_cost_lists[country], transmitter_list))
    #     print(cheapest_cost_per_list[country])

    return cheapest_cost_per_list



if __name__ == '__main__':
    from helpers import generate_triple, visualise_graph
    transmitter_list = ["A", "B", "C", "D", "E", "F"]
    colors = ['blue', 'green', 'yellow', 'red', 'purple', 'white']
    transmitter_cost_list = [[2, 4, 6, 8, 10, 12], [1, 2, 8, 10, 12, 14]]
    neighborlist = generate_triple(True)
    list_of_countries = full_hillclimb(neighborlist, transmitter_list, transmitter_cost_list, 10, 100)
    for countrylist in list_of_countries[0:2]:
        print(" " + countrylist[-3], end = "")
        print("-" + countrylist[-1])
        for node in countrylist[:-3]:
            print(node, end = "")
        print()
        print("  " + countrylist[-2])
        print()

        visualise_graph(countrylist, neighborlist, transmitter_list, colors)
