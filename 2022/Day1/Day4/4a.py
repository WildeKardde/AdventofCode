# Day 4, Advent of Code 2022
# Lists provide to sets of numbers
# Identify how many lists contain one set of numbers fully contained within second set
# Practice set contains 2 such lists
# 613 is too high

# pull data file
# pairlists = open("4p.dat")
pairlists = open("4a.dat")

# initializations
setscontained = 0
pairsets=[]

for pairset in pairlists:
#    pairset = list(pairset)
    print ()
    print (pairset)
    pairset = pairset.strip()
    pairsets = pairset.split(',')
    print (pairsets)
    firstset = pairsets[0].split('-')
    secondset = pairsets[1].split('-')
    print (firstset)
    print (secondset)
    print (firstset[0], firstset[1], secondset[0], secondset[1])
    if firstset[0] >= secondset[0] and firstset[1] <= secondset[1]:
        setscontained += 1
        print ("First is within Second")
    elif secondset[0] >= firstset[0] and secondset[1] <= firstset[1]:
        setscontained += 1
        print ("Second is within First")

print ("Sets contained within other sets: ", setscontained)

# how to segment string based on '-' and ',' ?
# firstset, secondset, firststart, firstend, secondstart, secondend
# Check both firstset in secondset, and secondset in firstset

