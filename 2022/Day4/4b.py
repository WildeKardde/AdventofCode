## Day 4b, Advent of Code 2022
## Identify how many pairs overlap at all
## Practice data has 4 pairs that overlap

## Correct result == 928

## pull data file
# pairlists = open("4p.dat")
pairlists = open("4a.dat")

## initializations
setsoverlap = 0
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
    overlapflag = 0

## Setting each list item to own variable for testing purposes

    firstfirst = int(firstset[0])
    firstlast = int(firstset[1])
    secondfirst = int(secondset[0])
    secondlast = int(secondset[1])
    print (firstfirst, firstlast, secondfirst, secondlast)

    if firstlast < secondfirst:
        overlapflag = 1
    elif secondlast < firstfirst:
        overlapflag = 1

    if overlapflag == 0:
        setsoverlap += 1

print ("Total number of pairs that have any overlap: ", setsoverlap)