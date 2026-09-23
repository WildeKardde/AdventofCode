# 2022 - Day 1 Advent of Code Challenege
# Elves inventory their carried calories,
#  separated per elf by a blank line
# Find elf carrying most Calories
# Answer is total calories carried by that elf

# Part B: Determine top 3 elves by calorie count
# Answer is total of calories carried by all 3

# callist = open("1a_practice.dat")
callist = open("1a.dat")

calcurrent = 0
calcurrenttotal = 0
caltotaltop = 0
caltotalsecond = 0
caltotalthird = 0

for num in callist:
    print (num)
    if num != "\n":
        calcurrenttotal += int(num)
    elif num == "\n":
        if calcurrenttotal > caltotalthird:
            caltotalthird = calcurrenttotal
            if caltotalthird > caltotalsecond:
                caltotalthird = caltotalsecond
                caltotalsecond = calcurrenttotal
                if caltotalsecond > caltotaltop:
                    caltotalsecond = caltotaltop
                    caltotaltop = calcurrenttotal
        calcurrenttotal = 0
    print ("Top:", caltotaltop)
    print ("Second:", caltotalsecond)
    print ("Third:", caltotalthird)

if calcurrenttotal > caltotalthird:
    caltotalthird = calcurrenttotal
    if caltotalthird > caltotalsecond:
        caltotalthird = caltotalsecond
        caltotalsecond = calcurrenttotal
        if caltotalsecond > caltotaltop:
            caltotalsecond = caltotaltop
            caltotaltop = calcurrenttotal

print (caltotaltop + caltotalsecond + caltotalthird)

