# Advent of Code 2022, Day 3b
# Each line represents the contents of a single elves rucksack
# For each group of 3 elves, identify the common item
# Assign priority to each item found and total for answer
# The first three lines represent group 1
# The next threee lines represent group 2, etc
# Practice Result is 70

saveditems=[]
itemlist=[]
totalval = 0
#  itemlistrear=[]

def pulllist(rucklist):
    rucklist = rucklist.strip()
    rucklist = list (rucklist)
    return rucklist


rucksacklist = open("3a_practice.dat")
# rucksacklist = open("3a.dat")

for itemlist in rucksacklist:
    pulllist(itemlist)

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
