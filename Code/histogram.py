"""
Made by Rosa Slagt. To make a histogram of the cost and freuquency of the transmitters.
"""

def histogram(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)

    # to avoid magic numbers. There are five columns (four for cost, the fifth for the wrong nodes)
    column_number = 3
    hist = data.hist(column=column_number, bins=data.max(axis=0)[column_number] - data.min(axis=0)[column_number], grid=False)

    plt.title('Cost differental costs ')
    plt.xlabel('Costs')
    plt.ylabel('Frequency')

    plt.show()

# To be able to run the program seperately from main
histogram("random.csv")
