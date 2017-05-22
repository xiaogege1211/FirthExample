from os import listdir
from os.path import isfile, join
import random

def getRandomCat() :
    allFiles = [f for f in listdir() if isfile(f) and f.endswith(('.jpg', '.png'))]
    return random.choice(allFiles)

x = getRandomCat()
print(x)
