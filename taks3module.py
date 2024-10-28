import math

def calculateRadiusCircumscribed(side, numSides):
    return side / (2 * math.sin(math.pi / numSides))
    
def calculateRadiusInscibed(side, numSides):
    return side / (2 * math.tan(math.pi / numSides))