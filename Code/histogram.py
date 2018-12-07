

def histogram(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)
    # print(data)
    column_number = 3
    hist = data.hist(column=column_number, bins=data.max(axis=0)[column_number] - data.min(axis=0)[column_number], grid=False)

    plt.title('Cost differental costs ')
    plt.xlabel('Costs')
    plt.ylabel('Frequency')

    plt.show()



histogram("random.csv")
print("bah")