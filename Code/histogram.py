"""
Made by Rosa Slagt. To make a histogram of the cost and freuquency of the transmitters.
"""

def histogram(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)


    #  there are four cost coloumns
    column_number = 2

    data.hist(column=column_number, bins=data.max(axis=0)[column_number] - data.min(axis=0)[column_number], grid=False)

    plt.title('19, 20, 21, 23, 36, 37, 38')
    plt.xlabel('Kosten')
    plt.ylabel('Frequentie')

    plt.show()

# To be able to run the program seperately from main
if __name__ == '__main__':

    histogram("random_valid_resultsA_D_100000.csv")
