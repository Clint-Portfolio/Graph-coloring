import pandas as pd
import matplotlib.pyplot as plt

def histogram(filename):

    data = pd.read_csv(filename, sep=';', header=None)
    #print(data)

    hist = data.hist(column=5, bins=10)


    plt.title('Amount of wrong nodes ')
    plt.xlabel('wrong nodes')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.20)

    plt.show()



histogram("random.csv")
print("bah")