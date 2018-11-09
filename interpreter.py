import csv
from bs4 import BeautifulSoup

# importeer usabuurlanden
INPUT_CSV = "buurlanden_NL.csv"


if __name__ == "__main__":
    # open usabuurlanden
    with open(INPUT_CSV, newline='') as csvfile:
        #reader = csv.DictReader(csvfile)
        lines = csvfile.readlines()
        #print(lines[0])

        #provinces = lines.split(';')
        #province = provinces[-1].strip('/r/n')
        #province_neigbours = lines.split(',')
        #province_neigbour = province_neigbours[-1].strip('/r/n')

        for line in lines:
            split_list = line.split(';')
            provinces = split_list[0].strip('/r/n')
            print(provinces)

            #province = provinces[line]
            #print(province)
            #print(province, end=(": "))
            #print( )

            province_neigbours = split_list[1]
            #print(province_neigbours)
            #province_neigbours_without_enters = province_neigbours[-1].strip('/r/n')
            province_neigbour = province_neigbours.split(',')

            province_neigbour[-1] = province_neigbour[-1].strip('/r/n')
            print(province_neigbour)
            #print(type(province_neigbour))

        #for j in range(len(lines)):
        #    print(provinces[j])
        #    print(province_neigbour[j])

# lijst maken van de provincies
# lijst maken van province_neigbour



# pak het eerste item van de csv
#states_list = []
#state_list.append(buurlanden_NL[0])
