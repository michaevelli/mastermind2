import sys
import random

random.seed
length = 4
types = 6
code = "0000"
bot = False

def countCorrectPos(guess):
    guesslist = list(guess)
    codelist = list(code)
    count = 0
    for i in range(length):
        if guesslist[i] == codelist[i]:
            count += 1
    return count

def countCorrectType(guess):
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


# Argument Checking
for i in range(len(sys.argv)):
    if sys.argv[i] == "-b":
        bot = True
        sys.argv.pop(i)
        break

if len(sys.argv) == 3:
    try:
        length = int(sys.argv[1])
        types = int(sys.argv[2])
        if length > 9 or types > 9 or length < 1 or types < 1:
            raise Exception
    except:
        print("Error: Length and numbers must be integers between 1 and 9 inclusive")
        sys.exit(1)
elif len(sys.argv) == 4:
    try:
        length = int(sys.argv[1])
        types = int(sys.argv[2])
        if length > 9 or types > 9 or length < 1 or types < 1:
            raise Exception
    except:
        print("Error: Length and numbers must be integers between 1 and 9 inclusive")
        sys.exit(1)
    try:
        code = int(sys.argv[3])
    except:
        print("Error: Code must consist of integers")
        sys.exit(1)
    try:
        code = str(sys.argv[3])
        if len(code) != length:
            raise Exception
        for x in code:
            if int(x) > types:
                raise Exception
    except:
        print("Error: Code does not match length and number format")
        sys.exit(1)
elif len(sys.argv) != 1 and len(sys.argv) != 3 and len(sys.argv) != 4:
    try:
        raise Exception("Error: Unrecognised argument format\nusage: mastermind [options] [length numbers] [code]\n  options:\n    -b Bot mode")
    except Exception as e:
        print(e)
        sys.exit(1)

# Generate Code
if code == "0000":
    code = ""
    for i in range(length):
        code += str(random.randint(1, types))

# Debugging argument
if bot:
    print("Length: " + str(length) + " Numbers: " + str(types) + " Code: " + code)

# Play Game
guess = input("Guess code or 'q' to quit: ")
count = 1
while str(guess) != code:
    if str(guess) == "q":
        print("Code was " + code)
        sys.exit(0)
    if len(str(guess)) != length:
        print("Guess is not in correct format")
        guess = input("Guess code or 'q' to quit: ")
        continue
    pos = countCorrectPos(guess)
    typ = countCorrectType(guess)
    if bot:
        print(str(pos) + " " + str(int(typ)-int(pos)))
    else:
        print("Guess is " + guess + ". " + str(pos) + " in correct position and number. " + str(int(typ) - int(pos)) + " correct number")
    guess = input("Guess code or 'q' to quit: ")
    count += 1
print("Correct! Code is " + code + ". " + str(count) + " guesses.")