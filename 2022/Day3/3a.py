# Day 3 Advent of Code 2022
# Each line represent contents of a rucksack
# Rucksack is divided into two compartment
# Each letter represents one item in that rucksack
# Matching letters need to be in same compartment
# Capital items are different than loewrcase items
# Each compartment holds an equal amount of rucksack items
# First half of line is in first compartment, 2nd half in 2nd compartment
# Lowercase items a to z have priorities 1 to 26
# Uppercase items A to Z have priorities 27 to 52
# Find item type that appears in both compartments of each rucksack
# Total the priority numbers of all such items

saveditems=[]
itemlist=[]
totalval = 0
#  itemlistrear=[]

# rucksacklist = open("3a_practice.dat")
rucksacklist = open("3a.dat")

for itemlist in rucksacklist:
    i = 0
    itemlist = itemlist.strip()
    itemlist = list(itemlist)
    print (itemlist)

    fullitemlength = len(itemlist)
    print (fullitemlength)

    itemlength = fullitemlength // 2
    print (itemlength)

    itemlistrear = itemlist[itemlength:]
    print(itemlist[0:itemlength])
    print (itemlistrear)

    for item in itemlist[0:itemlength]:
#        print(itemlist[i])
        if item in itemlistrear:
            print(item)
            saveditems.append(item)
            break
#        i += 1

print(saveditems)

lettervalues = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
                'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39,
                'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

# currlet = ' '
# for n in saveditems:
#     if n != currlet:
#         currval = lettervalues[n]
#         totalval = totalval + currval
#         print ("Letter: ", n, ", Current Value: ", currval, ", and Total: ", totalval)
#     currlet = n

for n in saveditems:
    currval = lettervalues[n]
    totalval = totalval + currval
    print ("Letter: ", n, ", Current Value: ", currval, ", and Total: ", totalval)

print(totalval)

