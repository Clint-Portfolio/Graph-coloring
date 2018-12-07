

def histogram(filename):
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)
    # print(data)

    hist = data.hist(column=[1, 2, 3, 4], bins='auto', grid=False)


    plt.title('Cost differental costs ')
    plt.xlabel('Costs')
    plt.ylabel('Frequency')

    plt.show()



histogram("random.csv")
print("bah")