"""
A function that returns a list of all the neighbors that have the same type
"""


def matching_neighbors(countrylist, neighborlist):
    country_number_list = []
    for country_number in range(len(countrylist)):
        for neighbor in [i for i in neighborlist[country_number] if i > country_number]:
            if countrylist[country_number] == countrylist[neighbor]:
                country_number_list.append(country_number)
                return [country_number]
    return country_number_list

def new_matching_neighbors(countrylist, neighborlist):
    country_number_list = []
    for country_number in range(len(countrylist)):
        for neighbor in [i for i in neighborlist[country_number] if i > country_number]:
            if countrylist[country_number] == countrylist[neighbor]:
                country_number_list.append(country_number)
                return country_number
    return -1


def change_number(countrylist, position, base):
        if countrylist[position + 1] == base:
            countrylist = change_number(countrylist, position + 1, base)
        countrylist[position] = (countrylist[position] + 1) % base
        return countrylist


def worker_function(transmitter_list, neighborlist, worker_id, start, stop):
    import copy
    from helpers import check_for_matching_neighbors
    log = open(f"winninglog_worker{worker_id}.txt", 'a')
    log.write(f"Start: {start}, Stop: {stop}\n")
    while start <= stop:
        # print(f"\n\n\n")
        number = copy.deepcopy(start)
        countrylist = []
        length_transmitter_list = len(transmitter_list)
        for i in range(len(neighborlist)):
            if number == 0:
                countrylist.append(transmitter_list[0])
            else:
                countrylist.append(transmitter_list[number % length_transmitter_list])
                number //= length_transmitter_list
        matching_neighbor_list = matching_neighbors(countrylist, neighborlist)
        if matching_neighbor_list == []:
            write = "".join(countrylist)
            log.write(f"{write} {start}\n")
            start += 1
        else:
            for country in matching_neighbor_list:
                # if neighbor N has a matching neighor, go forward by len(transmitter_list) ^ N
                start += len(transmitter_list)**country


def new_worker_function(transmitter_list, neighborlist, worker_id, start, stop):
    import copy
    iterating_list = []
    highest_integer = len(transmitter_list) - 1
    number = copy.deepcopy(start)
    for i in range(len(neighborlist)):
        if number == 0:
            iterating_list.append(0)
        else:
            iterating_list.append(number % len(transmitter_list))
            number //= len(transmitter_list)
    print(iterating_list)
    open(f"winninglog_worker{worker_id}.txt", 'a').write(f"{start} {stop}\n")
    while start <= stop:
        matching_neighbor = new_matching_neighbors(iterating_list, neighborlist)
        if matching_neighbor == -1:
            open(f"winninglog_worker{worker_id}.txt", 'a').write(f"{iterating_list}\n")
            start = start + 1
        else:
            iterating_list = change_number(iterating_list, matching_neighbor, highest_integer)
            start += len(transmitter_list)**matching_neighbor


if __name__ == '__main__':
    import sys
    from helpers import generate_triple, provinces, country_to_number
    transmitter_list = ['A', 'B', 'C']
    if len(sys.argv) == 2:
        countries, neighbors = provinces(sys.argv[1])
        neighborlist = country_to_number(countries, neighbors)
    else:
        neighborlist = generate_triple(True)
    worker_function(transmitter_list, neighborlist, 0, 0, len(transmitter_list)**len(neighborlist))
