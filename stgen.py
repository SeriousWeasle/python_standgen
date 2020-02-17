from random import randint

with open("adjectives.txt", "r") as af:
    adjectives = af.readlines()

with open("nouns.txt", "r") as nf:
    nouns = nf.readlines()

while True:
    stcount = input("How many stand names should be generated: ")
    try:
        stcount = int(stcount)
        for i in range(stcount):
            x = randint(0, len(adjectives) - 1)
            y = randint(0, len(nouns) - 1)
            a = adjectives[x][0:len(adjectives[x])-1]
            n = nouns[y][0:len(nouns[y])-1]
            print(a,n)
    except:
        print("invalid input, please try again")