import sys

def countCorrectPos(guess, code):
    guesslist = list(guess)
    codelist = list(code)
    count = 0
    for i in range(length):
        if guesslist[i] == codelist[i]:
            count += 1
    return count

def countCorrectType(guess, code):
    guesslist = list(guess)
    codelist = list(code)
    count = 0
    for i in range(length):
        for j in range(length):
            if codelist[i] == guesslist[j]:
                count += 1
                guesslist[j] = 0
                break
    return count

length = 4
types = 6
oldguesses = []

# Only allow correct arguments
if len(sys.argv) != 3:
    print("q")
    sys.exit(1)

try:
    length = int(sys.argv[1])
    types = int(sys.argv[2])
    if length > 9 or types > 9 or length < 1 or types < 2:
        raise Exception
except:
    print("q")
    sys.exit(1)

# Create set of possibilities and total set
totalset = []
possibleset = []
setscore = []

for i in range(pow(types, length)):
    number = ""
    for j in range(length):
        number += str(int(i / pow(types, length - j - 1)) % types + 1)
    totalset += [number]
    possibleset += [number]
    setscore += [0]

# Create set of possible results
resultset = []
for i in range(length+1):
    for j in range(length+1):
        if (length - j) >= i and i+j <= length:
            resultset += [(i,j)]
resultset.remove((length-1, 1))

guess = ""
for i in range(int(length/2)):
    guess += "1"
for i in range(length - int(length/2)):
    guess += "2"

print("Guess: " + guess)
oldguesses += [guess]

pos = int(input("Number in correct position: "))
typ = int(input("Number of correct number not in correct position: "))
count = 1
while(pos != length or typ != 0):
    # remove bad guesses from possibilities set
    newguesses = []
    for x in possibleset:
        posspos = countCorrectPos(guess, x)
        posstyp = countCorrectType(guess, x) - posspos
        if (pos == posspos and typ == posstyp):
            newguesses += [x]
    possibleset = newguesses

    if (len(possibleset) == 0):
        print("q")
        sys.exit(1)

    
    # minmax
    for i in range(len(totalset)):
        x = totalset[i]
        if x in oldguesses:
            setscore[i] = 0
            continue
        setscore[i] = pow(types, length)
        for resultpos, resulttyp in resultset:
            countmincount = 0
            for y in possibleset:
                resultpos2 = countCorrectPos(x, y)
                resulttyp2 = countCorrectType(x, y) - resultpos2
                if ((resultpos, resulttyp) != (resultpos2, resulttyp2)):
                    countmincount += 1
            if countmincount < setscore[i]:
                setscore[i] = countmincount
    # guess max min
    # get highest scores
    hs = [i for i, j in enumerate(setscore) if j == max(setscore)]
    guess = totalset[setscore.index(max(setscore))]
    for i in hs:
        if totalset[i] in possibleset:
            guess = totalset[i]
            break
    count += 1
    print("Guess: " + guess)
    oldguesses += [guess]
    pos = int(input("Number in correct position: "))
    typ = int(input("Number of correct number not in correct position: "))



print("I guessed the code in " + str(count) + " guesses!")