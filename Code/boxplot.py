
def boxplot(filename):
    import csv 
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv(filename, sep=';', header=None)
    print()


    # plot boxplot
    #data.boxplot(column='4', return_type='axes')
    data.plot.box()
    plt.title('Boxplots for the cost functions')
    plt.show()

 

# To be able to run the program seperately from main
if __name__ == '__main__':

    boxplot("test.csv")