# 2022 - Day 1 Advent of Code Challenege
# Elves inventory their carried calories,
#  separated per elf by a blank line
# Find elf carrying most Calories
# Answer is total calories carried by that elf

# callist = open("1a_practice.dat")
callist = open("1a.dat")

calcurrent = 0
calcurrenttotal = 0
caltotalhigh = 0

for num in callist:
#    print (num)
    if num != "\n":
        calcurrenttotal += int(num)
    elif num == "\n":
        if calcurrenttotal > caltotalhigh:
            caltotalhigh = calcurrenttotal
        calcurrenttotal = 0

print (caltotalhigh)

