# Day 4, Advent of Code 2022
# Lists provide to sets of numbers
# Identify how many lists contain one set of numbers fully contained within second set
# Practice set contains 2 such lists
# 613 is too high

## Needed to verify set items were integers else 7 > 13 was true, for example
## New result: 599 -- Correct!

## pull data file
# pairlists = open("4p.dat")
pairlists = open("4a.dat")

## initializations
setscontained = 0
pairsets=[]

## Begin to loop through list

for pairset in pairlists:
#    pairset = list(pairset)

## Turn each line into a list of four objects
    print ()
    print (pairset)
    pairset = pairset.strip()
    pairsets = pairset.split(',')
    print (pairsets)
    firstset = pairsets[0].split('-')
    secondset = pairsets[1].split('-')
    # print (firstset)
    # print (secondset)
    # print (firstset[0], firstset[1], secondset[0], secondset[1])

## Setting each list item to own variable for testing purposes

#    firstfirst = int(firstset[0])
#    firstlast = int(firstset[1])
#    secondfirst = int(secondset[0])
#    secondlast = int(secondset[1])
#    print (firstfirst, firstlast, secondfirst, secondlast)

    if int(firstset[0]) >= int(secondset[0]) and int(firstset[1]) <= int(secondset[1]):
        setscontained += 1
        print ("First is within Second")
    elif int(secondset[0]) >= int(firstset[0]) and int(secondset[1]) <= int(firstset[1]):
        setscontained += 1
        print ("Second is within First")

    ## End of for loop, next sequence

## Print results

print ("Sets contained within other sets: ", setscontained)
