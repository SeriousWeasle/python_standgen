with open("nouns_.txt", "r") as nf:
    nouns_nf = nf.readlines()

nouns = []
for s in nouns_nf:
    nouns.append(s.split(". ")[1])

with open ("nouns.txt", "a") as f:
    for n in nouns:
        f.write(n)