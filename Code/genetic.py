from helpers import generate_triple, calculate_cost, countrylist_to_transmitter_amount

transmitter_list = ["A", "B", "C", "D"]
full_transmitter_cost_list = [[12, 26, 27, 30, 37, 39, 41], [19, 20, 21, 23, 36, 37, 38], [16, 17, 31, 33, 36, 56, 57], [3, 34, 36, 39, 41, 43, 58]]
transmitter_cost = full_transmitter_cost_list[1]

def score(neighbor_list, generation_list, transmitter_cost, transmitter_list):
    score_list = []
    for nodelist in generation_list:
        transmitter_count = countrylist_to_transmitter_amount(nodelist, transmitter_list)
        score = 0
        same_neighbors = 0
        for node in range(len(nodelist)):
            for neighbor in neighbor_list[node]:
                if nodelist[neighbor] == nodelist[node]:
                    same_neighbors += 1
        score -= calculate_cost(transmitter_count, transmitter_cost)
        score = score - score * (same_neighbors // 2)
        score_list.append([nodelist, score])

    score_list.sort(reverse=True, key=lambda x: x[1])
    return(score_list)


"""
A culling formula to make a 'breeding ground' of a generation.
The average of the population is calculated
'fitness' is determined by dividing the average by the score.
The generation is then put into the 'breeding ground' according to fitness
"""


def cull(generation_score_list):
    import random
    average = 0
    for i in generation_score_list:
        average += i[1]
    average = average / len(generation_score_list)

    breeding_ground = []
    avg_fitness = 0
    for parent in generation_score_list:
        if parent[1] == 0:
            break
        fitness = average / parent[1]
        avg_fitness += fitness
        while fitness > 1:
            breeding_ground.append(parent[0])
            fitness -= 1
        if fitness > random.random():
            breeding_ground.append(parent[0])

    return(breeding_ground)


def breed(parent_list, transmitter_list, generation_size):
    import random
    new_generation = []
    children = []

    while len(children) < generation_size:
        father = parent_list[random.randrange(0, len(parent_list))]
        mother = parent_list[random.randrange(0, len(parent_list))]
        splice = random.randint(1, len(mother) - 2)
        children.append(father[:splice] + mother[splice:])
        children.append(mother[:splice] + father[splice:])
    return(children)

def mutation(child_list, mutation_chance=0):
    import random
    for child in range(len(child_list)):
        for node in range(len(child_list[child])):
            if mutation_chance > random.randint(0, 10000):
                child_list[child][node] = transmitter_list[random.randrange(0, len(transmitter_list))]
    return(child_list)

def genetic(transmitter_list, neighbor_list=generate_triple(True), generation_size=100, generations=5, mutation_chance=0):
    import random
    for generation in range(generations - 1):
        generation_list = []
        for i in range(generation_size):
            node_colors = []
            for node in range(len(neighbor_list)):
                node_colors.append(transmitter_list[random.randrange(0, len(transmitter_list))])
            generation_list.append(node_colors)
        generation_list = score(neighbor_list, generation_list, transmitter_cost, transmitter_list)
        if generation % 500 == 0:
            print(f"generation {generation}:")
            sum = 0
            for i in generation_list:
                sum += i[1]
            print(f"Total average = {sum / len(generation_list)}", end = "  ")
            sum = 0
            for i in generation_list[:(len(generation_list) // 5)]:
                sum += i[1]
            print(f"Average of top 20%: {sum / (len(generation_list) // 5)}", end = "  ")
            sum = 0
            for i in generation_list[:(len(generation_list) // 10)]:
                sum += i[1]
            print(f"Average of top 10%: {sum / (len(generation_list) // 10)}")
        generation_list = cull(generation_list)
        generation_list = breed(generation_list, transmitter_list, generation_size)
        generation_list = mutation(generation_list, mutation_chance)
    generation_list = score(neighbor_list, generation_list, transmitter_cost, transmitter_list)
    generation_list = cull(generation_list)
    generation_list = breed(generation_list, transmitter_list, generation_size)
    return(generation_list)


if __name__ == '__main__':
    child_list = genetic(transmitter_list, generate_triple(True), 200, 50000, 5)
    child_list = score(generate_triple(True), child_list, transmitter_cost, transmitter_list)
    print()
    for i in child_list[0:2]:
        print(i[1])
        print(f" {i[0][-3]}-{i[0][-2]}")
        print("".join(i[0][:-3]))
        print(f"  {i[0][-1]}")
        print()
