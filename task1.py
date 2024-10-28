import random as rand

def displayRandStrings (setOfChars, count, length):
    for n in range(count):
        s = ""
        for m in range(length):
            s += chr(rand.choice(setOfChars))
        print(s)

displayRandStrings(range(ord("a"), ord("z")), 3, 4)
