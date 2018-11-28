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

