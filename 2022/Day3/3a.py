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

rucksacklist = open("3a_practice.dat")
# rucksacklist = open("3a.dat")