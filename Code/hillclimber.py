def hillclimb(neighborlist, transmitter_list, cost_list, iterations, writefile):
    import random
    import copy
    from helpers import cost, generate_random_country, check_for_matching_neighbors

    iterating_list = generate_random_country(neighborlist, transmitter_list)
    current_cost = cost(iterating_list, cost_list, transmitter_list)
    writefile.write(f"{current_cost};")
    cheapest_cost = cost_list[-1] * len(iterating_list)
    for i in range(iterations):
        changing_node = random.randrange(len(iterating_list))
        random_color = copy.deepcopy(transmitter_list)
        random_color.remove(iterating_list[changing_node])

        for color in random_color:
            new_countrylist = copy.deepcopy(iterating_list)
            new_countrylist[changing_node] = color
            if cost(new_countrylist, cost_list, transmitter_list) < cheapest_cost and not check_for_matching_neighbors(new_countrylist, neighborlist):
                cheapest_country = copy.deepcopy(new_countrylist)
                iterating_list = new_countrylist
                cheapest_cost = cost(new_countrylist, cost_list, transmitter_list)
                break
        current_cost = cost(iterating_list, cost_list, transmitter_list)
        writefile.write(f"{current_cost};")

    writefile.write(f"{current_cost}\n")
    return cheapest_country, cheapest_cost


def full_hillclimb(neighborlist, transmitter_list, list_of_cost_lists, generations=10, iterations=10):
    from helpers import cost
    import copy
    cheapest_cost_per_list = []
    filename = "Ukraine_hillclimber"

    for cost_index in range(len(list_of_cost_lists)):
        cost_list = list_of_cost_lists[cost_index]
        writefile = open(f"{filename}_{str(cost_index)}.csv", 'a')
        cheapest_cost = list_of_cost_lists[cost_index][-1] * len(neighborlist)
        cheapest_country = []

        for generation in range(generations):
            countrylist, country_cost = hillclimb(neighborlist, copy.deepcopy(transmitter_list), cost_list, iterations, writefile)
            if country_cost < cheapest_cost:
                cheapest_cost = country_cost
                cheapest_country = copy.deepcopy(countrylist)
                print(cheapest_cost, "".join(cheapest_country))
        print()
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
