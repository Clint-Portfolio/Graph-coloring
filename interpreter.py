import csv
from bs4 import BeautifulSoup

# importeer usabuurlanden
INPUT_CSV = "buurlanden_NL.csv"


if __name__ == "__main__":
    # open usabuurlanden
    with open(INPUT_CSV, newline='') as csvfile:
        #reader = csv.DictReader(csvfile)
        lines = csvfile.readlines()
        print(lines[0])

        for i in lines:
            provinces = i.split(';')
            province_neigbours = i.split(',')
            print(provinces)
            print(province_neigbours)

        #split
        #state_list = []

        #
        #    state_list.append()


# pak het eerste item van de csv
#states_list = []
#state_list.append(buurlanden_NL[0])
