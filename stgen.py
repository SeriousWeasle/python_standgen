from random import randint
import random

with open("adjectives.txt", "r") as af:
    adjectives = af.readlines()

with open("nouns.txt", "r") as nf:
    nouns = nf.readlines()

while True:
    stcount = input("How many stand names should be generated: ")
    flipchance = input("Chance to flip (0-100): ")
    try:
        stcount = int(stcount)
        flipchance = float(flipchance)
        for i in range(stcount):
            x = randint(0, len(adjectives) - 1)
            y = randint(0, len(nouns) - 1)
            invert = random.random() * 100
            a = adjectives[x][0:len(adjectives[x])-1]
            n = nouns[y][0:len(nouns[y])-1]
            if(invert < flipchance):
                print(n,a)
            else:
                print(a,n)
    except:
        print("invalid input, please try again")