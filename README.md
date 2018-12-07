# Radio Russia
The Russian government wants a proper distribution of transmission frequencies. There are exactly seven types of transmission masts available. For a good distribution it is necessary that two adjacent provinces do not have the same transmitter types.

## The Project:
### Assignment 1
a) Create a transmitter device for Ukraine. Every province must have a sender type, no two adjacent provinces may have the same sender type. Come up with a transmitter for the entire country, the fewer transmitter types you use, the better.

b) Do the same for China, the USA and ultimately for mother Russia.

c) It is cheaper to have fewer transmitter types, but also to have approximately the same number of all types of channels. For each country with every minimum number of transmitter types, try to determine what a balanced distribution would look like.

### Assignment 2
There are four possible cost schemes. For each country, see which cost scheme is the most advantageous

Transmitters | A | B | C | D | E | F | G
-------------|---|---|---|---|---|---|---
Cost 1 | 12 | 26 | 27 | 30 | 37 | 39 | 41
Cost 2 | 19 | 20 | 21 | 23 | 36 | 37 | 38
Cost 3 | 16 | 17 | 31 | 33 | 36 | 56 | 57
Cost 4 | 3  | 34 | 36 | 39 | 41 | 43 | 58

![Map of Russia](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Bla_bla_Russia.svg/1280px-Bla_bla_Russia.svg.png)

# Getting Started:
## Prerequisites:
This code is written in **Python3.7.1** . The necessary packages to be able to successfully run the program can be found in requirements.txt. Those can ben installed with pip dmv. on the following way:

`pip install -r requirements.txt `

## Starting the program:
    python main.py greedy Data/Ukraine.csv Greedyukraine.csv

    general statement:

    python main.py <algorithm> <csv to read> <file to write to>

## Structure:
The Python scrips can be found in the folder "Code", input values in the map "Data", results in "Results".

## Authors:
Clint, Rosa
AKA *Team ¯\_(ツ)_/¯'); DROP TABLE teams;--*

Acknowledgments:
*Arne,
StackOverflow,
Wikipedia &
Minor Programming UvA.*

# Upper bound cost:
The most expensive solution would be that every district has the most expensive transmitter.

That would give: (most expensive transmitter) * (amount of provinces)

# Lower bound cost:
The most inexpensive solution would be that every district has the least expensive transmitter.

That would give: (cheapest transmitter) * (amount of provinces)

# The four colour theorem

The four colour theorem was one of the first mathematical problems solved using a computer. The theorem states that any "map",
as represented by a planar graph, can be coloured with just 4 colours so that the
# State space
The general size of a state space in this problem is:

(number of transmitters) ^ (amount of provinces)

Thus, as Ukraine has 25 provinces, the size of the initial problem is:

7 ^ 25

We can shrink the state space, since the four colour theorem has shown that a solution is possible with only four colours. That will give us the following state space size:

4 ^ amount of provinces.

It is possible that our algorithms are not advanced enough to solve the four colour theorem, so that we will need more colours. This will be discussed in the results section.

# Algorithms

1. Random

This algorithm randomly inserts transmitter types in the country. It then checks the cost for each country as well as the amount of nodes that have at least 1 neighbor of the same type.

This script is used to probe the state space, to give an estimate of the number of solutions, and the cost distribution.

2. Greedy

This algorithm will insert the cheapest available transmitter type in a country, thus the only constraint is that no neighbour has the same transmitter type.

The algorithm contains 2 heuristics:

    -Most neighbours: The algorithm picks the top N provinces with most neighbours connected to it, fills them in with the most expensive colour available and then performs the greedy as stated. It then again fills in the cheapest available colour in the most connected neighbours.
    -Starting point: The script initiates the algorithm with a different starting province.

3. Breadth-first

This algorithm generates a list of "None" as long as the number of provinces. It then generates all valid possibilities in node 0 as a list of "None" with the available colours.

Then, it picks the next neighbour that is "None", and repeats the process recursively until it has filled in all the provinces

This script is very RAM heavy, and is not suitable for larger countries, or small laptops.

4. Depth first

This algorithm generates a base N number from the starting number, where N is the number of transmitters available. It then checks what the first node to have a matching neighbour and adds (the index of this node) ** N to the number, which practically means the node will go up 1 transmitter type.

The program is written using multiprocessing for more computing power, and it is not advised to run it on a sub-8 core processor as it will spawn 8 processes.

5. Hill climber

This algorithm generates a random valid graph, picks a random node and shuffles the transmitter list. It then checks for each transmitter in the random transmitter list whether or not it is cheaper and if it fits.

If both these constraints are met, it changes the node to the chosen transmitter type, and picks a new random node to change. The script iterates over <generations> starting countries for <iterations> cycles, as described in the script. It then returns for each transmitter cost the cheapest country.

6. Genetic

This algorithm generates a random country, and picks the best countries according to the following formula -(total cost * matching neighbours). It breeds these countries and mutates the children by cutting the parents at a randomly chosen point and adding the halves together.

This program is still a work in progress, as it returns random countries even after 10000 generations and 50000 children


7. Random hill climber

To explore the state space for correct answers, the random hillclimber generates countries with no matching neighbours and calculates the cost for each of the cost lists.

It implements a hill climber technique as it memorizes the cheapest graph for each cost list.



# results

**Ukraine:**

*Random (to give an indication of the state space of Ukraine):*

Valid results that are found with a N=1000.000: 5.
Average costs valid results: 604,4
Lowest cost (valid result): 566
Cost list: 19, 20, 21, 23, 36, 37, 38

![Ukraine random](/histogram_random_cost.png)

![Ukraine random](/histogram_random_wrong_nodes.png)

*Greedy:*

Cost: 502

Cost list: [19, 20, 21, 23, 36, 37, 38]

![Ukraine greedy](/Results/Ukraine_greedy.jpg)

*Hill climber:*

Generations: 1000
Iterations: 10000
Cost: 635
Cost list: [12, 26, 27, 30, 37, 39, 41]
Cost: 758
Cost list: [19, 20, 21, 23, 36, 37, 38]
Cost: 912
Cost list: [16, 17, 31, 33, 36, 56, 57]
Cost: 970
Cost list: [3, 34, 36, 39, 41, 43, 58]


**USA:**

*Greedy:*

Cost: 1081

Cost list: [19, 20, 21, 23, 36, 37, 38]

![USA greedy](/Results/USA_greedy.jpg)


*Russia:*

Greedy:

Cost: 1646

Cost list: [19, 20, 21, 23, 36, 37, 38]

![Russia greedy](/Results/russia_greedy.jpg)

It is noted that the greedy algorithms prefer a less deviating cost list.
