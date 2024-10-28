import random as rand

N = []
countryCode = "+380"
operatorCode = "98"

def randPhoneNum(countryCode, operatorCode):
    s = ""
    for i in range(7):
        s+= chr(rand.choice(range(ord("0"), ord("9"))))
    return countryCode + operatorCode + s

print(randPhoneNum(countryCode, operatorCode))
