## Day 5, Advent of Code 2022
## Using map of crate positions and given movements:
## Identify top crate of each stack once reorganizing is completed
## When multiple crates are moved from one position to another:
## Top crate of old stack becomes bottom crate of those moved
## Practice results == CMZ

## Input data file
reorg = open("5p.dat")

## Remove starting crate positions from data file
## Place starting crate positions into list of lists?
## Note: Practice data has 3 stacks, full data has 9

for item in reorg:
    print (item)


## Begin loop of movements
## Parse data from each movement line (move 3 from 1 to 3)


## Perform Movement


## Identify topmost crate of each column


## Give results as single word