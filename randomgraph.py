
# making graphs of the costsfunction from random

import csv
import pandas as pd
from bs4 import BeautifulSoup
from collections import OrderedDict
import matplotlib.pyplot as plt
import json

INPUT_CSV = "random.csv"

def read_CSV(INPUT_CSV):
    cost1 = []
    cost2 = []
    cost3 = []
    cost4 = []

    with open(INPUT_CSV) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            cost1.append(row["cost1"])
            cost2.append(row["cost2"])
            cost3.append(row["cost3"])
            cost4.append(row["cost4"])
    return (cost1, cost2, cost3, cost4)

