# Day 2 Advent of Code 2022
# Rock - Paper - Scissors Tournament Scoring
# Opponent choice: A - Rock, B - Paper, C - Scissors
# Score based on what you play, and outcome of round
# X - Rock - 1pt, Y - Paper - 2pt, Z - Scissors - 3 Pt
# Loss = 0 pt, draw = 3 pt, win = 6 pt
# Example score:
#   1st round: Paper (2pt) beats Rock, Win (6pt) = 8pt
#   2nd round: Rock (1pt) loses to Paper, Loss (0pt) = 1pt
#   3rd round: Scissors (3pt) ties Scissors, Draw (3pt) = 6pt
# Total = 8 + 1 + 6 = 15pt

# Part two:
# X = Lose, Y = Draw, Z = Win, scoring stays the same
# Example score:
#   1st round: Draw (3pt) for Rock = Rock (1pt) = 4pt
#   2nd round: Lose (0pt) for Paper = Rock (1pt) = 1pt
#   3rd round: Win (6pt) for Scissors = Rock (1pt) = 7pt
# Total = 4 + 1 + 7 = 12pt

# tourny = open("2a_practice.dat")
tourny = open("2a.dat")

choicepoints = 0
roundpoints = 0
roundscore = 0
totalscore = 0

for tournyround in tourny:
    roundlist = list(tournyround)
#    print (roundlist)
#   ['A', ' ', 'Y', '\n']
#   ['B', ' ', 'X', '\n']
#   ['C', ' ', 'Z']
    opp = roundlist[0]
    self = roundlist[2]

    if self == "X":
        roundpoints = 0
        if opp == "A":
            choicepoints = 3
        elif opp == "B":
            choicepoints = 1
        elif opp == "C":
            roundpoints = 2

    elif self == "Y":
        roundpoints = 3
        if opp == "A":
            choicepoints = 1
        elif opp == "B":
            choicepoints = 2
        elif opp == "C":
            choicepoints = 3

    elif self == "Z":
        roundpoints = 6
        if opp == "A":
            choicepoints = 2
        elif opp == "B":
            choicepoints = 3
        elif opp == "C":
            choicepoints = 1

    roundscore = choicepoints + roundpoints
    totalscore += roundscore
    roundpoints = 0
    choicepoints = 0

print (totalscore)