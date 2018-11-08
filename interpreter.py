import csv
from bs4 import BeautifulSoup

# importeer usabuurlanden
INPUT_CSV = 'usabuurlanden.csv'


# pak het eerste item van de csv
states_list = []

#state_list.append(usabuurlanden[0])



if __name__ == "__main__":
    # open usabuurlanden
    with open(INPUT_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        []


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """
    writer = csv.writer(outfile)
    writer.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])

    # movies are assigned to disk
    for movie in range(len(movies[0])):
        writer.writerow([movies[0][movie], movies[1][movie], movies[2][movie], movies[3][movie], movies[4][movie]])
