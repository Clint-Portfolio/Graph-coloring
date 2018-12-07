def matching_neighbors(countrylist, neighborlist):
    country_number_list = []
    for country_number in range(len(countrylist)):
        for neighbor in [i for i in neighborlist[country_number] if i > country_number]:
            if countrylist[country_number] == countrylist[neighbor]:
                country_number_list.append(country_number)
                return [country_number]
    return country_number_list


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



def depth_first(neighborlist, transmitter_list):
    import multiprocessing as mp
    jobs = []
    total_possibilities = len(transmitter_list)**len(neighborlist)
    num_jobs = 8
    job_0 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 0, 0 * (total_possibilities // num_jobs), 1 * (total_possibilities // num_jobs)))
    job_1 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 1, 1 * (total_possibilities // num_jobs), 2 * (total_possibilities // num_jobs)))
    job_2 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 2, 2 * (total_possibilities // num_jobs), 3 * (total_possibilities // num_jobs)))
    job_3 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 3, 3 * (total_possibilities // num_jobs), 4 * (total_possibilities // num_jobs)))
    job_4 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 4, 4 * (total_possibilities // num_jobs), 5 * (total_possibilities // num_jobs)))
    job_5 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 5, 5 * (total_possibilities // num_jobs), 6 * (total_possibilities // num_jobs)))
    job_6 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 6, 6 * (total_possibilities // num_jobs), 7 * (total_possibilities // num_jobs)))
    job_7 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 7, 7 * (total_possibilities // num_jobs), (total_possibilities // num_jobs)))
    job_0.start()
    job_1.start()
    job_2.start()
    job_3.start()
    job_4.start()
    job_5.start()
    job_6.start()
    job_7.start()
    print("All processes started")
    job_0.join()
    job_1.join()
    job_2.join()
    job_3.join()
    job_4.join()
    job_5.join()
    job_6.join()
    job_7.join()
    print("All processes finished")
    return


if __name__ == '__main__':
    from helpers import generate_triple
    country = depth_first(generate_triple(just_numbers=True), ['A', 'B', 'C', 'D'])
    for i in country:
        print(i)
