import csv
from bs4 import BeautifulSoup

# importeer usabuurlanden
INPUT_CSV = 'usabuurlanden.csv'

# open usabuurlanden
with open('usabuurlanden.csv', newline='') as csvfile:
    read = csv.DictReader(csvfile)

list =[]

for row in read:
    list.append(row)


if __name__ == "__main__":
    print(list)
