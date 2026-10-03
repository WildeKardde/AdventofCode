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
        choicepoints = 1
        if opp == "A":
            roundpoints = 3
        elif opp == "C":
            roundpoints = 6

    elif self == "Y":
        choicepoints = 2
        if opp == "A":
            roundpoints = 6
        elif opp == "B":
            roundpoints = 3

    elif self == "Z":
        choicepoints = 3
        if opp == "B":
            roundpoints = 6
        elif opp == "C":
            roundpoints = 3

    print ("Opponent: ", opp, " Self: ", self)
    print ("Choice point: ", choicepoints, " Round point: ", roundpoints)

    roundscore = choicepoints + roundpoints
    totalscore += roundscore
    roundpoints = 0
    choicepoints = 0

    print ("Round score: ", roundscore, " Total score: ", totalscore)


print (totalscore)