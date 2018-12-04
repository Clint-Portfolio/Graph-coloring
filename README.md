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

## Structure:
The Python scrips can be found in the folder "Code", input values in the map "Data".

## Authors:
Clint, Rosa, Liora
AKA *Team drop.table.nodes*

Acknowledgments:
*Arne,
StackOverflow,
Wikipedia &
Minor Programming UvA.*

# Upperbound cost:
The most expensive solution would be that every district has the most expensive transmitter.

That would give: 58 * amount_of_provinces

# Lowerbound cost:
The most inexpensive solution would be that every district has the least expensive transmitter. 

That would five: 3 * amount_of_provinces

# Statespace
The statespace of the amount of possibilities for transmitters in the provinces is:

7 ^ amound_of_provinces.

We could tight the statespace, since the fourcolourproblem has shown that a solution is possible with only four colors. That will give us the following statespace:

4 ^ amount_of_provinces.

Only, it is possible that our algoritms are advandighed enough to solve the fourcolor problem, so that we will need more colors. 


