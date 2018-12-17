"""
Made by Rosa Slagt. To make a histogram of the cost and freuquency of the transmitters.
"""

def histogram(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)

    #  there are four cost coloumns
    column_number = 3

    hist = data.hist(column=column_number, bins=data.max(axis=0)[column_number] - data.min(axis=0)[column_number], grid=False)

    plt.title('19, 20, 21, 23, 36, 37, 38')
    plt.xlabel('Kosten')
    plt.ylabel('Frequentie')

    plt.show()
