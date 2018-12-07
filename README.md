# Radio Russia
The Russian government wants a proper distribution of transmission frequencies. There are exactly seven types of transmission masts available. For a good distribution it is necessary that two adjacent provinces do not have the same transmitter types.

## The Project:
### Assignment 1
a) Create a transmitter device for Ukraine. Every province must have a sender type, no two adjacent provinces may have the same sender type. Come up with a transmitter for the entire country, the fewer transmitter types you use, the better.

b) Do the same for China, the USA and ultimately for mother Russia.

c) It is cheaper to have fewer transmitter types, but also to have approximately the same number of all types of channels. For each country with every minimum number of transmitter types, try to determine what a balanced distribution would look like.

### Assignment 2
There are four possible cost schemes. For each country, see which cost scheme is the most advantageous
![Alt Text](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Bla_bla_Russia.svg/1280px-Bla_bla_Russia.svg.png)

# Getting Started:
## Prerequisites:
This code is written in **Python3.7.1** . The necessary packages to be able to succesfully run the program can be found in requirements.txt. Those can ben installed with pip dmv. on the following way:

`pip install -r requirements.txt `

## Starting the program:
    python main.py greedy Data/Ukraine.csv Greedyukraine.csv

## Structure:
The Python scrips can be found in the folder "Code", input values in the map "Data", results in "Results".

## Authors:
Clint, Rosa, Liora
AKA *Team ¯\_(ツ)_/¯'); DROP TABLE teams;--*

Acknowledgments:
*Arne,
StackOverflow,
Wikipedia &
Minor Programming UvA.*

# Upper bound cost:
The most expensive solution would be that every district has the most expensive transmitter.

That would give: 58 * amount of provinces

# Lower bound cost:
The most inexpensive solution would be that every district has the least expensive transmitter.

That would five: 3 * amount of provinces

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

# results

**Ukraine:**

*Greedy:*

Cost: 502

Cost list: [19, 20, 21, 23, 36, 37, 38]

![Ukraine greedy](/Results/Ukraine_greedy.jpg)

*Hill climber:*



**USA:**

*Greedy:*

Cost: 1081

Cost list: [19, 20, 21, 23, 36, 37, 38]

![USA greedy](/Results/USA_greedy.jpg)


*Russia:*

Greedy:

Cost: 1646

Cost list: [19, 20, 21, 23, 36, 37, 38]

![Russia greedy](/Results/Russia_greedy.jpg)

It is noted that the greedy algorithms prefer a less deviating cost list.
