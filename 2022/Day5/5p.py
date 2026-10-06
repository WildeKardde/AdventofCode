## 2022 Advent of Code Day 5
## Practice / Test Code

## Initialize
cratesdata = []
crateslist = []
moveslist = []

## Get Data
testdoc = open("5p.dat")

## Internal Functions
  ## Parse Movement Line
def moveparse(mlist):
    sendit = []
    for u in mlist:
        if u in [1234567890]:
            sendit.append[u]
    return sendit

  ## Turn crates data from line to column
  ## 3 Wide Crate map should have 11 slots prior to newline;
  ## Relevant Data in slots 1, 5, 9 (Every 4)
  ## Relevant Data begins on End -2 including Newline


def craftshift(cratemap):
    cratesend = []
    maplength = len(cratemap)
    ## Need to count list from last to first

for line in testdoc:
    heighttop = list(line)
#    print (line)
#    print (heighttop)
    if heighttop[0] in [' ', '[']:
        cratesdata.append(heighttop)
    else:
        moveslist.append(heighttop)

print(cratesdata)
#    print(moveslist)

## Test for End of line, reverse counting
newcrates=[]
for x in cratesdata[-4::-2]:
    newcrates.append(x)
print (newcrates)



