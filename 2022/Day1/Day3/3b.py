# Advent of Code 2022, Day 3b
# Each line represents the contents of a single elves rucksack
# For each group of 3 elves, identify the common item
# Assign priority to each item found and total for answer
# The first three lines represent group 1
# The next threee lines represent group 2, etc
# Practice Result is 70

rucksacklist = []
badgeslist = []
flist = 0
slist = 1
tlist = 2
totalval = 0
lettervalues = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
                'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39,
                'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
# rucksackfull = open("3a_practice.dat")
rucksackfull = open("3a.dat")

for itemlist in rucksackfull:
    itemlist = itemlist.strip()
    itemlist = list(itemlist)
    rucksacklist.append(itemlist)

print (rucksacklist)
rucksacklength = len(rucksacklist)
print (rucksacklength)

while flist < rucksacklength:
    sharedlist = []
    firstlist = rucksacklist[flist]
    secondlist = rucksacklist[slist]
    thirdlist = rucksacklist[tlist]
    print (firstlist, secondlist, thirdlist)
    if len(firstlist) >= len(secondlist):
        for n in secondlist:
            if n in firstlist:
                sharedlist.append(n)
                print (sharedlist)
    else:
        for n in firstlist:
            if n in secondlist:
                sharedlist.append(n)
                print (sharedlist)
    for n in sharedlist:
        if n in thirdlist:
            badgeslist.append(n)
            print (n)
            break
    flist += 3
    slist += 3
    tlist += 3

print(badgeslist)
for n in badgeslist:
    currval = lettervalues[n]
    totalval = totalval + currval
    print ("Letter: ", n, ", Current Value: ", currval, ", and Total: ", totalval)

print(totalval)