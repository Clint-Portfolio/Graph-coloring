def is_finished(countrylist, last_color):
    for country in countrylist:
        if country == last_color:
            return False
    return True


def num_to_colorlist(transmitter_list, country_length, number):
    digits = []
    colorlist = []
    length_transmitter_list = len(transmitter_list)
    for i in range(country_length):
        digits.append(number % length_transmitter_list)
        number //= length_transmitter_list
    for i in digits:
        colorlist.append(transmitter_list[i])
    return colorlist

# def check_correct_config(colorlist, neighborlist):
#     configfile = open("configs.txt", 'a')
#     if check_for_matching_neighbors(iterating_list, neighborlist) == 0:
#         all_possible_configurations.append(iterating_list)
#         configfile.write(f"{iterating_list}\n")


def worker_function(transmitter_list, neighborlist, worker_id, start, stop):
    from helpers import check_for_matching_neighbors
    logfile = open(f"logfile_{worker_id}.txt", 'w')
    logfile.write(f"from {start}; to {stop}\n")
    write = False
    for number in range(start, stop):
        if number % 1000 == 0:
            write = True
        digits = []
        length_transmitter_list = len(transmitter_list)
        for i in range(len(neighborlist)):
            digits.append(transmitter_list[number % length_transmitter_list])
            number //= length_transmitter_list
        if check_for_matching_neighbors(digits, neighborlist) == 0:
            configfile = open("configs.txt", 'a')
            configfile.write(f"{digits}\n")
            print(digits)
        if write:
            digits = "".join(digits)
            logfile.write(f"{digits}\n")
            write = False




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
    job_7 = mp.Process(target=worker_function, args=(transmitter_list, neighborlist, 7, 7 * (total_possibilities // num_jobs), 8 * (total_possibilities // num_jobs)))
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
