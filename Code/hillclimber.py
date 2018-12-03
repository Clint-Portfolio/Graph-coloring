def hillclimb(neighborlist, transmitter_list, cost_list):
    import random
    import copy
    from helpers import cost_from_country_list
    iterating_list = [transmitter_list[random.randrange(len(transmitter_list))] for i in range(len(neighborlist))]
    print(iterating_list)
    best_found = False
    while not best_found:
        changing_node = random.randrange(len(iterating_list))
        random_color = copy.deepcopy(transmitter_list)
        random_color.remove(iterating_list[changing_node])







if __name__ == '__main__':
    from helpers import generate_triple, generate_random_country, check_for_matching_neighbors, visualise_graph
    transmitter_list = ["A", "B", "C", "D", "E"]
    colors = ['blue', 'green', 'yellow', 'red', 'purple']
    neighborlist = generate_triple(True)
    countrylist = generate_random_country(neighborlist, transmitter_list)



    import networkx as nx
    import matplotlib.pyplot as plt
    gr = []
    country_colors = ['blue', 'green', 'yellow', 'red', 'purple', 'orange', 'pink', 'black', 'white', 'gold']
    for node in range(len(countrylist)):
        for neighbor in neighborlist[node]:
            gr.append((node, neighbor))
        # country_colors.append(transmitter_colors[transmitter_list.index(countrylist[node])])
    print()
    print(country_colors)
    for i in range(len(countrylist)):
        print(i, countrylist[i], country_colors[i])
    graph = nx.Graph(gr)
    sorted(nx.Graph(gr))
    print("edges added")
    nx.draw(graph, node_color=country_colors, with_labels=True)
    plt.show()



    print(countrylist)
    print(check_for_matching_neighbors(countrylist, neighborlist))
    print(" " + countrylist[-3], end = "")
    print("-" + countrylist[-1])
    for node in countrylist[:-3]:
        print(node, end = "")
    print()
    print("  " + countrylist[-2])
    print()





    # visualise_graph(countrylist, neighborlist, transmitter_list, colors)
